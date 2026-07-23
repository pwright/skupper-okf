---
type: DocumentationLandscapePage
title: "Application and Service Inventory"
id: application-inventory
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/application-inventory
tags:
  - skupper
  - docs-landscape
  - plan
timestamp: 2026-07-23T19:54:51Z
---

# Application and Service Inventory

Application and Service Inventory is the source list of workloads, services, clients, ports, and ownership information used to decide what Skupper should connect. It should identify candidate services before any topology or routing design is finalized.

## Appears in

- [Plan a Skupper Deployment](./plan-skupper.md) / Planning Inputs

## Sources

- [Skupper example applications](../workflows/skupper-examples.md): Generated local source showing how example applications are split into frontends, backends, and gRPC services.
- [Connector concept](../concepts/connector.md): Generated local concept source for the workload side of a service exposure plan.
- [Listener concept](../concepts/listener.md): Generated local concept source for the client-facing side of a service exposure plan.
- [Service exposure with the CLI](../../human/skupper-docs/input/kube-cli/service-exposure.md): Local source for translating a workload and port into connector/listener configuration.
- [Workload concept](../../human/skupper-docs/input/refdog/concepts/workload.md): Local concept source for workload terminology.

## Website Links

- [Skupper service exposure guide](https://skupper.io/docs/kube-cli/service-exposure.html)
- [Refdog connector concept](https://skupperproject.github.io/refdog/concepts/connector.html)
- [Refdog workload concept](https://skupperproject.github.io/refdog/concepts/workload.html)

## Draft Notes

- Capture service name, workload selector or host, port, protocol assumptions, owning team, and consuming clients.
- Mark whether each service is a first rollout candidate, later candidate, or out of scope.
- Keep service inventory separate from topology decisions so alternatives can be compared.
