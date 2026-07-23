---
type: DocumentationLandscapePage
title: "System Service Configuration"
id: system-service
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/system-service
tags:
  - skupper
  - docs-landscape
  - platform
related:
  - host-profile
timestamp: 2026-07-23T22:00:00Z
---

# System Service Configuration

System service configuration defines how local host services are represented by Skupper resources and started or reloaded in a local-system site.

## Appears in

- [Skupper Platform and Managed-Environment Guides](./platform-guides.md) / Platform Inputs

## Dependencies

- [Host Compatibility Profile](./host-profile.md)

## Sources

- [human/skupper-docs/input/system-cli/service-exposure.md](../../human/skupper-docs/input/system-cli/service-exposure.md) - System CLI service exposure source.
- [human/skupper-docs/input/system-yaml/service-exposure.md](../../human/skupper-docs/input/system-yaml/service-exposure.md) - System YAML service exposure source.
- [human/skupper-docs/input/refdog/resources/connector.md](../../human/skupper-docs/input/refdog/resources/connector.md) - Connector resource reference.
- [generated/skupper-ansible/skupper-ansible-module-resource.md](../skupper-ansible/skupper-ansible-module-resource.md) - Generated resource automation source.
- [generated/skupper-ansible/skupper-ansible-module-system.md](../skupper-ansible/skupper-ansible-module-system.md) - Generated system reload and lifecycle source.

## Website Links

- [System CLI service exposure](https://skupper.io/docs/system-cli/service-exposure.html)
- [System YAML service exposure](https://skupper.io/docs/system-yaml/service-exposure.html)
- [Connector resource reference](https://skupperproject.github.io/refdog/resources/connector.html)
- [Skupper Ansible repository](https://github.com/skupperproject/skupper-ansible)

## Draft Notes

- Keep service endpoint host and port details explicit.
- Include reload or start requirements after resource files change.
- Add application reachability checks after connector status checks.
