# Skupper OKF MVP

This repository is a minimal starting point for treating Skupper documentation as a curated human source and building an OKF-style LLM wiki beside it.

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

The `human/` directory is populated by scripts. Each upstream repository gets its own repo-named subdirectory, for example `human/skupper-docs/` and `human/skupper-example-hello-world/`. These are snapshots, not the source of truth. The source of truth for the initial snapshots remains the upstream Skupper repositories:

```text
https://github.com/skupperproject/skupper-docs.git
https://github.com/skupperproject/skupper-example-hello-world.git
```

## Quick start

```bash
just init
just tree
```

`just init` creates the local OKF layout and fetches `skupper-docs` into `human/skupper-docs/` and `skupper-example-hello-world` into `human/skupper-example-hello-world/`.

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
