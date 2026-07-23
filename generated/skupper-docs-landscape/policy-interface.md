---
type: DocumentationLandscapePage
title: "Policy Interface"
id: policy-interface
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/policy-interface
tags:
  - skupper
  - docs-landscape
  - integrate
timestamp: 2026-07-23T21:45:00Z
---

# Policy Interface

The policy interface covers Skupper and platform controls that constrain who can configure the application network and what services can be exposed.

## Appears in

- [Integrate Skupper](./integrate-skupper.md) / Operations Interfaces

## Sources

- [human/skupper-docs/input/overview/resources.md](../../human/skupper-docs/input/overview/resources.md) - Local overview of Kubernetes resources and ownership.
- [human/skupper-docs/input/kube-yaml/service-exposure.md](../../human/skupper-docs/input/kube-yaml/service-exposure.md) - Local source for service exposure resources.
- [human/skupper-docs/refdog/crds/skupper_cluster_policy_crd.yaml](../../human/skupper-docs/refdog/crds/skupper_cluster_policy_crd.yaml) - Local CRD candidate for cluster policy.
- [human/skupper-docs/input/refdog/resources/listener.md](../../human/skupper-docs/input/refdog/resources/listener.md) - Listener resource reference.
- [human/skupper-docs/input/refdog/resources/connector.md](../../human/skupper-docs/input/refdog/resources/connector.md) - Connector resource reference.

## Website Links

- [Skupper resources overview](https://skupper.io/docs/overview/resources.html)
- [Service exposure with YAML](https://skupper.io/docs/kube-yaml/service-exposure.html)
- [Listener resource reference](https://skupperproject.github.io/refdog/resources/listener.html)
- [Connector resource reference](https://skupperproject.github.io/refdog/resources/connector.html)

## Draft Notes

- Keep administrative RBAC, service exposure policy, and cluster policy as separate topics.
- Validate cluster policy examples before treating them as a primary documented interface.
- Add review checks for routing keys, selectors, host bindings, and namespace boundaries.
