# codex-seo-machine
Yes. The clean move is not to “port Claude Code files 1:1,” but to rebuild the repo as a Codex-first agent workspace.

seomachine is structured around:
	•	custom slash-command workflows like /research, /write, /optimize
	•	specialized agent roles
	•	context files for brand voice, style, SEO guidance
	•	optional Python-based data integrations for GA4, GSC, DataForSEO  ￼

For a Codex version, the right adaptation is:
	1.	replace Claude-specific command/agent conventions with prompt-driven runbooks
	2.	keep the workflow stages
	3.	make the repo executable by an agent working from:
	•	README.md
	•	AGENTS.md
	•	task briefs in /tasks
	•	structured templates in /system
	4.	treat the coding agent itself as the reasoning engine, instead of wiring in external LLM provider calls

What the Codex version should look like

Core idea

A Codex-native SEO workspace where the agent can:
	•	research a topic
	•	build a search-intent brief
	•	draft or rewrite long-form content
	•	optimize on-page SEO
	•	generate metadata and internal links
	•	review existing content performance
	•	output publish-ready markdown

That preserves the value of the original project while removing Claude-only assumptions. The original repo’s value is in its workflow design, not the model binding.  ￼

⸻

Recommended repo structure

seo-machine-codex/
├─ README.md
├─ AGENTS.md
├─ .env.example
├─ pyproject.toml
├─ requirements.txt
├─ Makefile
├─ system/
│  ├─ operating-principles.md
│  ├─ quality-bar.md
│  ├─ output-contracts.md
│  ├─ seo-rubric.md
│  └─ publishing-checklist.md
├─ context/
│  ├─ brand-voice.md
│  ├─ audience.md
│  ├─ offers.md
│  ├─ products.md
│  ├─ editorial-guidelines.md
│  ├─ seo-guidelines.md
│  ├─ examples-good.md
│  └─ examples-bad.md
├─ tasks/
│  ├─ research-topic.md
│  ├─ write-article.md
│  ├─ rewrite-article.md
│  ├─ optimize-article.md
│  ├─ analyze-existing.md
│  ├─ performance-review.md
│  ├─ build-topic-cluster.md
│  └─ publish-draft.md
├─ prompts/
│  ├─ planner.md
│  ├─ researcher.md
│  ├─ serp-analyst.md
│  ├─ writer.md
│  ├─ editor.md
│  ├─ seo-optimizer.md
│  ├─ meta-generator.md
│  ├─ internal-linker.md
│  └─ cro-reviewer.md
├─ workflows/
│  ├─ article-workflow.md
│  ├─ refresh-workflow.md
│  ├─ bofu-workflow.md
│  └─ cluster-workflow.md
├─ data_sources/
│  ├─ google_search_console/
│  ├─ google_analytics/
│  ├─ serp/
│  └─ utils/
├─ scripts/
│  ├─ run_task.py
│  ├─ validate_article.py
│  ├─ score_seo.py
│  ├─ extract_internal_links.py
│  └─ build_brief.py
├─ workspace/
│  ├─ topics/
│  ├─ research/
│  ├─ briefs/
│  ├─ drafts/
│  ├─ refreshes/
│  ├─ published/
│  └─ reports/
└─ templates/
   ├─ research-brief.md
   ├─ article-draft.md
   ├─ content-refresh.md
   ├─ metadata.md
   └─ topic-cluster.md


⸻

AGENTS.md for Codex

This is the most important file. It tells Codex how to behave.

Suggested AGENTS.md

# SEO Machine Codex - Agent Operating Manual

You are the build-and-execution agent for an SEO content system.

## Mission
Research, plan, write, optimize, and maintain high-quality SEO content that is useful to humans and aligned with business goals.

## Non-Negotiables
- Do not invent facts, statistics, quotes, or product claims.
- Use provided context files before drafting.
- Every article must satisfy search intent first, SEO second.
- Write clearly, concretely, and with strong information gain.
- Prefer original synthesis over generic filler.
- Do not ship outputs that fail the validation checklist.
- Preserve traceability: save each major artifact to the correct workspace directory.

## Operating Sequence
For any content task, follow this order:
1. Read relevant files in `/context` and `/system`
2. Read the requested task file in `/tasks`
3. Create or update a research brief in `/workspace/briefs`
4. Produce the requested artifact
5. Run validation against `/system/output-contracts.md` and `/system/quality-bar.md`
6. Revise until the output passes

## Agent Roles
When useful, simulate these roles internally:
- Planner
- Researcher
- SERP Analyst
- Writer
- Editor
- SEO Optimizer
- CRO Reviewer

## File Discipline
- Research notes go in `/workspace/research`
- Briefs go in `/workspace/briefs`
- Drafts go in `/workspace/drafts`
- Finalized content goes in `/workspace/published`
- Audits and reviews go in `/workspace/reports`

## Output Standard
Every major deliverable must include:
- objective
- audience
- target keyword
- search intent
- outline
- final artifact
- unresolved assumptions
- next recommended step


⸻

Task files Codex can execute

Instead of Claude slash commands, use task markdown files.

tasks/research-topic.md

# Task: Research Topic

## Goal
Create a research brief for the requested topic.

## Inputs
- Primary keyword
- Secondary/supporting keywords
- Audience
- Product/service context
- Existing content, if any

## Required Output
Save to `/workspace/briefs/<slug>-brief.md`

Include:
1. Primary keyword
2. Search intent
3. Audience pain points
4. Key questions to answer
5. Likely competitor content patterns
6. Differentiation opportunities
7. Recommended article angle
8. Recommended H2/H3 outline
9. Conversion opportunities
10. Sources or evidence collected

tasks/write-article.md

# Task: Write Article

## Goal
Write a long-form, SEO-oriented article from an approved brief.

## Required Inputs
- Brief from `/workspace/briefs`
- Relevant context files
- Brand voice and editorial guidelines

## Required Output
Save to `/workspace/drafts/<slug>.md`

## Article Requirements
- Strong intro aligned to search intent
- Clear structure with descriptive headings
- Useful examples, specifics, and concrete advice
- Natural use of target and related keywords
- No fluff
- Include CTA opportunities where relevant

## Post-Write
Also generate:
- title tag options
- meta description options
- suggested internal links
- FAQ section if justified

tasks/optimize-article.md

# Task: Optimize Article

## Goal
Improve an existing article for clarity, search intent, structure, and conversion.

## Required Output
1. Optimized draft
2. Change log
3. SEO improvement summary
4. Risk notes where claims need verification


⸻

Prompt files for internal role simulation

Codex does better when each role is explicit.

prompts/researcher.md

You are the Researcher.

Your job:
- identify the true search intent
- collect recurring questions
- identify gaps in existing content
- surface concrete information gain opportunities

Output:
- search intent
- audience pain points
- must-cover questions
- differentiation opportunities
- risks/unknowns

prompts/writer.md

You are the Writer.

Your job:
- turn the brief into a high-quality article
- prioritize clarity, usefulness, and specificity
- avoid generic SEO padding
- write with momentum and clean structure

Rules:
- every section must earn its place
- do not repeat the same point with new wording
- prefer examples, contrasts, and direct explanation

prompts/seo-optimizer.md

You are the SEO Optimizer.

Your job:
- improve title structure
- tighten heading hierarchy
- ensure search intent match
- identify missing semantic coverage
- improve snippet-worthiness
- recommend internal linking anchors

Do not:
- keyword stuff
- degrade readability
- make fake performance claims


⸻

Output contracts

This is what keeps the agent from hand-waving.

system/output-contracts.md

# Output Contracts

## Research Brief Contract
Must include:
- keyword
- intent
- audience
- pains
- questions
- outline
- differentiation angle
- conversion opportunities
- assumptions
- recommended next action

## Article Contract
Must include:
- working title
- target keyword
- intent statement
- complete article body
- metadata options
- internal link suggestions
- author notes
- revision risks

## Audit Contract
Must include:
- current state summary
- issues by severity
- exact fixes recommended
- revised metadata
- internal linking recommendations
- priority order


⸻

Validation checklist

This is where most agentic builds get stronger.

system/quality-bar.md

# Quality Bar

An output fails if any of the following are true:

## Research
- Search intent is vague
- No differentiation angle is identified
- No conversion path is considered

## Writing
- Introduction does not match likely user intent
- Headings are generic
- Sections are repetitive
- Claims are unsupported
- Article reads like AI filler
- No concrete examples or applied insight

## SEO
- Target keyword unclear
- Title lacks specificity
- Missing semantic subtopics
- Weak internal link opportunities
- Meta description not compelling

## Editorial
- Tone conflicts with brand voice
- Excessive jargon
- Unclear CTA
- No obvious information gain

Do not finalize until fixed.


⸻

CLI wrapper for Codex orchestration

A simple local wrapper helps.

scripts/run_task.py

Behavior:
	•	accepts a task name + slug/topic
	•	copies the right template
	•	tells Codex which files to read
	•	writes artifacts to the right folders

Example usage:

python scripts/run_task.py research-topic "best podcast hosting for small creators"
python scripts/run_task.py write-article "best podcast hosting for small creators"
python scripts/run_task.py optimize-article "how to start a podcast"

Minimal design

TASK_MAP = {
    "research-topic": "tasks/research-topic.md",
    "write-article": "tasks/write-article.md",
    "rewrite-article": "tasks/rewrite-article.md",
    "optimize-article": "tasks/optimize-article.md",
    "analyze-existing": "tasks/analyze-existing.md",
}

The script should:
	1.	slugify topic
	2.	create workspace paths
	3.	print a Codex execution brief like:
	•	read these files
	•	perform this task
	•	save outputs here
	•	validate against these files

⸻

The key adaptation from Claude Code to Codex

Here’s the important design difference:

Claude Code repo style
	•	native command files
	•	native agent files
	•	model-specific operating assumptions

Codex repo style
	•	AGENTS.md as behavioral control plane
	•	task markdown files as execution units
	•	prompt files as internal role specs
	•	scripts/templates to enforce deterministic outputs

That is the correct translation layer.

⸻

What to keep from the original repo

Keep these ideas from seomachine:
	•	research-first workflow
	•	specialized role decomposition
	•	strong context files
	•	structured workspace folders
	•	analysis + writing + optimization as separate passes
	•	optional data integrations for performance review  ￼

Drop or replace:
	•	Claude-specific command wiring
	•	Anthropic-specific setup assumptions from the original README prerequisites  ￼

⸻

Best next deliverable

The strongest next step is to create these 5 files first:
	1.	README.md
	2.	AGENTS.md
	3.	system/output-contracts.md
	4.	tasks/research-topic.md
	5.	tasks/write-article.md

Once those exist, Codex can already operate the repo.

