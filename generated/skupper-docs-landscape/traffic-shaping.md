---
type: DocumentationLandscapePage
title: "Traffic Shaping"
id: traffic-shaping
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/traffic-shaping
tags:
  - skupper
  - docs-landscape
  - optimize
related:
  - service-priorities
  - rate-controls
timestamp: 2026-07-23T21:00:00Z
---

# Traffic Shaping

Traffic shaping covers source-backed ways to influence where application traffic goes, especially link cost and multi-key listener distribution.

## Appears in

- [Optimize Skupper](./optimize-skupper.md) / Optimization Levers

## Dependencies

- [Service Priorities](./service-priorities.md)
- [Rate Controls](./rate-controls.md)

## Sources

- [human/skupper-docs/input/overview/load-balancing.md](../../human/skupper-docs/input/overview/load-balancing.md) - Local source for load balancing and failover behavior.
- [generated/concepts/network-deployment-concerns.md](../concepts/network-deployment-concerns.md) - Generated source for traffic direction, link cost, and multi-key listener notes.
- [human/skupper-docs/input/refdog/resources/multi-key-listener.md](../../human/skupper-docs/input/refdog/resources/multi-key-listener.md) - MultiKeyListener resource reference.
- [human/skupper-docs/input/refdog/concepts/multi-key-listener.md](../../human/skupper-docs/input/refdog/concepts/multi-key-listener.md) - Concept source for multi-key listener behavior.
- [generated/concepts/routing-key.md](../concepts/routing-key.md) - Generated source for routing key relationships.

## Website Links

- [Load balancing and failover](https://skupper.io/docs/overview/load-balancing.html)
- [Multi-key listener concept](https://skupperproject.github.io/refdog/concepts/multi-key-listener.html)
- [MultiKeyListener resource reference](https://skupperproject.github.io/refdog/resources/multi-key-listener.html)
- [Routing key concept](https://skupperproject.github.io/refdog/concepts/routing-key.html)

## Draft Notes

- Avoid generic rate-limiting claims unless a source-backed Skupper control is identified.
- Focus near-term content on weighted distribution, failover strategy, and link-cost implications.
- Add validation steps that use observer data to confirm traffic moved as expected.
