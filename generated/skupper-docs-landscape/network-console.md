---
type: DocumentationLandscapePage
title: "Network Console"
id: network-console
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/network-console
tags:
  - skupper
  - docs-landscape
  - observe
related:
  - metrics-export
  - event-collection
timestamp: 2026-07-23T20:45:00Z
---

# Network Console

The network console is the Skupper UI for observing topology, services, connections, traffic flows, and related network state.

## Appears in

- [Observe Skupper](./observe-skupper.md) / Collection and Presentation

## Dependencies

- [Metrics Export](./metrics-export.md)
- [Event Collection](./event-collection.md)

## Sources

- [human/skupper-docs/input/console/index.md](../../human/skupper-docs/input/console/index.md) - Local source for installing and using the network console.
- [human/skupper-docs/input/console/configuration.md](../../human/skupper-docs/input/console/configuration.md) - Local source for console and observer configuration.
- [generated/skupper-console/console.md](../skupper-console/console.md) - Generated source describing console API calls, resources, and metrics queries.
- [generated/concepts/network-observer-api.md](../concepts/network-observer-api.md) - Generated source for observer API scope and example usage.
- [sources/skupper-console.md](../../sources/skupper-console.md) - Local source inventory for the console repository.

## Website Links

- [Network console](https://skupper.io/docs/console/index.html)
- [Network console configuration](https://skupper.io/docs/console/configuration.html)
- [Skupper console repository](https://github.com/skupperproject/skupper-console)
- [Skupper project](https://skupper.io/)

## Draft Notes

- Build this page around deployment, access, data sources, and common operator tasks.
- Keep generated API details in source links rather than duplicating every endpoint.
- Include placement guidance because the console location can affect visibility and access across firewalls.
