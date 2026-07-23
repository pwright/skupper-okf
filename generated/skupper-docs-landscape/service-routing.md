---
type: DocumentationLandscapePage
title: "Service Routing Configuration"
id: service-routing
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/service-routing
tags:
  - skupper
  - docs-landscape
  - configure
related:
  - service-address
  - routing-mode
timestamp: 2026-07-23T20:17:03Z
---

# Service Routing Configuration

Service routing configuration controls how listener endpoints map to backend connectors, primarily through routing keys and, for some use cases, multi-key listener strategies or link cost.

## Appears in

- [Configure Skupper](./configure-skupper.md) / Configuration Resources

## Dependencies

- [Service Address](./service-address.md)
- [Routing Mode](./routing-mode.md)

## Sources

- [generated/concepts/routing-key.md](../concepts/routing-key.md) - Routing key concept and matching behavior for listeners and connectors.
- [generated/concepts/listener.md](../concepts/listener.md) - Listener behavior and multi-key listener notes.
- [generated/concepts/connector.md](../concepts/connector.md) - Connector behavior and matching status signals.
- [human/skupper-docs/input/overview/load-balancing.md](../../human/skupper-docs/input/overview/load-balancing.md) - Preferred use of multi-key listeners for per-service load balancing and failover.
- [human/skupper-docs/input/refdog/resources/multi-key-listener.md](../../human/skupper-docs/input/refdog/resources/multi-key-listener.md) - MultiKeyListener resource reference.

## Website Links

- [Load balancing overview](https://skupper.io/docs/overview/load-balancing.html)
- [Multi-key listener resource reference](https://skupperproject.github.io/refdog/resources/multi-key-listener.html)
- [Routing key concept](https://skupperproject.github.io/refdog/concepts/routing-key.html)
- [Service exposure with YAML](https://skupper.io/docs/kube-yaml/service-exposure.html)

## Draft Notes

- Expand routing examples around three cases: one listener to one connector, one listener to many connectors, and one endpoint to multiple routing keys.
- Be explicit that link cost is network-level and affects traffic over a link, while multi-key listener configuration is the better source-backed path for per-service control.
- Add verification guidance based on listener and connector matching status fields.
