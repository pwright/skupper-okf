---
type: EnterpriseSessionRecoveryPage
title: "HTTP/2 (and gRPC)"
id: http2-grpc
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: maps/enterprise-session-recovery.bs
external: https://pwright.github.io/skupper-okf/generated/enterprise-session-recovery/http2-grpc
tags:
  - skupper
  - enterprise-session-recovery
  - web-interactive
related:
  - multiplexed-session
  - reconnect-retry
  - tcp
  - tls
  - web-api-access
---

# HTTP/2 (and gRPC)

This protocol family has mixed fit with Skupper: TCP-based HTTP and gRPC are natural candidates, while QUIC requires a non-Skupper UDP path or a protocol translation layer.

## Skupper Suitability

Skupper is a strong fit for HTTP/2 and gRPC services when the application can tolerate stream or connection interruption through normal client retry, deadlines, and idempotency rules. It is useful for private service reachability and can be paired with Skupper flow visibility to observe service traffic, but it does not make an interrupted gRPC stream magically resume.

## Appears in

- Enterprise Traffic Patterns / Web and Interactive

## Dependency Check

The map dependency check resolved all declared dependencies for this topic: Multiplexed Session, Reconnect (and Retry), TLS, TCP.

Dependencies:

- [Multiplexed Session](./multiplexed-session.md)
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
