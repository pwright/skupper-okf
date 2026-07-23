---
type: DocumentationLandscapePage
title: "Service Metrics"
id: service-metrics
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/service-metrics
tags:
  - skupper
  - docs-landscape
  - observe
related:
  - metrics-export
timestamp: 2026-07-23T20:45:00Z
---

# Service Metrics

Service metrics make exposed Skupper service activity visible, including the listener, connector, and routing-key relationships that define reachability.

## Appears in

- [Observe Skupper](./observe-skupper.md) / Observability Signals

## Dependencies

- [Metrics Export](./metrics-export.md)

## Sources

- [generated/concepts/network-observer-api.md](../concepts/network-observer-api.md) - Generated source for services, listeners, connectors, and connection records.
- [generated/skupper-console/console.md](../skupper-console/console.md) - Generated source for console service and metrics queries.
- [generated/concepts/routing-key.md](../concepts/routing-key.md) - Generated source for routing keys in service and observer records.
- [human/skupper-docs/input/kube-cli/service-exposure.md](../../human/skupper-docs/input/kube-cli/service-exposure.md) - CLI service exposure workflow.
- [human/skupper-docs/input/refdog/topics/resource-status.md](../../human/skupper-docs/input/refdog/topics/resource-status.md) - Local resource status topic.

## Website Links

- [Service exposure with the Skupper CLI](https://skupper.io/docs/kube-cli/service-exposure.html)
- [Resource status topic](https://skupperproject.github.io/refdog/topics/resource-status.html)
- [Network console](https://skupper.io/docs/console/index.html)
- [Skupper console repository](https://github.com/skupperproject/skupper-console)

## Draft Notes

- Add a field map from listener and connector status to service-level health once source coverage is complete.
- Keep service metrics outcome-focused: reachable, matched, selected, active, or failing.
- Include examples that connect a traffic symptom back to a listener or connector definition.
