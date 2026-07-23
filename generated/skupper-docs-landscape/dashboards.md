---
type: DocumentationLandscapePage
title: "Dashboards and Alerts"
id: dashboards
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/dashboards
tags:
  - skupper
  - docs-landscape
  - observe
related:
  - metrics-export
  - log-collection
timestamp: 2026-07-23T20:45:00Z
---

# Dashboards and Alerts

Dashboards and alerts turn collected Skupper metrics, logs, and observer data into repeatable views and notifications for operators.

## Appears in

- [Observe Skupper](./observe-skupper.md) / Collection and Presentation

## Dependencies

- [Metrics Export](./metrics-export.md)
- [Log Collection](./log-collection.md)

## Sources

- [human/skupper-docs/input/console/configuration.md](../../human/skupper-docs/input/console/configuration.md) - Local source for Prometheus configuration, persistence, and additional volumes.
- [generated/skupper-console/console.md](../skupper-console/console.md) - Generated source for console metrics queries and traffic views.
- [generated/concepts/network-observer-api.md](../concepts/network-observer-api.md) - Generated source for monitoring and console use cases.
- [human/skupper-docs/input/troubleshooting/index.md](../../human/skupper-docs/input/troubleshooting/index.md) - Local troubleshooting source for symptoms and diagnostics.
- [sources/skupper-console.md](../../sources/skupper-console.md) - Local source inventory for console-related material.

## Website Links

- [Network console configuration](https://skupper.io/docs/console/configuration.html)
- [Network console](https://skupper.io/docs/console/index.html)
- [Skupper console repository](https://github.com/skupperproject/skupper-console)
- [Prometheus](https://prometheus.io/)

## Draft Notes

- Keep alert recommendations generic until source-backed metric names and thresholds are available.
- Add starter dashboards for sites, links, services, and flows once metrics fields are mapped.
- Include a note that dashboards should distinguish missing telemetry from unhealthy Skupper resources.
