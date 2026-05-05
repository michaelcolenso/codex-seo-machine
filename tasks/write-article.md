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
Also generate, inline in the draft:
- title tag options
- meta description options
- suggested internal links
- FAQ section if justified

Then produce the reports `/publish` requires — both scripts only write a file when `--output` is supplied:

```
python scripts/validate_article.py workspace/drafts/<slug>.md
python scripts/score_seo.py workspace/drafts/<slug>.md \
  --output workspace/reports/<slug>-seo-score.md
python scripts/extract_internal_links.py workspace/drafts/<slug>.md \
  --output workspace/reports/<slug>-internal-links.md
```

The validator must pass before proceeding to `/publish`.
