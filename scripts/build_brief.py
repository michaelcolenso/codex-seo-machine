#!/usr/bin/env python3
from __future__ import annotations

import argparse
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from scripts.run_task import slugify


def create_brief_markdown(topic: str, keyword: str, audience: str) -> str:
    outline = [
        "Problem framing and who this is for",
        "Decision criteria and tradeoffs",
        "Step-by-step implementation guidance",
        "Common mistakes and how to avoid them",
        "Recommended next action",
    ]
    outline_md = "\n".join(f"{i + 1}. {item}" for i, item in enumerate(outline))

    return f"""# Research Brief: {topic}

## objective
Produce an actionable research brief that can be used to draft an intent-matched article.

## audience
{audience}

## target keyword
{keyword}

## search intent
Informational with commercial investigation: reader wants practical guidance and a clear path to action.

## outline
{outline_md}

## final artifact
### keyword
- Primary keyword: {keyword}
- Secondary keywords:
  - {keyword} checklist
  - {keyword} best practices
  - {keyword} mistakes

### intent
- Primary intent: informational
- Secondary intent: commercial investigation

### audience
- Small-to-mid sized operators who need practical, low-fluff guidance.

### pains
- Unclear starting point
- Conflicting advice
- Risk of wasted effort from generic playbooks

### questions
- What should be done first?
- What sequence produces reliable outcomes?
- Which mistakes are most costly?

### outline
{outline_md}

### differentiation angle
- Focus on implementation details, decision criteria, and failure-avoidance—not generic definitions.

### conversion opportunities
- Invite reader to run a scoped audit or request implementation support.

### assumptions
- Context files are placeholders, so the brief uses neutral tone and non-brand-specific recommendations.
- No proprietary performance data is available.

### recommended next action
Draft the article in `/workspace/drafts/{slugify(topic)}.md` and run `scripts/validate_article.py` before publishing.

## unresolved assumptions
- Exact product positioning and voice preferences are not yet populated in `context/` files.

## next recommended step
Write the article from this brief and validate it against the quality bar.
"""


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Generate a research brief scaffold")
    parser.add_argument("topic", help="Topic or working title")
    parser.add_argument("--keyword", help="Primary keyword (defaults to topic)")
    parser.add_argument(
        "--audience",
        default="Operators and marketers seeking practical SEO workflow execution guidance",
        help="Intended audience",
    )
    parser.add_argument("--output", help="Optional explicit output path")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    keyword = args.keyword or args.topic
    output = Path(args.output) if args.output else Path(f"workspace/briefs/{slugify(args.topic)}-brief.md")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(create_brief_markdown(args.topic, keyword, args.audience), encoding="utf-8")
    print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
