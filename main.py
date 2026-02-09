#!/usr/bin/env python3
"""
Awesome Papers — Unified CLI Entry Point

Usage:
    python main.py init                 # Interactive configuration wizard
    python main.py search               # Search arXiv papers
    python main.py suggest              # Generate keywords from paper titles (LLM)
    python main.py export-bib           # Export BibTeX from paper data
    python main.py readme               # Generate README.md

Examples:
    python main.py init
    python main.py search --max-results 500 --recent 6m --bibtex
    python main.py suggest --titles "3D Gaussian Splatting" "NeRF" --apply
    python main.py suggest --arxiv-ids 2308.04079 2311.12897 --apply
    python main.py export-bib --output output/references.bib --category "Dynamic Scene"
    python main.py readme --show-latest --show-abstracts
"""

import sys
import argparse
from pathlib import Path

# Ensure project root is on the path
PROJECT_ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(PROJECT_ROOT / "scripts"))


def cmd_init(args):
    """Run interactive configuration wizard."""
    from init_config import run_init
    run_init()


def cmd_search(args):
    """Run arXiv paper search."""
    from arxiv_crawler import ArxivCrawler

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
        print(f"\n[OK] Saved {len(papers)} papers.")
    except Exception as e:
        print(f"[ERROR] Search failed: {e}")
        sys.exit(1)


def cmd_suggest(args):
    """Generate keywords from paper titles using LLM."""
    from keyword_generator import KeywordGenerator

    generator = KeywordGenerator(
        api_key=args.api_key,
        base_url=args.base_url,
        model=args.model
    )

    # Collect titles
    titles = []
    if args.titles:
        titles.extend(args.titles)
    if args.arxiv_ids:
        fetched = generator.fetch_titles_from_arxiv(args.arxiv_ids)
        titles.extend(fetched)

    if not titles:
        print("No paper titles provided. Use --titles or --arxiv-ids.")
        print("\nExample:")
        print('  python main.py suggest --titles "3D Gaussian Splatting" "NeRF"')
        print('  python main.py suggest --arxiv-ids 2308.04079 2311.12897')
        sys.exit(1)

    print(f"\nAnalyzing {len(titles)} paper title(s):")
    for i, t in enumerate(titles, 1):
        print(f"  {i}. {t}")

    result = generator.generate_keywords(titles)
    if not result:
        sys.exit(1)

    generator.display_results(result)

    if args.apply:
        generator.apply_to_config(result)
    else:
        print("Tip: Add --apply to auto-write these keywords to user_config.json")


def cmd_export_bib(args):
    """Export BibTeX from paper data."""
    from bibtex_exporter import BibtexExporter

    exporter = BibtexExporter()
    papers = exporter.load_papers(args.input)

    if not papers:
        print("No papers to export.")
        sys.exit(1)

    if args.category:
        papers = exporter.filter_by_category(papers, args.category)
    if args.date_from or args.date_to:
        papers = exporter.filter_by_date(papers, args.date_from, args.date_to)

    if not papers:
        print("No papers match the filter criteria.")
        sys.exit(1)

    exporter.export(papers, args.output)


def cmd_readme(args):
    """Generate README.md."""
    from readme_generator import ReadmeGenerator

    try:
        generator = ReadmeGenerator()
        generator.show_latest_papers = args.show_latest
        generator.show_abstracts = args.show_abstracts
        success = generator.generate_readme()
        if success:
            print("\n[OK] README.md generated successfully.")
        else:
            print("[ERROR] README generation failed.")
            sys.exit(1)
    except Exception as e:
        print(f"[ERROR] README generator failed: {e}")
        sys.exit(1)


def build_parser() -> argparse.ArgumentParser:
    """Build the main argument parser with subcommands."""
    parser = argparse.ArgumentParser(
        description='Awesome Papers — Unified CLI',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )
    subparsers = parser.add_subparsers(dest='command', help='Available commands')

    # --- init ---
    sp_init = subparsers.add_parser('init', help='Interactive configuration wizard')
    sp_init.set_defaults(func=cmd_init)

    # --- search ---
    sp_search = subparsers.add_parser('search', help='Search arXiv papers')
    sp_search.add_argument('--citations', action='store_true',
                           help='Fetch citation counts from Semantic Scholar')
    sp_search.add_argument('--bibtex', action='store_true',
                           help='Fetch BibTeX for each paper')
    sp_search.add_argument('--max-results', type=int, default=None,
                           help='Maximum number of papers (default: from user_config.json, or 1000)')
    sp_search.add_argument('--date-from', type=str, default=None,
                           help='Start date filter (YYYY-MM-DD)')
    sp_search.add_argument('--date-to', type=str, default=None,
                           help='End date filter (YYYY-MM-DD)')
    sp_search.add_argument('--recent', type=str, default=None,
                           help='Recent period filter (e.g., 30d, 6m, 1y, 2y)')
    sp_search.set_defaults(func=cmd_search)

    # --- suggest ---
    sp_suggest = subparsers.add_parser('suggest', help='Generate keywords from paper titles (LLM)')
    sp_suggest.add_argument('--titles', nargs='+', type=str, default=None,
                            help='Paper titles to analyze')
    sp_suggest.add_argument('--arxiv-ids', nargs='+', type=str, default=None,
                            help='arXiv IDs to fetch and analyze')
    sp_suggest.add_argument('--apply', action='store_true',
                            help='Auto-write keywords to user_config.json')
    sp_suggest.add_argument('--api-key', type=str, default=None,
                            help='OpenAI-compatible API key')
    sp_suggest.add_argument('--base-url', type=str, default=None,
                            help='API base URL')
    sp_suggest.add_argument('--model', type=str, default=None,
                            help='Model name')
    sp_suggest.set_defaults(func=cmd_suggest)

    # --- export-bib ---
    sp_bib = subparsers.add_parser('export-bib', help='Export BibTeX from paper data')
    sp_bib.add_argument('--input', type=str, default=None,
                        help='Input JSON file (default: latest papers_*.json)')
    sp_bib.add_argument('--output', type=str, default='output/references.bib',
                        help='Output .bib file (default: output/references.bib)')
    sp_bib.add_argument('--category', type=str, default=None,
                        help='Filter by category (e.g., "Dynamic Scene")')
    sp_bib.add_argument('--date-from', type=str, default=None,
                        help='Filter start date (YYYY-MM-DD)')
    sp_bib.add_argument('--date-to', type=str, default=None,
                        help='Filter end date (YYYY-MM-DD)')
    sp_bib.set_defaults(func=cmd_export_bib)

    # --- readme ---
    sp_readme = subparsers.add_parser('readme', help='Generate README.md')
    sp_readme.add_argument('--show-latest', action='store_true',
                           help='Include latest papers section')
    sp_readme.add_argument('--show-abstracts', action='store_true',
                           help='Include paper abstracts')
    sp_readme.set_defaults(func=cmd_readme)

    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        print("\nTip: Run 'python main.py init' to get started!")
        sys.exit(0)

    args.func(args)


if __name__ == "__main__":
    main()
