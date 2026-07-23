---
type: DocumentationLandscapePage
title: "Compatibility Reference"
id: compatibility-reference
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/compatibility-reference
tags:
  - skupper
  - docs-landscape
  - reference
related:
  - version-matrix
  - platform-matrix
timestamp: 2026-07-23T22:15:00Z
---

# Compatibility Reference

The compatibility reference records version and platform assumptions that affect Skupper commands, resources, local-system support, and generated documentation.

## Appears in

- [Skupper Reference](./skupper-reference.md) / Runtime Reference

## Dependencies

- [Version Matrix](./version-matrix.md)
- [Platform Matrix](./platform-matrix.md)

## Sources

- [human/skupper-docs/input/install/index.md](../../human/skupper-docs/input/install/index.md) - Local installation source.
- [human/skupper-docs/input/refdog/commands/version.md](../../human/skupper-docs/input/refdog/commands/version.md) - Version command reference.
- [human/skupper-docs/input/system-cli/index.md](../../human/skupper-docs/input/system-cli/index.md) - System platform workflow index.
- [generated/skupper-ansible/skupper-ansible-module-system.md](../skupper-ansible/skupper-ansible-module-system.md) - Generated source for Podman, Docker, and Linux choices.
- [generated/skupper/skupper-api-network-observer.md](../skupper/skupper-api-network-observer.md) - Generated API source with platform enum values.

## Website Links

- [Installation](https://skupper.io/docs/install/index.html)
- [Version command](https://skupperproject.github.io/refdog/commands/version.html)
- [System CLI workflows](https://skupper.io/docs/system-cli/index.html)
- [Skupper Ansible repository](https://github.com/skupperproject/skupper-ansible)

## Draft Notes

- Keep compatibility claims limited to locally sourced platforms and version surfaces.
- Add an explicit "unknown or not yet sourced" bucket for gaps.
- Include both user-facing docs versions and generated source snapshots in future expansion.
