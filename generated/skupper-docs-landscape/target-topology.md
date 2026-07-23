---
type: DocumentationLandscapePage
title: "Target Application Network Topology"
id: target-topology
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/target-topology
tags:
  - skupper
  - docs-landscape
  - plan
related:
  - site-inventory
  - traffic-flows
timestamp: 2026-07-23T19:54:51Z
---

# Target Application Network Topology

Target Application Network Topology translates known sites, workloads, and traffic requirements into a proposed Skupper application network shape. It should describe where sites exist, which links are needed, where services are consumed, and which paths or constraints influence the design.

## Appears in

- [Plan a Skupper Deployment](./plan-skupper.md) / Deployment Design

## Dependencies

- [Cluster and Host Inventory](./site-inventory.md)
- [Traffic Flow Requirements](./traffic-flows.md)

## Sources

- [Network deployment concerns](../concepts/network-deployment-concerns.md): Generated local planning source for sites, links, link access, link constraints, service routing, and traffic direction.
- [Skupper connectivity overview](../../human/skupper-docs/input/overview/connectivity.md): Local source for the basic multi-cluster and hybrid connectivity model.
- [Site concept](../../human/skupper-docs/input/refdog/concepts/site.md): Local concept source for sites as places where workloads run and links join them.
- [Link concept](../../human/skupper-docs/input/refdog/concepts/link.md): Local concept source for link behavior, dynamic links, and larger network shapes.
- [Skupper example applications](../workflows/skupper-examples.md): Generated local source showing small and larger example topologies.

## Website Links

- [Skupper connectivity overview](https://skupper.io/docs/overview/connectivity.html)
- [Refdog site concept](https://skupperproject.github.io/refdog/concepts/site.html)
- [Refdog link concept](https://skupperproject.github.io/refdog/concepts/link.html)

## Draft Notes

- Start from actual application placement and traffic needs rather than drawing an idealized network first.
- Record which sites need link access and which sites initiate links.
- Separate required topology from optional resilience or optimization paths.
