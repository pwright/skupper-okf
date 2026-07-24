---
type: EnterpriseSessionRecoveryPage
title: "Pooled Reuse"
id: pooled-reuse
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: maps/enterprise-session-recovery.bs
external: https://pwright.github.io/skupper-okf/generated/enterprise-session-recovery/pooled-reuse
tags:
  - skupper
  - enterprise-session-recovery
  - session-behaviour
related:
  - direct-db
  - http1
  - ipp
  - keepalive-timeouts
  - ldap
  - mail
  - tcp
---

# Pooled Reuse

This behavior describes how much state survives connection loss. Skupper does not convert socket-bound state into resumable state.

## Skupper Suitability

Skupper is a good fit for pooled HTTP or service-client connections. Pools already expect to discard and recreate TCP connections, so Skupper connection replacement aligns with normal client behavior.

## Appears in

- Enterprise Traffic Patterns / Session Behaviour

## Dependency Check

The map dependency check resolved all declared dependencies for this topic: TCP, Keepalive (and Timeouts).

Dependencies:

- [TCP](./tcp.md)
- [Keepalive (and Timeouts)](./keepalive-timeouts.md)

Used by:

- [Direct DB (JDBC/native)](./direct-db.md)
- [HTTP/1.1](./http1.md)
- [IPP (Printing)](./ipp.md)
- [LDAP](./ldap.md)
- [SMTP (and IMAP)](./mail.md)

## Related Skupper Docs

- [Skupper multi-site connectivity](../skupper-docs-landscape/multi-site-connectivity.md)
- [Private connectivity](../skupper-docs-landscape/private-connectivity.md)
- [Firewall and egress controls](../skupper-docs-landscape/network-controls.md)
- [Service exposure](../skupper-docs-landscape/service-exposure.md)
- [Service routing](../skupper-docs-landscape/service-routing.md)
- [Connector configuration](../skupper-docs-landscape/connector-config.md)
- [Recovery procedure](../skupper-docs-landscape/recovery-procedure.md)

## Draft Notes

- Validate the workload by breaking the TCP path and observing client-visible behavior, not just by checking that Skupper reconnects.
- Document whether the application requires same-socket continuity, logical session resume, durable progress, or ordinary retry.
