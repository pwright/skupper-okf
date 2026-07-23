---
type: DocumentationLandscapePage
title: "Linux Host Prerequisites"
id: host-prerequisites
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/host-prerequisites
tags:
  - skupper
  - docs-landscape
  - install
timestamp: 2026-07-23T19:57:36Z
---

# Linux Host Prerequisites

Linux Host Prerequisites covers the local-system requirements for Skupper on Podman, Docker, or Linux. Local source coverage is mostly command-reference level, so keep this page focused on platform selection, CLI availability, and controller/runtime checks.

## Appears in

- [Install Skupper](./install-skupper.md) / Prerequisites and Validation

## Sources

- [Skupper installation guide](../../human/skupper-docs/input/install/index.md): Local source stating that local systems use the CLI and `skupper system install`.
- [System install command](../../human/skupper-docs/input/refdog/commands/system/install.md): Primary local command source for local environment checks and configuration.
- [CLI command overview](../../human/skupper-docs/refdog/config/commands/overview.md): Local source for Docker, Podman, and Linux namespace and command behavior.
- [Platform concept](../../human/skupper-docs/input/refdog/concepts/platform.md): Local concept source for supported platforms.
- [Skupper Ansible non-Kubernetes workflow](../skupper-ansible/skupper-ansible-workflow-non-kubernetes.md): Generated local source for Podman and Docker lifecycle caveats.

## Website Links

- [Skupper installation docs](https://skupper.io/docs/install/index.html)
- [Refdog system install command](https://skupperproject.github.io/refdog/commands/system/install.html)
- [Refdog platform concept](https://skupperproject.github.io/refdog/concepts/platform.html)

## Draft Notes

- Verify whether host-specific package and runtime prerequisites are documented elsewhere before adding prescriptive steps.
- Capture selected platform value: `podman`, `docker`, or `linux`.
- Mention Docker versus Podman caveats only when backed by local Ansible or command docs.
