#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path

REQUIRED_HEADINGS = [
    "working title",
    "target keyword",
    "intent statement",
    "complete article body",
    "metadata options",
    "internal link suggestions",
    "author notes",
    "revision risks",
]
GENERIC_HEADINGS = {"introduction", "conclusion", "overview", "summary"}
JARGON_TERMS = {"synergy", "leverage", "bandwidth", "paradigm", "best-in-class"}
CTA_TERMS = {"next step", "contact", "book", "start", "request", "demo"}


@dataclass
class ValidationResult:
    passed: bool
    errors: list[str]
    warnings: list[str]


def extract_section(text: str, heading: str) -> str:
    pattern = rf"(?ims)^##\s+{re.escape(heading)}\s*$\n(.*?)(?=^##\s+|\Z)"
    match = re.search(pattern, text)
    return match.group(1).strip() if match else ""


def validate_article_text(text: str) -> ValidationResult:
    lowered = text.lower()
    errors: list[str] = []
    warnings: list[str] = []

    for heading in REQUIRED_HEADINGS:
        if not re.search(rf"(?im)^##\s+{re.escape(heading)}\s*$", lowered):
            errors.append(f"Missing required section: {heading}")

    if errors:
        return ValidationResult(False, errors, warnings)

    keyword = extract_section(text, "target keyword").splitlines()[0].strip()
    body = extract_section(text, "complete article body")

    body_headings = re.findall(r"(?im)^###\s+(.+?)\s*$", body)
    normalized_headings = [h.strip().lower() for h in body_headings]

    if len(body_headings) < 3:
        errors.append("Article body must include at least three descriptive H3 headings")

    duplicates = sorted({h for h in normalized_headings if normalized_headings.count(h) > 1})
    if duplicates:
        errors.append(f"Duplicate body headings detected: {', '.join(duplicates)}")

    generic = [h for h in normalized_headings if h in GENERIC_HEADINGS]
    if generic:
        errors.append(f"Generic body headings detected: {', '.join(generic)}")

    first_paragraph = ""
    body_blocks = [block.strip() for block in body.split("\n\n") if block.strip()]
    for block in body_blocks:
        if not block.startswith("###"):
            first_paragraph = block
            break

    if keyword and keyword.lower() not in first_paragraph.lower():
        errors.append("Introduction does not clearly align to target keyword intent")

    if "example" not in body.lower():
        errors.append("No concrete examples found in article body")

    if not any(term in body.lower() for term in CTA_TERMS):
        errors.append("No clear CTA language found in article body")

    claim_pattern = re.compile(r"\b\d+(?:\.\d+)?%\b|\b\d+x\b", re.IGNORECASE)
    if claim_pattern.search(body):
        warnings.append("Quantified claims detected; verify evidence and citation support")

    jargon_hits = [term for term in JARGON_TERMS if term in body.lower()]
    if len(jargon_hits) >= 2:
        warnings.append(f"Potentially excessive jargon terms found: {', '.join(sorted(jargon_hits))}")

    return ValidationResult(not errors, errors, warnings)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Validate an article against repository quality requirements")
    parser.add_argument("article_path", help="Path to markdown article")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    article_path = Path(args.article_path)
    text = article_path.read_text(encoding="utf-8")
    result = validate_article_text(text)

    print(f"Validation file: {article_path}")
    print(f"Status: {'PASS' if result.passed else 'FAIL'}")

    if result.errors:
        print("\nErrors:")
        for error in result.errors:
            print(f"- {error}")

    if result.warnings:
        print("\nWarnings:")
        for warning in result.warnings:
            print(f"- {warning}")

    return 0 if result.passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
