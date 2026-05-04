# Task: Performance Review

## Goal
Diagnose how a piece of content (or a cluster) is performing against expectations, separate page-level issues from distribution-level issues, and recommend a single next action.

## Required Inputs
- Article URL or path, or a cluster identifier
- Time window for the review (default: trailing 90 days vs. previous 90)
- Metric snapshot: impressions, clicks, position, sessions, conversions — whichever are available
- AI-search signal if available: citation count, share-of-voice across a prompt panel, AI Overview presence
- Original brief, if one exists

## Required Output
Save to `/workspace/reports/<slug>-performance.md`

Must include:
1. Headline diagnosis — one sentence stating what is happening and why
2. Metric table — primary metrics with current value, prior period, delta, and direction
3. Page-level vs. distribution-level split — is the page underperforming, or is the surface (SERP, AI answer, social) the bottleneck
4. Root-cause hypotheses — at least two, ranked by likelihood, each with the evidence that supports it
5. Recommended next action — one of: refresh, rewrite, redirect, expand into a cluster, leave alone and re-check later
6. Expected impact and how it will be measured
7. Confidence level and what would change the recommendation

## Review Checks
- Is intent still aligned with current SERP behavior, or has the SERP shifted (AI Overview added, intent changed, format changed)
- Is the page still ranking but losing clicks (CTR collapse from AI answers or featured snippets)
- Is the page losing rank to specific competitors — note which
- Are citations in AI answers tracking with or against organic ranking
- Are conversions degrading independently of traffic
- Does the page still match the product and offers in `context/`

## Acceptance Criteria
- Headline diagnosis is testable, not vague (no "performance is mixed")
- Recommendation is one action, not a menu
- Confidence is stated explicitly, with the data that would change it
- Report is short enough to read in under five minutes

## Post-Review
Hand off the recommended action to the matching task: `/optimize`, `/rewrite`, `/cluster`, or close as "no action."
