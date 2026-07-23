---
type: DocumentationLandscapePage
title: "Version Matrix"
id: version-matrix
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/version-matrix
tags:
  - skupper
  - docs-landscape
  - reference
timestamp: 2026-07-23T22:15:00Z
---

# Version Matrix

A version matrix records which Skupper documentation, command references, generated CRDs, APIs, and automation docs belong to the same release or source snapshot.

## Appears in

- [Skupper Reference](./skupper-reference.md) / Matrices and Terms

## Sources

- [human/skupper-docs/_source.md](../../human/skupper-docs/_source.md) - Local source metadata for the synced docs snapshot.
- [sources/skupper-docs.md](../../sources/skupper-docs.md) - Source inventory for Skupper docs.
- [sources/skupper-ansible.md](../../sources/skupper-ansible.md) - Source inventory for Skupper Ansible.
- [human/skupper-docs/input/refdog/commands/version.md](../../human/skupper-docs/input/refdog/commands/version.md) - Version command reference.
- [generated/skupper/skupper-api-network-observer.md](../skupper/skupper-api-network-observer.md) - Generated API source candidate for snapshot alignment.

## Website Links

- [Version command](https://skupperproject.github.io/refdog/commands/version.html)
- [Skupper docs repository](https://github.com/skupperproject/skupper-docs)
- [Skupper repository](https://github.com/skupperproject/skupper)
- [Skupper Ansible repository](https://github.com/skupperproject/skupper-ansible)

## Draft Notes

- Use local `_source.md` and `sources/*.md` files as the primary version evidence.
- Avoid claiming compatibility between releases without source-backed release notes.
- Include generated timestamp and source commit where available.
