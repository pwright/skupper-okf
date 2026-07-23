---
type: DocumentationLandscapePage
title: "Observability Integration"
id: observability-integration
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/observability-integration
tags:
  - skupper
  - docs-landscape
  - integrate
related:
  - metrics-interface
  - logging-interface
timestamp: 2026-07-23T21:45:00Z
---

# Observability Integration

Observability integration connects Skupper network state, metrics, logs, flows, and console data with monitoring and diagnostic workflows.

## Appears in

- [Integrate Skupper](./integrate-skupper.md) / Integration Patterns

## Dependencies

- [Metrics Interface](./metrics-interface.md)
- [Logging Interface](./logging-interface.md)

## Sources

- [human/skupper-docs/input/console/index.md](../../human/skupper-docs/input/console/index.md) - Local source for the network console.
- [human/skupper-docs/input/console/configuration.md](../../human/skupper-docs/input/console/configuration.md) - Local source for metrics endpoint, Prometheus, logging profile, and persistence.
- [generated/skupper-console/console.md](../skupper-console/console.md) - Generated source for console API and metrics usage.
- [generated/concepts/network-observer-api.md](../concepts/network-observer-api.md) - Generated source for observer API resources and monitoring use cases.
- [human/skupper-docs/input/troubleshooting/index.md](../../human/skupper-docs/input/troubleshooting/index.md) - Local source for diagnostic evidence collection.

## Website Links

- [Network console](https://skupper.io/docs/console/index.html)
- [Network console configuration](https://skupper.io/docs/console/configuration.html)
- [Troubleshooting](https://skupper.io/docs/troubleshooting/index.html)
- [Skupper console repository](https://github.com/skupperproject/skupper-console)

## Draft Notes

- Keep console UI, observer API, Prometheus metrics, and logs as distinct interfaces.
- Add scrape examples only where the local configuration source documents them.
- Include missing-telemetry diagnosis separately from actual network health.
