---
type: DocumentationLandscapePage
title: "Flow Metrics"
id: flow-metrics
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/flow-metrics
tags:
  - skupper
  - docs-landscape
  - observe
related:
  - metrics-export
timestamp: 2026-07-23T20:45:00Z
---

# Flow Metrics

Flow metrics describe traffic records for application communication across the Skupper network, including data the observer and console use for traffic views.

## Appears in

- [Observe Skupper](./observe-skupper.md) / Observability Signals

## Dependencies

- [Metrics Export](./metrics-export.md)

## Sources

- [generated/concepts/network-observer-api.md](../concepts/network-observer-api.md) - Generated source for flow and application-flow endpoints.
- [generated/skupper/skupper-api-network-observer.md](../skupper/skupper-api-network-observer.md) - Generated OpenAPI source for observer resources.
- [generated/skupper-console/console.md](../skupper-console/console.md) - Generated source for console time-series and flow API calls.
- [human/skupper-docs/input/console/configuration.md](../../human/skupper-docs/input/console/configuration.md) - Local source for flow record retention and vanflow logging profile options.
- [generated/concepts/routing-key.md](../concepts/routing-key.md) - Generated source for routing-key usage in flow records.

## Website Links

- [Network console configuration](https://skupper.io/docs/console/configuration.html)
- [Network console](https://skupper.io/docs/console/index.html)
- [Skupper console repository](https://github.com/skupperproject/skupper-console)
- [Skupper repository](https://github.com/skupperproject/skupper)

## Draft Notes

- Treat flow metrics as observer-collected data, not as a promise that every deployment has persistent traffic history.
- Add examples showing how flow records relate to service addresses and routing keys.
- Document retention knobs before describing long-term trend analysis.
