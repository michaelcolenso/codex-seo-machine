# Task: Analyze Existing

## Goal
Audit a published or draft article and produce an actionable improvement plan that conforms to the Audit Contract in `system/output-contracts.md`.

## Required Inputs
- Path to the existing article (markdown, HTML, or pasted text)
- Target keyword (if known) or current ranking keyword set
- Recent performance signal, if available (sessions, queries, position, citations)
- Business context: relevant `context/` files (audience, offers, brand voice)

## Required Output
Save to `/workspace/reports/<slug>-analysis.md`

Must include (per Audit Contract):
1. Current state summary — what the article does well, what it does not
2. Issues by severity (P0 blocking publication, P1 affecting performance, P2 polish)
3. Exact fixes recommended, scoped at the section or sentence level — not vague advice
4. Revised metadata (title tag + meta description options)
5. Internal linking recommendations — incoming and outgoing, with anchor text
6. Priority order — a numbered sequence the writer can execute top-to-bottom

## Analysis Checks
- Intent match: does the article answer the query the keyword represents
- Structural coverage: H2/H3 hierarchy, scannability, snippet-friendly passages
- Information gain: what does this piece say that the SERP top 5 do not
- Evidence quality: claims, statistics, and examples — supported or hand-waved
- Conversion path: clear CTA, mid-article hooks, alignment to lifecycle stage
- AEO readiness: quotable passages, FAQ self-containment, schema fitness
- Quality bar failures from `system/quality-bar.md`

## Acceptance Criteria
- Every issue is tagged with severity and paired with a concrete fix
- Priority order is executable without further scoping
- Metadata revisions are written, not just suggested as a direction
- Report passes a self-check against the Audit Contract before saving

## Post-Analysis
Recommend the next task: typically `/rewrite` for P0-heavy reports, `/optimize` for P1/P2-heavy reports, or `/performance` if the issue is distribution rather than the page itself.
