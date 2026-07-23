---
type: DocumentationLandscapePage
title: "Linux Host Integration"
id: host-integration
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/host-integration
tags:
  - skupper
  - docs-landscape
  - integrate
related:
  - host-service-binding
  - host-identity
timestamp: 2026-07-23T21:45:00Z
---

# Linux Host Integration

Linux host integration connects services on local-system platforms such as Podman, Docker, or Linux sites into a Skupper application network.

## Appears in

- [Integrate Skupper](./integrate-skupper.md) / Integration Patterns

## Dependencies

- [Host Service Binding](./host-service-binding.md)
- [Host Identity](./host-identity.md)

## Sources

- [human/skupper-docs/input/system-cli/site-configuration.md](../../human/skupper-docs/input/system-cli/site-configuration.md) - Local CLI source for system site configuration.
- [human/skupper-docs/input/system-cli/service-exposure.md](../../human/skupper-docs/input/system-cli/service-exposure.md) - Local CLI source for exposing local-system services.
- [human/skupper-docs/input/system-yaml/site-configuration.md](../../human/skupper-docs/input/system-yaml/site-configuration.md) - Local YAML source for system site configuration.
- [generated/skupper-ansible/skupper-ansible-module-system.md](../skupper-ansible/skupper-ansible-module-system.md) - Generated source for system-site lifecycle automation.
- [generated/skupper-ansible/skupper-ansible-workflow-non-kubernetes.md](../skupper-ansible/skupper-ansible-workflow-non-kubernetes.md) - Generated source for non-Kubernetes automation.

## Website Links

- [System site configuration](https://skupper.io/docs/system-cli/site-configuration.html)
- [System service exposure](https://skupper.io/docs/system-cli/service-exposure.html)
- [System YAML workflows](https://skupper.io/docs/system-yaml/index.html)
- [Skupper Ansible repository](https://github.com/skupperproject/skupper-ansible)

## Draft Notes

- Separate Podman, Docker, and Linux-specific assumptions only where source docs provide them.
- Include lifecycle actions such as start, reload, stop, and bundle generation in future expansion.
- Validate host service reachability through connector status and application checks.
