#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import unicodedata
from pathlib import Path

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

TASK_ALIASES = {
    "research": "research-topic",
    "write": "write-article",
    "rewrite": "rewrite-article",
    "optimize": "optimize-article",
    "analyze": "analyze-existing",
    "analyze-existing": "analyze-existing",
    "performance": "performance-review",
    "performance-review": "performance-review",
    "cluster": "build-topic-cluster",
    "build-topic-cluster": "build-topic-cluster",
    "publish": "publish-draft",
    "publish-draft": "publish-draft",
}

OUTPUT_HINTS = {
    "research-topic": "workspace/briefs/{slug}-brief.md",
    "write-article": "workspace/drafts/{slug}.md",
    "rewrite-article": "workspace/drafts/{slug}-rewrite.md",
    "optimize-article": "workspace/reports/{slug}-optimization.md",
    "analyze-existing": "workspace/reports/{slug}-analysis.md",
    "performance-review": "workspace/reports/{slug}-performance.md",
    "build-topic-cluster": "workspace/reports/{slug}-cluster.md",
    "publish-draft": "workspace/published/{slug}.md",
}


def slugify(value: str) -> str:
    normalized = unicodedata.normalize("NFKD", value)
    ascii_text = normalized.encode("ascii", "ignore").decode("ascii")
    cleaned = re.sub(r"[^a-zA-Z0-9]+", "-", ascii_text.lower()).strip("-")
    return cleaned or "untitled"


def normalize_task(task: str) -> str:
    cleaned = task.strip().lstrip("/").lower()
    if cleaned in TASK_MAP:
        return cleaned
    if cleaned in TASK_ALIASES:
        return TASK_ALIASES[cleaned]
    raise ValueError(f"Unknown task '{task}'. Run with --list to see valid options.")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Prepare Codex execution brief for a task")
    parser.add_argument("task", nargs="?", help="Task key (or alias such as /research)")
    parser.add_argument("topic", nargs="?", help="Topic or title")
    parser.add_argument("--list", action="store_true", dest="list_tasks", help="List tasks and aliases")
    return parser


def print_task_list() -> None:
    print("Canonical tasks:")
    for task in sorted(TASK_MAP):
        print(f"- {task}")
    print("\nAliases:")
    for alias, canonical in sorted(TASK_ALIASES.items()):
        print(f"- /{alias} -> {canonical}")


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    if args.list_tasks:
        print_task_list()
        return 0

    if not args.task or not args.topic:
        parser.error("task and topic are required unless using --list")

    try:
        task_name = normalize_task(args.task)
    except ValueError as error:
        parser.error(str(error))

    slug = slugify(args.topic)
    task_path = Path(TASK_MAP[task_name])
    output_path = Path(OUTPUT_HINTS[task_name].format(slug=slug))
    output_path.parent.mkdir(parents=True, exist_ok=True)

    print("Codex execution brief")
    print("=====================")
    print(f"Task: {task_name}")
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
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
