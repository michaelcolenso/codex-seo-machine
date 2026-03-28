# SEO Machine Codex

Codex-native version of SEO Machine: a structured workspace for researching, writing, optimizing, and publishing long-form SEO content.

## What this is

This repository mirrors the practical workflow style of the original SEO Machine project, adapted for Codex execution:

- Task-driven operations from `tasks/` (research, write, optimize, publish)
- Reusable role prompts in `prompts/` (planner, researcher, writer, editor, CRO reviewer)
- Quality and output contracts in `system/`
- Script helpers for bootstrapping tasks and validating output in `scripts/`
- Standardized artifact storage in `workspace/` folders

## Quick start

1. Read `AGENTS.md` for operating and quality rules.
2. Populate business context in `context/`.
3. List available task commands:
   ```bash
   python scripts/run_task.py --list
   ```
4. Run a task brief using canonical task names or slash aliases:
   ```bash
   python scripts/run_task.py research-topic "best podcast hosting for small creators"
   python scripts/run_task.py /write "best podcast hosting for small creators"
   ```
5. Save generated outputs in the destination path printed by the script.
6. Run sanity tests when changing scripts:
   ```bash
   make test
   ```
7. Execute a full local workflow run (brief -> draft -> validate -> score -> link suggestions -> publish copy):
   ```bash
   make full-run
   ```
8. Run full verification (tests + full run + validator):
   ```bash
   make check
   ```

## Command aliases

`run_task.py` supports friendly aliases inspired by command-style workflows:

- `/research` → `research-topic`
- `/write` → `write-article`
- `/rewrite` → `rewrite-article`
- `/optimize` → `optimize-article`
- `/analyze` → `analyze-existing`
- `/performance` → `performance-review`
- `/cluster` → `build-topic-cluster`
- `/publish` → `publish-draft`


## Output paths

`run_task.py` writes a destination hint based on task type:

- Research: `workspace/briefs/{slug}-brief.md`
- Write: `workspace/drafts/{slug}.md`
- Rewrite: `workspace/drafts/{slug}-rewrite.md`
- Optimize: `workspace/reports/{slug}-optimization.md`
- Analyze: `workspace/reports/{slug}-analysis.md`
- Performance: `workspace/reports/{slug}-performance.md`
- Cluster: `workspace/reports/{slug}-cluster.md`
- Publish: `workspace/published/{slug}.md`

## Repository structure

- `system/` operating rules, output contracts, quality checklist
- `context/` brand, audience, offers, and editorial knowledge
- `tasks/` executable markdown task briefs
- `prompts/` role-specific guidance
- `workflows/` multi-stage workflow recipes
- `scripts/` orchestration and validation helpers
- `templates/` reusable artifact templates
- `workspace/` generated work artifacts (`briefs/`, `research/`, `drafts/`, `published/`, `reports/`)

## Core workflow

1. Read relevant files in `context/` + `system/`.
2. Execute the chosen task contract from `tasks/`.
3. Create/update the brief in `workspace/briefs/`.
4. Produce draft or optimization output.
5. Validate against `system/output-contracts.md` and `system/quality-bar.md`.
6. Revise until the artifact passes.

## Helpful files to read first

- `AGENTS.md`
- `system/output-contracts.md`
- `system/quality-bar.md`
- `tasks/research-topic.md`
- `tasks/write-article.md`

## Automation scripts

- `scripts/build_brief.py` generates a research-brief scaffold aligned to the output contract.
- `scripts/validate_article.py` checks required article sections and quality heuristics.
- `scripts/score_seo.py` scores an article against rubric dimensions and can write a report.
- `scripts/extract_internal_links.py` suggests internal links from local workspace artifacts.
- `scripts/full_run.py` executes an end-to-end local run and writes artifacts into `workspace/`.
