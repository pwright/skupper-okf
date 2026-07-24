---
type: EnterpriseSessionRecoveryPage
title: "Session Identity"
id: session-identity
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: maps/enterprise-session-recovery.bs
external: https://pwright.github.io/skupper-okf/generated/enterprise-session-recovery/session-identity
tags:
  - skupper
  - enterprise-session-recovery
  - protocol-state
related:
  - broker-database-endpoints
  - logical-session-resume
  - tracked-session-state
---

# Session Identity

This is protocol or application state. Skupper does not store it, but it can keep the required endpoints reachable after a path or site change.

## Skupper Suitability

Skupper does not create protocol session identity. It can carry the new TCP connection used to present a client ID, token, consumer group, or database session attributes, but identity continuity must be defined by the application protocol.

## Appears in

- Enterprise TCP Sessions and Recovery / State Above TCP

## Dependency Check

The map dependency check resolved all declared dependencies for this topic: Broker (and database endpoints).

Dependencies:

- [Broker (and database endpoints)](./broker-database-endpoints.md)

Used by:

- [Session Resumption](./logical-session-resume.md)
- [Tracked Session State](./tracked-session-state.md)

## Related Skupper Docs

- [Service exposure](../skupper-docs-landscape/service-exposure.md)
- [Service routing](../skupper-docs-landscape/service-routing.md)
- [Connector configuration](../skupper-docs-landscape/connector-config.md)
- [Secure Skupper](../skupper-docs-landscape/secure-skupper.md)
- [Mutual authentication](../skupper-docs-landscape/mutual-authentication.md)
- [Trust boundaries](../skupper-docs-landscape/trust-boundaries.md)
- [Listener concept](../concepts/listener.md)

## Draft Notes

- Validate the workload by breaking the TCP path and observing client-visible behavior, not just by checking that Skupper reconnects.
- Document whether the application requires same-socket continuity, logical session resume, durable progress, or ordinary retry.
