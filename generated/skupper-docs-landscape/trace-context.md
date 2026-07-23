---
type: DocumentationLandscapePage
title: "Trace Context"
id: trace-context
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/trace-context
tags:
  - skupper
  - docs-landscape
  - observe
timestamp: 2026-07-23T20:45:00Z
---

# Trace Context

Trace context is correlation data from application requests that can help connect Skupper traffic observations with application-level tracing systems.

## Appears in

- [Observe Skupper](./observe-skupper.md) / Collection and Presentation

## Sources

- [generated/concepts/network-observer-api.md](../concepts/network-observer-api.md) - Generated source for application-flow and flow records.
- [generated/skupper/skupper-api-network-observer.md](../skupper/skupper-api-network-observer.md) - Generated OpenAPI source for observer API fields.
- [generated/skupper-console/console.md](../skupper-console/console.md) - Generated source for console application-flow calls.
- [human/skupper-docs/input/console/configuration.md](../../human/skupper-docs/input/console/configuration.md) - Local source for observer collection options.
- [generated/skupper-docs-landscape/trace-correlation.md](./trace-correlation.md) - Related landscape page for correlation usage.

## Website Links

- [Network console](https://skupper.io/docs/console/index.html)
- [Network console configuration](https://skupper.io/docs/console/configuration.html)
- [Skupper console repository](https://github.com/skupperproject/skupper-console)
- [Skupper repository](https://github.com/skupperproject/skupper)

## Draft Notes

- Treat trace context as optional unless sources show it is always present.
- Confirm exact observer fields before writing field-level documentation.
- Add integration notes only after identifying source-backed tracing system examples.
