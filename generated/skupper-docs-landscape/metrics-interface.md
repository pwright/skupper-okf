---
type: DocumentationLandscapePage
title: "Metrics Interface"
id: metrics-interface
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/metrics-interface
tags:
  - skupper
  - docs-landscape
  - integrate
timestamp: 2026-07-23T21:45:00Z
---

# Metrics Interface

The metrics interface exposes Skupper observer metrics for Prometheus-compatible scraping and console time-series views.

## Appears in

- [Integrate Skupper](./integrate-skupper.md) / Operations Interfaces

## Sources

- [human/skupper-docs/input/console/configuration.md](../../human/skupper-docs/input/console/configuration.md) - Local source for the observer metrics endpoint, service, and scrape configuration.
- [generated/skupper-console/console.md](../skupper-console/console.md) - Generated source for console metrics queries.
- [generated/concepts/network-observer-api.md](../concepts/network-observer-api.md) - Generated source for observer monitoring use cases.
- [generated/skupper/skupper-api-network-observer.md](../skupper/skupper-api-network-observer.md) - Generated OpenAPI source for observer API resources.
- [generated/skupper-docs-landscape/metrics-export.md](./metrics-export.md) - Related landscape page for metrics export.

## Website Links

- [Network console configuration](https://skupper.io/docs/console/configuration.html)
- [Network console](https://skupper.io/docs/console/index.html)
- [Skupper console repository](https://github.com/skupperproject/skupper-console)
- [Prometheus](https://prometheus.io/)

## Draft Notes

- Include endpoint, service, path, and security notes from the console configuration source.
- Avoid listing individual metric names until they are mapped from current source.
- Distinguish metrics scraping from REST API resource queries.
