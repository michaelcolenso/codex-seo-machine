#!/usr/bin/env python3
from __future__ import annotations

import argparse
import sys
import shutil
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from scripts.build_brief import create_brief_markdown
from scripts.extract_internal_links import render_report, suggest_links
from scripts.run_task import slugify
from scripts.score_seo import render_scorecard, score_article
from scripts.validate_article import validate_article_text


def create_article_markdown(topic: str, keyword: str) -> str:
    return f"""# {topic}

## working title
{topic}: a practical implementation guide

## target keyword
{keyword}

## intent statement
Help the reader implement {keyword} with a concrete sequence of actions and decision criteria.

## complete article body
If you searched for **{keyword}**, you likely need a clear path you can execute this week. This guide focuses on practical decisions, sequencing, and risk reduction.

### Define the outcome and constraints before choosing tactics
Start by documenting the business outcome, available resources, and non-negotiable constraints. This prevents random activity and keeps execution aligned.

### Build an execution sequence that reduces rework
Move from research to structure to production to validation. Example: build a brief first, draft second, then validate against contracts before publishing.

### Add quality gates before publication
Create checklists for required sections, evidence review, and CTA clarity. Include a final next step so readers know what action to take.

### Common mistakes and how to avoid them
Avoid generic headings, unsupported claims, and vague recommendations. Use concrete examples tied to likely implementation scenarios.

### Recommended next step
Run a small pilot on one topic, measure quality against the rubric, then scale once results are repeatable. If you need implementation support, contact the team to request a scoped audit.

## metadata options
- Title tag option 1: {topic}: practical step-by-step guide
- Title tag option 2: {topic} checklist for small teams
- Meta description option 1: Learn how to execute {keyword} with a clear workflow, quality checks, and practical examples.
- Meta description option 2: A no-fluff implementation guide to {keyword}, including sequencing, pitfalls, and next steps.

## internal link suggestions
- Link to related brief and optimization reports in `/workspace/reports`.

## author notes
- No external statistics included; examples are process-based and implementation-oriented.

## revision risks
- Context files are placeholders; refine tone and offer framing after brand context is fully populated.
"""


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run an end-to-end local SEO workflow execution")
    parser.add_argument("--topic", default="SEO workflow implementation for small teams", help="Topic for the full run")
    parser.add_argument("--keyword", help="Primary keyword (defaults to topic)")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    topic = args.topic
    keyword = args.keyword or topic
    slug = slugify(topic)

    brief_path = Path(f"workspace/briefs/{slug}-brief.md")
    draft_path = Path(f"workspace/drafts/{slug}.md")
    score_path = Path(f"workspace/reports/{slug}-seo-score.md")
    links_path = Path(f"workspace/reports/{slug}-internal-links.md")
    publish_path = Path(f"workspace/published/{slug}.md")

    brief_path.parent.mkdir(parents=True, exist_ok=True)
    draft_path.parent.mkdir(parents=True, exist_ok=True)
    score_path.parent.mkdir(parents=True, exist_ok=True)
    publish_path.parent.mkdir(parents=True, exist_ok=True)

    brief_path.write_text(create_brief_markdown(topic, keyword, "Operators and marketers running SEO content systems"), encoding="utf-8")
    draft_path.write_text(create_article_markdown(topic, keyword), encoding="utf-8")

    validation = validate_article_text(draft_path.read_text(encoding="utf-8"))
    if not validation.passed:
        print("Validation failed:")
        for error in validation.errors:
            print(f"- {error}")
        return 1

    score_path.write_text(render_scorecard(score_article(draft_path.read_text(encoding="utf-8"))) + "\n", encoding="utf-8")
    links_path.write_text(render_report(draft_path, suggest_links(draft_path)), encoding="utf-8")
    shutil.copy2(draft_path, publish_path)

    print("Full run complete")
    print(f"- Brief: {brief_path}")
    print(f"- Draft: {draft_path}")
    print(f"- SEO score report: {score_path}")
    print(f"- Internal links report: {links_path}")
    print(f"- Published draft: {publish_path}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
