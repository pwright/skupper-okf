---
type: DocumentationLandscapePage
title: "Traffic Baseline"
id: traffic-baseline
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/traffic-baseline
tags:
  - skupper
  - docs-landscape
  - optimize
timestamp: 2026-07-23T21:00:00Z
---

# Traffic Baseline

A traffic baseline records normal service volume, connection patterns, flow behavior, and error symptoms before optimization changes are made.

## Appears in

- [Optimize Skupper](./optimize-skupper.md) / Analysis Inputs

## Sources

- [generated/concepts/network-observer-api.md](../concepts/network-observer-api.md) - Generated source for connection, service, and flow data.
- [generated/skupper-console/console.md](../skupper-console/console.md) - Generated source for console time-series and flow queries.
- [human/skupper-docs/input/console/configuration.md](../../human/skupper-docs/input/console/configuration.md) - Local source for metrics, flow retention, and Prometheus configuration.
- [human/skupper-docs/input/troubleshooting/index.md](../../human/skupper-docs/input/troubleshooting/index.md) - Local source for capturing symptoms and diagnostic data.
- [generated/skupper-docs-landscape/flow-metrics.md](./flow-metrics.md) - Related landscape page for flow metrics.

## Website Links

- [Network console](https://skupper.io/docs/console/index.html)
- [Network console configuration](https://skupper.io/docs/console/configuration.html)
- [Troubleshooting](https://skupper.io/docs/troubleshooting/index.html)
- [Skupper console repository](https://github.com/skupperproject/skupper-console)

## Draft Notes

- Baselines should include time window, workload mix, topology, and active Skupper configuration.
- Keep baseline evidence repeatable so post-change results are comparable.
- Note observer retention settings when using historical traffic data.
