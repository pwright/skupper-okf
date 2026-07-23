---
type: DocumentationLandscapePage
title: "Linux Host Pattern"
id: host-pattern
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/host-pattern
tags:
  - skupper
  - docs-landscape
  - platform
related:
  - host-profile
  - system-service
timestamp: 2026-07-23T22:00:00Z
---

# Linux Host Pattern

The Linux host pattern runs a local-system Skupper site on Podman, Docker, or Linux and connects host services to the application network.

## Appears in

- [Skupper Platform and Managed-Environment Guides](./platform-guides.md) / Platform Patterns

## Dependencies

- [Host Compatibility Profile](./host-profile.md)
- [System Service Configuration](./system-service.md)

## Sources

- [human/skupper-docs/input/system-cli/index.md](../../human/skupper-docs/input/system-cli/index.md) - System CLI workflow index.
- [human/skupper-docs/input/system-yaml/index.md](../../human/skupper-docs/input/system-yaml/index.md) - System YAML workflow index.
- [human/skupper-docs/input/refdog/topics/system-namespaces.md](../../human/skupper-docs/input/refdog/topics/system-namespaces.md) - System namespaces topic.
- [generated/skupper-ansible/skupper-ansible-module-system.md](../skupper-ansible/skupper-ansible-module-system.md) - Generated source for system site lifecycle.
- [generated/skupper-ansible/skupper-ansible-workflow-non-kubernetes.md](../skupper-ansible/skupper-ansible-workflow-non-kubernetes.md) - Generated non-Kubernetes workflow.

## Website Links

- [System CLI workflows](https://skupper.io/docs/system-cli/index.html)
- [System YAML workflows](https://skupper.io/docs/system-yaml/index.html)
- [System namespaces topic](https://skupperproject.github.io/refdog/topics/system-namespaces.html)
- [Skupper Ansible repository](https://github.com/skupperproject/skupper-ansible)

## Draft Notes

- Describe lifecycle actions and resource file placement separately.
- Keep Podman, Docker, and Linux engine differences source-backed.
- Add service binding and link validation checks.
