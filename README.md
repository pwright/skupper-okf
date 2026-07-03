# Skupper OKF MVP

This repository is a minimal starting point for treating Skupper documentation as a curated human source and building an OKF-style LLM wiki beside it.

The intended split is:

```text
human/      copied snapshot of skupperproject/skupper-docs main; do not edit directly
generated/  agent-produced OKF notes; disposable and rebuildable
reviewed/   human-promoted OKF notes; trusted enough for downstream use
indexes/    generated indexes and coverage reports
maps/       Blockscape JSON maps generated from reviewed or generated OKF
prompts/    reusable prompts for extraction, review, and mapping
sources/    provenance records for upstream repositories
_system/    local operating rules for humans and agents
```

The `human/` directory is populated by a script. It is a snapshot, not the source of truth. The source of truth remains the upstream Skupper documentation repository:

```text
https://github.com/skupperproject/skupper-docs.git
```

## Quick start

```bash
just init
just tree
```

`just init` creates the local OKF layout and fetches `skupper-docs` from GitHub into `human/`.

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
human/
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
1. Refresh human/ from skupper-docs main.
2. Use prompts/extract-from-human.md to generate OKF pages into generated/.
3. Validate front matter and source provenance.
4. Promote useful pages into reviewed/.
5. Generate indexes and Blockscape maps from reviewed/.
6. Feed focused context packs to Codex or other coding agents.
```


```bash
just sync-human
```

## Generated content policy

Generated content is not authoritative by default. Every generated or reviewed OKF file should record:

```yaml
source_repo: https://github.com/skupperproject/skupper-docs.git
source_branch: main
source_commit: <commit>
source_paths:
  - <path inside human/>
status: generated
reviewed: false
```

Promoted files should move to `reviewed/` and set `status: reviewed` plus review metadata.
