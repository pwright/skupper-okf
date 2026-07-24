---
type: EnterpriseSessionRecoveryPage
title: "Reconnect (and Retry)"
id: reconnect-retry
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: maps/enterprise-session-recovery.bs
external: https://pwright.github.io/skupper-okf/generated/enterprise-session-recovery/reconnect-retry
tags:
  - skupper
  - enterprise-session-recovery
  - session-behaviour
related:
  - durable-position
  - http1
  - http2-grpc
  - kafka
  - ldap
  - mail
  - middleboxes
  - network-path
  - reconnectable-session
  - redis
---

# Reconnect (and Retry)

This behavior describes how much state survives connection loss. Skupper does not convert socket-bound state into resumable state.

## Skupper Suitability

Skupper fits reconnect-and-retry patterns when the client can reopen the connection to a stable service address and apply bounded retry policy. It improves reachability, but retry safety and duplicate-effect handling remain application concerns.

## Appears in

- Enterprise Traffic Patterns / Session Behaviour

## Dependency Check

The map dependency check resolved all declared dependencies for this topic: Network Path, Middleboxes (NAT, firewall, LB).

Dependencies:

- [Network Path](./network-path.md)
- [Middleboxes (NAT, firewall, LB)](./middleboxes.md)

Used by:

- [Durable Position](./durable-position.md)
- [HTTP/1.1](./http1.md)
- [HTTP/2 (and gRPC)](./http2-grpc.md)
- [Kafka](./kafka.md)
- [LDAP](./ldap.md)
- [SMTP (and IMAP)](./mail.md)
- [Reconnectable Session](./reconnectable-session.md)
- [Redis Protocol](./redis.md)

## Related Skupper Docs

- [Client-listener-router-connector reconnects](../concepts/client-listener-router-connector-reconnects.md)
- [Restored connectivity](../skupper-docs-landscape/restored-connectivity.md)
- [Fault isolation](../skupper-docs-landscape/fault-isolation.md)
- [Recovery procedure](../skupper-docs-landscape/recovery-procedure.md)
- [Layered checks](../skupper-docs-landscape/layered-checks.md)
- [Health checks](../skupper-docs-landscape/health-checks.md)
- [Skupper multi-site connectivity](../skupper-docs-landscape/multi-site-connectivity.md)

## Draft Notes

- Validate the workload by breaking the TCP path and observing client-visible behavior, not just by checking that Skupper reconnects.
- Document whether the application requires same-socket continuity, logical session resume, durable progress, or ordinary retry.
