---
type: DocumentationLandscapePage
title: "Rate Controls"
id: rate-controls
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/rate-controls
tags:
  - skupper
  - docs-landscape
  - optimize
timestamp: 2026-07-23T21:00:00Z
---

# Rate Controls

Rate controls are candidate controls for limiting or smoothing traffic; current local source coverage primarily supports observing traffic and shaping paths rather than documenting explicit Skupper rate limits.

## Appears in

- [Optimize Skupper](./optimize-skupper.md) / Validation Inputs

## Sources

- [generated/concepts/network-observer-api.md](../concepts/network-observer-api.md) - Generated source for observing connections and flows.
- [generated/skupper-console/console.md](../skupper-console/console.md) - Generated source for console traffic and metrics views.
- [human/skupper-docs/input/console/configuration.md](../../human/skupper-docs/input/console/configuration.md) - Local source for observer retention, logging, and metrics collection.
- [human/skupper-docs/input/overview/load-balancing.md](../../human/skupper-docs/input/overview/load-balancing.md) - Local source for traffic distribution controls.
- [human/skupper-docs/input/troubleshooting/index.md](../../human/skupper-docs/input/troubleshooting/index.md) - Local source for diagnosing overload symptoms.

## Website Links

- [Network console](https://skupper.io/docs/console/index.html)
- [Network console configuration](https://skupper.io/docs/console/configuration.html)
- [Load balancing and failover](https://skupper.io/docs/overview/load-balancing.html)
- [Troubleshooting](https://skupper.io/docs/troubleshooting/index.html)

## Draft Notes

- Keep this page marked as thin coverage until explicit Skupper rate-control documentation is identified.
- Document observed overload symptoms and path-shaping alternatives before introducing any rate-limit guidance.
- If rate limits are delegated to the application, ingress, or platform layer, state that boundary explicitly with sources.
