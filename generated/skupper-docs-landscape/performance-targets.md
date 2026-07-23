---
type: DocumentationLandscapePage
title: "Met Performance Targets"
id: performance-targets
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/performance-targets
tags:
  - skupper
  - docs-landscape
  - optimize
related:
  - routing-tuning
  - capacity-tuning
timestamp: 2026-07-23T21:00:00Z
---

# Met Performance Targets

Met performance targets means the Skupper network is carrying the intended traffic within agreed expectations for reachability, throughput, latency, and stability.

## Appears in

- [Optimize Skupper](./optimize-skupper.md) / Optimization Outcomes

## Dependencies

- [Routing Tuning](./routing-tuning.md)
- [Capacity Tuning](./capacity-tuning.md)

## Sources

- [generated/concepts/network-deployment-concerns.md](../concepts/network-deployment-concerns.md) - Generated source for resource allocation, link access, observer placement, and traffic direction.
- [human/skupper-docs/input/overview/load-balancing.md](../../human/skupper-docs/input/overview/load-balancing.md) - Local source for load balancing and failover behavior.
- [human/skupper-docs/input/refdog/topics/large-networks.md](../../human/skupper-docs/input/refdog/topics/large-networks.md) - Local source candidate for large-network considerations.
- [generated/concepts/network-observer-api.md](../concepts/network-observer-api.md) - Generated source for observing services, connections, and flows.
- [human/skupper-docs/input/troubleshooting/index.md](../../human/skupper-docs/input/troubleshooting/index.md) - Local troubleshooting source for checking symptoms and collecting evidence.

## Website Links

- [Load balancing and failover](https://skupper.io/docs/overview/load-balancing.html)
- [Large networks topic](https://skupperproject.github.io/refdog/topics/large-networks.html)
- [Network console](https://skupper.io/docs/console/index.html)
- [Troubleshooting](https://skupper.io/docs/troubleshooting/index.html)

## Draft Notes

- Define targets as workload-specific acceptance criteria, not generic Skupper benchmarks.
- Use observer and test evidence to separate application bottlenecks from Skupper routing or capacity limits.
- Add a future checklist for baseline, tuning change, validation run, and rollback decision.
