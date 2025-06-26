import arxiv
import datetime
import json
import os
import re
import sys
import requests
import argparse
from typing import List, Dict, Optional
from dataclasses import dataclass, asdict
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

    def to_dict(self):
        return asdict(self)

class ArxivCrawler:
    def __init__(self, fetch_citations: bool = False):
        self.logger = setup_logger("arxiv_crawler")
        
        # Load search configuration and generate search query
        self.search_query = self._load_search_config()
        
        self.output_dir = Path("data")
        self.output_dir.mkdir(exist_ok=True)
        self.github_token = os.getenv("GITHUB_TOKEN")
        self.github_headers = {
            "Authorization": f"token {self.github_token}" if self.github_token else "",
            "Accept": "application/vnd.github.v3+json"
        }
        self.fetch_citations = fetch_citations
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

    def _load_search_config(self) -> str:
        """从配置文件加载搜索配置并生成搜索查询"""
        try:
            config_path = Path("data/search_config.json")
            if not config_path.exists():
                self.logger.warning(f"Search config file not found: {config_path}, using default query")
                return '(abs:"gaussian splatting" OR ti:"gaussian splatting" OR abs:"3d gaussian" OR ti:"3d gaussian" OR abs:"gaussian splat" OR ti:"gaussian splat" OR abs:"3dgs" OR ti:"3dgs" OR abs:"4d gaussian" OR ti:"4d gaussian")'
            
            with open(config_path, "r", encoding="utf-8") as f:
                config_data = json.load(f)
                
            search_config = config_data.get("search_config", {})
            
            # Build query parts
            query_parts = []
            
            # Keywords for both abstract and title
            both_keywords = search_config.get("both_abstract_and_title", [])
            for keyword in both_keywords:
                query_parts.append(f'abs:"{keyword}"')
                query_parts.append(f'ti:"{keyword}"')
            
            # Keywords for abstract only
            abs_keywords = search_config.get("abstract_only", [])
            for keyword in abs_keywords:
                query_parts.append(f'abs:"{keyword}"')
            
            # Keywords for title only
            title_keywords = search_config.get("title_only", [])
            for keyword in title_keywords:
                query_parts.append(f'ti:"{keyword}"')
            
            if not query_parts:
                self.logger.warning("No search keywords found in config, using default query")
                return '(abs:"gaussian splatting" OR ti:"gaussian splatting")'
            
            # Join all parts with OR
            search_query = "(" + " OR ".join(query_parts) + ")"
            
            self.logger.info(f"Generated search query from config: {search_query}")
            return search_query
            
        except Exception as e:
            self.logger.error(f"Error loading search config: {e}, using default query")
            return '(abs:"gaussian splatting" OR ti:"gaussian splatting")'

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
            r'(?:https?://)?github\.com/[\w-]+/[\w.-]+(?:/[^\s\)\]]*)?',  # 基本的GitHub URL
            r'(?:https?://)?raw\.githubusercontent\.com/[\w-]+/[\w.-]+',   # raw.githubusercontent.com链接
            r'(?:https?://)?gist\.github\.com/[\w-]+/[\w.-]+',            # GitHub Gist链接
        ]
        
        # 首先在代码指示词附近查找
        for indicator in code_indicators:
            idx = search_text.lower().find(indicator)
            if idx != -1:
                # 在指示词前后200个字符范围内查找
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
            # 确保URL以https://开头
            if not url.startswith('http'):
                url = 'https://' + url
                
            # 清理URL
            url = url.rstrip('/')  # 移除末尾的斜杠
            url = re.sub(r'[.,;:\)]$', '', url)  # 移除末尾的标点符号
            url = url.split('#')[0]  # 移除hash部分
            url = url.split('?')[0]  # 移除query参数
            
            # 确保URL是一个有效的仓库URL
            if '/blob/' in url or '/tree/' in url:
                url = url.split('/blob/')[0] if '/blob/' in url else url.split('/tree/')[0]
            
            return url
        except Exception as e:
            self.logger.error(f"清理GitHub URL时出错: {e}")
            return None

    def _verify_github_repo(self, url: str) -> bool:
        """验证GitHub仓库是否存在"""
        try:
            # 从URL中提取owner和repo
            parts = url.split('github.com/')[-1].split('/')
            if len(parts) < 2:
                return False
            
            owner, repo = parts[0], parts[1]
            # 清理repo名称
            repo = repo.split('#')[0].split('?')[0]
            
            # 如果没有GitHub token，直接返回True（假设链接有效）
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
                return True  # rate limit exceeded时也返回True
            else:
                self.logger.warning(f"GitHub仓库不存在或无法访问: {owner}/{repo} (状态码: {response.status_code})")
                return False
            
        except Exception as e:
            self.logger.error(f"验证GitHub仓库时出错: {e}")
            return True  # 出错时也返回True，避免漏掉可能有效的链接

    def _get_citations(self, arxiv_id: str) -> tuple[int, str]:
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
        keywords = set()  # Use set to avoid duplicates
        text = (abstract + " " + title).lower()
        
        # Check common keywords
        for keyword in self.common_keywords:
            if keyword.lower() in text:
                keywords.add(keyword)
        
        # Check category keywords
        for category_keywords in self.category_keywords.values():
            for keyword in category_keywords:
                if keyword.lower() in text:
                    keywords.add(keyword)
        
        return list(keywords)

    def _direct_arxiv_search(self, max_results: int = 50) -> List[Paper]:
        """直接使用requests访问arXiv API的备用搜索方法"""
        try:
            import xml.etree.ElementTree as ET
            import urllib.parse
            
            # 使用 HTTP 端点避免重定向问题
            base_url = "http://export.arxiv.org/api/query"
            
            # 构建查询参数
            params = {
                'search_query': 'abs:"gaussian splatting"',  # 使用简单查询
                'start': 0,
                'max_results': max_results,
                'sortBy': 'submittedDate',
                'sortOrder': 'descending'
            }
            
            # 构建完整URL
            query_string = urllib.parse.urlencode(params)
            full_url = f"{base_url}?{query_string}"
            
            self.logger.info(f"直接访问 arXiv API: {full_url}")
            
            # 发送请求
            response = requests.get(full_url, timeout=30)
            response.raise_for_status()
            
            # 解析XML响应
            root = ET.fromstring(response.content)
            
            # 定义命名空间
            namespaces = {
                'atom': 'http://www.w3.org/2005/Atom',
                'arxiv': 'http://arxiv.org/schemas/atom'
            }
            
            papers = []
            entries = root.findall('atom:entry', namespaces)
            
            for entry in entries:
                try:
                    # 提取基本信息
                    title = entry.find('atom:title', namespaces)
                    title = title.text.strip() if title is not None else "No title"
                    
                    summary = entry.find('atom:summary', namespaces)
                    abstract = summary.text.strip().replace('\n', ' ') if summary is not None else ""
                    
                    # 提取作者
                    authors = []
                    for author in entry.findall('atom:author', namespaces):
                        name = author.find('atom:name', namespaces)
                        if name is not None:
                            authors.append(name.text.strip())
                    
                    # 提取链接
                    arxiv_url = ""
                    pdf_url = ""
                    for link in entry.findall('atom:link', namespaces):
                        rel = link.get('rel', '')
                        href = link.get('href', '')
                        if rel == 'alternate':
                            arxiv_url = href
                        elif link.get('title') == 'pdf':
                            pdf_url = href
                    
                    # 提取日期
                    published = entry.find('atom:published', namespaces)
                    published_date = published.text[:10] if published is not None else ""
                    
                    # 提取分类
                    categories = []
                    for category in entry.findall('atom:category', namespaces):
                        term = category.get('term', '')
                        if term:
                            categories.append(term)
                    
                    # 提取关键词
                    keywords = self._extract_keywords(abstract, title)
                    
                    paper = Paper(
                        title=title,
                        authors=authors,
                        abstract=abstract,
                        arxiv_url=arxiv_url,
                        pdf_url=pdf_url,
                        published_date=published_date,
                        categories=categories,
                        github_url="",
                        keywords=keywords,
                        citations=0,
                        semantic_url=""
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

    def search_papers(self, max_results: int = 300) -> List[Paper]:
        """Search papers on arXiv"""
        try:
            # 首先尝试直接API方法
            self.logger.info("尝试直接 API 方法来绕过重定向问题...")
            papers = self._direct_arxiv_search(max_results)
            
            if papers:
                self.logger.info(f"直接 API 方法成功获取 {len(papers)} 篇论文")
                return papers
            
            # 如果直接API失败，使用原始方法
            self.logger.info("直接 API 方法失败，尝试使用 arxiv 库...")
            
            # 简化客户端配置，避免版本兼容性问题
            client = arxiv.Client(
                page_size=100,
                delay_seconds=3,
                num_retries=3
            )
            
            # 尝试强制使用 HTTP 端点来解决重定向问题
            try:
                # 检查是否可以访问 arxiv 模块的内部配置
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
                            
                            # Clean abstract text
                            abstract = result.summary.replace('\n', ' ').strip()
                            # Find GitHub link in title and abstract
                            github_url = self._find_github_url(abstract, result.title.strip())
                            # Extract keywords from title and abstract
                            keywords = self._extract_keywords(abstract, result.title.strip())
                            
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
                                semantic_url=semantic_url
                            )
                            papers.append(paper)
                            processed_count += 1
                            self.logger.info(f"Successfully processed paper: {paper.title}")
                        except Exception as e:
                            self.logger.error(f"Error processing single paper: {e}")
                            continue
                    
                    # 如果成功处理了一些论文，跳出重试循环
                    if papers:
                        break
                        
                except Exception as e:
                    retry_count += 1
                    error_msg = str(e)
                    
                    # 处理不同类型的错误
                    if "HTTP 301" in error_msg or "301" in error_msg:
                        self.logger.warning(f"遇到重定向错误，第 {retry_count} 次重试: {e}")
                        if retry_count < max_retries:
                            import time
                            time.sleep(5)  # 等待5秒后重试
                            continue
                    elif "Page of results was unexpectedly empty" in error_msg:
                        self.logger.info(f"Reached end of available results. Successfully processed {processed_count} papers.")
                        break
                    elif "HTTP" in error_msg and retry_count < max_retries:
                        self.logger.warning(f"遇到网络错误，第 {retry_count} 次重试: {e}")
                        import time
                        time.sleep(10)  # 网络错误等待更长时间
                        continue
                    else:
                        self.logger.warning(f"Search interrupted: {e}. Continuing with {processed_count} papers collected so far.")
                        break
            
            # 如果重试后仍然没有论文，尝试降级策略
            if not papers and retry_count >= max_retries:
                self.logger.warning("所有重试都失败了，尝试使用更简单的搜索查询...")
                try:
                    # 使用更简单的查询作为后备
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
                                semantic_url=""
                            )
                            papers.append(paper)
                            processed_count += 1
                            self.logger.info(f"[Fallback] Successfully processed paper: {paper.title}")
                        except Exception as e:
                            self.logger.error(f"Error processing fallback paper: {e}")
                            continue
                            
                except Exception as e:
                    self.logger.error(f"Fallback search also failed: {e}")
            
            self.logger.info(f"Total papers collected: {len(papers)}")
            return papers
            
        except Exception as e:
            self.logger.error(f"Error searching papers: {e}")
            # 不要直接抛出异常，而是返回空列表
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
    parser.add_argument('--max-results', type=int, default=1000,
                      help='最大获取论文数量（默认500，推荐不超过1000以避免API限制）')
    args = parser.parse_args()

    crawler = ArxivCrawler(fetch_citations=args.citations)
    try:
        papers = crawler.search_papers(max_results=args.max_results)
        crawler.save_papers(papers)
    except Exception as e:
        crawler.logger.error(f"爬虫运行失败: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 