---
type: DocumentationLandscapePage
title: "Trace Correlation"
id: trace-correlation
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/trace-correlation
tags:
  - skupper
  - docs-landscape
  - observe
related:
  - trace-context
timestamp: 2026-07-23T20:45:00Z
---

# Trace Correlation

Trace correlation connects observed Skupper traffic records with application trace context where that context is available from the workload or monitoring stack.

## Appears in

- [Observe Skupper](./observe-skupper.md) / Observability Signals

## Dependencies

- [Trace Context](./trace-context.md)

## Sources

- [generated/concepts/network-observer-api.md](../concepts/network-observer-api.md) - Generated source for flows, connections, and application-flow records.
- [generated/skupper/skupper-api-network-observer.md](../skupper/skupper-api-network-observer.md) - Generated OpenAPI source for observer API fields.
- [generated/skupper-console/console.md](../skupper-console/console.md) - Generated source for console application-flow calls.
- [human/skupper-docs/input/console/configuration.md](../../human/skupper-docs/input/console/configuration.md) - Local source for observer collection settings.
- [generated/skupper-docs-landscape/trace-context.md](./trace-context.md) - Related landscape page for trace context.

## Website Links

- [Network console](https://skupper.io/docs/console/index.html)
- [Network console configuration](https://skupper.io/docs/console/configuration.html)
- [Skupper console repository](https://github.com/skupperproject/skupper-console)
- [Skupper repository](https://github.com/skupperproject/skupper)

## Draft Notes

- Source coverage is limited; avoid implying full distributed tracing support without an explicit source.
- Start future expansion by listing observer fields that can be used for correlation.
- Keep application instrumentation requirements separate from Skupper observer behavior.
