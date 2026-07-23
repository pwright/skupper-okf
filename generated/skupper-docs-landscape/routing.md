---
type: DocumentationLandscapePage
title: "Service Routing"
id: routing
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/routing
tags:
  - skupper
  - docs-landscape
  - discover
related:
  - sites
timestamp: 2026-07-23T19:44:12Z
---

# Service Routing

Service routing is how Skupper maps client connections at one site to matching workloads at another site. The main user-facing key is the routing key shared by listeners and connectors; the Skupper routers exchange reachability and forward traffic across links.

## Appears in

- [Discover Skupper](./discover-skupper.md) / Foundations

## Dependencies

- [Sites](./sites.md)

## Sources

- [Routing overview](../../human/skupper-docs/input/overview/routing.md): Local overview source for routing behavior.
- [Generated routing-key concept](../concepts/routing-key.md): Generated local note explaining routing-key semantics.
- [Listener concept](../concepts/listener.md): Generated local note for client-side service endpoint behavior.
- [Connector concept](../concepts/connector.md): Generated local note for backend workload attachment behavior.
- [Load balancing overview](../../human/skupper-docs/input/overview/load-balancing.md): Local source for routing-related load distribution behavior.

## Website Links

- [Routing overview](https://skupper.io/docs/overview/routing.html)
- [Load balancing overview](https://skupper.io/docs/overview/load-balancing.html)

## Draft Notes

- Make routing-key matching the central concept for new readers.
- Defer protocol and router-internal details to reference or architecture pages.
