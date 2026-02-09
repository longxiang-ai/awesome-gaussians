import arxiv
import datetime
import json
import os
import re
import sys
import time
import requests
import argparse
from typing import List, Dict, Optional, Tuple
from dataclasses import dataclass, asdict, field
from pathlib import Path
from utils.logger import setup_logger
from requests.exceptions import RequestException
import urllib3

# 禁用 SSL 警告，因为我们会强制使用 HTTP
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


@dataclass
class Paper:
    title: str
    authors: List[str]
    abstract: str
    arxiv_url: str
    pdf_url: str
    published_date: str
    categories: List[str]
    github_url: str = ""
    keywords: List[str] = None
    citations: int = 0
    semantic_url: str = ""
    links: Dict[str, str] = field(default_factory=dict)
    bibtex: str = ""

    def __post_init__(self):
        if self.keywords is None:
            self.keywords = []
        if self.links is None:
            self.links = {}

    def to_dict(self):
        return asdict(self)


def parse_relative_period(period_str: str) -> datetime.timedelta:
    """Parse a relative period string like '6m', '1y', '2y', '30d' into timedelta."""
    period_str = period_str.strip().lower()
    match = re.match(r'^(\d+)\s*([dmy])$', period_str)
    if not match:
        raise ValueError(f"Invalid period format: '{period_str}'. Use format like '30d', '6m', '1y', '2y'.")
    value = int(match.group(1))
    unit = match.group(2)
    if unit == 'd':
        return datetime.timedelta(days=value)
    elif unit == 'm':
        return datetime.timedelta(days=value * 30)
    elif unit == 'y':
        return datetime.timedelta(days=value * 365)
    raise ValueError(f"Unknown unit: {unit}")


class ArxivCrawler:
    def __init__(self, fetch_citations: bool = False, fetch_bibtex: bool = False,
                 date_from: str = None, date_to: str = None, recent: str = None):
        self.logger = setup_logger("arxiv_crawler")
        self.output_dir = Path("data")
        self.output_dir.mkdir(exist_ok=True)

        # Load user config first
        self.user_config = self._load_user_config()

        # Load search configuration and generate search query
        self.search_query = self._load_search_config()

        # Parse time range (CLI args override config)
        self.date_start, self.date_end = self._resolve_time_range(date_from, date_to, recent)

        self.github_token = os.getenv("GITHUB_TOKEN")
        self.github_headers = {
            "Authorization": f"token {self.github_token}" if self.github_token else "",
            "Accept": "application/vnd.github.v3+json"
        }
        self.fetch_citations = fetch_citations
        self.fetch_bibtex = fetch_bibtex
        self.semantic_api_url = "https://api.semanticscholar.org/v1/paper/arXiv:"

        # Load keywords configuration
        try:
            keywords_path = self.output_dir / "keywords.json"
            if not keywords_path.exists():
                self.logger.error(f"Keywords file not found: {keywords_path}")
                raise FileNotFoundError(f"Keywords file not found: {keywords_path}")

            with open(keywords_path, "r", encoding="utf-8") as f:
                keywords_data = json.load(f)
                self.common_keywords = keywords_data["common_keywords"]["keywords"]
                self.category_keywords = {
                    category: info["keywords"]
                    for category, info in keywords_data["categories"].items()
                }
                self.logger.info(f"Successfully loaded keywords configuration")
        except Exception as e:
            self.logger.error(f"Failed to load keywords configuration: {e}")
            raise

    def _load_user_config(self) -> dict:
        """Load user_config.json if it exists."""
        config_path = self.output_dir / "user_config.json"
        if config_path.exists():
            try:
                with open(config_path, "r", encoding="utf-8") as f:
                    config = json.load(f)
                    self.logger.info("Loaded user_config.json")
                    return config
            except Exception as e:
                self.logger.warning(f"Failed to load user_config.json: {e}")
        return {}

    def _load_search_config(self) -> str:
        """从配置文件加载搜索配置并生成搜索查询。优先使用 user_config.json。"""
        try:
            # Try user_config.json first
            search_cfg = self.user_config.get("search", {}).get("keywords", {})
            if search_cfg and any(search_cfg.get(k) for k in ["both_abstract_and_title", "abstract_only", "title_only"]):
                self.logger.info("Using keywords from user_config.json")
                both_keywords = search_cfg.get("both_abstract_and_title", [])
                abs_keywords = search_cfg.get("abstract_only", [])
                title_keywords = search_cfg.get("title_only", [])
                domains = self.user_config.get("search", {}).get("domains", [])
            else:
                # Fallback to search_config.json
                config_path = Path("data/search_config.json")
                if not config_path.exists():
                    self.logger.warning(f"Search config file not found: {config_path}, using default query")
                    return '(abs:"gaussian splatting" OR ti:"gaussian splatting" OR abs:"3d gaussian" OR ti:"3d gaussian" OR abs:"gaussian splat" OR ti:"gaussian splat" OR abs:"3dgs" OR ti:"3dgs" OR abs:"4d gaussian" OR ti:"4d gaussian")'

                with open(config_path, "r", encoding="utf-8") as f:
                    config_data = json.load(f)

                sc = config_data.get("search_config", {})
                both_keywords = sc.get("both_abstract_and_title", [])
                abs_keywords = sc.get("abstract_only", [])
                title_keywords = sc.get("title_only", [])
                domains = []

            # Build query parts
            query_parts = []

            for keyword in both_keywords:
                query_parts.append(f'abs:"{keyword}"')
                query_parts.append(f'ti:"{keyword}"')

            for keyword in abs_keywords:
                query_parts.append(f'abs:"{keyword}"')

            for keyword in title_keywords:
                query_parts.append(f'ti:"{keyword}"')

            if not query_parts:
                self.logger.warning("No search keywords found in config, using default query")
                return '(abs:"gaussian splatting" OR ti:"gaussian splatting")'

            # Join keyword parts with OR
            keyword_query = "(" + " OR ".join(query_parts) + ")"

            # Add domain filter if specified
            if domains:
                domain_parts = " OR ".join(f'cat:{d}' for d in domains)
                search_query = f"{keyword_query} AND ({domain_parts})"
            else:
                search_query = keyword_query

            self.logger.info(f"Generated search query from config: {search_query}")
            return search_query

        except Exception as e:
            self.logger.error(f"Error loading search config: {e}, using default query")
            return '(abs:"gaussian splatting" OR ti:"gaussian splatting")'

    def _resolve_time_range(self, date_from: str = None, date_to: str = None,
                            recent: str = None) -> Tuple[Optional[datetime.datetime], Optional[datetime.datetime]]:
        """Resolve time range from CLI args or user_config.json.

        CLI arguments take highest priority, then user_config.json.

        Returns:
            (start_date, end_date) — either or both may be None (no filter).
        """
        # Use date-only (midnight) to avoid boundary issues:
        # paper dates are parsed as "YYYY-MM-DD" (midnight 00:00:00),
        # so comparing against datetime.now() with a time component
        # would incorrectly exclude papers published on the boundary day.
        today = datetime.datetime.now().replace(hour=23, minute=59, second=59, microsecond=0)

        # CLI --recent overrides everything
        if recent:
            try:
                delta = parse_relative_period(recent)
                start = (today - delta).replace(hour=0, minute=0, second=0, microsecond=0)
                self.logger.info(f"Time filter (CLI --recent): {start.strftime('%Y-%m-%d')} to {today.strftime('%Y-%m-%d')}")
                return start, today
            except ValueError as e:
                self.logger.warning(f"Invalid --recent value: {e}, ignoring")

        # CLI --date-from / --date-to
        if date_from or date_to:
            start = None
            end = None
            if date_from:
                try:
                    start = datetime.datetime.strptime(date_from, "%Y-%m-%d")
                except ValueError:
                    self.logger.warning(f"Invalid --date-from: {date_from}")
            if date_to:
                try:
                    end = datetime.datetime.strptime(date_to, "%Y-%m-%d")
                except ValueError:
                    self.logger.warning(f"Invalid --date-to: {date_to}")
            if start or end:
                self.logger.info(f"Time filter (CLI): {start} to {end}")
                return start, end

        # user_config.json
        tr = self.user_config.get("search", {}).get("time_range", {})
        mode = tr.get("mode", "none")

        if mode == "relative":
            period = tr.get("relative", "1y")
            if period:
                try:
                    delta = parse_relative_period(period)
                    start = (today - delta).replace(hour=0, minute=0, second=0, microsecond=0)
                    self.logger.info(f"Time filter (config relative={period}): {start.strftime('%Y-%m-%d')} to {today.strftime('%Y-%m-%d')}")
                    return start, today
                except ValueError as e:
                    self.logger.warning(f"Invalid relative period in config: {e}")

        elif mode == "absolute":
            start = None
            end = None
            if tr.get("start_date"):
                try:
                    start = datetime.datetime.strptime(tr["start_date"], "%Y-%m-%d")
                except ValueError:
                    pass
            if tr.get("end_date"):
                try:
                    end = datetime.datetime.strptime(tr["end_date"], "%Y-%m-%d")
                except ValueError:
                    pass
            if start or end:
                self.logger.info(f"Time filter (config absolute): {start} to {end}")
                return start, end

        # No time filter
        self.logger.info("No time filter applied")
        return None, None

    def _filter_by_date(self, papers: List['Paper']) -> List['Paper']:
        """Filter papers by the resolved time range."""
        if not self.date_start and not self.date_end:
            return papers

        filtered = []
        for paper in papers:
            try:
                pub_date = datetime.datetime.strptime(paper.published_date, "%Y-%m-%d")
            except (ValueError, TypeError):
                filtered.append(paper)  # keep papers with unparseable dates
                continue

            if self.date_start and pub_date < self.date_start:
                continue
            if self.date_end and pub_date > self.date_end:
                continue
            filtered.append(paper)

        self.logger.info(f"Date filter: {len(papers)} -> {len(filtered)} papers")
        return filtered

    # ------------------------------------------------------------------ #
    #  Link extraction
    # ------------------------------------------------------------------ #

    def _extract_all_links(self, abstract: str, arxiv_url: str, pdf_url: str,
                           title: str = "") -> Dict[str, str]:
        """Extract and classify all links from abstract, plus known arxiv/pdf links."""
        links: Dict[str, str] = {}

        # Always add arxiv and pdf
        if arxiv_url:
            links["arxiv"] = arxiv_url
        if pdf_url:
            links["pdf"] = pdf_url

        # Extract all URLs from abstract
        search_text = f"{abstract} {title}"
        url_pattern = r'https?://[^\s<>"\)\]}\',;]+'
        raw_urls = re.findall(url_pattern, search_text)

        for url in raw_urls:
            url = self._clean_url(url)
            if not url:
                continue

            url_lower = url.lower()

            # Skip arxiv links (already have them)
            if 'arxiv.org' in url_lower:
                continue

            # GitHub
            if 'github.com' in url_lower or 'raw.githubusercontent.com' in url_lower:
                if 'github' not in links:
                    cleaned = self._clean_github_url(url)
                    if cleaned:
                        links['github'] = cleaned
                continue

            # HuggingFace datasets
            if 'huggingface.co/datasets' in url_lower:
                if 'dataset' not in links:
                    links['dataset'] = url
                continue

            # HuggingFace (non-dataset)
            if 'huggingface.co' in url_lower:
                if 'huggingface' not in links:
                    links['huggingface'] = url
                continue

            # Video links
            if any(domain in url_lower for domain in ['youtube.com', 'youtu.be', 'bilibili.com']):
                if 'video' not in links:
                    links['video'] = url
                continue

            # Dataset keywords in URL
            if any(kw in url_lower for kw in ['dataset', 'data', 'benchmark']):
                if 'dataset' not in links:
                    links['dataset'] = url
                continue

            # Demo/online tool
            if any(kw in url_lower for kw in ['demo', 'app', 'gradio', 'streamlit']):
                if 'demo' not in links:
                    links['demo'] = url
                continue

            # Everything else -> project page
            if 'project' not in links:
                links['project'] = url

        return links

    def _clean_url(self, url: str) -> Optional[str]:
        """Clean a raw URL extracted from text."""
        if not url:
            return None
        # Remove trailing punctuation that got captured
        url = re.sub(r'[.,;:!?\)\]\}]+$', '', url)
        url = url.rstrip('/')
        if len(url) < 10:
            return None
        return url

    def _find_github_url(self, text: str, title: str = "") -> Optional[str]:
        """从文本中查找GitHub链接"""
        # 合并所有可能包含GitHub链接的文本
        search_text = f"{text} {title}"

        # 添加更多常见的代码链接引导语
        code_indicators = [
            "code", "implementation", "source", "github", "repository",
            "official", "project", "available at", "released at"
        ]

        # 直接查找GitHub链接的正则表达式
        patterns = [
            r'(?:https?://)?github\.com/[\w-]+/[\w.-]+(?:/[^\s\)\]]*)?',
            r'(?:https?://)?raw\.githubusercontent\.com/[\w-]+/[\w.-]+',
            r'(?:https?://)?gist\.github\.com/[\w-]+/[\w.-]+',
        ]

        # 首先在代码指示词附近查找
        for indicator in code_indicators:
            idx = search_text.lower().find(indicator)
            if idx != -1:
                context = search_text[max(0, idx-200):min(len(search_text), idx+200)]
                for pattern in patterns:
                    matches = re.finditer(pattern, context, re.IGNORECASE)
                    for match in matches:
                        url = self._clean_github_url(match.group(0))
                        if url:
                            return url

        # 如果没找到，在整个文本中查找
        for pattern in patterns:
            matches = re.finditer(pattern, search_text, re.IGNORECASE)
            for match in matches:
                url = self._clean_github_url(match.group(0))
                if url:
                    return url

        return None

    def _clean_github_url(self, url: str) -> Optional[str]:
        """清理和验证GitHub URL"""
        try:
            if not url.startswith('http'):
                url = 'https://' + url

            url = url.rstrip('/')
            url = re.sub(r'[.,;:\)]$', '', url)
            url = url.split('#')[0]
            url = url.split('?')[0]

            if '/blob/' in url or '/tree/' in url:
                url = url.split('/blob/')[0] if '/blob/' in url else url.split('/tree/')[0]

            return url
        except Exception as e:
            self.logger.error(f"清理GitHub URL时出错: {e}")
            return None

    def _verify_github_repo(self, url: str) -> bool:
        """验证GitHub仓库是否存在"""
        try:
            parts = url.split('github.com/')[-1].split('/')
            if len(parts) < 2:
                return False

            owner, repo = parts[0], parts[1]
            repo = repo.split('#')[0].split('?')[0]

            if not self.github_token:
                self.logger.warning("未设置GitHub token，跳过仓库验证")
                return True

            api_url = f"https://api.github.com/repos/{owner}/{repo}"
            response = requests.get(api_url, headers=self.github_headers)
            if response.status_code == 200:
                self.logger.info(f"验证GitHub仓库成功: {owner}/{repo}")
                return True
            elif response.status_code == 403:
                self.logger.warning(f"GitHub API rate limit exceeded，跳过验证: {owner}/{repo}")
                return True
            else:
                self.logger.warning(f"GitHub仓库不存在或无法访问: {owner}/{repo} (状态码: {response.status_code})")
                return False

        except Exception as e:
            self.logger.error(f"验证GitHub仓库时出错: {e}")
            return True

    def _get_citations(self, arxiv_id: str) -> tuple:
        """获取论文引用数"""
        if not self.fetch_citations:
            return 0, ''

        try:
            response = requests.get(f"{self.semantic_api_url}{arxiv_id}")
            if response.status_code == 200:
                data = response.json()
                return data.get('citationCount', 0), data.get('url', '')
            return 0, ''
        except Exception as e:
            self.logger.error(f"获取引用数时出错: {e}")
            return 0, ''

    def _extract_keywords(self, abstract: str, title: str) -> List[str]:
        """Extract keywords from abstract and title"""
        keywords = set()
        text = (abstract + " " + title).lower()

        for keyword in self.common_keywords:
            if keyword.lower() in text:
                keywords.add(keyword)

        for category_keywords in self.category_keywords.values():
            for keyword in category_keywords:
                if keyword.lower() in text:
                    keywords.add(keyword)

        return list(keywords)

    # ------------------------------------------------------------------ #
    #  BibTeX
    # ------------------------------------------------------------------ #

    def _fetch_bibtex(self, arxiv_id: str) -> str:
        """Fetch BibTeX entry from arXiv for a given paper ID."""
        # Strip version suffix (e.g. 2411.09156v1 -> 2411.09156)
        clean_id = re.sub(r'v\d+$', '', arxiv_id)
        url = f"https://arxiv.org/bibtex/{clean_id}"
        try:
            response = requests.get(url, timeout=15)
            if response.status_code == 200:
                bib = response.text.strip()
                if bib.startswith('@'):
                    return bib
                self.logger.warning(f"Unexpected BibTeX response for {clean_id}")
                return ""
            else:
                self.logger.warning(f"BibTeX fetch failed for {clean_id}: HTTP {response.status_code}")
                return ""
        except Exception as e:
            self.logger.error(f"BibTeX fetch error for {clean_id}: {e}")
            return ""

    def _get_arxiv_id(self, arxiv_url: str) -> str:
        """Extract arXiv ID from URL."""
        # Handle URLs like http://arxiv.org/abs/2411.09156v1
        return arxiv_url.rstrip('/').split('/')[-1]

    # ------------------------------------------------------------------ #
    #  Search methods
    # ------------------------------------------------------------------ #

    def _direct_arxiv_search(self, max_results: int = 50) -> List[Paper]:
        """直接使用requests访问arXiv API的备用搜索方法"""
        try:
            import xml.etree.ElementTree as ET
            import urllib.parse

            base_url = "http://export.arxiv.org/api/query"

            params = {
                'search_query': self.search_query,
                'start': 0,
                'max_results': max_results,
                'sortBy': 'submittedDate',
                'sortOrder': 'descending'
            }

            query_string = urllib.parse.urlencode(params)
            full_url = f"{base_url}?{query_string}"

            self.logger.info(f"直接访问 arXiv API: {full_url}")

            response = requests.get(full_url, timeout=30)
            response.raise_for_status()

            root = ET.fromstring(response.content)

            namespaces = {
                'atom': 'http://www.w3.org/2005/Atom',
                'arxiv': 'http://arxiv.org/schemas/atom'
            }

            papers = []
            entries = root.findall('atom:entry', namespaces)

            for entry in entries:
                try:
                    title_el = entry.find('atom:title', namespaces)
                    title = title_el.text.strip() if title_el is not None else "No title"

                    summary = entry.find('atom:summary', namespaces)
                    abstract = summary.text.strip().replace('\n', ' ') if summary is not None else ""

                    authors = []
                    for author in entry.findall('atom:author', namespaces):
                        name = author.find('atom:name', namespaces)
                        if name is not None:
                            authors.append(name.text.strip())

                    arxiv_url = ""
                    pdf_url = ""
                    for link in entry.findall('atom:link', namespaces):
                        rel = link.get('rel', '')
                        href = link.get('href', '')
                        if rel == 'alternate':
                            arxiv_url = href
                        elif link.get('title') == 'pdf':
                            pdf_url = href

                    published = entry.find('atom:published', namespaces)
                    published_date = published.text[:10] if published is not None else ""

                    categories = []
                    for category in entry.findall('atom:category', namespaces):
                        term = category.get('term', '')
                        if term:
                            categories.append(term)

                    keywords = self._extract_keywords(abstract, title)
                    github_url = self._find_github_url(abstract, title) or ""
                    all_links = self._extract_all_links(abstract, arxiv_url, pdf_url, title)
                    if github_url and 'github' not in all_links:
                        all_links['github'] = github_url

                    # Fetch BibTeX if enabled
                    bibtex = ""
                    if self.fetch_bibtex and arxiv_url:
                        aid = self._get_arxiv_id(arxiv_url)
                        bibtex = self._fetch_bibtex(aid)
                        time.sleep(0.3)  # rate limit

                    paper = Paper(
                        title=title,
                        authors=authors,
                        abstract=abstract,
                        arxiv_url=arxiv_url,
                        pdf_url=pdf_url,
                        published_date=published_date,
                        categories=categories,
                        github_url=github_url,
                        keywords=keywords,
                        citations=0,
                        semantic_url="",
                        links=all_links,
                        bibtex=bibtex
                    )
                    papers.append(paper)
                    self.logger.info(f"[Direct API] Successfully processed paper: {title}")

                except Exception as e:
                    self.logger.error(f"Error processing paper from direct API: {e}")
                    continue

            return papers

        except Exception as e:
            self.logger.error(f"Direct arXiv API search failed: {e}")
            return []

    def search_papers(self, max_results: int = None) -> List[Paper]:
        """Search papers on arXiv.

        Priority for max_results: explicit argument > user_config.json > default (1000).
        """
        if max_results is None:
            config_max = self.user_config.get("search", {}).get("max_results")
            max_results = config_max if config_max else 1000

        try:
            # 首先尝试直接API方法
            self.logger.info("尝试直接 API 方法来绕过重定向问题...")
            papers = self._direct_arxiv_search(max_results)

            if papers:
                self.logger.info(f"直接 API 方法成功获取 {len(papers)} 篇论文")
                papers = self._filter_by_date(papers)
                return papers

            # 如果直接API失败，使用原始方法
            self.logger.info("直接 API 方法失败，尝试使用 arxiv 库...")

            client = arxiv.Client(
                page_size=100,
                delay_seconds=3,
                num_retries=3
            )

            try:
                import arxiv.arxiv as arxiv_module
                original_base_url = getattr(arxiv_module, 'BASE_URL', None)
                if original_base_url:
                    arxiv_module.BASE_URL = "http://export.arxiv.org/api/"
                    self.logger.info("成功切换到 HTTP 端点")
            except Exception as e:
                self.logger.warning(f"无法修改 arXiv 端点，使用默认设置: {e}")

            search = arxiv.Search(
                query=self.search_query,
                max_results=max_results,
                sort_by=arxiv.SortCriterion.SubmittedDate,
                sort_order=arxiv.SortOrder.Descending
            )

            papers = []
            processed_count = 0
            retry_count = 0
            max_retries = 3

            while retry_count < max_retries:
                try:
                    self.logger.info(f"尝试获取论文，第 {retry_count + 1} 次尝试...")

                    for result in client.results(search):
                        try:
                            arxiv_id = result.entry_id.split('/')[-1]
                            citations, semantic_url = self._get_citations(arxiv_id) if self.fetch_citations else (0, '')

                            abstract = result.summary.replace('\n', ' ').strip()
                            github_url = self._find_github_url(abstract, result.title.strip())
                            keywords = self._extract_keywords(abstract, result.title.strip())
                            all_links = self._extract_all_links(
                                abstract, result.entry_id, result.pdf_url, result.title.strip()
                            )
                            if github_url and 'github' not in all_links:
                                all_links['github'] = github_url

                            bibtex = ""
                            if self.fetch_bibtex:
                                bibtex = self._fetch_bibtex(arxiv_id)
                                time.sleep(0.3)

                            paper = Paper(
                                title=result.title.strip(),
                                authors=[author.name.strip() for author in result.authors],
                                abstract=abstract,
                                arxiv_url=result.entry_id,
                                pdf_url=result.pdf_url,
                                published_date=result.published.strftime("%Y-%m-%d"),
                                categories=[cat for cat in result.categories],
                                github_url=github_url or "",
                                keywords=keywords,
                                citations=citations,
                                semantic_url=semantic_url,
                                links=all_links,
                                bibtex=bibtex
                            )
                            papers.append(paper)
                            processed_count += 1
                            self.logger.info(f"Successfully processed paper: {paper.title}")
                        except Exception as e:
                            self.logger.error(f"Error processing single paper: {e}")
                            continue

                    if papers:
                        break

                except Exception as e:
                    retry_count += 1
                    error_msg = str(e)

                    if "HTTP 301" in error_msg or "301" in error_msg:
                        self.logger.warning(f"遇到重定向错误，第 {retry_count} 次重试: {e}")
                        if retry_count < max_retries:
                            time.sleep(5)
                            continue
                    elif "Page of results was unexpectedly empty" in error_msg:
                        self.logger.info(f"Reached end of available results. Successfully processed {processed_count} papers.")
                        break
                    elif "HTTP" in error_msg and retry_count < max_retries:
                        self.logger.warning(f"遇到网络错误，第 {retry_count} 次重试: {e}")
                        time.sleep(10)
                        continue
                    else:
                        self.logger.warning(f"Search interrupted: {e}. Continuing with {processed_count} papers collected so far.")
                        break

            # 降级策略
            if not papers and retry_count >= max_retries:
                self.logger.warning("所有重试都失败了，尝试使用更简单的搜索查询...")
                try:
                    simple_search = arxiv.Search(
                        query='abs:"gaussian splatting"',
                        max_results=min(50, max_results),
                        sort_by=arxiv.SortCriterion.SubmittedDate,
                        sort_order=arxiv.SortOrder.Descending
                    )

                    for result in client.results(simple_search):
                        try:
                            paper = Paper(
                                title=result.title.strip(),
                                authors=[author.name.strip() for author in result.authors],
                                abstract=result.summary.replace('\n', ' ').strip(),
                                arxiv_url=result.entry_id,
                                pdf_url=result.pdf_url,
                                published_date=result.published.strftime("%Y-%m-%d"),
                                categories=[cat for cat in result.categories],
                                github_url="",
                                keywords=[],
                                citations=0,
                                semantic_url="",
                                links={},
                                bibtex=""
                            )
                            papers.append(paper)
                            processed_count += 1
                            self.logger.info(f"[Fallback] Successfully processed paper: {paper.title}")
                        except Exception as e:
                            self.logger.error(f"Error processing fallback paper: {e}")
                            continue

                except Exception as e:
                    self.logger.error(f"Fallback search also failed: {e}")

            # Apply date filter
            papers = self._filter_by_date(papers)

            self.logger.info(f"Total papers collected: {len(papers)}")
            return papers

        except Exception as e:
            self.logger.error(f"Error searching papers: {e}")
            self.logger.warning("返回空的论文列表以确保程序继续运行")
            return []

    def save_papers(self, papers: List[Paper]):
        """保存论文信息到JSON文件"""
        try:
            today = datetime.datetime.now().strftime("%Y-%m-%d")
            output_file = self.output_dir / f"papers_{today}.json"

            papers_dict = [paper.to_dict() for paper in papers]
            with open(output_file, "w", encoding="utf-8") as f:
                json.dump(papers_dict, f, ensure_ascii=False, indent=2)

            self.logger.info(f"成功保存{len(papers)}篇论文到{output_file}")
        except Exception as e:
            self.logger.error(f"保存论文数据时出错: {e}")
            raise


def main():
    parser = argparse.ArgumentParser(description='arXiv论文爬虫')
    parser.add_argument('--citations', action='store_true',
                        help='是否获取引用数和Semantic Scholar链接')
    parser.add_argument('--bibtex', action='store_true',
                        help='是否获取每篇论文的BibTeX引用')
    parser.add_argument('--max-results', type=int, default=None,
                        help='最大获取论文数量（默认从user_config.json读取，否则1000）')
    parser.add_argument('--date-from', type=str, default=None,
                        help='检索起始日期 (YYYY-MM-DD)')
    parser.add_argument('--date-to', type=str, default=None,
                        help='检索结束日期 (YYYY-MM-DD)')
    parser.add_argument('--recent', type=str, default=None,
                        help='检索最近时间段，如 30d, 6m, 1y, 2y')
    args = parser.parse_args()

    crawler = ArxivCrawler(
        fetch_citations=args.citations,
        fetch_bibtex=args.bibtex,
        date_from=args.date_from,
        date_to=args.date_to,
        recent=args.recent
    )
    try:
        papers = crawler.search_papers(max_results=args.max_results)
        crawler.save_papers(papers)
    except Exception as e:
        crawler.logger.error(f"爬虫运行失败: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
