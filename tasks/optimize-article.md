# Task: Optimize Article

## Goal
Improve an existing article for clarity, search intent, structure, and conversion. Use when the page is fundamentally sound but has fixable issues — distinct from `/rewrite`, which restructures.

## Required Inputs
- Path to the existing article in `/workspace/drafts/` or `/workspace/published/`
- Any analysis report at `/workspace/reports/<slug>-analysis.md`, if one exists
- Target keyword and current performance signal, if available

## Required Output
1. Optimized draft saved to `/workspace/drafts/<slug>.md` (updates the existing draft in place)
2. Optimization report saved to `/workspace/reports/<slug>-optimization.md`, including:
   - Change log (sections added, removed, edited)
   - SEO improvement summary
   - Risk notes where claims need verification

## Post-Optimize
Generate the reports `/publish` requires — both scripts only write a file when `--output` is supplied:

```
python scripts/validate_article.py workspace/drafts/<slug>.md
python scripts/score_seo.py workspace/drafts/<slug>.md \
  --output workspace/reports/<slug>-seo-score.md
python scripts/extract_internal_links.py workspace/drafts/<slug>.md \
  --output workspace/reports/<slug>-internal-links.md
```

The validator must pass before proceeding to `/publish`.
