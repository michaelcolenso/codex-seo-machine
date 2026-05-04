# Task: Publish Draft

## Goal
Take a validated draft from `/workspace/drafts/` and produce a publication-ready artifact in `/workspace/published/` with the metadata, links, and review state needed for a CMS handoff.

## Required Inputs
- Path to the draft in `/workspace/drafts/`
- Approved metadata (title tag, meta description) — pick one option from the draft's metadata section
- Approved internal links — pick from `/workspace/reports/<slug>-internal-links.md` and from any external link review
- Author or owner attribution
- Publication date target (today, scheduled, or evergreen)

## Required Output
Save to `/workspace/published/<slug>.md`

Must include:
1. Final article body — final headings, final prose, no draft-only notes
2. Final metadata block — chosen title tag, meta description, slug, canonical URL, publish date, author
3. Resolved internal links — every link target is a real URL or a real workspace path, not a placeholder
4. Schema recommendations — FAQPage, HowTo, Article, or Product as applicable, with the JSON-LD payload
5. Open Graph / social card copy — title, description, image filename
6. Featured-image brief — subject, style, alt text
7. Pre-publish checklist (signed) — see below
8. Post-publish checklist — see below

## Pre-Publish Checklist (must all be true)
- Validator passes: `scripts/validate_article.py`
- SEO score is recorded in `/workspace/reports/<slug>-seo-score.md`
- Internal links are resolved — no `<TBD>`, no broken paths
- Every quantified claim has a citation or has been removed
- Metadata is final, not draft
- Author notes and revision risks have been reviewed and either resolved or accepted
- CTA is present and points to a live destination

## Post-Publish Checklist
- URL submitted to Search Console for indexing
- Internal links from existing published pieces updated to point to the new piece (where the link suggestions report indicates)
- Added to the cluster map if the piece belongs to one
- Baseline metrics captured for the next `/performance` review (impressions, position, citations) on day 0

## Acceptance Criteria
- Draft is unchanged in `/workspace/drafts/`; the published file is the canonical artifact
- Pre-publish checklist is fully signed before the file is written
- All link targets and CTA destinations resolve
- Schema, OG, and featured-image briefs are concrete enough to hand to a developer or designer without follow-up questions

## Post-Publish
Schedule the first `/performance` review for trailing-30 and trailing-90. If the piece is part of a cluster, update the cluster's production state to "shipped."
