"""
BibTeX Exporter — export BibTeX entries from paper data files.

Usage:
    # Export from a specific data file
    python scripts/bibtex_exporter.py --input data/papers_2025-01-01.json --output output/references.bib

    # Export from the latest data file
    python scripts/bibtex_exporter.py --output output/references.bib

    # Filter by category
    python scripts/bibtex_exporter.py --category "Dynamic Scene" --output output/dynamic.bib

    # Filter by date range
    python scripts/bibtex_exporter.py --date-from 2024-06-01 --date-to 2025-01-01 --output output/recent.bib
"""

import json
import re
import sys
import time
import datetime
import argparse
import requests
from pathlib import Path
from typing import List, Dict, Optional

# Allow running from project root
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT / "scripts"))

from utils.logger import setup_logger


class BibtexExporter:
    def __init__(self):
        self.logger = setup_logger("bibtex_exporter")
        self.data_dir = PROJECT_ROOT / "data"

        # Load keywords for categorization
        keywords_path = self.data_dir / "keywords.json"
        self.keyword_categories = {}
        if keywords_path.exists():
            try:
                with open(keywords_path, "r", encoding="utf-8") as f:
                    kw_data = json.load(f)
                    self.keyword_categories = kw_data.get("categories", {})
            except Exception:
                pass

    def load_papers(self, input_path: str = None) -> List[Dict]:
        """Load papers from a JSON file. If no path given, use the latest."""
        if input_path:
            path = Path(input_path)
        else:
            json_files = sorted(self.data_dir.glob("papers_*.json"))
            if not json_files:
                self.logger.error("No paper data files found in data/")
                return []
            path = json_files[-1]

        self.logger.info(f"Loading papers from {path}")
        with open(path, "r", encoding="utf-8") as f:
            papers = json.load(f)
        self.logger.info(f"Loaded {len(papers)} papers")
        return papers

    def filter_by_category(self, papers: List[Dict], category: str) -> List[Dict]:
        """Filter papers that belong to a specific category."""
        cat_keywords = []
        for cat_name, cat_info in self.keyword_categories.items():
            if cat_name.lower() == category.lower():
                cat_keywords = [kw.lower() for kw in cat_info.get("keywords", [])]
                break

        if not cat_keywords:
            self.logger.warning(f"Category '{category}' not found in keywords.json. "
                                f"Available: {list(self.keyword_categories.keys())}")
            return []

        filtered = []
        for paper in papers:
            title_lower = paper.get("title", "").lower()
            paper_kws = [k.lower() for k in (paper.get("keywords") or [])]
            if any(ckw in title_lower or any(ckw in pk for pk in paper_kws) for ckw in cat_keywords):
                filtered.append(paper)

        self.logger.info(f"Category '{category}' filter: {len(papers)} -> {len(filtered)} papers")
        return filtered

    def filter_by_date(self, papers: List[Dict], date_from: str = None, date_to: str = None) -> List[Dict]:
        """Filter papers by date range."""
        start = datetime.datetime.strptime(date_from, "%Y-%m-%d") if date_from else None
        end = datetime.datetime.strptime(date_to, "%Y-%m-%d") if date_to else None

        filtered = []
        for paper in papers:
            try:
                pub = datetime.datetime.strptime(paper["published_date"], "%Y-%m-%d")
            except (ValueError, KeyError):
                filtered.append(paper)
                continue
            if start and pub < start:
                continue
            if end and pub > end:
                continue
            filtered.append(paper)

        self.logger.info(f"Date filter: {len(papers)} -> {len(filtered)} papers")
        return filtered

    def fetch_bibtex(self, arxiv_id: str) -> str:
        """Fetch BibTeX from arXiv API."""
        clean_id = re.sub(r'v\d+$', '', arxiv_id)
        url = f"https://arxiv.org/bibtex/{clean_id}"
        try:
            response = requests.get(url, timeout=15)
            if response.status_code == 200:
                bib = response.text.strip()
                if bib.startswith('@'):
                    return bib
            return ""
        except Exception as e:
            self.logger.error(f"BibTeX fetch error for {clean_id}: {e}")
            return ""

    def get_arxiv_id(self, paper: Dict) -> str:
        """Extract arXiv ID from paper data."""
        url = paper.get("arxiv_url", "")
        return url.rstrip('/').split('/')[-1] if url else ""

    def export(self, papers: List[Dict], output_path: str) -> int:
        """Export BibTeX entries for all papers to a .bib file.

        First checks if papers already have bibtex in their data,
        otherwise fetches from arXiv.

        Returns the number of entries exported.
        """
        output = Path(output_path)
        output.parent.mkdir(parents=True, exist_ok=True)

        entries = []
        total = len(papers)

        for i, paper in enumerate(papers):
            arxiv_id = self.get_arxiv_id(paper)
            if not arxiv_id:
                continue

            # Use existing bibtex if available
            bib = paper.get("bibtex", "")
            if not bib:
                self.logger.info(f"[{i+1}/{total}] Fetching BibTeX for {arxiv_id}...")
                bib = self.fetch_bibtex(arxiv_id)
                time.sleep(0.5)  # Rate limiting

            if bib:
                entries.append(bib)
                self.logger.info(f"[{i+1}/{total}] Got BibTeX for: {paper.get('title', arxiv_id)[:60]}")
            else:
                self.logger.warning(f"[{i+1}/{total}] No BibTeX for {arxiv_id}")

        # Write to file
        with open(output, "w", encoding="utf-8") as f:
            f.write("\n\n".join(entries))
            f.write("\n")

        self.logger.info(f"Exported {len(entries)} BibTeX entries to {output}")
        print(f"\n[OK] Exported {len(entries)}/{total} BibTeX entries to {output}")
        return len(entries)


def main():
    parser = argparse.ArgumentParser(description='BibTeX Exporter for arXiv papers')
    parser.add_argument('--input', type=str, default=None,
                        help='Input JSON file path (default: latest papers_*.json)')
    parser.add_argument('--output', type=str, default='output/references.bib',
                        help='Output .bib file path (default: output/references.bib)')
    parser.add_argument('--category', type=str, default=None,
                        help='Filter by paper category (e.g., "Dynamic Scene")')
    parser.add_argument('--date-from', type=str, default=None,
                        help='Filter start date (YYYY-MM-DD)')
    parser.add_argument('--date-to', type=str, default=None,
                        help='Filter end date (YYYY-MM-DD)')
    args = parser.parse_args()

    exporter = BibtexExporter()

    # Load papers
    papers = exporter.load_papers(args.input)
    if not papers:
        print("No papers to export.")
        sys.exit(1)

    # Apply filters
    if args.category:
        papers = exporter.filter_by_category(papers, args.category)
    if args.date_from or args.date_to:
        papers = exporter.filter_by_date(papers, args.date_from, args.date_to)

    if not papers:
        print("No papers match the filter criteria.")
        sys.exit(1)

    # Export
    exporter.export(papers, args.output)


if __name__ == "__main__":
    main()
