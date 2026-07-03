# Prompt: extract OKF from human source docs

Use `human/` as read-only source material. Create small OKF-style Markdown pages under `generated/`.

Rules:

- Preserve source provenance in YAML front matter.
- Prefer one concept, command, resource, or workflow per file.
- Do not rewrite the original documentation as marketing copy.
- Do not invent source paths.
- Mark all outputs as `status: generated` and `reviewed: false`.

Suggested front matter:

```yaml
type: Concept
title: <title>
id: skupper-concept-<slug>
status: generated
reviewed: false
source_repo: https://github.com/skupperproject/skupper-docs.git
source_branch: main
source_commit: <commit from sources/skupper-docs.md>
source_paths:
  - <path inside human/>
tags: []
related: []
```

Output directories:

```text
generated/concepts/
generated/resources/
generated/workflows/
generated/architecture/
```
