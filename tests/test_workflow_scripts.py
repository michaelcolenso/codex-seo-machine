import tempfile
import unittest
from pathlib import Path

from scripts.build_brief import create_brief_markdown
from scripts.extract_internal_links import render_report
from scripts.full_run import create_article_markdown
from scripts.score_seo import score_article
from scripts.validate_article import validate_article_text


class WorkflowScriptTests(unittest.TestCase):
    def test_build_brief_contains_required_sections(self) -> None:
        brief = create_brief_markdown("Test Topic", "test keyword", "test audience")
        self.assertIn("## objective", brief)
        self.assertIn("### keyword", brief)
        self.assertIn("### recommended next action", brief)

    def test_validate_article_passes_for_full_run_article(self) -> None:
        article = create_article_markdown("Test Topic", "test keyword")
        result = validate_article_text(article)
        self.assertTrue(result.passed, msg=f"Errors: {result.errors}")

    def test_score_article_returns_all_dimensions(self) -> None:
        article = create_article_markdown("Test Topic", "test keyword")
        scores = score_article(article)
        self.assertEqual(len(scores), 6)
        self.assertTrue(all(1 <= value <= 5 for value in scores.values()))

    def test_render_links_report_handles_empty_suggestions(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            article_path = Path(tmpdir) / "article.md"
            article_path.write_text("# Title\n", encoding="utf-8")
            report = render_report(article_path, [])
            self.assertIn("No strong candidates found yet", report)


if __name__ == "__main__":
    unittest.main()
