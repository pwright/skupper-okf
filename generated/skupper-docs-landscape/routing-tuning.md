---
type: DocumentationLandscapePage
title: "Routing Tuning"
id: routing-tuning
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/routing-tuning
tags:
  - skupper
  - docs-landscape
  - optimize
related:
  - topology-analysis
  - path-selection
timestamp: 2026-07-23T21:00:00Z
---

# Routing Tuning

Routing tuning adjusts how traffic moves through a Skupper network by reviewing topology, link costs, and service-level distribution choices.

## Appears in

- [Optimize Skupper](./optimize-skupper.md) / Optimization Levers

## Dependencies

- [Topology Analysis](./topology-analysis.md)
- [Path Selection Data](./path-selection.md)

## Sources

- [generated/concepts/network-deployment-concerns.md](../concepts/network-deployment-concerns.md) - Generated source for link cost, multi-key listeners, and topology notes.
- [human/skupper-docs/input/overview/load-balancing.md](../../human/skupper-docs/input/overview/load-balancing.md) - Local source for load balancing and failover controls.
- [human/skupper-docs/input/refdog/topics/load-balancing.md](../../human/skupper-docs/input/refdog/topics/load-balancing.md) - Refdog source candidate for routing behavior.
- [human/skupper-docs/input/refdog/resources/multi-key-listener.md](../../human/skupper-docs/input/refdog/resources/multi-key-listener.md) - MultiKeyListener resource reference.
- [human/skupper-docs/input/refdog/resources/link.md](../../human/skupper-docs/input/refdog/resources/link.md) - Link resource reference.

## Website Links

- [Load balancing and failover](https://skupper.io/docs/overview/load-balancing.html)
- [Load balancing topic](https://skupperproject.github.io/refdog/topics/load-balancing.html)
- [MultiKeyListener resource reference](https://skupperproject.github.io/refdog/resources/multi-key-listener.html)
- [Link resource reference](https://skupperproject.github.io/refdog/resources/link.html)

## Draft Notes

- Distinguish network-wide link-cost effects from per-service multi-key listener behavior.
- Capture current topology and traffic paths before changing cost or distribution strategy.
- Include examples for failover and weighted distribution only where the source examples support them.
