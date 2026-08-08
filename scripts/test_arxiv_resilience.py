#!/usr/bin/env python3
"""Regression tests for the resilient arXiv update workflow."""

import datetime
import json
import logging
import os
import sys
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SCRIPTS_DIR = PROJECT_ROOT / "scripts"
sys.path.insert(0, str(PROJECT_ROOT))
sys.path.insert(0, str(SCRIPTS_DIR))

import main as cli_main
import arxiv_crawler
from arxiv_crawler import (
    ARXIV_API_URL,
    ArxivCrawler,
    ArxivResponseError,
    ArxivTemporaryError,
    Paper,
)
from readme_generator import ReadmeGenerator


ATOM_FEED = b"""<?xml version="1.0" encoding="UTF-8"?>
<feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:arxiv="http://arxiv.org/schemas/atom">
  <entry>
    <title>Reliable Gaussian Splatting</title>
    <summary>A test paper about gaussian splatting.</summary>
    <author><name>Test Author</name></author>
    <link rel="alternate" href="https://arxiv.org/abs/2608.00001v1" />
    <link title="pdf" href="https://arxiv.org/pdf/2608.00001v1" />
    <published>2026-08-08T00:00:00Z</published>
    <category term="cs.CV" />
  </entry>
</feed>
"""

EMPTY_ATOM_FEED = b"""<?xml version="1.0" encoding="UTF-8"?>
<feed xmlns="http://www.w3.org/2005/Atom" />
"""


class FakeResponse:
    def __init__(self, status_code, content=b"", headers=None):
        self.status_code = status_code
        self.content = content
        self.headers = headers or {}


def make_crawler(output_dir=None):
    crawler = object.__new__(ArxivCrawler)
    crawler.logger = logging.getLogger("test_arxiv_resilience")
    crawler.search_query = 'abs:"gaussian splatting"'
    crawler.user_config = {"search": {"max_results": 500}}
    crawler.date_start = None
    crawler.date_end = None
    crawler.fetch_citations = False
    crawler.fetch_bibtex = False
    crawler.common_keywords = []
    crawler.category_keywords = {}
    crawler.output_dir = Path(output_dir) if output_dir else Path("data")
    return crawler


def make_paper():
    return Paper(
        title="Reliable Gaussian Splatting",
        authors=["Test Author"],
        abstract="A test abstract.",
        arxiv_url="https://arxiv.org/abs/2608.00001v1",
        pdf_url="https://arxiv.org/pdf/2608.00001v1",
        published_date="2026-08-08",
        categories=["cs.CV"],
    )


def search_args():
    return SimpleNamespace(
        citations=False,
        bibtex=False,
        date_from=None,
        date_to=None,
        recent=None,
        max_results=500,
    )


class ArxivRequestTests(unittest.TestCase):
    def test_https_success_parses_paper_and_uses_identifying_headers(self):
        crawler = make_crawler()
        response = FakeResponse(200, ATOM_FEED)

        with patch.object(arxiv_crawler.requests, "get", return_value=response) as request:
            papers = crawler.search_papers(max_results=500)

        self.assertEqual(len(papers), 1)
        self.assertEqual(papers[0].title, "Reliable Gaussian Splatting")
        request.assert_called_once()
        call_args, call_kwargs = request.call_args
        self.assertEqual(call_args[0], ARXIV_API_URL)
        self.assertTrue(ARXIV_API_URL.startswith("https://"))
        self.assertIn("awesome-gaussians", call_kwargs["headers"]["User-Agent"])
        self.assertEqual(call_kwargs["timeout"], (10, 60))

    def test_429_honors_retry_after_then_succeeds(self):
        crawler = make_crawler()
        responses = [
            FakeResponse(429, headers={"Retry-After": "12"}),
            FakeResponse(200, ATOM_FEED),
        ]

        with patch.object(arxiv_crawler.requests, "get", side_effect=responses) as request:
            with patch.object(arxiv_crawler.time, "sleep") as sleep:
                papers = crawler.search_papers(max_results=500)

        self.assertEqual(len(papers), 1)
        self.assertEqual(request.call_count, 2)
        sleep.assert_called_once_with(12.0)

    def test_repeated_rate_limits_are_bounded_and_never_create_data(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            for repetition in range(10):
                with self.subTest(repetition=repetition):
                    crawler = make_crawler(temp_dir)
                    with patch.object(
                        arxiv_crawler.requests,
                        "get",
                        return_value=FakeResponse(429),
                    ) as request:
                        with patch.object(arxiv_crawler.time, "sleep"):
                            with self.assertRaises(ArxivTemporaryError):
                                crawler.search_papers(max_results=500)
                    self.assertEqual(request.call_count, 4)
                    self.assertEqual(list(Path(temp_dir).glob("papers_*.json")), [])

    def test_5xx_and_timeout_become_temporary_failures(self):
        crawler = make_crawler()
        scenarios = (
            FakeResponse(503),
            arxiv_crawler.requests.Timeout("timed out"),
        )
        for scenario in scenarios:
            with self.subTest(scenario=type(scenario).__name__):
                with patch.object(
                    arxiv_crawler.requests,
                    "get",
                    side_effect=scenario if isinstance(scenario, Exception) else None,
                    return_value=None if isinstance(scenario, Exception) else scenario,
                ):
                    with patch.object(arxiv_crawler.time, "sleep"):
                        with self.assertRaises(ArxivTemporaryError):
                            crawler.search_papers(max_results=500)

    def test_malformed_xml_is_a_real_error(self):
        crawler = make_crawler()
        with patch.object(
            arxiv_crawler.requests,
            "get",
            return_value=FakeResponse(200, b"not xml"),
        ):
            with self.assertRaises(ArxivResponseError):
                crawler.search_papers(max_results=500)


class PersistenceTests(unittest.TestCase):
    def test_atomic_save_writes_valid_non_empty_json(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            crawler = make_crawler(temp_dir)
            output_file = crawler.save_papers([make_paper()])

            with output_file.open(encoding="utf-8") as saved_file:
                records = json.load(saved_file)
            self.assertEqual(len(records), 1)
            self.assertEqual(records[0]["title"], "Reliable Gaussian Splatting")
            self.assertEqual(list(Path(temp_dir).glob("*.tmp")), [])

    def test_empty_save_does_not_overwrite_existing_file(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            crawler = make_crawler(temp_dir)
            today = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d")
            output_file = Path(temp_dir) / f"papers_{today}.json"
            output_file.write_text('[{"preserved": true}]', encoding="utf-8")

            with self.assertRaises(ValueError):
                crawler.save_papers([])

            self.assertEqual(
                json.loads(output_file.read_text(encoding="utf-8")),
                [{"preserved": True}],
            )

    def test_invalid_record_does_not_create_a_file(self):
        class InvalidPaper:
            def to_dict(self):
                return {"title": "missing required fields"}

        with tempfile.TemporaryDirectory() as temp_dir:
            crawler = make_crawler(temp_dir)
            with self.assertRaises(ValueError):
                crawler.save_papers([InvalidPaper()])
            self.assertEqual(list(Path(temp_dir).glob("papers_*.json")), [])


class CliExitCodeTests(unittest.TestCase):
    def test_no_results_returns_3_without_saving(self):
        with patch.object(arxiv_crawler, "ArxivCrawler") as crawler_class:
            crawler_class.return_value.search_papers.return_value = []
            result = cli_main.cmd_search(search_args())

        self.assertEqual(result, 3)
        crawler_class.return_value.save_papers.assert_not_called()

    def test_temporary_failure_returns_75_without_saving(self):
        with patch.object(arxiv_crawler, "ArxivCrawler") as crawler_class:
            crawler_class.return_value.search_papers.side_effect = ArxivTemporaryError("429")
            result = cli_main.cmd_search(search_args())

        self.assertEqual(result, 75)
        crawler_class.return_value.save_papers.assert_not_called()

    def test_unexpected_failure_returns_1(self):
        with patch.object(arxiv_crawler, "ArxivCrawler") as crawler_class:
            crawler_class.return_value.search_papers.side_effect = ArxivResponseError("bad XML")
            result = cli_main.cmd_search(search_args())

        self.assertEqual(result, 1)


class ReadmeFallbackTests(unittest.TestCase):
    def test_uses_latest_dated_valid_file_not_mtime(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            data_dir = Path(temp_dir)
            valid_record = make_paper().to_dict()
            (data_dir / "papers_2026-08-06.json").write_text(
                json.dumps([valid_record]), encoding="utf-8"
            )
            (data_dir / "papers_2026-08-07.json").write_text("[]", encoding="utf-8")
            invalid_record = dict(valid_record)
            invalid_record["authors"] = "not a list"
            (data_dir / "papers_2026-08-08.json").write_text(
                json.dumps([invalid_record]), encoding="utf-8"
            )
            (data_dir / "papers_2026-08-09.json").write_text("{broken", encoding="utf-8")

            generator = object.__new__(ReadmeGenerator)
            generator.logger = logging.getLogger("test_readme_fallback")
            generator.data_dir = data_dir
            papers = generator.load_latest_papers()

            self.assertEqual(papers, [valid_record])
            self.assertEqual(generator.latest_data_file.name, "papers_2026-08-06.json")

    def test_valid_data_generates_readme_end_to_end(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            data_dir = root / "data"
            data_dir.mkdir()
            keywords = {
                "categories": {
                    "Test Category": {
                        "description": "Test papers",
                        "keywords": ["gaussian"],
                    }
                },
                "common_keywords": {"keywords": ["gaussian"]},
            }
            (data_dir / "keywords.json").write_text(
                json.dumps(keywords), encoding="utf-8"
            )
            (data_dir / "papers_2026-08-08.json").write_text(
                json.dumps([make_paper().to_dict()]), encoding="utf-8"
            )
            (root / "README_template.md").write_text(
                "# Test\n{{NAVIGATION}}\n{{TABLE_OF_CONTENTS}}\n"
                "{{LATEST_PAPERS}}\n{{CATEGORIZED_PAPERS}}\n{{LAST_UPDATE}}\n",
                encoding="utf-8",
            )

            previous_cwd = Path.cwd()
            try:
                os.chdir(root)
                generator = ReadmeGenerator()
                self.assertTrue(generator.generate_readme())
                readme = (root / "README.md").read_text(encoding="utf-8")
            finally:
                os.chdir(previous_cwd)

            self.assertIn("Reliable Gaussian Splatting", readme)
            self.assertNotIn("{{CATEGORIZED_PAPERS}}", readme)


class WorkflowPolicyTests(unittest.TestCase):
    def test_workflow_maps_only_expected_exit_codes_to_successful_skip(self):
        workflow = (PROJECT_ROOT / ".github/workflows/update-papers.yml").read_text(
            encoding="utf-8"
        )
        self.assertIn("3|75)", workflow)
        self.assertIn('fresh_data=false', workflow)
        self.assertIn('exit "$crawl_exit"', workflow)
        self.assertIn("jq -e", workflow)
        self.assertIn("length > 0", workflow)
        self.assertIn("steps.crawl.outputs.fresh_data == 'true'", workflow)


if __name__ == "__main__":
    unittest.main()
