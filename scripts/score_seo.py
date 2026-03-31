#!/usr/bin/env python3
from __future__ import annotations

import argparse
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from scripts.validate_article import extract_section


def bounded_score(value: int) -> int:
    return max(1, min(5, value))


def score_article(text: str) -> dict[str, int]:
    keyword = extract_section(text, "target keyword").strip().lower()
    body = extract_section(text, "complete article body")
    metadata = extract_section(text, "metadata options")
    links = extract_section(text, "internal link suggestions")

    headings = [line[4:].strip() for line in body.splitlines() if line.startswith("### ")]

    intent_match = 5 if keyword and keyword in body.lower() else 2
    topical_completeness = bounded_score(1 + len(headings))
    readability = bounded_score(1 + min(4, len([h for h in headings if len(h.split()) >= 4])))
    snippet = 4 if "title tag" in metadata.lower() and "meta description" in metadata.lower() else 2
    internal_fit = 4 if "- " in links else 2
    conversion = 4 if any(term in body.lower() for term in ["next step", "contact", "request", "book"]) else 2

    return {
        "Intent match": intent_match,
        "Topical completeness": topical_completeness,
        "Readability and structure": readability,
        "Snippet-worthiness": snippet,
        "Internal linking fit": internal_fit,
        "Conversion clarity": conversion,
    }


def render_scorecard(scores: dict[str, int]) -> str:
    total = sum(scores.values())
    max_total = len(scores) * 5
    lines = ["# SEO Scorecard", "", "| Dimension | Score (1-5) |", "| --- | --- |"]
    for dimension, score in scores.items():
        lines.append(f"| {dimension} | {score} |")
    lines += ["", f"**Total:** {total}/{max_total}"]
    return "\n".join(lines)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Score an article against SEO rubric dimensions")
    parser.add_argument("article_path", help="Path to markdown article")
    parser.add_argument("--output", help="Optional output report path")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    article_path = Path(args.article_path)
    text = article_path.read_text(encoding="utf-8")
    report = render_scorecard(score_article(text))

    if args.output:
        out = Path(args.output)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(report + "\n", encoding="utf-8")
        print(out)
    else:
        print(report)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
