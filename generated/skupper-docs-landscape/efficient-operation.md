---
type: DocumentationLandscapePage
title: "Efficient Resource Use"
id: efficient-operation
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/efficient-operation
tags:
  - skupper
  - docs-landscape
  - optimize
related:
  - resource-tuning
  - traffic-shaping
timestamp: 2026-07-23T21:00:00Z
---

# Efficient Resource Use

Efficient resource use means Skupper components and observer services have enough CPU, memory, and placement capacity for the workload without over-allocating where traffic does not require it.

## Appears in

- [Optimize Skupper](./optimize-skupper.md) / Optimization Outcomes

## Dependencies

- [Runtime Resource Tuning](./resource-tuning.md)
- [Traffic Shaping](./traffic-shaping.md)

## Sources

- [generated/concepts/network-deployment-concerns.md](../concepts/network-deployment-concerns.md) - Generated source for router resource allocation and observer placement.
- [human/skupper-docs/input/kube-yaml/site-configuration.md](../../human/skupper-docs/input/kube-yaml/site-configuration.md) - Local YAML source for site resource settings.
- [human/skupper-docs/input/console/configuration.md](../../human/skupper-docs/input/console/configuration.md) - Local source for observer and Prometheus resource requests and limits.
- [human/skupper-docs/input/overview/load-balancing.md](../../human/skupper-docs/input/overview/load-balancing.md) - Local source for traffic distribution controls.
- [generated/concepts/network-observer-api.md](../concepts/network-observer-api.md) - Generated source for observing traffic and connections.

## Website Links

- [Site configuration with YAML](https://skupper.io/docs/kube-yaml/site-configuration.html)
- [Network console configuration](https://skupper.io/docs/console/configuration.html)
- [Load balancing and failover](https://skupper.io/docs/overview/load-balancing.html)
- [Network console](https://skupper.io/docs/console/index.html)

## Draft Notes

- Treat efficiency as measured utilization plus acceptable service behavior.
- Document router and observer resources separately because they are tuned through different configuration surfaces.
- Avoid recommending lower resource settings without a validation loop and rollback point.
