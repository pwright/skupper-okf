---
type: DocumentationLandscapePage
title: "Host Installation"
id: host-installation
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/host-installation
tags:
  - skupper
  - docs-landscape
  - install
related:
  - host-prerequisites
  - host-package
timestamp: 2026-07-23T19:57:36Z
---

# Host Installation

Host Installation covers the local-system path for Podman, Docker, or Linux sites. Local source coverage says the CLI is required on local systems and that `skupper system install` installs or starts the local controller environment.

## Appears in

- [Install Skupper](./install-skupper.md) / Installation Methods

## Dependencies

- [Linux Host Prerequisites](./host-prerequisites.md)
- [Host Package](./host-package.md)

## Sources

- [Skupper installation guide](../../human/skupper-docs/input/install/index.md): Primary local source for CLI use on local systems and `skupper system install`.
- [System install command](../../human/skupper-docs/input/refdog/commands/system/install.md): Local command reference for checking and configuring local requirements.
- [CLI command overview](../../human/skupper-docs/refdog/config/commands/overview.md): Local source for Docker, Podman, and Linux CLI behavior.
- [System namespaces topic](../../human/skupper-docs/input/refdog/topics/system-namespaces.md): Local source candidate for local-system namespace behavior.
- [Skupper Ansible non-Kubernetes workflow](../skupper-ansible/skupper-ansible-workflow-non-kubernetes.md): Generated local source for Podman, Docker, and Linux lifecycle automation context.

## Website Links

- [Skupper installation docs](https://skupper.io/docs/install/index.html)
- [Refdog system install command](https://skupperproject.github.io/refdog/commands/system/install.html)
- [Refdog command reference](https://skupperproject.github.io/refdog/commands/index.html)

## Draft Notes

- Distinguish Podman, Docker, and Linux behavior where the command reference does.
- Include local controller lifecycle and reload behavior only where sourced.
- Avoid assuming package-manager installation details beyond the Skupper CLI install path.
