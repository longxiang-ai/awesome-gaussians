"""
LLM-powered keyword generator.

Given a few paper titles (or arXiv IDs), uses an OpenAI-compatible LLM to
suggest search keywords, expanded terms, and a category structure.

Usage:
    # From paper titles
    python scripts/keyword_generator.py --titles "3D Gaussian Splatting for Real-Time Rendering" "Dynamic 3D Gaussians"

    # From arXiv IDs (fetches titles automatically)
    python scripts/keyword_generator.py --arxiv-ids 2308.04079 2311.12897

    # Auto-write to user_config.json
    python scripts/keyword_generator.py --titles "Paper Title" --apply
"""

import json
import re
import sys
import argparse
import requests
from pathlib import Path
from typing import List, Dict, Optional

# Allow running from project root
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT / "scripts"))

CONFIG_PATH = PROJECT_ROOT / "data" / "user_config.json"

from utils.logger import setup_logger


SYSTEM_PROMPT = """You are an expert research assistant specializing in academic paper search and keyword extraction.

Given a list of paper titles, your task is to:
1. Identify the core research topics and themes
2. Generate search keywords suitable for arXiv paper retrieval
3. Suggest expanded/related terms to broaden the search scope
4. Propose a categorization structure for organizing results

Return your response as a JSON object with this exact structure:
{
  "core_keywords": ["keyword1", "keyword2", ...],
  "expanded_keywords": ["related_term1", "related_term2", ...],
  "suggested_categories": {
    "Category Name": {
      "keywords": ["kw1", "kw2"],
      "description": "Brief description"
    }
  },
  "search_config": {
    "both_abstract_and_title": ["most important keywords"],
    "abstract_only": ["broader terms"],
    "title_only": ["very specific terms"]
  }
}

Guidelines:
- core_keywords: 3-8 essential terms that precisely capture the research focus
- expanded_keywords: 5-15 related terms for discovering adjacent work
- suggested_categories: 3-8 thematic categories for organizing papers
- search_config: keywords organized by search scope for arXiv API queries
- Keep keywords concise (1-3 words each)
- Use lowercase for all keywords
- Include both full terms and common abbreviations (e.g., "3dgs" and "3d gaussian splatting")
- Return ONLY the JSON object, no markdown fences or extra text"""


USER_PROMPT_TEMPLATE = """Analyze these paper titles and generate search keywords for finding similar papers on arXiv:

Paper Titles:
{titles_text}

Please generate comprehensive search keywords based on these papers."""


class KeywordGenerator:
    def __init__(self, api_key: str = None, base_url: str = None, model: str = None):
        self.logger = setup_logger("keyword_generator")

        # Load from config if not provided
        config = self._load_config()
        api_keys = config.get("api_keys", {})

        self.api_key = api_key or api_keys.get("openai_api_key", "")
        self.base_url = base_url or api_keys.get("openai_base_url", "https://api.openai.com/v1")
        self.model = model or api_keys.get("openai_model", "gpt-4o-mini")

        if not self.api_key:
            self.logger.error("No API key configured. Run 'python main.py init' to set up.")

    def _load_config(self) -> dict:
        """Load user_config.json."""
        if CONFIG_PATH.exists():
            try:
                with open(CONFIG_PATH, "r", encoding="utf-8") as f:
                    return json.load(f)
            except Exception:
                pass
        return {}

    def _save_config(self, config: dict):
        """Save user_config.json."""
        CONFIG_PATH.parent.mkdir(parents=True, exist_ok=True)
        with open(CONFIG_PATH, "w", encoding="utf-8") as f:
            json.dump(config, f, ensure_ascii=False, indent=2)

    def fetch_titles_from_arxiv(self, arxiv_ids: List[str]) -> List[str]:
        """Fetch paper titles from arXiv by IDs."""
        import xml.etree.ElementTree as ET

        titles = []
        # Batch fetch using arXiv API
        ids_str = ",".join(arxiv_ids)
        url = f"http://export.arxiv.org/api/query?id_list={ids_str}&max_results={len(arxiv_ids)}"

        try:
            response = requests.get(url, timeout=30)
            response.raise_for_status()
            root = ET.fromstring(response.content)

            ns = {'atom': 'http://www.w3.org/2005/Atom'}
            for entry in root.findall('atom:entry', ns):
                title_el = entry.find('atom:title', ns)
                if title_el is not None and title_el.text:
                    titles.append(title_el.text.strip().replace('\n', ' '))

            self.logger.info(f"Fetched {len(titles)} titles from arXiv")
        except Exception as e:
            self.logger.error(f"Failed to fetch titles from arXiv: {e}")

        return titles

    def generate_keywords(self, paper_titles: List[str]) -> Optional[Dict]:
        """Call LLM to generate keywords from paper titles."""
        if not self.api_key:
            print("[ERROR] No API key configured. Run 'python main.py init' first.")
            return None

        if not paper_titles:
            print("[ERROR] No paper titles provided.")
            return None

        titles_text = "\n".join(f"  {i+1}. {t}" for i, t in enumerate(paper_titles))
        user_msg = USER_PROMPT_TEMPLATE.format(titles_text=titles_text)

        # Use OpenAI-compatible chat completions API
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        payload = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_msg}
            ],
            "temperature": 0.3,
            "max_tokens": 2000
        }

        api_url = f"{self.base_url.rstrip('/')}/chat/completions"

        self.logger.info(f"Calling LLM API: {api_url} model={self.model}")
        print(f"\nCalling LLM ({self.model})...")

        try:
            response = requests.post(api_url, headers=headers, json=payload, timeout=60)
            response.raise_for_status()
            data = response.json()

            content = data["choices"][0]["message"]["content"].strip()

            # Try to extract JSON from the response
            # Handle potential markdown code fences
            json_match = re.search(r'```(?:json)?\s*\n?(.*?)\n?```', content, re.DOTALL)
            if json_match:
                content = json_match.group(1).strip()

            result = json.loads(content)
            self.logger.info("Successfully generated keywords from LLM")
            return result

        except requests.exceptions.HTTPError as e:
            self.logger.error(f"LLM API error: {e}")
            if hasattr(e, 'response') and e.response is not None:
                self.logger.error(f"Response: {e.response.text[:500]}")
            print(f"[ERROR] API request failed: {e}")
            return None
        except json.JSONDecodeError as e:
            self.logger.error(f"Failed to parse LLM response as JSON: {e}")
            self.logger.error(f"Raw response: {content[:500]}")
            print(f"[ERROR] Could not parse LLM response. Raw output:")
            print(content[:1000])
            return None
        except Exception as e:
            self.logger.error(f"Unexpected error calling LLM: {e}")
            print(f"[ERROR] {e}")
            return None

    def apply_to_config(self, result: Dict):
        """Write generated keywords into user_config.json."""
        config = self._load_config()

        # Update search keywords
        search_config = result.get("search_config", {})
        if search_config:
            config.setdefault("search", {}).setdefault("keywords", {})
            kw = config["search"]["keywords"]

            # Merge with existing (deduplicate)
            for scope in ["both_abstract_and_title", "abstract_only", "title_only"]:
                existing = set(kw.get(scope, []))
                new_kws = search_config.get(scope, [])
                existing.update(new_kws)
                kw[scope] = sorted(existing)

        # Update custom categories
        suggested = result.get("suggested_categories", {})
        if suggested:
            config.setdefault("categories", {}).setdefault("custom_categories", {})
            config["categories"]["custom_categories"].update(suggested)

        self._save_config(config)
        print(f"\n[OK] Keywords applied to {CONFIG_PATH}")

    def display_results(self, result: Dict):
        """Pretty-print the generated keywords."""
        print("\n" + "=" * 60)
        print("  Generated Keywords")
        print("=" * 60)

        core = result.get("core_keywords", [])
        expanded = result.get("expanded_keywords", [])
        categories = result.get("suggested_categories", {})
        search_cfg = result.get("search_config", {})

        print(f"\n  Core Keywords ({len(core)}):")
        for kw in core:
            print(f"    - {kw}")

        print(f"\n  Expanded Keywords ({len(expanded)}):")
        for kw in expanded:
            print(f"    - {kw}")

        if categories:
            print(f"\n  Suggested Categories ({len(categories)}):")
            for cat, info in categories.items():
                desc = info.get("description", "")
                kws = info.get("keywords", [])
                print(f"    [{cat}] {desc}")
                print(f"      Keywords: {', '.join(kws)}")

        if search_cfg:
            print(f"\n  Search Config:")
            for scope, kws in search_cfg.items():
                print(f"    {scope}: {', '.join(kws)}")

        print()


def main():
    parser = argparse.ArgumentParser(description='LLM-powered keyword generator for arXiv search')
    parser.add_argument('--titles', nargs='+', type=str, default=None,
                        help='Paper titles to analyze')
    parser.add_argument('--arxiv-ids', nargs='+', type=str, default=None,
                        help='arXiv IDs to fetch and analyze')
    parser.add_argument('--apply', action='store_true',
                        help='Auto-write generated keywords to user_config.json')
    parser.add_argument('--api-key', type=str, default=None,
                        help='OpenAI-compatible API key (overrides config)')
    parser.add_argument('--base-url', type=str, default=None,
                        help='API base URL (overrides config)')
    parser.add_argument('--model', type=str, default=None,
                        help='Model name (overrides config)')
    args = parser.parse_args()

    generator = KeywordGenerator(
        api_key=args.api_key,
        base_url=args.base_url,
        model=args.model
    )

    # Collect paper titles
    titles = []
    if args.titles:
        titles.extend(args.titles)
    if args.arxiv_ids:
        fetched = generator.fetch_titles_from_arxiv(args.arxiv_ids)
        titles.extend(fetched)

    if not titles:
        print("No paper titles provided. Use --titles or --arxiv-ids.")
        print("\nExample:")
        print('  python scripts/keyword_generator.py --titles "3D Gaussian Splatting" "NeRF"')
        print('  python scripts/keyword_generator.py --arxiv-ids 2308.04079 2311.12897')
        sys.exit(1)

    print(f"\nAnalyzing {len(titles)} paper title(s):")
    for i, t in enumerate(titles, 1):
        print(f"  {i}. {t}")

    # Generate keywords
    result = generator.generate_keywords(titles)
    if not result:
        sys.exit(1)

    # Display results
    generator.display_results(result)

    # Apply to config
    if args.apply:
        generator.apply_to_config(result)
    else:
        print("Tip: Add --apply to auto-write these keywords to user_config.json")


if __name__ == "__main__":
    main()
