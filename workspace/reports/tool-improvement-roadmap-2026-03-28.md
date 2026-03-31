# SEO Machine Codex — Improvement Roadmap (2026-03-28)

## objective
Define a comprehensive, no-constraints improvement plan for turning this repository from a local scaffold into a production-grade SEO content operating system.

## audience
Maintainers, technical leads, content operations leads, and product owners planning the next phase of platform investment.

## target keyword
SEO content operations platform roadmap

## search intent
Strategic/implementation planning: identify highest-impact upgrades across product, engineering, quality, data, workflow automation, and governance.

## outline
1. Current maturity diagnosis
2. North-star product direction
3. Priority architecture changes
4. AI quality and trust upgrades
5. UX and workflow upgrades
6. Measurement and experimentation layer
7. Enterprise-grade controls
8. 90-day implementation plan

## final artifact

### 1) Current maturity diagnosis
The current tool is a strong **local execution prototype**: it can generate artifacts and run lightweight checks, but it is still limited by heuristic validation, synthetic draft generation, and minimal governance/observability.

### 2) North-star direction (what to build)
Reframe the project as an **SEO Content OS** with four layers:
1. **Planning layer** (topic strategy, clustering, intent map, opportunity scoring)
2. **Production layer** (briefing, drafting, optimization, QA, publishing)
3. **Intelligence layer** (SERP ingestion, content performance data, attribution, experimentation)
4. **Governance layer** (approval workflows, policy checks, evidence traceability, audit logs)

### 3) Architecture improvements (nothing off the table)
1. **Move from markdown-only contracts to typed schemas**
   - Define Pydantic/JSON schemas for brief/article/audit artifacts.
   - Store metadata in frontmatter and validate deterministically.
2. **Introduce a workflow engine**
   - Use DAG-based orchestration (Temporal/Prefect/Airflow) for deterministic multi-step runs.
   - Add retries, resumability, and run-level state tracking.
3. **Create a content graph datastore**
   - Persist topics, entities, keywords, pages, internal links, and relationships in a graph DB.
   - Replace overlap-based link suggestions with graph-aware recommendations.
4. **Build a plugin adapter architecture**
   - Separate connectors for CMS, analytics, Search Console, and SERP providers.
   - Enable provider swaps without core logic rewrites.

### 4) AI quality and trust upgrades
1. **Evidence-bound generation**
   - Require every factual claim to attach a citation reference object.
   - Fail QA when claim-citation mapping is incomplete.
2. **Model policy routing**
   - Use smaller models for extraction/scoring and larger models for synthesis.
   - Add route-level cost/latency budgets.
3. **Critic loop and disagreement checks**
   - Add editor/critic agents with explicit contradiction detection and quality arbitration.
4. **Grounded rewriting over free-form generation**
   - Prefer source-conditioned transforms (brief + evidence + style guide) to reduce hallucination risk.

### 5) UX and workflow improvements
1. **Build a web UI with run traces**
   - Show run timeline, artifacts, failed checks, and one-click fixes.
2. **Human-in-the-loop checkpoints**
   - Require approvals before publish, with role-based signoff (SEO, editorial, legal).
3. **Smart diff views**
   - Show semantic and SEO deltas between revisions (intent coverage, heading quality, entity inclusion).
4. **Actionable QA output**
   - Convert validator errors into fix suggestions linked to exact sections.

### 6) Measurement and experimentation
1. **Quality score that blends static + live metrics**
   - Combine contract compliance, editorial quality, and post-publish performance.
2. **Closed-loop optimization**
   - Feed CTR, rank movement, engagement, and conversion metrics back into rewriting priorities.
3. **Experiment framework**
   - A/B test titles, intros, and CTA variants with guardrails and confidence thresholds.
4. **Opportunity queue**
   - Auto-rank refresh candidates by decay, traffic potential, and business value.

### 7) Enterprise-grade capabilities
1. **Policy engine**
   - Enforce prohibited claims, compliance constraints, and regulated-content rules.
2. **Auditability and lineage**
   - Track source-to-claim lineage and all edits by actor/model/version.
3. **Permissions and secrets hygiene**
   - Role-based access controls; scoped credentials for each external integration.
4. **SLOs and reliability**
   - Define SLOs for run success rate, validation accuracy, and publish latency.

### 8) Suggested 90-day plan
- **Days 0–30:** typed schemas, robust validator rewrite, run metadata store, better tests/fixtures.
- **Days 31–60:** CMS + Search Console connectors, evidence-bound generation, UI for run review.
- **Days 61–90:** experimentation framework, opportunity queue, approval workflows, and policy engine.

## unresolved assumptions
- Business priorities between speed, quality, and cost are not yet explicitly ranked.
- Target CMS and analytics stack are not specified.
- Compliance requirements (if any) are not documented.

## next recommended step
Create an architecture decision record (ADR) selecting the first production milestone: schema-first validator + run datastore + approval checkpoints.
