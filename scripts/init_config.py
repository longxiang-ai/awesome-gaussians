"""
Interactive configuration initialization script.
Guides user through setting up search keywords, domains, time range, and API keys.
"""

import json
import sys
import os
from pathlib import Path

# Allow running from project root or scripts/
PROJECT_ROOT = Path(__file__).resolve().parent.parent
CONFIG_PATH = PROJECT_ROOT / "data" / "user_config.json"

# Common arXiv CS domains for selection
ARXIV_DOMAINS = {
    "cs.CV": "Computer Vision and Pattern Recognition",
    "cs.GR": "Graphics",
    "cs.AI": "Artificial Intelligence",
    "cs.LG": "Machine Learning",
    "cs.CL": "Computation and Language",
    "cs.RO": "Robotics",
    "cs.MM": "Multimedia",
    "cs.NE": "Neural and Evolutionary Computing",
    "eess.IV": "Image and Video Processing",
    "eess.SP": "Signal Processing",
    "stat.ML": "Machine Learning (Statistics)",
}

DEFAULT_CONFIG = {
    "search": {
        "keywords": {
            "both_abstract_and_title": [],
            "abstract_only": [],
            "title_only": []
        },
        "domains": [],
        "time_range": {
            "mode": "relative",
            "relative": "1y",
            "start_date": None,
            "end_date": None
        },
        "max_results": 500
    },
    "categories": {
        "description": "Custom category keywords (merged with data/keywords.json). Leave empty to use defaults only.",
        "custom_categories": {}
    },
    "api_keys": {
        "openai_api_key": "",
        "openai_base_url": "https://api.openai.com/v1",
        "openai_model": "gpt-4o-mini"
    }
}


def load_config() -> dict:
    """Load existing config or return default."""
    if CONFIG_PATH.exists():
        try:
            with open(CONFIG_PATH, "r", encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            pass
    return json.loads(json.dumps(DEFAULT_CONFIG))


def save_config(config: dict):
    """Save config to file."""
    CONFIG_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(CONFIG_PATH, "w", encoding="utf-8") as f:
        json.dump(config, f, ensure_ascii=False, indent=2)
    print(f"\n[OK] Configuration saved to {CONFIG_PATH}")


def prompt_input(prompt: str, default: str = "") -> str:
    """Prompt user for input with optional default."""
    if default:
        result = input(f"{prompt} [{default}]: ").strip()
        return result if result else default
    return input(f"{prompt}: ").strip()


def prompt_yes_no(prompt: str, default: bool = True) -> bool:
    """Prompt user for yes/no answer."""
    suffix = " [Y/n]" if default else " [y/N]"
    answer = input(f"{prompt}{suffix}: ").strip().lower()
    if not answer:
        return default
    return answer in ("y", "yes")


def step_keywords(config: dict):
    """Step 1: Configure search keywords."""
    print("\n" + "=" * 60)
    print("  Step 1: Search Keywords Configuration")
    print("=" * 60)
    print("\nKeywords are used to search arXiv papers.")
    print("You can configure keywords for different search scopes:\n")
    print("  1. Both abstract and title (recommended for core terms)")
    print("  2. Abstract only (for broader terms)")
    print("  3. Title only (for very specific terms)\n")

    search = config.setdefault("search", {})
    keywords = search.setdefault("keywords", {})

    # Both abstract and title
    current = keywords.get("both_abstract_and_title", [])
    if current:
        print(f"Current [both] keywords: {', '.join(current)}")
    kw_input = prompt_input(
        "Enter keywords for BOTH abstract & title (comma-separated, empty to keep current)",
        ", ".join(current) if current else ""
    )
    if kw_input:
        keywords["both_abstract_and_title"] = [k.strip() for k in kw_input.split(",") if k.strip()]

    # Abstract only
    current = keywords.get("abstract_only", [])
    if current:
        print(f"\nCurrent [abstract-only] keywords: {', '.join(current)}")
    kw_input = prompt_input(
        "Enter keywords for ABSTRACT only (comma-separated, empty to keep current)",
        ", ".join(current) if current else ""
    )
    if kw_input:
        keywords["abstract_only"] = [k.strip() for k in kw_input.split(",") if k.strip()]

    # Title only
    current = keywords.get("title_only", [])
    if current:
        print(f"\nCurrent [title-only] keywords: {', '.join(current)}")
    kw_input = prompt_input(
        "Enter keywords for TITLE only (comma-separated, empty to keep current)",
        ", ".join(current) if current else ""
    )
    if kw_input:
        keywords["title_only"] = [k.strip() for k in kw_input.split(",") if k.strip()]


def step_domains(config: dict):
    """Step 2: Configure arXiv domains."""
    print("\n" + "=" * 60)
    print("  Step 2: arXiv Domain Selection")
    print("=" * 60)
    print("\nAvailable arXiv domains:\n")

    domain_list = list(ARXIV_DOMAINS.items())
    for i, (code, desc) in enumerate(domain_list, 1):
        print(f"  {i:2d}. {code:10s} - {desc}")

    current = config.get("search", {}).get("domains", [])
    if current:
        print(f"\nCurrently selected: {', '.join(current)}")

    print("\nEnter domain numbers separated by commas (e.g., 1,2,3)")
    print("Leave empty to search all domains (no filtering)")
    selection = prompt_input("Your selection", "")

    if selection:
        selected = []
        for s in selection.split(","):
            s = s.strip()
            if s.isdigit():
                idx = int(s) - 1
                if 0 <= idx < len(domain_list):
                    selected.append(domain_list[idx][0])
            elif s in ARXIV_DOMAINS:
                selected.append(s)
        config.setdefault("search", {})["domains"] = selected
        if selected:
            print(f"Selected domains: {', '.join(selected)}")
        else:
            print("No valid domains selected, will search all domains.")
    else:
        config.setdefault("search", {})["domains"] = []
        print("Will search all domains (no filtering).")


def step_time_range(config: dict):
    """Step 3: Configure time range."""
    print("\n" + "=" * 60)
    print("  Step 3: Time Range Configuration")
    print("=" * 60)
    print("\nChoose how to filter papers by date:\n")
    print("  1. Relative period (e.g., last 6 months, 1 year, 2 years)")
    print("  2. Absolute date range (e.g., 2024-01-01 to 2025-06-01)")
    print("  3. No time filter (fetch all available papers)\n")

    time_range = config.setdefault("search", {}).setdefault("time_range", {})
    current_mode = time_range.get("mode", "relative")
    current_rel = time_range.get("relative", "1y")
    print(f"Current setting: mode={current_mode}, relative={current_rel}")

    choice = prompt_input("Your choice (1/2/3)", "1")

    if choice == "1":
        time_range["mode"] = "relative"
        print("\nExamples: 30d (30 days), 6m (6 months), 1y (1 year), 2y (2 years)")
        period = prompt_input("Enter relative period", current_rel or "1y")
        time_range["relative"] = period
        time_range["start_date"] = None
        time_range["end_date"] = None
    elif choice == "2":
        time_range["mode"] = "absolute"
        start = prompt_input("Start date (YYYY-MM-DD)", time_range.get("start_date", ""))
        end = prompt_input("End date (YYYY-MM-DD)", time_range.get("end_date", ""))
        time_range["start_date"] = start
        time_range["end_date"] = end
        time_range["relative"] = None
    else:
        time_range["mode"] = "none"
        time_range["relative"] = None
        time_range["start_date"] = None
        time_range["end_date"] = None
        print("Time filter disabled.")


def step_max_results(config: dict):
    """Step 4: Configure max results."""
    print("\n" + "=" * 60)
    print("  Step 4: Max Results")
    print("=" * 60)

    current = config.get("search", {}).get("max_results", 500)
    val = prompt_input(f"Maximum number of papers to fetch", str(current))
    try:
        config.setdefault("search", {})["max_results"] = int(val)
    except ValueError:
        print(f"Invalid number, keeping {current}")
        config.setdefault("search", {})["max_results"] = current


def step_api_keys(config: dict):
    """Step 5: Configure API keys."""
    print("\n" + "=" * 60)
    print("  Step 5: API Key Configuration (Optional)")
    print("=" * 60)
    print("\nAn OpenAI-compatible API key enables intelligent keyword")
    print("generation from paper titles. Supports OpenAI, DeepSeek, Qwen, etc.\n")

    api_keys = config.setdefault("api_keys", {})

    if prompt_yes_no("Would you like to configure an API key?", default=False):
        base_url = prompt_input(
            "API Base URL",
            api_keys.get("openai_base_url", "https://api.openai.com/v1")
        )
        api_key = prompt_input("API Key (input will be visible)", api_keys.get("openai_api_key", ""))
        model = prompt_input(
            "Model name",
            api_keys.get("openai_model", "gpt-4o-mini")
        )
        api_keys["openai_base_url"] = base_url
        api_keys["openai_api_key"] = api_key
        api_keys["openai_model"] = model
        print("\nAPI key configured successfully.")
    else:
        print("Skipping API key configuration.")
        print("You can configure it later by editing data/user_config.json")
        print("or by re-running: python main.py init")


def run_init():
    """Run the full interactive initialization."""
    print("\n" + "#" * 60)
    print("#  Awesome Papers - Configuration Wizard")
    print("#" * 60)
    print("\nThis wizard will help you set up your search configuration.")
    print("Press Enter to accept the default value shown in [brackets].\n")

    config = load_config()

    step_keywords(config)
    step_domains(config)
    step_time_range(config)
    step_max_results(config)
    step_api_keys(config)

    # Summary
    print("\n" + "=" * 60)
    print("  Configuration Summary")
    print("=" * 60)
    search = config.get("search", {})
    kw = search.get("keywords", {})
    print(f"\n  Keywords (both):     {', '.join(kw.get('both_abstract_and_title', []))}")
    print(f"  Keywords (abstract): {', '.join(kw.get('abstract_only', []))}")
    print(f"  Keywords (title):    {', '.join(kw.get('title_only', []))}")
    print(f"  Domains:             {', '.join(search.get('domains', [])) or 'All'}")
    tr = search.get("time_range", {})
    if tr.get("mode") == "relative":
        print(f"  Time range:          Last {tr.get('relative', '1y')}")
    elif tr.get("mode") == "absolute":
        print(f"  Time range:          {tr.get('start_date')} to {tr.get('end_date')}")
    else:
        print(f"  Time range:          No filter")
    print(f"  Max results:         {search.get('max_results', 500)}")
    api = config.get("api_keys", {})
    has_key = bool(api.get("openai_api_key"))
    print(f"  API key:             {'Configured' if has_key else 'Not configured'}")

    if prompt_yes_no("\nSave this configuration?"):
        save_config(config)
    else:
        print("Configuration discarded.")


def main():
    try:
        run_init()
    except KeyboardInterrupt:
        print("\n\nConfiguration cancelled.")
        sys.exit(0)


if __name__ == "__main__":
    main()
