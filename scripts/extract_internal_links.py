#!/usr/bin/env python3
from __future__ import annotations

import argparse
import sys
import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from scripts.validate_article import extract_section


STOPWORDS = {
    "the",
    "and",
    "for",
    "with",
    "from",
    "that",
    "this",
    "your",
    "into",
    "how",
    "what",
    "why",
    "when",
    "where",
}


def tokenize(value: str) -> set[str]:
    tokens = re.findall(r"[a-zA-Z]{3,}", value.lower())
    return {token for token in tokens if token not in STOPWORDS}


def candidate_files(root: Path, current: Path) -> list[Path]:
    candidates: list[Path] = []
    for folder in [root / "workspace/published", root / "workspace/drafts", root / "workspace/briefs"]:
        if not folder.exists():
            continue
        for path in folder.glob("*.md"):
            if path.resolve() != current.resolve():
                candidates.append(path)
    return sorted(candidates)


def suggest_links(article_path: Path, limit: int = 5) -> list[tuple[str, str, int]]:
    root = Path(__file__).resolve().parents[1]
    current_text = article_path.read_text(encoding="utf-8")
    keyword = extract_section(current_text, "target keyword")
    body = extract_section(current_text, "complete article body")
    current_terms = tokenize(keyword + " " + body)

    scored: list[tuple[str, str, int]] = []
    for candidate in candidate_files(root, article_path):
        content = candidate.read_text(encoding="utf-8")
        title = content.splitlines()[0].lstrip("# ").strip() if content.strip() else candidate.stem
        terms = tokenize(title + " " + content[:600])
        overlap = len(current_terms & terms)
        if overlap > 0:
            scored.append((title, candidate.relative_to(root).as_posix(), overlap))

    scored.sort(key=lambda item: item[2], reverse=True)
    return scored[:limit]


def render_report(article_path: Path, suggestions: list[tuple[str, str, int]]) -> str:
    lines = [f"# Internal Link Suggestions for {article_path.name}", "", "## Suggested links"]
    if not suggestions:
        lines.append("- No strong candidates found yet. Add more published content to improve suggestions.")
    else:
        for title, path, overlap in suggestions:
            lines.append(f"- [{title}]({path}) — relevance overlap score: {overlap}")
    return "\n".join(lines) + "\n"


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Generate internal link suggestions from local workspace artifacts")
    parser.add_argument("article_path", help="Path to markdown article")
    parser.add_argument("--output", help="Optional output report path")
    parser.add_argument("--limit", type=int, default=5, help="Maximum number of suggestions")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    article_path = Path(args.article_path)
    report = render_report(article_path, suggest_links(article_path, limit=args.limit))

    if args.output:
        out = Path(args.output)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(report, encoding="utf-8")
        print(out)
    else:
        print(report)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
