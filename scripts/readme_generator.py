import json
import datetime
import sys
import os
from pathlib import Path
from typing import List, Dict
import re
from utils.logger import setup_logger
from collections import defaultdict
import argparse

class ReadmeGenerator:
    def __init__(self):
        self.logger = setup_logger("readme_generator")
        self.data_dir = Path("data")
        self.template_path = Path("README_template.md")
        self.readme_path = Path("README.md")
        
        # Check necessary directories and files
        if not self.data_dir.exists():
            self.logger.error(f"Data directory not found: {self.data_dir}")
            raise FileNotFoundError(f"Data directory not found: {self.data_dir}")
            
        if not self.template_path.exists():
            self.logger.error(f"Template file not found: {self.template_path}")
            raise FileNotFoundError(f"Template file not found: {self.template_path}")
            
        # Read template file
        try:
            with open(self.template_path, "r", encoding="utf-8") as f:
                self.template_content = f.read()
                self.logger.info(f"Successfully read template file, size: {len(self.template_content)} bytes")
        except Exception as e:
            self.logger.error(f"Failed to read template file: {e}")
            raise

        # Load keyword categories and common keywords from JSON
        try:
            keywords_path = self.data_dir / "keywords.json"
            if not keywords_path.exists():
                self.logger.error(f"Keywords file not found: {keywords_path}")
                raise FileNotFoundError(f"Keywords file not found: {keywords_path}")
            
            with open(keywords_path, "r", encoding="utf-8") as f:
                keywords_data = json.load(f)
                self.keyword_categories = keywords_data["categories"]
                self.common_keywords = keywords_data["common_keywords"]["keywords"]
                self.logger.info(f"Successfully loaded {len(self.keyword_categories)} keyword categories")
                self.logger.info(f"Successfully loaded {len(self.common_keywords)} common keywords")
        except Exception as e:
            self.logger.error(f"Failed to load keywords data: {e}")
            raise

        # Add configuration options
        self.show_latest_papers = False  # Default to not show latest papers section

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
        """Group papers by month"""
        papers_by_month = {}
        for paper in papers:
            date = datetime.datetime.strptime(paper["published_date"], "%Y-%m-%d")
            month_key = date.strftime("%B %Y")  # Format: "February 2024"
            if month_key not in papers_by_month:
                papers_by_month[month_key] = []
            papers_by_month[month_key].append(paper)
        return papers_by_month

    def _extract_keywords(self, abstract: str, title: str) -> List[str]:
        """Extract keywords from abstract and title"""
        keywords = []
        text = (abstract + " " + title).lower()
        
        # Check each common keyword
        for keyword in self.common_keywords:
            if keyword.lower() in text:
                keywords.append(keyword)
                
        return keywords

    def format_paper_entry(self, paper: Dict) -> str:
        """Format a single paper entry"""
        try:
            arxiv_id = paper["arxiv_url"].split("/")[-1]
            
            # Basic information
            entry = f'- **[{paper["title"]}](https://arxiv.org/abs/{arxiv_id})**  \n'
            
            # Add authors
            authors = paper["authors"]
            entry += f'  Authors: {", ".join(authors)}  \n'
            
            # Add links with different styles
            links = []
            # Always add arXiv PDF link
            links.append(f'[![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/{arxiv_id}.pdf)')
            
            # Handle GitHub link with stars count
            if paper["github_url"]:
                parts = paper["github_url"].split('github.com/')[-1].split('/')
                if len(parts) >= 2:
                    owner, repo = parts[0], parts[1]
                    links.append(f'[![GitHub](https://img.shields.io/github/stars/{owner}/{repo}?style=social)]({paper["github_url"]})')
            
            # Extract project URL from abstract if exists
            project_url = None
            if paper["abstract"]:
                # Look for URLs in the abstract
                urls = re.findall(r'https?://[^\s<>"]+|www\.[^\s<>"]+', paper["abstract"])
                for url in urls:
                    if not url.startswith('http'):
                        url = 'https://' + url
                    if 'arxiv.org' not in url and 'github.com' not in url:
                        project_url = url
                        break
            
            # Handle project/demo link
            if project_url:
                links.append(f'[![Project](https://img.shields.io/badge/-Project-blue)]({project_url})')
            elif paper.get("project_url"):  # If there's a project URL in metadata
                links.append(f'[![Project](https://img.shields.io/badge/-Project-blue)]({paper["project_url"]})')
            
            # Handle Semantic Scholar citations
            if paper["semantic_url"]:
                links.append(f'[![Citations](https://img.shields.io/badge/📚_Citations-{paper["citations"]}-green)]({paper["semantic_url"]})')
            
            entry += f'  Links: {" | ".join(links)}  \n'
            
            # Add abstract with collapsible HTML
            abstract = paper["abstract"]
            entry += f'  <details><summary>Abstract</summary>\n\n  {abstract}\n  </details>  \n'
            
            # Add keywords (use existing keywords or extract from abstract/title)
            if paper["keywords"]:
                keywords = paper["keywords"]
            else:
                keywords = self._extract_keywords(paper["abstract"], paper["title"])
            if keywords:
                entry += f'  Keywords: {", ".join(keywords)}  \n'
            
            return entry
        except Exception as e:
            self.logger.error(f"Error formatting paper entry: {e}")
            return ""

    def categorize_paper(self, paper: Dict) -> List[str]:
        """Categorize paper based on its keywords and title"""
        categories = set()
        
        # Convert paper title and keywords to lowercase for matching
        title = paper["title"].lower()
        keywords = [k.lower() for k in paper["keywords"]] if paper["keywords"] else []
        
        # Check each category's keywords
        for category, category_info in self.keyword_categories.items():
            category_keywords = category_info["keywords"]
            for keyword in category_keywords:
                if keyword.lower() in title or any(keyword.lower() in k for k in keywords):
                    categories.add(category)
                    
        return list(categories)

    def generate_navigation(self, categorized_papers: Dict[str, List[Dict]]) -> str:
        """Generate navigation section with descriptions"""
        nav = "## Categories\n\n"
        for category in sorted(categorized_papers.keys()):
            if categorized_papers[category]:  # Only show categories with papers
                paper_count = len(categorized_papers[category])
                description = self.keyword_categories[category]["description"]
                nav += f"- [{category}](#{category.lower().replace(' ', '-')}) ({paper_count} papers) - {description}\n"
        return nav + "\n"

    def generate_categorized_sections(self, categorized_papers: Dict[str, List[Dict]]) -> str:
        """Generate sections for each category"""
        sections = "## Categorized Papers\n\n"
        for category in sorted(categorized_papers.keys()):
            if categorized_papers[category]:  # Only show categories with papers
                sections += f"### {category}\n\n"
                for paper in categorized_papers[category]:
                    sections += self.format_paper_entry(paper)
                sections += "\n"
        return sections

    def generate_readme(self):
        """Generate README file"""
        try:
            self.logger.info("Starting README generation...")
            
            # Load paper data
            papers = self.load_latest_papers()
            if not papers:
                self.logger.error("No paper data found, cannot generate README")
                return False
                
            self.logger.info(f"Loaded {len(papers)} papers")
            
            # Group by month
            papers_by_month = self.group_papers_by_month(papers)
            self.logger.info(f"Grouped by months: {list(papers_by_month.keys())}")
            
            # Categorize papers
            categorized_papers = defaultdict(list)
            for paper in papers:
                categories = self.categorize_paper(paper)
                for category in categories:
                    categorized_papers[category].append(paper)
            
            # Generate sections
            navigation = self.generate_navigation(categorized_papers)
            
            # Only generate latest papers section if enabled
            latest_papers_section = ""
            if self.show_latest_papers:
                latest_papers_section = "## Latest Papers\n> 🔄 Updated Daily\n\n"
                for month, month_papers in sorted(papers_by_month.items(), reverse=True):
                    self.logger.info(f"Processing {len(month_papers)} papers for {month}")
                    latest_papers_section += f"### {month}\n"
                    for paper in month_papers:
                        paper_entry = self.format_paper_entry(paper)
                        latest_papers_section += paper_entry
                    latest_papers_section += "\n"
            
            categorized_sections = self.generate_categorized_sections(categorized_papers)
            
            # Generate table of contents based on show_latest_papers
            toc = "## Table of Contents\n\n"
            if self.show_latest_papers:
                toc += "- [Latest Papers](#latest-papers)\n"
            toc += "- [Categorized Papers](#categorized-papers)\n"
            toc += "- [Classic Papers](#classic-papers)\n"
            toc += "- [Open Source Projects](#open-source-projects)\n"
            toc += "- [Applications](#applications)\n"
            toc += "- [Tutorials & Blogs](#tutorials--blogs)\n\n"
            
            # Update README
            readme_content = self.template_content
            readme_content = readme_content.replace("{{NAVIGATION}}", navigation)
            readme_content = readme_content.replace("{{TABLE_OF_CONTENTS}}", toc)
            readme_content = readme_content.replace("{{LATEST_PAPERS}}", latest_papers_section)
            readme_content = readme_content.replace("{{CATEGORIZED_PAPERS}}", categorized_sections)
            readme_content = readme_content.replace(
                "{{LAST_UPDATE}}", 
                datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            )
            
            # Ensure parent directory exists
            self.readme_path.parent.mkdir(parents=True, exist_ok=True)
            
            self.logger.info(f"Writing README file: {self.readme_path}")
            with open(self.readme_path, "w", encoding="utf-8") as f:
                f.write(readme_content)
            
            if self.readme_path.exists():
                self.logger.info(f"README.md successfully generated, size: {self.readme_path.stat().st_size} bytes")
                return True
            else:
                self.logger.error("README.md generation failed")
                return False
                
        except Exception as e:
            self.logger.error(f"Error generating README: {e}")
            raise

def main():
    parser = argparse.ArgumentParser(description='README Generator')
    parser.add_argument('--show-latest', action='store_true',
                      help='Show latest papers section in chronological order')
    args = parser.parse_args()

    try:
        generator = ReadmeGenerator()
        generator.show_latest_papers = args.show_latest  # Set from command line argument
        success = generator.generate_readme()
        if not success:
            sys.exit(1)
    except Exception as e:
        print(f"README generator failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 