---
type: DocumentationLandscapePage
title: "Routing Policy"
id: routing-policy
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/routing-policy
tags:
  - skupper
  - docs-landscape
  - extend
related:
  - service-definition
timestamp: 2026-07-23T20:01:23Z
---

# Routing Policy

Routing Policy defines how Skupper should match and distribute service traffic after a service is onboarded. Local sources support routing-key matching, many-to-many listener/connector relationships, multi-key listeners, and link cost as an application-network-wide influence.

## Appears in

- [Extend a Skupper Application Network](./extend-skupper.md) / Expansion Controls

## Dependencies

- [Service Definition](./service-definition.md)

## Sources

- [Routing key concept](../concepts/routing-key.md): Primary generated local source for routing keys, listener/connector matching, and multi-key listener behavior.
- [Skupper load balancing and failover](../../human/skupper-docs/input/overview/load-balancing.md): Local source for multi-key listener strategies and link cost behavior.
- [Network deployment concerns](../concepts/network-deployment-concerns.md): Generated local source for traffic direction decisions.
- [Multi-key listener resource](../../human/skupper-docs/input/refdog/resources/multi-key-listener.md): Local resource reference candidate for multi-key listener definitions.
- [Link concept](../../human/skupper-docs/input/refdog/concepts/link.md): Local concept source for links and network-wide connectivity.

## Website Links

- [Skupper load balancing and failover](https://skupper.io/docs/overview/load-balancing.html)
- [Refdog routing key concept](https://skupperproject.github.io/refdog/concepts/routing-key.html)
- [Refdog MultiKeyListener resource](https://skupperproject.github.io/refdog/resources/multi-key-listener.html)

## Draft Notes

- Prefer routing keys and multi-key listeners for per-service policy; link cost affects all services on a link.
- Record whether the policy is simple matching, weighted distribution, or failover order.
- Validate policy with listener/connector status and, where available, observer service binding data.
