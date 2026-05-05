# Task: Rewrite Article

## Goal
Produce a substantively new draft of an existing article — not a polish pass. Use when the original misses intent, lost rankings, or no longer reflects the product, audience, or evidence base.

## Required Inputs
- Path to the existing article (`/workspace/published/` or `/workspace/drafts/`)
- The original brief or, if missing, a fresh brief from `/workspace/briefs/`
- Reason for the rewrite (intent shift, ranking decline, AEO retrofit, product change, factual rot)
- Any analysis report at `/workspace/reports/<slug>-analysis.md`

## Required Output
Save to `/workspace/drafts/<slug>-rewrite.md`

Must include (per Article Contract):
1. Working title
2. Target keyword
3. Intent statement
4. Complete article body — restructured, not lightly edited
5. Metadata options (title tag and meta description)
6. Internal link suggestions
7. Author notes — what changed and why
8. Revision risks

## Rewrite Requirements
- Preserve any earned ranking signals: keep the URL, primary keyword, and the canonical question the article answers, unless the rewrite reason explicitly calls for changing them
- Do not retain prose just because it exists — every section must earn its place against the new brief
- If the original had backlinks, keep the anchor-text targets reachable (same H2 or a redirect-friendly section)
- Replace any unsupported claim, dated statistic, or vague advice — do not let it survive the rewrite
- Address the specific failures called out in the analysis report, if one exists

## Acceptance Criteria
- Passes `scripts/validate_article.py`
- Author notes section enumerates the structural changes (sections added, removed, merged, reordered)
- Revision risks section flags anything the rewrite did not fully resolve
- Diff vs. the original is substantive, not cosmetic — at least the intro, outline, and CTA are reworked

## Post-Rewrite
Generate the reports `/publish` requires — both scripts only write a file when `--output` is supplied:

```
python scripts/score_seo.py workspace/drafts/<slug>-rewrite.md \
  --output workspace/reports/<slug>-seo-score.md
python scripts/extract_internal_links.py workspace/drafts/<slug>-rewrite.md \
  --output workspace/reports/<slug>-internal-links.md
```

Then proceed to `/publish`.
