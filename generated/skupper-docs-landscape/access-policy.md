---
type: DocumentationLandscapePage
title: "Access Policy"
id: access-policy
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/access-policy
tags:
  - skupper
  - docs-landscape
  - secure
related:
  - rbac
  - service-policy
timestamp: 2026-07-23T20:30:00Z
---

# Access Policy

Access policy covers who can administer Skupper resources and which application services are exposed through the application network.

## Appears in

- [Secure Skupper](./secure-skupper.md) / Security Controls

## Dependencies

- [Role-Based Access Control](./rbac.md)
- [Service Exposure Policy](./service-policy.md)

## Sources

- [human/skupper-docs/input/overview/resources.md](../../human/skupper-docs/input/overview/resources.md) - Local overview of Kubernetes resources involved in Skupper operation.
- [human/skupper-docs/input/kube-yaml/service-exposure.md](../../human/skupper-docs/input/kube-yaml/service-exposure.md) - Declarative source for service exposure resources.
- [human/skupper-docs/input/refdog/resources/listener.md](../../human/skupper-docs/input/refdog/resources/listener.md) - Listener fields used to define exposed service endpoints.
- [human/skupper-docs/input/refdog/resources/connector.md](../../human/skupper-docs/input/refdog/resources/connector.md) - Connector fields used to target backend workloads.
- [human/skupper-docs/refdog/crds/skupper_cluster_policy_crd.yaml](../../human/skupper-docs/refdog/crds/skupper_cluster_policy_crd.yaml) - Local CRD candidate for cluster policy coverage.

## Website Links

- [Service exposure with YAML](https://skupper.io/docs/kube-yaml/service-exposure.html)
- [Skupper resources overview](https://skupper.io/docs/overview/resources.html)
- [Listener resource reference](https://skupperproject.github.io/refdog/resources/listener.html)
- [Connector resource reference](https://skupperproject.github.io/refdog/resources/connector.html)

## Draft Notes

- Split administrative authorization from service exposure decisions in the expanded page.
- Validate cluster policy behavior against source docs before documenting it as a supported user workflow.
- Include a future review checklist for listener names, routing keys, connector selectors, and namespace ownership.
