---
type: DocumentationLandscapePage
title: "Link Metrics"
id: link-metrics
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/link-metrics
tags:
  - skupper
  - docs-landscape
  - observe
related:
  - metrics-export
timestamp: 2026-07-23T20:45:00Z
---

# Link Metrics

Link metrics capture observable behavior for connections between Skupper sites, helping operators verify connectivity and investigate degraded paths.

## Appears in

- [Observe Skupper](./observe-skupper.md) / Observability Signals

## Dependencies

- [Metrics Export](./metrics-export.md)

## Sources

- [generated/concepts/network-observer-api.md](../concepts/network-observer-api.md) - Generated source for router links and topology observations.
- [generated/skupper-console/console.md](../skupper-console/console.md) - Generated source for console link and topology queries.
- [human/skupper-docs/input/refdog/commands/link/status.md](../../human/skupper-docs/input/refdog/commands/link/status.md) - Local command reference for link status.
- [human/skupper-docs/input/refdog/resources/link.md](../../human/skupper-docs/input/refdog/resources/link.md) - Link resource reference.
- [human/skupper-docs/input/kube-cli/site-linking.md](../../human/skupper-docs/input/kube-cli/site-linking.md) - CLI source for creating and checking links.

## Website Links

- [Site linking with the Skupper CLI](https://skupper.io/docs/kube-cli/site-linking.html)
- [Link status command](https://skupperproject.github.io/refdog/commands/link/status.html)
- [Link resource reference](https://skupperproject.github.io/refdog/resources/link.html)
- [Network console](https://skupper.io/docs/console/index.html)

## Draft Notes

- Expand with examples for healthy, pending, and failed links once status fields are mapped.
- Keep link metrics separate from routing or latency tuning guidance.
- Include direct command checks as a fallback when observer metrics are unavailable.
