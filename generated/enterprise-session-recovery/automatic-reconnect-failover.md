---
type: EnterpriseSessionRecoveryPage
title: "Automatic Reconnect (and failover)"
id: automatic-reconnect-failover
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: maps/enterprise-session-recovery.bs
external: https://pwright.github.io/skupper-okf/generated/enterprise-session-recovery/automatic-reconnect-failover
tags:
  - skupper
  - enterprise-session-recovery
  - connection-management
related:
  - durable-position-recovery
  - endpoint-discovery
  - failure-detection
  - logical-session-resume
  - reconnect-and-retry
  - topology-reconstruction
  - transparent-work-replay
---

# Automatic Reconnect (and failover)

This is client-side connection behavior. Skupper helps by providing service addresses and links, while the client detects failures and reconnects.

## Skupper Suitability

Skupper supports automatic recovery of its network links, and that pairs well with client libraries that automatically reconnect. It does not reconnect the application socket on behalf of the client library.

## Appears in

- Enterprise TCP Sessions and Recovery / Client Connection Management

## Dependency Check

The map dependency check resolved all declared dependencies for this topic: Failure Detection, Endpoint Discovery.

Dependencies:

- [Failure Detection](./failure-detection.md)
- [Endpoint Discovery](./endpoint-discovery.md)

Used by:

- [Durable-Position Recovery](./durable-position-recovery.md)
- [Session Resumption](./logical-session-resume.md)
- [Reconnect (and retry)](./reconnect-and-retry.md)
- [Topology Reconstruction (and subscriptions)](./topology-reconstruction.md)
- [Transparent Replay (session and work)](./transparent-work-replay.md)

## Related Skupper Docs

- [Client-listener-router-connector reconnects](../concepts/client-listener-router-connector-reconnects.md)
- [Restored connectivity](../skupper-docs-landscape/restored-connectivity.md)
- [Fault isolation](../skupper-docs-landscape/fault-isolation.md)
- [Recovery procedure](../skupper-docs-landscape/recovery-procedure.md)
- [Layered checks](../skupper-docs-landscape/layered-checks.md)
- [Health checks](../skupper-docs-landscape/health-checks.md)
- [Flow metrics](../skupper-docs-landscape/flow-metrics.md)

## Draft Notes

- Validate the workload by breaking the TCP path and observing client-visible behavior, not just by checking that Skupper reconnects.
- Document whether the application requires same-socket continuity, logical session resume, durable progress, or ordinary retry.
