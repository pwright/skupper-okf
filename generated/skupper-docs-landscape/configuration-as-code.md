---
type: DocumentationLandscapePage
title: "Configuration as Code"
id: configuration-as-code
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/configuration-as-code
tags:
  - skupper
  - docs-landscape
  - develop
related:
  - declarative-resources
  - version-control
timestamp: 2026-07-23T21:30:00Z
---

# Configuration as Code

Configuration as code keeps Skupper site, link, and service definitions in reviewable files that can be applied consistently across environments.

## Appears in

- [Develop with Skupper](./develop-skupper.md) / Development Interfaces

## Dependencies

- [Declarative Resources](./declarative-resources.md)
- [Version Control](./version-control.md)

## Sources

- [human/skupper-docs/input/kube-yaml/index.md](../../human/skupper-docs/input/kube-yaml/index.md) - Local source index for Kubernetes YAML workflows.
- [human/skupper-docs/input/system-yaml/index.md](../../human/skupper-docs/input/system-yaml/index.md) - Local source index for local-system YAML workflows.
- [human/skupper-docs/input/kube-yaml/custom-labels.md](../../human/skupper-docs/input/kube-yaml/custom-labels.md) - Local source for custom labels and annotations.
- [generated/skupper-ansible/skupper-ansible-module-resource.md](../skupper-ansible/skupper-ansible-module-resource.md) - Generated source for applying resource YAML through automation.
- [human/skupper-docs/input/refdog/resources/index.md](../../human/skupper-docs/input/refdog/resources/index.md) - Resource reference index.

## Website Links

- [Kubernetes YAML workflows](https://skupper.io/docs/kube-yaml/index.html)
- [System YAML workflows](https://skupper.io/docs/system-yaml/index.html)
- [Custom labels with YAML](https://skupper.io/docs/kube-yaml/custom-labels.html)
- [Refdog resource reference](https://skupperproject.github.io/refdog/resources/index.html)

## Draft Notes

- Document file layout, environment overlays, secret boundaries, and status validation.
- Keep generated credentials out of long-lived version control unless sources explicitly support that practice.
- Add review checklist items for namespaces, site names, link access, routing keys, and backend selectors.
