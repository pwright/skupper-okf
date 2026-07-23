---
type: DocumentationLandscapePage
title: "Host Package"
id: host-package
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/host-package
tags:
  - skupper
  - docs-landscape
  - install
related:
  - host-prerequisites
timestamp: 2026-07-23T19:57:36Z
---

# Host Package

Host Package identifies the local-system Skupper artifact used on Podman, Docker, or Linux. The current local installation source treats the CLI as the required local-system package and uses `skupper system install` to prepare or start the local controller environment.

## Appears in

- [Install Skupper](./install-skupper.md) / Prerequisites and Validation

## Dependencies

- [Linux Host Prerequisites](./host-prerequisites.md)

## Sources

- [Skupper installation guide](../../human/skupper-docs/input/install/index.md): Primary local source for CLI installation and local-system controller setup.
- [System install command](../../human/skupper-docs/input/refdog/commands/system/install.md): Local command reference for local environment setup.
- [CLI command overview](../../human/skupper-docs/refdog/config/commands/overview.md): Local source for local-system platform behavior.
- [Skupper Ansible controller module](../skupper-ansible/skupper-ansible-module-controller.md): Generated local source for Podman and Docker controller lifecycle context.
- [Skupper source entry](../../sources/skupper.md): Local source record for upstream release artifacts.

## Website Links

- [Skupper releases](https://skupper.io/releases/index.html)
- [Skupper GitHub releases](https://github.com/skupperproject/skupper/releases)
- [Refdog system install command](https://skupperproject.github.io/refdog/commands/system/install.html)

## Draft Notes

- Treat the CLI as the documented local-system package unless more specific host packaging docs are added.
- Capture runtime engine assumptions separately from package download instructions.
- Include package provenance and version verification before expanding automation examples.
