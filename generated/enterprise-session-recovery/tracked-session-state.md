---
type: EnterpriseSessionRecoveryPage
title: "Tracked Session State"
id: tracked-session-state
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: maps/enterprise-session-recovery.bs
external: https://pwright.github.io/skupper-okf/generated/enterprise-session-recovery/tracked-session-state
tags:
  - skupper
  - enterprise-session-recovery
  - protocol-state
related:
  - session-identity
  - transparent-work-replay
---

# Tracked Session State

This is protocol or application state. Skupper does not store it, but it can keep the required endpoints reachable after a path or site change.

## Skupper Suitability

Skupper does not track application session state. It is suitable only when the server, broker, database, or client library records enough state for a replacement TCP connection to continue safely.

## Appears in

- Enterprise TCP Sessions and Recovery / State Above TCP

## Dependency Check

The map dependency check resolved all declared dependencies for this topic: Session Identity.

Dependencies:

- [Session Identity](./session-identity.md)

Used by:

- [Transparent Replay (session and work)](./transparent-work-replay.md)

## Related Skupper Docs

- [Service exposure](../skupper-docs-landscape/service-exposure.md)
- [Service routing](../skupper-docs-landscape/service-routing.md)
- [Connector configuration](../skupper-docs-landscape/connector-config.md)
- [Secure Skupper](../skupper-docs-landscape/secure-skupper.md)
- [Mutual authentication](../skupper-docs-landscape/mutual-authentication.md)
- [Trust boundaries](../skupper-docs-landscape/trust-boundaries.md)

## Draft Notes

- Validate the workload by breaking the TCP path and observing client-visible behavior, not just by checking that Skupper reconnects.
- Document whether the application requires same-socket continuity, logical session resume, durable progress, or ordinary retry.
