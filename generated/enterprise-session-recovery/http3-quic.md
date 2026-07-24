---
type: EnterpriseSessionRecoveryPage
title: "HTTP/3 (QUIC)"
id: http3-quic
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: maps/enterprise-session-recovery.bs
external: https://pwright.github.io/skupper-okf/generated/enterprise-session-recovery/http3-quic
tags:
  - skupper
  - enterprise-session-recovery
  - web-interactive
related:
  - independent-request
  - multiplexed-session
  - quic
  - tls
  - web-api-access
---

# HTTP/3 (QUIC)

This protocol family has mixed fit with Skupper: TCP-based HTTP and gRPC are natural candidates, while QUIC requires a non-Skupper UDP path or a protocol translation layer.

## Skupper Suitability

Skupper is a poor fit for native HTTP/3 because it depends on QUIC over UDP. For the same web application, Skupper is much more appropriate when the service can also be reached through HTTP/1.1 or HTTP/2.

## Appears in

- Enterprise Traffic Patterns / Web and Interactive

## Dependency Check

The map dependency check resolved all declared dependencies for this topic: Independent Exchange, Multiplexed Session, TLS, QUIC.

Dependencies:

- [Independent Exchange](./independent-request.md)
- [Multiplexed Session](./multiplexed-session.md)
- [TLS](./tls.md)
- [QUIC](./quic.md)

Used by:

- [Web (and APIs)](./web-api-access.md)

## Related Skupper Docs

- [Secure Skupper](../skupper-docs-landscape/secure-skupper.md)
- [Mutual authentication](../skupper-docs-landscape/mutual-authentication.md)
- [Trust boundaries](../skupper-docs-landscape/trust-boundaries.md)

## Draft Notes

- Validate the workload by breaking the TCP path and observing client-visible behavior, not just by checking that Skupper reconnects.
- Document whether the application requires same-socket continuity, logical session resume, durable progress, or ordinary retry.
