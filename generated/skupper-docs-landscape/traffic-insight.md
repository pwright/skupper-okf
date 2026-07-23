---
type: DocumentationLandscapePage
title: "Traffic Insight"
id: traffic-insight
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/traffic-insight
tags:
  - skupper
  - docs-landscape
  - observe
related:
  - flow-metrics
  - trace-correlation
timestamp: 2026-07-23T20:45:00Z
---

# Traffic Insight

Traffic insight is the ability to inspect application flows, connection paths, and service activity across the Skupper network.

## Appears in

- [Observe Skupper](./observe-skupper.md) / Operational Visibility

## Dependencies

- [Flow Metrics](./flow-metrics.md)
- [Trace Correlation](./trace-correlation.md)

## Sources

- [generated/concepts/network-observer-api.md](../concepts/network-observer-api.md) - Generated source for observer endpoints that expose connections, flows, and services.
- [generated/skupper/skupper-api-network-observer.md](../skupper/skupper-api-network-observer.md) - Generated OpenAPI source for the network observer API.
- [generated/skupper-console/console.md](../skupper-console/console.md) - Generated source for console traffic, topology, and time-series queries.
- [human/skupper-docs/input/console/configuration.md](../../human/skupper-docs/input/console/configuration.md) - Local source for observer retention and vanflow logging options.
- [generated/concepts/routing-key.md](../concepts/routing-key.md) - Generated source for routing-key fields used in service and flow records.

## Website Links

- [Network console](https://skupper.io/docs/console/index.html)
- [Network console configuration](https://skupper.io/docs/console/configuration.html)
- [Skupper console repository](https://github.com/skupperproject/skupper-console)
- [Skupper repository](https://github.com/skupperproject/skupper)

## Draft Notes

- Tie traffic views back to routing keys, listeners, connectors, and application flows.
- Document retention and collection limits carefully because the observer configuration controls how long flow records remain available.
- Include examples that answer practical questions: which services are active, which sites are involved, and whether errors cluster by service.
