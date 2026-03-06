import subprocess
import sys
import unittest
from pathlib import Path

# Ensure repo root on sys.path for importing scripts module
REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from scripts.run_task import normalize_task, slugify  # noqa: E402


class RunTaskUnitTests(unittest.TestCase):
    def test_slugify_ascii_and_symbols(self) -> None:
        self.assertEqual(slugify("Café + SEO!!!"), "cafe-seo")

    def test_slugify_fallback_for_empty_input(self) -> None:
        self.assertEqual(slugify("   !!!   "), "untitled")

    def test_normalize_task_accepts_alias_and_slash(self) -> None:
        self.assertEqual(normalize_task("/write"), "write-article")
        self.assertEqual(normalize_task("research"), "research-topic")

    def test_normalize_task_rejects_unknown(self) -> None:
        with self.assertRaises(ValueError):
            normalize_task("/not-a-real-task")


class RunTaskCliSmokeTests(unittest.TestCase):
    def run_cli(self, *args: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, "scripts/run_task.py", *args],
            cwd=REPO_ROOT,
            text=True,
            capture_output=True,
            check=False,
        )

    def test_list_displays_aliases(self) -> None:
        result = self.run_cli("--list")
        self.assertEqual(result.returncode, 0)
        self.assertIn("Canonical tasks:", result.stdout)
        self.assertIn("/write -> write-article", result.stdout)

    def test_alias_execution_prints_expected_output_path(self) -> None:
        result = self.run_cli("/optimize", "Email marketing strategy")
        self.assertEqual(result.returncode, 0)
        self.assertIn("Task: optimize-article", result.stdout)
        self.assertIn("workspace/reports/email-marketing-strategy-optimization.md", result.stdout)


if __name__ == "__main__":
    unittest.main()
