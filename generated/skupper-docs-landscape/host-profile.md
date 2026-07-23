---
type: DocumentationLandscapePage
title: "Host Compatibility Profile"
id: host-profile
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/host-profile
tags:
  - skupper
  - docs-landscape
  - platform
timestamp: 2026-07-23T22:00:00Z
---

# Host Compatibility Profile

A host compatibility profile records the local-system platform, container engine, namespace layout, and service endpoints needed for a Skupper host site.

## Appears in

- [Skupper Platform and Managed-Environment Guides](./platform-guides.md) / Platform Inputs

## Sources

- [human/skupper-docs/input/system-cli/index.md](../../human/skupper-docs/input/system-cli/index.md) - System CLI workflow index.
- [human/skupper-docs/input/system-yaml/index.md](../../human/skupper-docs/input/system-yaml/index.md) - System YAML workflow index.
- [human/skupper-docs/input/refdog/topics/system-namespaces.md](../../human/skupper-docs/input/refdog/topics/system-namespaces.md) - System namespaces topic.
- [generated/skupper-ansible/skupper-ansible-module-system.md](../skupper-ansible/skupper-ansible-module-system.md) - Generated source for Podman, Docker, and Linux system actions.
- [generated/skupper-ansible/skupper-ansible-module-controller.md](../skupper-ansible/skupper-ansible-module-controller.md) - Generated source for system controller lifecycle.

## Website Links

- [System CLI workflows](https://skupper.io/docs/system-cli/index.html)
- [System YAML workflows](https://skupper.io/docs/system-yaml/index.html)
- [System namespaces topic](https://skupperproject.github.io/refdog/topics/system-namespaces.html)
- [Skupper Ansible repository](https://github.com/skupperproject/skupper-ansible)

## Draft Notes

- Include platform, engine, permissions, network binding, and local service endpoint inventory.
- Keep Docker versus Podman guidance aligned with generated Ansible module notes.
- Add validation for system start, reload, and status output.
