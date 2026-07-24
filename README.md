# Skupper OKF MVP

This repository is a minimal starting point for treating Skupper documentation as a curated human source and building an OKF-style LLM wiki beside it.


## Ask about Skupper

This repo can be supplemented with code repos so you can query it like deepwiki, but with more scope (ie multiple repos).

See [Requirements](#requirements) and [Quick start](#quick-start) to set up the repository.


## Maps

- [Skupper Blockscape map](https://pwright.github.io/blockscape/?load=https://raw.githubusercontent.com/pwright/skupper-okf/refs/heads/main/maps/skupper.bs) from `maps/skupper.bs`
- [Skupper Docs Landscape](https://pwright.github.io/blockscape/?load=https://raw.githubusercontent.com/pwright/skupper-okf/refs/heads/main/maps/skupper-docs-landscape.bs) from `maps/skupper-docs-landscape.bs` - documentation coverage map with quality ratings

### Documentation Quality Ratings

The `rate_docs.py` script analyzes documentation files and adds quality ratings (3-10) to items in `maps/skupper-docs-landscape.bs`.

**How ratings are calculated:**

The script analyzes each documentation file's content indicators and calculates a score:

1. **Human links** (links to `human/` directory - indicates actual written content):
   - 5+ links: +3 points
   - 3-4 links: +2 points
   - 1-2 links: +1 point

2. **External links** (website references):
   - 4+ links: +2 points
   - 2-3 links: +1 point

3. **Sources** (reference material):
   - 5+ sources: +1 point
   - 3-4 sources: +0.5 points

4. **Specific draft notes** (actionable guidance, not generic TODOs):
   - Contains specific indicators (commands, procedures, examples): +1 point

5. **Review status**:
   - `confidence: reviewed` in frontmatter: +2 points

6. **Score to rating conversion**:
   - 8+ points → 9/10
   - 6.5-7.9 points → 8/10
   - 5-6.4 points → 7/10
   - 3.5-4.9 points → 6/10
   - 2-3.4 points → 5/10
   - 1-1.9 points → 4/10
   - <1 point → 3/10

Navigation-only stubs (`confidence: stub`) receive no rating.

**Usage:**

```bash
# Full rating pass - analyze all docs and update aggregates
python3 rate_docs.py

# Aggregate-only - preserve manual edits, only update parent nav ratings
python3 rate_docs.py --aggregate
```

**Rating scale:**
- No rating: Navigation-only stubs
- 3-4/10: Minimal draft with few content indicators
- 5-6/10: Moderate draft with some links and sources
- 7-8/10: Strong draft with multiple human/ links and references
- 9-10/10: Comprehensive content with extensive coverage

**Aggregate ratings for navigation items:**

Parent navigation items (e.g., "Configure", "Secure") that have no direct content receive an aggregate rating calculated as the average of all child topic ratings in their detailed map. For example:

- "Configure" detailed map contains 15 topics rated 6-9
- Average rating: 7.7
- "Configure" nav item displays: "Configure (8)"

This helps identify which major documentation sections are well-covered vs. need improvement.


The intended split is:

```text
human/      copied upstream snapshots by repo name; do not edit directly
generated/  agent-produced OKF notes; disposable and rebuildable
reviewed/   human-promoted OKF notes; trusted enough for downstream use
indexes/    generated indexes and coverage reports
maps/       Blockscape JSON maps generated from reviewed or generated OKF
prompts/    reusable prompts for extraction, review, and mapping
sources/    provenance records for upstream repositories
_system/    local operating rules for humans and agents
```

The `human/` directory is populated by scripts. Each upstream repository gets its own repo-named subdirectory, for example `human/skupper-docs/`, `human/skupper-example-hello-world/`, and `human/skupper-example-grpc/`. These are snapshots, not the source of truth. The source of truth for the initial snapshots remains the upstream Skupper repositories:

```text
https://github.com/skupperproject/skupper-docs.git
https://github.com/skupperproject/skupper-example-hello-world.git
https://github.com/skupperproject/skupper-example-grpc.git
https://github.com/skupperproject/skupper.git (full clone, gitignored)
```

The `human/skupper/` directory contains a full clone of the Skupper main repository, used for generating API and CRD documentation. This clone is gitignored and refreshed via `scripts/sync-human-skupper.sh`.

## Quick start

```bash
just init
just tree  # optional: view the directory structure
```

`just init` creates the local OKF layout and populates the `human/` directory by fetching upstream Skupper repositories:

- `human/skupper-docs/` — Skupper documentation
- `human/skewer/` — Skewer repository
- `human/skewer-yamls/` — root `skewer.yaml` files from Skupper example repos on `main`
- `human/skupper-ansible/` — Skupper Ansible collection
- `human/skupper-example-hello-world/` — Hello World example
- `human/skupper-example-grpc/` — gRPC example  
- `human/skupper/` — Full Skupper repo (for API/CRD generation, gitignored)
- `human/skupper-console/` — Console repo (for API extraction)
- `human/skupper-router/` — Router repo (for markdown extraction)

`just tree` displays the directory structure to verify the layout.

For an offline smoke test that does not contact GitHub:

```bash
just test
```

## Requirements

- `bash`
- `git`
- `rsync`
- `just`, optional but recommended

The scripts are ordinary command-line tools. They log progress to stderr and reserve stdout for machine-readable output such as the resolved source commit.

## Directory lifecycle

```text
human/<repo-name>/
  Refreshed from upstream. Do not hand-edit.

generated/
  Safe to delete and regenerate.

reviewed/
  Human-promoted knowledge. Treat as durable.

indexes/
  Safe to delete and regenerate.

maps/
  Generated Blockscape output. Review before treating as canonical.
```

## Basic workflow

```text
1. Refresh human/skupper-docs/ from skupper-docs main.
2. Use prompts/extract-from-human.md to generate OKF pages into generated/.
3. Validate front matter and source provenance.
4. Promote useful pages into reviewed/.
5. Generate indexes and Blockscape maps from reviewed/.
6. Feed focused context packs to Codex or other coding agents.
```


```bash
just sync-human
```

`just sync-human` also regenerates repeatable reference pages for the Skupper Ansible collection under `generated/skupper-ansible/`.

## Generated content policy

Generated content is not authoritative by default. Every generated or reviewed OKF file should record:

```yaml
source_repo: https://github.com/skupperproject/skupper-docs.git
source_branch: main
source_commit: <commit>
source_paths:
  - human/skupper-docs/<path>
status: generated
reviewed: false
```

Promoted files should move to `reviewed/` and set `status: reviewed` plus review metadata.
