import json
import datetime
import sys
import os
from pathlib import Path
from typing import List, Dict
import re
from utils.logger import setup_logger

class ReadmeGenerator:
    def __init__(self):
        self.logger = setup_logger("readme_generator")
        self.data_dir = Path("data")
        self.template_path = Path("README_template.md")
        self.readme_path = Path("README.md")
        
        # 检查必要的目录和文件
        if not self.data_dir.exists():
            self.logger.error(f"数据目录不存在: {self.data_dir}")
            raise FileNotFoundError(f"数据目录不存在: {self.data_dir}")
            
        if not self.template_path.exists():
            self.logger.error(f"模板文件不存在: {self.template_path}")
            raise FileNotFoundError(f"模板文件不存在: {self.template_path}")
            
        # 读取模板文件
        try:
            with open(self.template_path, "r", encoding="utf-8") as f:
                self.template_content = f.read()
                self.logger.info(f"成功读取模板文件，大小: {len(self.template_content)} 字节")
        except Exception as e:
            self.logger.error(f"读取模板文件失败: {e}")
            raise

    def load_latest_papers(self) -> List[Dict]:
        """加载最新的论文数据"""
        try:
            json_files = list(self.data_dir.glob("papers_*.json"))
            if not json_files:
                self.logger.warning("未找到论文数据文件")
                return []
            
            latest_file = max(json_files, key=lambda x: x.stat().st_mtime)
            self.logger.info(f"找到最新数据文件: {latest_file}")
            
            with open(latest_file, "r", encoding="utf-8") as f:
                papers = json.load(f)
                self.logger.info(f"成功从{latest_file}加载{len(papers)}篇论文")
                return papers
        except Exception as e:
            self.logger.error(f"加载论文数据时出错: {e}")
            raise

    def group_papers_by_month(self, papers: List[Dict]) -> Dict[str, List[Dict]]:
        """将论文按月份分组"""
        papers_by_month = {}
        for paper in papers:
            date = datetime.datetime.strptime(paper["published_date"], "%Y-%m-%d")
            month_key = date.strftime("%Y年%m月")
            if month_key not in papers_by_month:
                papers_by_month[month_key] = []
            papers_by_month[month_key].append(paper)
        return papers_by_month

    def format_paper_entry(self, paper: Dict) -> str:
        """格式化单个论文条目"""
        try:
            # 提取arXiv ID
            arxiv_id = paper["arxiv_url"].split("/")[-1]
            
            # 基础信息
            entry = f'- **[{paper["title"]}](https://arxiv.org/abs/{arxiv_id})**  \n'
            
            # 添加作者（限制长度）
            authors = paper["authors"]
            if len(authors) > 3:
                authors = authors[:3] + ["等"]
            entry += f'  作者: {", ".join(authors)}  \n'
            
            # 添加链接
            links = []
            links.append(f'[📄 论文](https://arxiv.org/pdf/{arxiv_id}.pdf)')
            if paper["github_url"]:
                links.append(f'[💻 代码]({paper["github_url"]})')
            entry += f'  链接: {" | ".join(links)}  \n'
            
            # 添加摘要预览（限制长度）
            abstract = paper["abstract"]
            if len(abstract) > 200:
                abstract = abstract[:200] + "..."
            entry += f'  摘要: {abstract}  \n'
            
            # 添加关键词
            if paper["keywords"]:
                entry += f'  关键词: {", ".join(paper["keywords"])}  \n'
            
            return entry
        except Exception as e:
            self.logger.error(f"格式化论文条目时出错: {e}")
            return ""

    def generate_readme(self):
        """生成README文件"""
        try:
            self.logger.info("开始生成README...")
            
            # 加载论文数据
            papers = self.load_latest_papers()
            if not papers:
                self.logger.error("没有找到论文数据，无法生成README")
                return False
                
            self.logger.info(f"加载了 {len(papers)} 篇论文")
            
            # 按月份分组
            papers_by_month = self.group_papers_by_month(papers)
            self.logger.info(f"按月份分组: {list(papers_by_month.keys())}")
            
            # 生成最新论文部分
            latest_papers_section = "## 最新论文\n> 🔄 每日更新\n\n"
            for month, month_papers in sorted(papers_by_month.items(), reverse=True):
                self.logger.info(f"处理 {month} 的 {len(month_papers)} 篇论文")
                latest_papers_section += f"### {month}\n"
                for paper in month_papers:
                    paper_entry = self.format_paper_entry(paper)
                    latest_papers_section += paper_entry
                latest_papers_section += "\n"
            
            self.logger.info(f"生成的论文部分大小: {len(latest_papers_section)} 字节")
            
            # 更新README
            readme_content = self.template_content.replace("{{LATEST_PAPERS}}", latest_papers_section)
            readme_content = readme_content.replace(
                "{{LAST_UPDATE}}", 
                datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            )
            
            # 确保父目录存在
            self.readme_path.parent.mkdir(parents=True, exist_ok=True)
            
            self.logger.info(f"正在写入README文件: {self.readme_path}")
            with open(self.readme_path, "w", encoding="utf-8") as f:
                f.write(readme_content)
            
            if self.readme_path.exists():
                self.logger.info(f"README.md 已成功生成，文件大小: {self.readme_path.stat().st_size} 字节")
                return True
            else:
                self.logger.error("README.md 未能成功生成")
                return False
                
        except Exception as e:
            self.logger.error(f"生成README时出错: {e}")
            raise

def main():
    try:
        generator = ReadmeGenerator()
        success = generator.generate_readme()
        if not success:
            sys.exit(1)
    except Exception as e:
        print(f"README生成器运行失败: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 