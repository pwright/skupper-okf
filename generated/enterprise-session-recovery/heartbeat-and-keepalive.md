---
type: EnterpriseSessionRecoveryPage
title: "Heartbeats (and TCP keepalive)"
id: heartbeat-and-keepalive
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: maps/enterprise-session-recovery.bs
external: https://pwright.github.io/skupper-okf/generated/enterprise-session-recovery/heartbeat-and-keepalive
tags:
  - skupper
  - enterprise-session-recovery
  - connection-management
related:
  - load-balancer-proxy-timeout
  - nat-firewall-state
  - same-tcp-continuity
  - tcp-connection
---

# Heartbeats (and TCP keepalive)

This is client-side connection behavior. Skupper helps by providing service addresses and links, while the client detects failures and reconnects.

## Skupper Suitability

Skupper can carry heartbeat traffic for TCP protocols and can help reveal broken paths, but keepalives should be tuned with router, firewall, proxy, and client timeout behavior in mind. Keepalives do not turn a broken socket into a resumed session.

## Appears in

- Enterprise TCP Sessions and Recovery / Client Connection Management

## Dependency Check

The map dependency check resolved all declared dependencies for this topic: TCP Connection, NAT (and firewall state), Idle Timeout (load balancer or proxy).

Dependencies:

- [TCP Connection](./tcp-connection.md)
- [NAT (and firewall state)](./nat-firewall-state.md)
- [Idle Timeout (load balancer or proxy)](./load-balancer-proxy-timeout.md)

Used by:

- [Same TCP Connection](./same-tcp-continuity.md)

## Related Skupper Docs

- [Skupper multi-site connectivity](../skupper-docs-landscape/multi-site-connectivity.md)
- [Private connectivity](../skupper-docs-landscape/private-connectivity.md)
- [Firewall and egress controls](../skupper-docs-landscape/network-controls.md)
- [Recovery procedure](../skupper-docs-landscape/recovery-procedure.md)
- [Layered checks](../skupper-docs-landscape/layered-checks.md)
- [Health checks](../skupper-docs-landscape/health-checks.md)
- [Service exposure](../skupper-docs-landscape/service-exposure.md)

## Draft Notes

- Validate the workload by breaking the TCP path and observing client-visible behavior, not just by checking that Skupper reconnects.
- Document whether the application requires same-socket continuity, logical session resume, durable progress, or ordinary retry.
