---
type: DocumentationLandscapePage
title: "Namespace Controls"
id: namespace-controls
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/namespace-controls
tags:
  - skupper
  - docs-landscape
  - secure
timestamp: 2026-07-23T20:30:00Z
---

# Namespace Controls

Namespace controls define where Skupper resources are created and how site, listener, connector, and attached-connector resources relate to application namespaces.

## Appears in

- [Secure Skupper](./secure-skupper.md) / Isolation Foundations

## Sources

- [human/skupper-docs/input/kube-cli/site-configuration.md](../../human/skupper-docs/input/kube-cli/site-configuration.md) - CLI site configuration source for namespace-scoped operations.
- [human/skupper-docs/input/kube-yaml/site-configuration.md](../../human/skupper-docs/input/kube-yaml/site-configuration.md) - YAML site configuration source.
- [human/skupper-docs/input/kube-yaml/service-exposure.md](../../human/skupper-docs/input/kube-yaml/service-exposure.md) - Source for normal and attached connector placement.
- [human/skupper-docs/input/refdog/topics/attached-connectors.md](../../human/skupper-docs/input/refdog/topics/attached-connectors.md) - Refdog topic source for connecting workloads in another namespace.
- [human/skupper-docs/input/refdog/resources/attached-connector.md](../../human/skupper-docs/input/refdog/resources/attached-connector.md) - AttachedConnector resource reference.

## Website Links

- [Site configuration with the Skupper CLI](https://skupper.io/docs/kube-cli/site-configuration.html)
- [Site configuration with YAML](https://skupper.io/docs/kube-yaml/site-configuration.html)
- [Service exposure with YAML](https://skupper.io/docs/kube-yaml/service-exposure.html)
- [Attached connectors topic](https://skupperproject.github.io/refdog/topics/attached-connectors.html)
- [AttachedConnector resource reference](https://skupperproject.github.io/refdog/resources/attached-connector.html)

## Draft Notes

- Clarify the difference between the site namespace and application workload namespaces.
- Add examples for attached connectors only after aligning terminology with the configure pages.
- Include RBAC and ownership notes where namespace-crossing resource placement is required.
