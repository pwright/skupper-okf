---
type: DocumentationLandscapePage
title: "Capacity Tuning"
id: capacity-tuning
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/capacity-tuning
tags:
  - skupper
  - docs-landscape
  - optimize
related:
  - traffic-baseline
  - headroom-model
timestamp: 2026-07-23T21:00:00Z
---

# Capacity Tuning

Capacity tuning adjusts Skupper resource allocation and topology choices based on observed traffic, expected growth, and available headroom.

## Appears in

- [Optimize Skupper](./optimize-skupper.md) / Optimization Levers

## Dependencies

- [Traffic Baseline](./traffic-baseline.md)
- [Capacity Headroom Model](./headroom-model.md)

## Sources

- [generated/concepts/network-deployment-concerns.md](../concepts/network-deployment-concerns.md) - Generated source for production traffic, router CPU allocation, and observer placement.
- [human/skupper-docs/input/kube-yaml/site-configuration.md](../../human/skupper-docs/input/kube-yaml/site-configuration.md) - Local source for declarative site resources.
- [human/skupper-docs/input/refdog/resources/site.md](../../human/skupper-docs/input/refdog/resources/site.md) - Site resource reference.
- [human/skupper-docs/input/console/configuration.md](../../human/skupper-docs/input/console/configuration.md) - Local source for observer and Prometheus resources and persistence.
- [generated/concepts/network-observer-api.md](../concepts/network-observer-api.md) - Generated source for observing connections and flows.

## Website Links

- [Site configuration with YAML](https://skupper.io/docs/kube-yaml/site-configuration.html)
- [Site resource reference](https://skupperproject.github.io/refdog/resources/site.html)
- [Network console configuration](https://skupper.io/docs/console/configuration.html)
- [Network console](https://skupper.io/docs/console/index.html)

## Draft Notes

- Start with measured traffic and current resource profile before changing resource limits.
- Document headroom assumptions explicitly because they vary by workload and cluster.
- Keep HA and replica guidance source-backed; do not infer performance improvements from additional routers.
