# MVP plan

## Intention

Create a small, reproducible OKF-style workspace where the curated Skupper documentation repository is copied into `human/`, then used as the source for generated and reviewed agent-readable knowledge.

## Non-goals

- Do not replace the Skupper documentation site.
- Do not rewrite all docs with an LLM immediately.
- Do not treat generated notes as authoritative without review.
- Do not require a custom database, web app, or MCP server in the MVP.

## Milestones

### 1. Snapshot source docs

Populate `human/` from `skupperproject/skupper-docs` main and record the commit in:

```text
human/_source.md
sources/skupper-docs.md
```

### 2. Generate first OKF pages

Use `prompts/extract-from-human.md` against a small set of source files and write the result to:

```text
generated/concepts/
generated/resources/
generated/workflows/
```

### 3. Promote manually reviewed pages

Move selected generated files into `reviewed/` after human review.

### 4. Build indexes

Generate indexes for:

```text
indexes/source-coverage.md
indexes/review-status.md
indexes/concepts.md
```

### 5. Generate maps

Create first Blockscape outputs from reviewed OKF pages:

```text
maps/skupper-overview.blockscape.json
maps/skupper-docs-landscape.blockscape.json
```

### 6. Add agent access later

A later iteration can add:

```text
skills/
mcp-okf-server/
context-packs/
```

The MVP should stay file-based.
