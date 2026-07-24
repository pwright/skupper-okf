---
type: EnterpriseSessionRecoveryPage
title: "Failure Detection"
id: failure-detection
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: maps/enterprise-session-recovery.bs
external: https://pwright.github.io/skupper-okf/generated/enterprise-session-recovery/failure-detection
tags:
  - skupper
  - enterprise-session-recovery
  - connection-management
related:
  - automatic-reconnect-failover
  - broker-database-endpoints
  - connection-pool
  - connection-replacement
  - retry-policy
  - session-expiry-window
  - tcp-connection
---

# Failure Detection

This is client-side connection behavior. Skupper helps by providing service addresses and links, while the client detects failures and reconnects.

## Skupper Suitability

Skupper contributes useful status, link, and flow signals for diagnosing connectivity, but application clients still need their own read, write, heartbeat, and request timeouts. Detection is shared between Skupper observability and application behavior.

## Appears in

- Enterprise TCP Sessions and Recovery / Client Connection Management

## Dependency Check

The map dependency check resolved all declared dependencies for this topic: TCP Connection, Broker (and database endpoints).

Dependencies:

- [TCP Connection](./tcp-connection.md)
- [Broker (and database endpoints)](./broker-database-endpoints.md)

Used by:

- [Automatic Reconnect (and failover)](./automatic-reconnect-failover.md)
- [Connection Pool](./connection-pool.md)
- [Connection Replacement](./connection-replacement.md)
- [Bounded Retry (and backoff)](./retry-policy.md)
- [Session Resume Window](./session-expiry-window.md)

## Related Skupper Docs

- [Recovery procedure](../skupper-docs-landscape/recovery-procedure.md)
- [Layered checks](../skupper-docs-landscape/layered-checks.md)
- [Health checks](../skupper-docs-landscape/health-checks.md)
- [Flow metrics](../skupper-docs-landscape/flow-metrics.md)
- [Traffic baseline](../skupper-docs-landscape/traffic-baseline.md)
- [Evidence bundle](../skupper-docs-landscape/evidence-bundle.md)
- [Client-listener-router-connector reconnects](../concepts/client-listener-router-connector-reconnects.md)

## Draft Notes

- Validate the workload by breaking the TCP path and observing client-visible behavior, not just by checking that Skupper reconnects.
- Document whether the application requires same-socket continuity, logical session resume, durable progress, or ordinary retry.
