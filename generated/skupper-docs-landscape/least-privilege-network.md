---
type: DocumentationLandscapePage
title: "Least-Privilege Application Network"
id: least-privilege-network
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/least-privilege-network
tags:
  - skupper
  - docs-landscape
  - secure
related:
  - access-policy
  - network-isolation
timestamp: 2026-07-23T20:30:00Z
---

# Least-Privilege Application Network

A least-privilege application network exposes only the intended services, keeps Skupper resources scoped to the intended namespaces, and depends on platform access controls for who can create or change those resources.

## Appears in

- [Secure Skupper](./secure-skupper.md) / Security Outcomes

## Dependencies

- [Access Policy](./access-policy.md)
- [Network Isolation](./network-isolation.md)

## Sources

- [human/skupper-docs/input/kube-cli/service-exposure.md](../../human/skupper-docs/input/kube-cli/service-exposure.md) - CLI workflow for selecting listeners and connectors.
- [human/skupper-docs/input/kube-yaml/service-exposure.md](../../human/skupper-docs/input/kube-yaml/service-exposure.md) - YAML examples for service exposure resources.
- [human/skupper-docs/input/refdog/resources/listener.md](../../human/skupper-docs/input/refdog/resources/listener.md) - Resource reference for listener configuration.
- [human/skupper-docs/input/refdog/resources/connector.md](../../human/skupper-docs/input/refdog/resources/connector.md) - Resource reference for connector configuration.
- [human/skupper-docs/input/overview/resources.md](../../human/skupper-docs/input/overview/resources.md) - Overview of Skupper resources created in Kubernetes.

## Website Links

- [Service exposure with the Skupper CLI](https://skupper.io/docs/kube-cli/service-exposure.html)
- [Service exposure with YAML](https://skupper.io/docs/kube-yaml/service-exposure.html)
- [Listener resource reference](https://skupperproject.github.io/refdog/resources/listener.html)
- [Connector resource reference](https://skupperproject.github.io/refdog/resources/connector.html)

## Draft Notes

- Frame this as a design and review page, not as a single command sequence.
- Add examples that compare broad service exposure with intentionally narrow listener and connector definitions.
- Future expansion should identify which controls belong to Skupper and which are inherited from Kubernetes namespace and RBAC policy.
