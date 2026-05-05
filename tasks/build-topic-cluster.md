# Task: Build Topic Cluster

## Goal
Design a pillar-and-spoke content cluster around a single high-value topic, with a concrete production sequence and internal-linking architecture.

## Required Inputs
- Pillar topic and primary keyword
- Audience and product context from `context/`
- Existing content inventory (what already lives in `/workspace/published/` and on the live site, if known)
- Business priority: traffic, AEO citation share, pipeline, or refresh — pick one

## Required Output
Save to `/workspace/reports/<slug>-cluster.md`

Must include:
1. Pillar definition — primary keyword, intent, working title, target word count
2. Spoke list — 6 to 12 supporting articles, each with: keyword, intent, working title, brief one-line angle, expected length
3. Cluster map — which spokes link to the pillar, which spokes link to each other, with anchor-text suggestions
4. Production sequence — order of writing, with reasoning (which pieces unblock others, which reuse research)
5. Coverage matrix — every reader question from the pillar brief mapped to either the pillar itself or a specific spoke; no orphan questions
6. Distinct-intent check — no two spokes target the same intent
7. Conversion paths — for each spoke, where the reader is in the funnel and what the natural next step is
8. Risks and dependencies — research gaps, product context needed, SME interviews required

## Cluster Requirements
- Spokes must each have a defensible reason to exist as a separate URL — no "pillar-fragment" spokes
- The pillar should be the broadest piece in the cluster; spokes go deep on one sub-question each
- Internal-linking plan must be bidirectional where it makes sense (pillar → spoke and spoke → pillar at minimum)
- Naming convention: pillar slug is the cluster name; spoke slugs nest naturally beneath it

## Acceptance Criteria
- Coverage matrix has zero orphan questions
- No two spokes have overlapping intent
- Production sequence is executable as a backlog without further planning
- For each spoke, a one-sentence brief is concrete enough to hand to `/research`

## Post-Cluster
Trigger `/research` for the pillar first, then for spokes in the production-sequence order. Track production state in the cluster report, updating as pieces ship.
