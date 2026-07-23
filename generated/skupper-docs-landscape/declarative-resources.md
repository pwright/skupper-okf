---
type: DocumentationLandscapePage
title: "Declarative Resources"
id: declarative-resources
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/declarative-resources
tags:
  - skupper
  - docs-landscape
  - develop
related:
  - resource-schema
  - examples
timestamp: 2026-07-23T21:30:00Z
---

# Declarative Resources

Declarative resources describe Skupper sites, links, listeners, connectors, and related objects as YAML that can be reviewed, applied, and versioned.

## Appears in

- [Develop with Skupper](./develop-skupper.md) / Development Interfaces

## Dependencies

- [Resource Schemas](./resource-schema.md)
- [Reference Examples](./examples.md)

## Sources

- [human/skupper-docs/input/kube-yaml/site-configuration.md](../../human/skupper-docs/input/kube-yaml/site-configuration.md) - Local source for Site YAML.
- [human/skupper-docs/input/kube-yaml/site-linking.md](../../human/skupper-docs/input/kube-yaml/site-linking.md) - Local source for link-related YAML.
- [human/skupper-docs/input/kube-yaml/service-exposure.md](../../human/skupper-docs/input/kube-yaml/service-exposure.md) - Local source for Listener, Connector, MultiKeyListener, and attached connector YAML.
- [human/skupper-docs/input/refdog/resources/index.md](../../human/skupper-docs/input/refdog/resources/index.md) - Local resource reference index.
- [generated/skupper-ansible/skupper-ansible-module-resource.md](../skupper-ansible/skupper-ansible-module-resource.md) - Generated source for applying Skupper resource YAML with Ansible.

## Website Links

- [Site configuration with YAML](https://skupper.io/docs/kube-yaml/site-configuration.html)
- [Site linking with YAML](https://skupper.io/docs/kube-yaml/site-linking.html)
- [Service exposure with YAML](https://skupper.io/docs/kube-yaml/service-exposure.html)
- [Refdog resource reference](https://skupperproject.github.io/refdog/resources/index.html)

## Draft Notes

- Expand by resource type and workflow stage rather than listing every field inline.
- Include validation and status checks after each applied resource set.
- Keep Kubernetes and local-system YAML differences explicit.
