---
type: DocumentationLandscapePage
title: "Service Exposure Policy"
id: service-policy
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/service-policy
tags:
  - skupper
  - docs-landscape
  - secure
timestamp: 2026-07-23T20:30:00Z
---

# Service Exposure Policy

Service exposure policy is the set of decisions that determines which service addresses are made available on the application network and which backend workloads they route to.

## Appears in

- [Secure Skupper](./secure-skupper.md) / Identity Foundations

## Sources

- [human/skupper-docs/input/kube-cli/service-exposure.md](../../human/skupper-docs/input/kube-cli/service-exposure.md) - CLI workflow for exposing services with listeners and connectors.
- [human/skupper-docs/input/kube-yaml/service-exposure.md](../../human/skupper-docs/input/kube-yaml/service-exposure.md) - YAML workflow for declarative service exposure.
- [human/skupper-docs/input/refdog/topics/service-exposure.md](../../human/skupper-docs/input/refdog/topics/service-exposure.md) - Refdog topic source for service exposure.
- [human/skupper-docs/input/refdog/resources/listener.md](../../human/skupper-docs/input/refdog/resources/listener.md) - Listener resource reference.
- [human/skupper-docs/input/refdog/resources/connector.md](../../human/skupper-docs/input/refdog/resources/connector.md) - Connector resource reference.

## Website Links

- [Service exposure with the Skupper CLI](https://skupper.io/docs/kube-cli/service-exposure.html)
- [Service exposure with YAML](https://skupper.io/docs/kube-yaml/service-exposure.html)
- [Service exposure topic](https://skupperproject.github.io/refdog/topics/service-exposure.html)
- [Listener resource reference](https://skupperproject.github.io/refdog/resources/listener.html)
- [Connector resource reference](https://skupperproject.github.io/refdog/resources/connector.html)

## Draft Notes

- Expand with an approval checklist for each exposed service address, port, protocol, routing key, and backend selector.
- Include attached connector policy once namespace ownership and binding behavior are documented.
- Avoid presenting service exposure as inherently global; describe exactly what the listener and connector definitions make reachable.
