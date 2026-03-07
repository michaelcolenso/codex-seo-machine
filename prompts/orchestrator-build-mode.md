# Codex / Claude Code Build Prompt

## SEO Arbitrage Platform — Deterministic Orchestrated Build Mode

You are a senior autonomous software engineer operating in deterministic build mode.

Your task is to build a complete local-first monorepo named:

`seo-arbitrage-platform`

You must build it in strict phase order.

You must not skip phases.

You must not invent new architecture outside this specification unless required to make the system run locally, in which case the change must be minimal and clearly justified in the README.

You must not leave placeholder implementations in core paths.

You must not output partial repositories.

You must create all required files.

You must keep the system runnable locally.

---


---

## STRICT EXECUTION PROTOCOL (NON-OPTIONAL)

For every phase, execute this exact loop:

1. Implement only that phase's scope.
2. Verify imports and module wiring.
3. Run required validation commands for the phase.
4. If any command fails, fix before continuing.
5. Print the required phase report format exactly.
6. Stop if acceptance criteria are not met.

You are forbidden to begin the next phase until all current-phase gates pass.

---

## ANTI-DRIFT RULES

- Do not rename required modules.
- Do not relocate required modules to different packages.
- Do not swap required libraries for alternatives unless local execution would otherwise fail.
- Do not omit command surfaces that are explicitly required.
- Do not replace deterministic logic with probabilistic or LLM-dependent behavior.
- Do not skip persistence paths required by the spec.

Any necessary deviation must be minimal, documented immediately in README, and listed in the final report under "minimal deviations from spec".

---

## EXPLICIT NO-SUBSTITUTION RULES

You must use the required stack and interfaces as declared in this prompt.

Forbidden substitutions include (non-exhaustive):

- Replacing Typer CLI with argparse-only entrypoints
- Replacing DuckDB/SQLite hybrid persistence with single-store shortcuts
- Replacing Astro output with a non-Astro static generator
- Replacing Playwright SERP collection with parser-only mocks in production paths

Test doubles are allowed in tests only.

---

## REQUIRED PHASE REPORT FORMAT

After each phase, print exactly these sections:

### Phase <N> Completion Summary
- Status: PASS | FAIL
- Acceptance gates: <list each gate with pass/fail>
- Notes: <brief>

### Files Created/Modified (Phase <N>)
- <relative path>

### Verification Commands (Phase <N>)
```bash
<exact command 1>
<exact command 2>
```

### Next Phase Decision
- Proceeding to Phase <N+1>: YES | NO

Do not omit this report format.

---

## REQUIRED COMMANDS AFTER EACH PHASE

At minimum run these command classes (adapt paths as needed):

1. Import check / module load check
2. Targeted tests for the phase
3. CLI help or command smoke tests for newly added command groups
4. File existence checks for required manifests

If a command cannot run locally, explicitly state why and provide the closest deterministic fallback command.


## PRIMARY OBJECTIVE

Build a production-quality foundation for a platform with three integrated systems:

1. **SEO Opportunity Radar v2**  
   Discovers SEO arbitrage opportunities by identifying keywords where demand exceeds SERP quality.
2. **Programmatic SEO Factory**  
   Converts validated keyword clusters into deployable static SEO sites backed by structured data.
3. **Dataset Crawler / Registry**  
   Discovers public structured datasets and APIs that can power defensible programmatic SEO assets.

---

## EXECUTION MODE

You must behave as a deterministic build agent, not a brainstorming agent.

That means:

- Build exactly what is specified.
- Do not skip required files.
- Do not replace required components with simpler unrelated substitutes.
- Do not write `TODO` in core logic.
- Do not hand-wave external integrations.
- Do not silently omit tests.
- Do not leave modules unimportable.
- Do not collapse multiple phases together unless explicitly allowed.
- Do not move ahead if the current phase does not pass its acceptance criteria.

---

## GLOBAL ENGINEERING RULES

Apply these rules to the entire repository.

### Code Quality

- Use Python 3.12+
- Use type hints everywhere
- Use docstrings for public classes and functions
- Keep imports modular and clean
- Avoid circular imports
- Prefer deterministic, readable implementations over clever abstractions
- Keep modules small and composable

### Implementation Rules

- Core logic must be real logic, not stubs
- Example data may be lightweight, but must be usable
- Every package must be importable
- Every CLI command must execute
- Every phase must leave the repo in a valid state
- Use local persistence only
- No paid services required
- No hosted cloud dependencies required for basic execution

### Approved Core Stack

- Python
- Typer
- Pydantic
- DuckDB
- SQLite
- Playwright
- BeautifulSoup
- httpx
- Jinja2
- Astro
- pytest

Do not substitute frameworks unless absolutely necessary to preserve local execution.

---

## MANDATORY OUTPUT DISCIPLINE

After each phase, you must do all of the following:

1. Create or update the required files for that phase
2. Ensure imports resolve
3. Ensure tests for that phase pass if tests are required in that phase
4. Print a concise phase completion summary
5. Print a list of files created or modified in that phase
6. Print the exact commands used to verify the phase
7. Only then proceed to the next phase

If a phase fails validation, fix it before proceeding.

---

## REPOSITORY SKELETON

Create this monorepo exactly:

```text
seo-arbitrage-platform/
├── README.md
├── pyproject.toml
├── .env.example
├── .gitignore
├── apps/
│   ├── radar_api/
│   ├── ops_dashboard/
│   └── site_builder/
├── packages/
│   ├── common/
│   ├── radar/
│   ├── serp/
│   ├── scoring/
│   ├── dataset_discovery/
│   ├── opportunity_selection/
│   ├── site_factory/
│   ├── templates/
│   ├── enrichment/
│   ├── internal_linking/
│   ├── publishing/
│   └── monitoring/
├── data/
│   ├── seeds/
│   ├── registries/
│   ├── raw/
│   ├── processed/
│   └── exports/
├── sites/
│   └── generated/
├── scripts/
├── docs/
└── tests/
```

Every Python package directory must include `__init__.py`.

---

## PHASE FILE MANIFESTS (MUST EXIST)

Each phase section below defines mandatory files/modules.

Rule: if a phase lists a file/module, that path must exist by end of the phase and be importable/executable as applicable.

---

## PHASE 0 — REPOSITORY FOUNDATION

### Required Files

- `README.md`
- `pyproject.toml`
- `.env.example`
- `.gitignore`
- `packages/common/__init__.py`
- all package `__init__.py` files
- a base config entrypoint

### Requirements

Set up:

- dependencies
- test tooling
- package discovery
- CLI entrypoint placeholder wiring
- local developer instructions

### Acceptance Criteria

- project installs locally
- `pytest` runs
- package imports resolve
- CLI entrypoint exists, even if only minimally wired

---

## PHASE 1 — CORE INFRASTRUCTURE

Implement exactly these modules:

- `packages/common/config.py`
- `packages/common/logging.py`
- `packages/common/db.py`
- `packages/common/models.py`
- `packages/common/job_queue.py`
- `packages/common/utils.py`

### Required Responsibilities

#### `config.py`

- environment loading
- runtime configuration object
- path configuration
- storage locations
- browser / scraper configuration
- defaults for local execution

#### `logging.py`

- structured logger setup
- console logging
- reusable logger getter

#### `db.py`

Hybrid storage:

- DuckDB for analytics tables
- SQLite for operational state

Include:

- initialization functions
- schema creation
- connection helpers
- simple repository helpers where useful

#### `models.py`

Use Pydantic models for:

- `Keyword`
- `SERPResult`
- `SERPSnapshot`
- `Dataset`
- `Opportunity`
- `OpportunityCluster`
- `SiteBlueprint`
- `GeneratedSite`
- `GeneratedPage`

#### `job_queue.py`

Implement SQLite-backed job queue with states:

- `pending`
- `running`
- `completed`
- `failed`

Must support:

- enqueue
- reserve next job
- mark running
- mark completed
- mark failed
- retry failed jobs optionally

#### `utils.py`

Shared helpers only:

- slugify
- hashing
- timestamps
- batching
- safe JSON IO
- filesystem helpers

### Acceptance Criteria

- DB init command works
- models import cleanly
- queue can enqueue and transition jobs correctly
- no placeholders in core methods

---

## PHASE 2 — DATASET CRAWLER / REGISTRY

Implement package:

`packages/dataset_discovery/`

### Required Modules

- `seed_sources.py`
- `crawler.py`
- `dataset_parser.py`
- `classifier.py`
- `dataset_scorer.py`
- `registry.py`
- `keyword_suggester.py`

### Functional Goals

1. crawl seed portals
2. discover candidate datasets
3. normalize dataset metadata
4. classify dataset type
5. score SEO usefulness
6. store registry records
7. generate keyword suggestions from datasets

### Seed Sources

Support at minimum:

- data.gov
- Socrata portals
- CKAN portals
- city open data portals

### CLI Commands

- `seo-platform datasets seed`
- `seo-platform datasets crawl`
- `seo-platform datasets classify`
- `seo-platform datasets score`
- `seo-platform datasets registry`
- `seo-platform datasets inspect`
- `seo-platform datasets suggest-keywords`

### Constraints

- Must support local test mode with example sources
- Network logic must be separated from parsing logic
- Registry records must be serializable to disk

### Acceptance Criteria

- crawl produces normalized dataset records
- registry persists sample records
- keyword suggestions are generated from a dataset
- commands run locally against example data

---

## PHASE 3 — RADAR V2 KEYWORD GENERATION

Implement package:

`packages/radar/`

### Required Modules

- `query_generator.py`
- `query_expander.py`
- `query_deduper.py`
- `batch_manager.py`
- `clusterer.py`
- `opportunity_ranker.py`

### Functional Goals

Support generation from:

- entity lists
- modifier lists
- geography lists
- template packs

### Example Templates

- `[city] building permits`
- `[city] restaurant inspections`
- `[company] lawsuits`

### Required Behaviors

- deterministic generation
- deduplication
- canonicalization
- batch partitioning
- lightweight keyword clustering before SERP scan
- ranking based on downstream viability fields

### Acceptance Criteria

- seed lists generate keyword sets
- duplicates are removed consistently
- batches are stable across runs
- cluster primitives work on sample data

---

## PHASE 4 — SERP COLLECTION

Implement package:

`packages/serp/`

### Required Modules

- `serp_scraper.py`
- `serp_parser.py`
- `serp_features.py`
- `serp_store.py`

### Tooling

Use:

- Playwright
- BeautifulSoup
- httpx where useful

### Minimum Capture Fields

- title
- url
- snippet
- rank
- domain

### Required Behaviors

- fetch result pages
- parse organic results
- normalize domains
- extract basic SERP features
- persist snapshots

### Acceptance Criteria

- parser works against saved HTML fixtures
- scraper pipeline can save a sample snapshot
- snapshot store works locally
- parsing logic is testable without live requests

---

## PHASE 5 — SERP WEAKNESS + DEMAND + MONETIZATION SCORING

Implement package:

`packages/scoring/`

### Required Modules

- `serp_weakness.py`
- `demand_model.py`
- `monetization_model.py`
- `opportunity_score.py`

### Weakness Signals

Must include scoring logic for:

- forums present
- affiliate spam
- low-authority domains
- stale results
- intent mismatch

### Required Outputs

- `serp_weakness_score`
- `demand_score`
- `monetization_score`
- `opportunity_score`

### Constraints

Use deterministic heuristics.  
Do not require paid keyword APIs for baseline operation.

### Acceptance Criteria

- sample SERPs can be scored
- composite opportunity score is reproducible
- individual score components are inspectable

---

## PHASE 6 — OPPORTUNITY CLUSTERING

Implement package:

`packages/opportunity_selection/`

### Required Modules

- `cluster_builder.py`
- `cluster_ranker.py`
- `cluster_export.py`

### Functional Goal

Cluster keyword opportunities into site-level opportunities.

Example:

- cluster name: Seattle Building Permits

### Required Behaviors

- build clusters from scored keywords
- rank clusters by site potential
- export clusters to disk

### Acceptance Criteria

- scored keywords cluster into coherent groups
- ranking is deterministic
- exports are readable JSON and CSV where appropriate

---

## PHASE 7 — PROGRAMMATIC SEO FACTORY

Implement package:

`packages/site_factory/`

### Required Modules

- `blueprint_generator.py`
- `data_model_generator.py`
- `page_generator.py`
- `site_generator.py`
- `site_validator.py`

### Outputs

- `site_blueprint.json`
- generated site artifacts under `sites/generated/`

### Required Behaviors

- create site blueprint from an opportunity cluster
- define page types and data contracts
- generate page payloads
- generate site structure
- validate resulting site package

### Acceptance Criteria

- blueprint can be produced from example cluster
- page payloads are emitted
- site package is generated locally
- validation catches obvious structural failures

---

## PHASE 8 — TEMPLATE SYSTEM

Implement package:

`packages/templates/`

Use:

- Jinja2

### Required Templates

- permit page
- inspection page
- contractor page
- entity page
- hub page

### Requirements

- template loader
- context validation
- rendering helpers
- sample render tests

### Acceptance Criteria

- all templates render from sample payloads
- rendered output is deterministic
- missing required context fails clearly

---

## PHASE 9 — INTERNAL LINKING ENGINE

Implement package:

`packages/internal_linking/`

### Required Behavior

Graph-based internal linking engine supporting:

- entity links
- geographic links
- sibling links
- recency hubs
- category hubs

### Acceptance Criteria

- sample pages receive structured internal links
- no self-link duplication
- orphan detection is possible

---

## PHASE 10 — STATIC SITE GENERATION

Use Astro.

Generate output into:

`sites/generated/<site_name>`

### Requirements

Include:

- routes
- sitemap
- schema markup
- build scripts
- content/data bridge from Python outputs to Astro inputs

### Constraints

- generated example site must build locally
- keep Astro project deterministic and minimal

### Acceptance Criteria

- example site compiles
- sitemap is generated
- schema markup is present on relevant pages
- build instructions work from README

---

## PHASE 11 — CLI

Implement Typer CLI for the entire platform.

### Required Commands

#### Radar

- `seo-platform radar generate`
- `seo-platform radar scan`
- `seo-platform radar score`
- `seo-platform radar cluster`
- `seo-platform radar top`

#### Datasets

- `seo-platform datasets seed`
- `seo-platform datasets crawl`
- `seo-platform datasets classify`
- `seo-platform datasets score`
- `seo-platform datasets registry`

#### Factory

- `seo-platform factory blueprint`
- `seo-platform factory build`
- `seo-platform factory export`
- `seo-platform factory validate`

### Requirements

- commands must wire into real modules
- help text must be useful
- commands must work on example data locally

### Acceptance Criteria

- CLI installs
- `--help` works for root and subcommands
- end-to-end sample flow runs from CLI

---

## PHASE 12 — VALIDATION SYSTEM

Implement:

- `packages/monitoring/validators.py`

### Opportunity Validation

Must validate:

- weak SERP exists
- dataset exists
- scalable page model exists
- monetization path exists
- cluster coherence exists

### Site Validation

Must validate:

- unique titles
- valid schema
- internal links present
- no orphan pages
- page uniqueness

### Acceptance Criteria

- validators return structured reports
- validators fail meaningfully
- validators integrate into CLI

---

## PHASE 13 — EXAMPLE DATA

Include example seeds:

- `data/seeds/cities.csv`
- `data/seeds/modifiers.csv`
- `data/seeds/entities.csv`

Include at least one worked example dataset:

- Seattle Building Permits

### Acceptance Criteria

- example data supports full demo flow
- files are documented in README

---

## PHASE 14 — END-TO-END DEMO FLOW

The README must show this exact flow:

```bash
seo-platform datasets crawl
seo-platform radar generate
seo-platform radar scan
seo-platform radar score
seo-platform radar cluster
seo-platform radar top
seo-platform factory blueprint seattle-permits
seo-platform factory build seattle-permits
```

### Requirements

README must include:

- local installation
- environment setup
- Playwright install step
- example data flow
- where outputs are written
- how to run tests
- architecture overview

---

## PHASE 15 — TESTS

Create tests for:

- query generation
- dedupe
- scoring
- clustering
- template rendering
- internal linking
- validation

### Requirements

- use pytest
- prefer fixture-driven tests
- include HTML fixtures for SERP parsing if needed
- tests must not require live network access by default

### Acceptance Criteria

- test suite runs locally
- critical logic is covered
- sample flow has at least one integration test

---

## REQUIRED FILE CONTRACTS

You must create real source files for every required module named in this prompt.

If a file is required and intentionally minimal, it must still contain valid implementation and imports.

Do not silently omit:

- apps
- docs
- tests
- templates
- example data
- CLI wiring
- Astro scaffolding

---

## NON-GOALS

Do not spend time on:

- production auth
- cloud deployment
- multi-user tenancy
- polished frontend dashboards
- advanced JS UI work beyond what is needed for Astro example site
- LLM integrations unless explicitly required for a non-core optional path

This is a local-first, deterministic execution build.

---

## DEFINITION OF DONE

The repository is only complete when all of the following are true:

1. full repository tree exists
2. all critical source files exist
3. README is complete
4. docs folder contains architectural documentation
5. CLI works locally
6. example opportunity output exists
7. example generated site exists
8. tests pass
9. example end-to-end commands are documented
10. no core modules contain placeholder logic

---

## REQUIRED FINAL REPORT

At the end, output:

1. full repository tree
2. summary of each phase completed
3. exact commands to install and run locally
4. exact commands to run tests
5. exact commands to run the end-to-end demo
6. known limitations, if any
7. list of any minimal deviations from spec and why they were necessary

---

## BUILD NOW

Execute the repository build in phase order.  
Do not skip phases.  
Do not compress the process into a vague summary.  
Create the actual repository contents.
