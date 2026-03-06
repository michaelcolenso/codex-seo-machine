#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path

try:
    from slugify import slugify
except ImportError:
    def slugify(value: str) -> str:
        return "-".join(value.lower().split())

TASK_MAP = {
    "research-topic": "tasks/research-topic.md",
    "write-article": "tasks/write-article.md",
    "rewrite-article": "tasks/rewrite-article.md",
    "optimize-article": "tasks/optimize-article.md",
    "analyze-existing": "tasks/analyze-existing.md",
    "performance-review": "tasks/performance-review.md",
    "build-topic-cluster": "tasks/build-topic-cluster.md",
    "publish-draft": "tasks/publish-draft.md",
}

OUTPUT_HINTS = {
    "research-topic": "workspace/briefs/{slug}-brief.md",
    "write-article": "workspace/drafts/{slug}.md",
    "rewrite-article": "workspace/refreshes/{slug}.md",
    "optimize-article": "workspace/refreshes/{slug}.md",
    "analyze-existing": "workspace/reports/{slug}-analysis.md",
    "performance-review": "workspace/reports/{slug}-performance.md",
    "build-topic-cluster": "workspace/reports/{slug}-cluster.md",
    "publish-draft": "workspace/published/{slug}.md",
}


def main() -> None:
    parser = argparse.ArgumentParser(description="Prepare Codex execution brief for a task")
    parser.add_argument("task", choices=sorted(TASK_MAP.keys()))
    parser.add_argument("topic", help="Topic or title")
    args = parser.parse_args()

    slug = slugify(args.topic)
    task_path = Path(TASK_MAP[args.task])
    output_path = Path(OUTPUT_HINTS[args.task].format(slug=slug))
    output_path.parent.mkdir(parents=True, exist_ok=True)

    print("Codex execution brief")
    print("=====================")
    print(f"Task: {args.task}")
    print(f"Topic: {args.topic}")
    print(f"Slug: {slug}")
    print("\nRead these files:")
    print(f"- {task_path}")
    print("- AGENTS.md")
    print("- system/output-contracts.md")
    print("- system/quality-bar.md")
    print("- context/brand-voice.md")
    print("- context/editorial-guidelines.md")
    print("\nPerform:")
    print("- Execute the task contract and produce the required artifact")
    print("\nSave output to:")
    print(f"- {output_path}")
    print("\nValidate against:")
    print("- system/output-contracts.md")
    print("- system/quality-bar.md")


if __name__ == "__main__":
    main()
