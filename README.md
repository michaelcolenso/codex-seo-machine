# SEO Machine Codex

Codex-first SEO content workspace for research, briefing, writing, optimization, and publishing.

## Quick start
1. Read `AGENTS.md` for operating rules.
2. Add business context in `context/`.
3. Run a task brief via:
   - `python scripts/run_task.py research-topic "best podcast hosting for small creators"`
   - `python scripts/run_task.py write-article "best podcast hosting for small creators"`
4. Save outputs into the `workspace/` paths specified by each task.

## Repository structure

- `system/` operating rules, output contracts, quality checklist
- `context/` brand, audience, offer, and editorial knowledge
- `tasks/` executable markdown task briefs
- `prompts/` role-specific guidance (researcher, writer, optimizer, etc.)
- `workflows/` multi-stage workflow recipes
- `scripts/` light orchestration and validation helpers
- `templates/` reusable artifact templates
- `workspace/` generated work artifacts
- `data_sources/` optional integrations and adapters

## Core workflow
1. Read relevant files in `context/` + `system/`.
2. Run the chosen task in `tasks/`.
3. Create/update brief in `workspace/briefs/`.
4. Generate draft or optimization output.
5. Validate against `system/output-contracts.md` and `system/quality-bar.md`.

## Initial high-priority files
- `README.md`
- `AGENTS.md`
- `system/output-contracts.md`
- `tasks/research-topic.md`
- `tasks/write-article.md`
