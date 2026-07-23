---
type: DocumentationLandscapePage
title: "Capacity Plan"
id: capacity-plan
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/capacity-plan
tags:
  - skupper
  - docs-landscape
  - plan
related:
  - traffic-flows
  - availability-targets
timestamp: 2026-07-23T19:54:51Z
---

# Capacity Plan

Capacity Plan estimates the resources and topology choices needed for expected Skupper traffic. The current local sources support conservative guidance around router CPU allocation, high-traffic sites, and the limits of adding routers for performance.

## Appears in

- [Plan a Skupper Deployment](./plan-skupper.md) / Requirements and Constraints

## Dependencies

- [Traffic Flow Requirements](./traffic-flows.md)
- [Availability Targets](./availability-targets.md)

## Sources

- [Network deployment concerns](../concepts/network-deployment-concerns.md): Primary generated local source for router CPU allocation, high availability behavior, and traffic direction concerns.
- [Kubernetes site configuration with YAML](../../human/skupper-docs/input/kube-yaml/site-configuration.md): Local source candidate for site resource settings and high-availability configuration.
- [Skupper load balancing and failover](../../human/skupper-docs/input/overview/load-balancing.md): Local source for connection distribution, failover, and link cost behavior.
- [Network console guide](../../human/skupper-docs/input/console/index.md): Local source for observing traffic and selecting a console location.
- [Network Observer API concept](../concepts/network-observer-api.md): Generated local source for runtime state and traffic-flow visibility.

## Website Links

- [Skupper load balancing and failover](https://skupper.io/docs/overview/load-balancing.html)
- [Skupper YAML site configuration](https://skupper.io/docs/kube-yaml/site-configuration.html)
- [Skupper network console](https://skupper.io/docs/console/index.html)

## Draft Notes

- Treat capacity numbers as planning assumptions until validated with workload tests.
- Document high-traffic sites and expected connection patterns before selecting router resources.
- Avoid claiming HA improves throughput; local sources say extra routers do not improve network performance.
