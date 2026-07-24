---
type: EnterpriseSessionRecoveryPage
title: "HTTP/1.1"
id: http1
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: maps/enterprise-session-recovery.bs
external: https://pwright.github.io/skupper-okf/generated/enterprise-session-recovery/http1
tags:
  - skupper
  - enterprise-session-recovery
  - web-interactive
related:
  - pooled-reuse
  - reconnect-retry
  - tcp
  - tls
  - web-api-access
---

# HTTP/1.1

This protocol family has mixed fit with Skupper: TCP-based HTTP and gRPC are natural candidates, while QUIC requires a non-Skupper UDP path or a protocol translation layer.

## Skupper Suitability

Skupper is a strong, common fit for HTTP/1.1 services that need private reachability across sites or clusters. HTTP request traffic tolerates connection replacement when clients use normal retry behavior, and Skupper can expose the service with listener and connector resources while preserving useful flow-level visibility for HTTP-oriented monitoring and troubleshooting.

## Appears in

- Enterprise Traffic Patterns / Web and Interactive

## Dependency Check

The map dependency check resolved all declared dependencies for this topic: Pooled Reuse, Reconnect (and Retry), TLS, TCP.

Dependencies:

- [Pooled Reuse](./pooled-reuse.md)
- [Reconnect (and Retry)](./reconnect-retry.md)
- [TLS](./tls.md)
- [TCP](./tcp.md)

Used by:

- [Web (and APIs)](./web-api-access.md)

## Related Skupper Docs

- [Service exposure](../skupper-docs-landscape/service-exposure.md)
- [Service routing](../skupper-docs-landscape/service-routing.md)
- [Connector configuration](../skupper-docs-landscape/connector-config.md)
- [Secure Skupper](../skupper-docs-landscape/secure-skupper.md)
- [Mutual authentication](../skupper-docs-landscape/mutual-authentication.md)
- [Trust boundaries](../skupper-docs-landscape/trust-boundaries.md)
- [Client-listener-router-connector reconnects](../concepts/client-listener-router-connector-reconnects.md)

## Draft Notes

- Validate the workload by breaking the TCP path and observing client-visible behavior, not just by checking that Skupper reconnects.
- Document whether the application requires same-socket continuity, logical session resume, durable progress, or ordinary retry.
