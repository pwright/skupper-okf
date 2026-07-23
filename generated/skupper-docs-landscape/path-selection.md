---
type: DocumentationLandscapePage
title: "Path Selection Data"
id: path-selection
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/path-selection
tags:
  - skupper
  - docs-landscape
  - optimize
timestamp: 2026-07-23T21:00:00Z
---

# Path Selection Data

Path selection data is the evidence used to understand which links and routing choices are carrying traffic between clients and backends.

## Appears in

- [Optimize Skupper](./optimize-skupper.md) / Analysis Inputs

## Sources

- [human/skupper-docs/input/overview/load-balancing.md](../../human/skupper-docs/input/overview/load-balancing.md) - Local source for link cost and distribution behavior.
- [generated/concepts/network-deployment-concerns.md](../concepts/network-deployment-concerns.md) - Generated source for path cost and traffic direction notes.
- [generated/concepts/network-observer-api.md](../concepts/network-observer-api.md) - Generated source for connection and flow observations.
- [human/skupper-docs/input/refdog/resources/link.md](../../human/skupper-docs/input/refdog/resources/link.md) - Link resource reference.
- [human/skupper-docs/input/refdog/resources/multi-key-listener.md](../../human/skupper-docs/input/refdog/resources/multi-key-listener.md) - MultiKeyListener resource reference.

## Website Links

- [Load balancing and failover](https://skupper.io/docs/overview/load-balancing.html)
- [Link resource reference](https://skupperproject.github.io/refdog/resources/link.html)
- [MultiKeyListener resource reference](https://skupperproject.github.io/refdog/resources/multi-key-listener.html)
- [Network console](https://skupper.io/docs/console/index.html)

## Draft Notes

- Document intended path, observed path, link cost, and service distribution in one evidence record.
- Keep per-service path control separate from global link-cost control.
- Add examples for multi-hop paths after confirming the source-backed routing behavior.
