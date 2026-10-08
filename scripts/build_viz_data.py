"""Build the GitHub Pages visualization site from the crawled paper data.

Merges every data/papers_YYYY-MM-DD.json snapshot (each only holds the latest
~500 papers), tags topics from data/keywords.json, lays papers out on a 2D map
by abstract similarity, and writes site/ plus data.json into the output folder.

Usage: python scripts/build_viz_data.py [--out _site]
"""

import argparse
import datetime
import glob
import html
import json
import logging
import os
import re
import shutil
from collections import Counter

import numpy as np
from sklearn.cluster import KMeans
from sklearn.decomposition import TruncatedSVD
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS, TfidfVectorizer
from sklearn.manifold import TSNE
from sklearn.preprocessing import normalize

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(ROOT, "data")
SITE_DIR = os.path.join(ROOT, "site")
SNAPSHOT_PATTERN = re.compile(r"papers_(\d{4}-\d{2}-\d{2})\.json$")

# Per-repository settings; everything else in this script and in site/ is shared.
SITE = {
    "title": "Gaussian Splatting Paper Atlas",
    "subject": "3D Gaussian Splatting",
    "search_hint": "e.g. SLAM, avatar, Marc Pollefeys",
    "repo": "longxiang-ai/awesome-gaussians",
    # Translations of the fields above for the page's language menu (site/i18n.js holds the rest of the UI).
    "i18n": {
        "zh": {
            "title": "高斯泼溅论文图谱",
            "subject": "高斯泼溅（3DGS）",
            "search_hint": "例如 SLAM、avatar、Marc Pollefeys",
        },
        "ja": {
            "title": "Gaussian Splatting 論文アトラス",
            "subject": "3D Gaussian Splatting",
            "search_hint": "例：SLAM、avatar、Marc Pollefeys",
        },
    },
}
# Words nearly every paper in this field shares; they carry no signal for the map.
DOMAIN_STOP_WORDS = {
    "gaussian", "gaussians", "splatting", "3d", "3dgs", "gs", "representation",
    "representations", "scene", "scenes", "rendering", "view", "views",
}
MIN_YEAR = 2023  # 3DGS was published Aug 2023; older hits are keyword noise

GENERIC_STOP_WORDS = {
    "method", "methods", "propose", "proposed", "approach", "novel", "paper",
    "results", "based", "framework", "performance", "state", "art", "existing",
    "demonstrate", "work", "achieves", "achieve", "introduce", "code", "available",
    "https", "github", "com", "io", "project", "page", "extensive", "experiments",
    "show", "model", "models", "quality", "using", "new", "high", "significantly",
    "outperforms", "leverages", "leveraging", "furthermore", "specifically",
    "additionally", "comprehensive", "effectively", "enables", "while",
}
CLUSTER_COUNT = 18

logger = logging.getLogger("build_viz_data")


def paper_id(paper):
    """arXiv id without version, e.g. 2609.01234."""
    tail = paper["arxiv_url"].rstrip("/").split("/abs/")[-1]
    return re.sub(r"v\d+$", "", tail)


def load_papers():
    """Merge all snapshots; later snapshots win for the same paper."""
    files = sorted(
        path for path in glob.glob(os.path.join(DATA_DIR, "papers_*.json"))
        if SNAPSHOT_PATTERN.search(path)
    )
    if not files:
        raise SystemExit("No data/papers_*.json snapshots found")

    papers = {}
    for path in files:
        try:
            with open(path, encoding="utf-8") as handle:
                records = json.load(handle)
        except (OSError, json.JSONDecodeError) as exc:
            logger.warning(f"Skipping unreadable snapshot {path}: {exc}")
            continue
        for record in records:
            if not isinstance(record, dict):
                continue
            if not record.get("title") or not record.get("arxiv_url"):
                continue
            date = str(record.get("published_date", ""))
            if not re.match(r"^\d{4}-\d{2}-\d{2}$", date) or int(date[:4]) < MIN_YEAR:
                continue
            papers[paper_id(record)] = record

    tracking_start = SNAPSHOT_PATTERN.search(files[0]).group(1)
    last_update = SNAPSHOT_PATTERN.search(files[-1]).group(1)
    logger.info(f"Merged {len(files)} snapshots into {len(papers)} unique papers")
    return papers, tracking_start, last_update


def load_topics():
    with open(os.path.join(DATA_DIR, "keywords.json"), encoding="utf-8") as handle:
        categories = json.load(handle)["categories"]
    topics = []
    for name, info in categories.items():
        # Whole-word match: plain substring matching lets "ar" hit "radar", "large", ...
        pattern = re.compile(
            r"\b(?:" + "|".join(re.escape(k) for k in info["keywords"]) + r")\b",
            re.IGNORECASE,
        )
        topics.append({"name": name, "description": info["description"], "pattern": pattern})
    return topics


def embed(texts):
    """TF-IDF -> SVD -> t-SNE 2D coordinates, plus the TF-IDF matrix for labels."""
    vectorizer = TfidfVectorizer(
        stop_words=list(ENGLISH_STOP_WORDS | GENERIC_STOP_WORDS | DOMAIN_STOP_WORDS),
        token_pattern=r"(?u)\b[a-zA-Z][a-zA-Z0-9\-]{1,}\b",
        ngram_range=(1, 2),
        min_df=3,
        max_df=0.4,
        sublinear_tf=True,
    )
    tfidf = vectorizer.fit_transform(texts)
    components = min(50, tfidf.shape[1] - 1, tfidf.shape[0] - 1)
    reduced = normalize(TruncatedSVD(n_components=components, random_state=0).fit_transform(tfidf))
    coords = TSNE(
        n_components=2,
        perplexity=min(40, max(5, len(texts) // 10)),
        init="pca",
        metric="cosine",
        random_state=0,
    ).fit_transform(reduced)
    # Scale to [0, 1] so the page can size the map freely.
    coords -= coords.min(axis=0)
    coords /= coords.max(axis=0)
    return coords, tfidf, np.array(vectorizer.get_feature_names_out())


def label_clusters(coords, tfidf, terms):
    count = min(CLUSTER_COUNT, len(coords))
    assignments = KMeans(n_clusters=count, n_init=10, random_state=0).fit_predict(coords)
    clusters = []
    for index in range(count):
        members = np.where(assignments == index)[0]
        weights = np.asarray(tfidf[members].mean(axis=0)).ravel()
        label_terms = []
        for term in terms[np.argsort(weights)[::-1]]:
            # Skip a unigram already covered by a chosen bigram and vice versa.
            if any(term in chosen or chosen in term for chosen in label_terms):
                continue
            label_terms.append(term)
            if len(label_terms) == 3:
                break
        center = np.median(coords[members], axis=0)
        clusters.append({
            "label": " · ".join(label_terms),
            "x": round(float(center[0]), 4),
            "y": round(float(center[1]), 4),
            "n": int(len(members)),
        })
    return assignments, clusters


def build_dataset():
    papers, tracking_start, last_update = load_papers()
    topics = load_topics()
    ordered = sorted(papers.items(), key=lambda item: item[1]["published_date"], reverse=True)

    texts = [f"{p['title']}. {p['title']}. {p.get('abstract') or ''}" for _, p in ordered]
    coords, tfidf, terms = embed(texts)
    assignments, clusters = label_clusters(coords, tfidf, terms)

    author_counts = Counter(a for _, p in ordered for a in p.get("authors") or [])
    authors = [name for name, _ in author_counts.most_common()]
    author_index = {name: i for i, name in enumerate(authors)}

    records = []
    for row, (pid, paper) in enumerate(ordered):
        text = f"{paper['title']} {paper.get('abstract') or ''}"
        record = {
            "id": pid,
            "t": " ".join(paper["title"].split()),  # arXiv titles can contain line breaks
            "d": paper["published_date"],
            "a": [author_index[a] for a in paper.get("authors") or []],
            "k": [i for i, topic in enumerate(topics) if topic["pattern"].search(text)],
            "x": round(float(coords[row][0]), 4),
            "y": round(float(coords[row][1]), 4),
            "c": int(assignments[row]),
        }
        if paper.get("github_url"):
            record["g"] = paper["github_url"]
        records.append(record)

    return {
        "site": SITE,
        "generated": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M UTC"),
        "tracking_start": tracking_start,
        "last_update": last_update,
        "topics": [{"name": t["name"], "description": t["description"]} for t in topics],
        "authors": authors,
        "clusters": clusters,
        "papers": records,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--out", default=os.path.join(ROOT, "_site"), help="output folder")
    args = parser.parse_args()
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")

    dataset = build_dataset()
    if os.path.exists(args.out):
        shutil.rmtree(args.out)
    shutil.copytree(SITE_DIR, args.out)
    index_path = os.path.join(args.out, "index.html")
    with open(index_path, encoding="utf-8") as handle:
        page = handle.read()
    for placeholder, value in {
        "{{TITLE}}": SITE["title"],
        "{{SUBJECT}}": SITE["subject"],
        "{{REPO_URL}}": f"https://github.com/{SITE['repo']}",
        "{{SEARCH_HINT}}": SITE["search_hint"],
    }.items():
        page = page.replace(placeholder, html.escape(value))
    with open(index_path, "w", encoding="utf-8") as handle:
        handle.write(page)
    with open(os.path.join(args.out, "data.json"), "w", encoding="utf-8") as handle:
        json.dump(dataset, handle, ensure_ascii=False, separators=(",", ":"))
    logger.info(f"Wrote {len(dataset['papers'])} papers to {args.out}/data.json")


if __name__ == "__main__":
    main()
