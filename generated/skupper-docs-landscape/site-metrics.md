---
type: DocumentationLandscapePage
title: "Site Metrics"
id: site-metrics
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/site-metrics
tags:
  - skupper
  - docs-landscape
  - observe
related:
  - metrics-export
timestamp: 2026-07-23T20:45:00Z
---

# Site Metrics

Site metrics describe observable state for Skupper sites, including information used by consoles and monitoring systems to reason about site health and topology.

## Appears in

- [Observe Skupper](./observe-skupper.md) / Observability Signals

## Dependencies

- [Metrics Export](./metrics-export.md)

## Sources

- [generated/concepts/network-observer-api.md](../concepts/network-observer-api.md) - Generated source for observer site and topology data.
- [generated/skupper-console/console.md](../skupper-console/console.md) - Generated source for console API and metrics usage.
- [human/skupper-docs/input/console/index.md](../../human/skupper-docs/input/console/index.md) - Local console source for network observation.
- [human/skupper-docs/input/refdog/commands/site/status.md](../../human/skupper-docs/input/refdog/commands/site/status.md) - Local command reference for site status.
- [human/skupper-docs/input/refdog/resources/site.md](../../human/skupper-docs/input/refdog/resources/site.md) - Site resource reference.

## Website Links

- [Network console](https://skupper.io/docs/console/index.html)
- [Site status command](https://skupperproject.github.io/refdog/commands/site/status.html)
- [Site resource reference](https://skupperproject.github.io/refdog/resources/site.html)
- [Skupper console repository](https://github.com/skupperproject/skupper-console)

## Draft Notes

- Distinguish metrics from status commands: metrics are collected over time, while status output is an immediate operational check.
- Add a future table of site-level fields after confirming exact observer API names.
- Include failure cases such as missing observer data separately from actual site failure.
