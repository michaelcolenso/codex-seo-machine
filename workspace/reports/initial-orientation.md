# Initial Orientation Report

## objective
Summarize core operating constraints and task requirements after reviewing priority repository files.

## audience
Repo operators and content agents preparing to execute SEO content tasks in this workspace.

## target keyword
N/A (repository orientation task)

## search intent
Navigational/instructional: understand how to execute research and writing tasks correctly in this repo.

## outline
1. Output contract requirements
2. Quality failure conditions
3. Research task output requirements
4. Writing task output requirements
5. Execution checklist for next run

## final artifact
### 1) Output contract requirements
- **Research briefs** must include keyword, intent, audience, pains, questions, outline, differentiation angle, conversion opportunities, assumptions, and recommended next action.
- **Articles** must include working title, target keyword, intent statement, complete body, metadata options, internal links, author notes, and revision risks.
- **Audits** must include summary, severity-ranked issues, exact fixes, revised metadata, linking recommendations, and priority order.

### 2) Quality failure conditions to avoid
- **Research** fails if intent is vague, differentiation is missing, or conversion path is absent.
- **Writing** fails if intro misses intent, headings are generic, sections repeat, claims lack support, content feels like filler, or examples are missing.
- **SEO** fails if keyword/targeting is unclear, title lacks specificity, semantic coverage is weak, links are weak, or meta description is uncompelling.
- **Editorial** fails if tone conflicts with brand, jargon is excessive, CTA is unclear, or information gain is weak.

### 3) Research task requirements (`tasks/research-topic.md`)
- Save to `/workspace/briefs/<slug>-brief.md`.
- Include 10 required sections: keyword, intent, pain points, questions, competitor patterns, differentiation, angle, outline, conversion opportunities, and evidence.

### 4) Writing task requirements (`tasks/write-article.md`)
- Save to `/workspace/drafts/<slug>.md`.
- Use approved brief + relevant context + brand/editorial guidance.
- Ensure intent-aligned intro, descriptive headings, concrete specifics/examples, natural keyword use, and CTA placement.
- Post-write deliverables: title tags, meta descriptions, internal links, and FAQ when justified.

### 5) Execution checklist for next run
1. Read relevant `context/` files + `system/` constraints.
2. Select task in `tasks/` and confirm required output path.
3. Draft artifact using the required fields/sections.
4. Validate against both `system/output-contracts.md` and `system/quality-bar.md` before finalizing.

## unresolved assumptions
- No specific target keyword or topic was provided in this turn.
- No brand-voice file was explicitly identified yet from `context/`.

## next recommended step
Provide a target topic/keyword, then run the `research-topic` task to produce `/workspace/briefs/<slug>-brief.md` before drafting an article.
