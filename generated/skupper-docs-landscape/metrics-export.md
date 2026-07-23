---
type: DocumentationLandscapePage
title: "Metrics Export"
id: metrics-export
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/metrics-export
tags:
  - skupper
  - docs-landscape
  - observe
timestamp: 2026-07-23T20:45:00Z
---

# Metrics Export

Metrics export is the collection path that makes Skupper observer and console data available to Prometheus-compatible systems and dashboard views.

## Appears in

- [Observe Skupper](./observe-skupper.md) / Collection and Presentation

## Sources

- [human/skupper-docs/input/console/configuration.md](../../human/skupper-docs/input/console/configuration.md) - Local source for Prometheus configuration, persistence, and observer options.
- [human/skupper-docs/input/console/index.md](../../human/skupper-docs/input/console/index.md) - Local source for installing the network observer and console.
- [generated/skupper-console/console.md](../skupper-console/console.md) - Generated source for console Prometheus-compatible queries.
- [generated/concepts/network-observer-api.md](../concepts/network-observer-api.md) - Generated source for monitoring use cases and observer API scope.
- [sources/skupper-console.md](../../sources/skupper-console.md) - Local source inventory for the console repository.

## Website Links

- [Network console configuration](https://skupper.io/docs/console/configuration.html)
- [Network console](https://skupper.io/docs/console/index.html)
- [Skupper console repository](https://github.com/skupperproject/skupper-console)
- [Prometheus](https://prometheus.io/)

## Draft Notes

- Document what is exported by the observer versus what is queried directly by the console.
- Include persistence and retention notes because metrics history depends on configuration.
- Avoid naming individual Prometheus metrics until the generated API or console source confirms them.
