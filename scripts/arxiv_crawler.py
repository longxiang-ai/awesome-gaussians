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
        self.search_query = '(abs:"gaussian splatting" OR ti:"gaussian splatting" OR \
                            abs:"3d gaussian" OR ti:"3d gaussian" OR \
                            abs:"gaussian splat" OR ti:"gaussian splat" OR \
                            abs:"3dgs" OR ti:"3dgs" OR \
                            abs:"4d gaussian" OR ti:"4d gaussian")'
        self.output_dir = Path("data")
        self.output_dir.mkdir(exist_ok=True)
        self.github_token = os.getenv("GITHUB_TOKEN")
        self.github_headers = {
            "Authorization": f"token {self.github_token}" if self.github_token else "",
            "Accept": "application/vnd.github.v3+json"
        }
        self.fetch_citations = fetch_citations
        self.semantic_api_url = "https://api.semanticscholar.org/v1/paper/arXiv:"

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

    def search_papers(self, max_results: int = 300) -> List[Paper]:
        """搜索arXiv上的论文"""
        try:
            client = arxiv.Client()
            search = arxiv.Search(
                query=self.search_query,
                max_results=max_results,
                sort_by=arxiv.SortCriterion.SubmittedDate,
                sort_order=arxiv.SortOrder.Descending
            )

            papers = []
            for result in client.results(search):
                try:
                    arxiv_id = result.entry_id.split('/')[-1]
                    citations, semantic_url = self._get_citations(arxiv_id) if self.fetch_citations else (0, '')
                    
                    # 清理摘要文本
                    abstract = result.summary.replace('\n', ' ').strip()
                    # 在标题和摘要中查找GitHub链接
                    github_url = self._find_github_url(abstract, result.title.strip())
                    
                    paper = Paper(
                        title=result.title.strip(),
                        authors=[author.name.strip() for author in result.authors],
                        abstract=abstract,
                        arxiv_url=result.entry_id,
                        pdf_url=result.pdf_url,
                        published_date=result.published.strftime("%Y-%m-%d"),
                        categories=[cat for cat in result.categories],
                        github_url=github_url or "",
                        keywords=self._extract_keywords(abstract),
                        citations=citations,
                        semantic_url=semantic_url
                    )
                    papers.append(paper)
                    self.logger.info(f"成功处理论文: {paper.title}")
                except Exception as e:
                    self.logger.error(f"处理单篇论文时出错: {e}")
                    continue
            
            return papers
        except Exception as e:
            self.logger.error(f"搜索论文时出错: {e}")
            raise

    def _extract_keywords(self, abstract: str, max_keywords: int = 5) -> List[str]:
        """从摘要中提取关键词（这里可以使用更复杂的NLP方法）"""
        # 简单实现，实际项目中可以使用更好的关键词提取算法
        common_keywords = [
            "gaussian splatting", "3d gaussian", "neural rendering",
            "real-time rendering", "3d reconstruction", "nerf"
        ]
        keywords = []
        for keyword in common_keywords:
            if keyword.lower() in abstract.lower():
                keywords.append(keyword)
                if len(keywords) >= max_keywords:
                    break
        return keywords

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
                      help='最大获取论文数量')
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