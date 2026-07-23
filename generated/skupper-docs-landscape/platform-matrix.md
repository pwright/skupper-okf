---
type: DocumentationLandscapePage
title: "Platform Matrix"
id: platform-matrix
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/platform-matrix
tags:
  - skupper
  - docs-landscape
  - reference
timestamp: 2026-07-23T22:15:00Z
---

# Platform Matrix

A platform matrix summarizes the documented Skupper platform modes, including Kubernetes and local-system platforms such as Podman, Docker, and Linux.

## Appears in

- [Skupper Reference](./skupper-reference.md) / Matrices and Terms

## Sources

- [human/skupper-docs/input/kube-cli/index.md](../../human/skupper-docs/input/kube-cli/index.md) - Kubernetes CLI workflow index.
- [human/skupper-docs/input/system-cli/index.md](../../human/skupper-docs/input/system-cli/index.md) - System CLI workflow index.
- [human/skupper-docs/input/refdog/concepts/platform.md](../../human/skupper-docs/input/refdog/concepts/platform.md) - Platform concept source.
- [generated/skupper-ansible/skupper-ansible-module-system.md](../skupper-ansible/skupper-ansible-module-system.md) - Generated source for Podman, Docker, and Linux choices.
- [generated/skupper/skupper-api-network-observer.md](../skupper/skupper-api-network-observer.md) - Generated source containing observer platform enum values.

## Website Links

- [Kubernetes CLI workflows](https://skupper.io/docs/kube-cli/index.html)
- [System CLI workflows](https://skupper.io/docs/system-cli/index.html)
- [Platform concept](https://skupperproject.github.io/refdog/concepts/platform.html)
- [Skupper Ansible repository](https://github.com/skupperproject/skupper-ansible)

## Draft Notes

- Separate documented workflow availability from runtime observation values.
- Keep managed-platform provider names out until source material documents them.
- Add columns for site creation, linking, service exposure, resource automation, and observer support.
