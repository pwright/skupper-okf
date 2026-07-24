---
type: EnterpriseSessionRecoveryPage
title: "Web (and APIs)"
id: web-api-access
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: maps/enterprise-session-recovery.bs
external: https://pwright.github.io/skupper-okf/generated/enterprise-session-recovery/web-api-access
tags:
  - skupper
  - enterprise-session-recovery
  - uses
related:
  - http1
  - http2-grpc
  - http3-quic
  - websocket
---

# Web (and APIs)

This is an enterprise traffic use case. Skupper fit depends on whether the workload can run over TCP and tolerate connection replacement.

## Skupper Suitability

Skupper is a strong fit for ordinary web and API access over HTTP/1.1 or HTTP/2, especially service-to-service traffic that needs private reachability without opening broad network paths. Exclude native HTTP/3/QUIC and be explicit about retry behavior for long-lived WebSocket or streaming calls.

## Appears in

- Enterprise Traffic Patterns / Enterprise Uses

## Dependency Check

The map dependency check resolved all declared dependencies for this topic: HTTP/1.1, HTTP/2 (and gRPC), HTTP/3 (QUIC), WebSocket.

Dependencies:

- [HTTP/1.1](./http1.md)
- [HTTP/2 (and gRPC)](./http2-grpc.md)
- [HTTP/3 (QUIC)](./http3-quic.md)
- [WebSocket](./websocket.md)

## Related Skupper Docs

- [Service exposure](../skupper-docs-landscape/service-exposure.md)
- [Service routing](../skupper-docs-landscape/service-routing.md)
- [Connector configuration](../skupper-docs-landscape/connector-config.md)
- [Secure Skupper](../skupper-docs-landscape/secure-skupper.md)
- [Mutual authentication](../skupper-docs-landscape/mutual-authentication.md)
- [Trust boundaries](../skupper-docs-landscape/trust-boundaries.md)
- [Skupper multi-site connectivity](../skupper-docs-landscape/multi-site-connectivity.md)

## Draft Notes

- Validate the workload by breaking the TCP path and observing client-visible behavior, not just by checking that Skupper reconnects.
- Document whether the application requires same-socket continuity, logical session resume, durable progress, or ordinary retry.
