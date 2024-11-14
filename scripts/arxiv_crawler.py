import arxiv
import datetime
import json
import os
import re
import sys
import requests
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

    def to_dict(self):
        return asdict(self)

class ArxivCrawler:
    def __init__(self):
        self.logger = setup_logger("arxiv_crawler")
        self.search_query = '(abs:"gaussian splatting" OR ti:"gaussian splatting" OR abs:"3d gaussian" OR ti:"3d gaussian")'
        self.output_dir = Path("data")
        self.output_dir.mkdir(exist_ok=True)
        self.github_token = os.getenv("GITHUB_TOKEN")
        self.headers = {
            "Authorization": f"token {self.github_token}" if self.github_token else "",
            "Accept": "application/vnd.github.v3+json"
        }

    def _find_github_url(self, text: str) -> Optional[str]:
        """从文本中查找GitHub链接"""
        patterns = [
            r'https?://github\.com/[\w-]+/[\w-]+',
            r'github\.com/[\w-]+/[\w-]+',
        ]
        
        for pattern in patterns:
            matches = re.findall(pattern, text.lower())
            if matches:
                url = matches[0]
                if not url.startswith('http'):
                    url = 'https://' + url
                
                if self._verify_github_repo(url):
                    return url
        return None

    def _verify_github_repo(self, url: str) -> bool:
        """验证GitHub仓库是否存在"""
        try:
            parts = url.rstrip('/').split('github.com/')[-1].split('/')
            if len(parts) < 2:
                return False
            
            owner, repo = parts[0], parts[1]
            api_url = f"https://api.github.com/repos/{owner}/{repo}"
            
            response = requests.get(api_url, headers=self.headers)
            return response.status_code == 200
        except RequestException as e:
            self.logger.error(f"GitHub API请求失败: {e}")
            return False
        except Exception as e:
            self.logger.error(f"验证GitHub仓库时出错: {e}")
            return False

    def search_papers(self, max_results: int = 100) -> List[Paper]:
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
                    # 清理摘要文本
                    abstract = result.summary.replace('\n', ' ').strip()
                    github_url = self._find_github_url(abstract)
                    
                    paper = Paper(
                        title=result.title.strip(),
                        authors=[author.name.strip() for author in result.authors],
                        abstract=abstract,
                        arxiv_url=result.entry_id,
                        pdf_url=result.pdf_url,
                        published_date=result.published.strftime("%Y-%m-%d"),
                        categories=[cat for cat in result.categories],
                        github_url=github_url or "",
                        keywords=self._extract_keywords(abstract)
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
    crawler = ArxivCrawler()
    try:
        papers = crawler.search_papers()
        crawler.save_papers(papers)
    except Exception as e:
        crawler.logger.error(f"爬虫运行失败: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 