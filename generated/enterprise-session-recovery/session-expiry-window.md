---
type: EnterpriseSessionRecoveryPage
title: "Session Resume Window"
id: session-expiry-window
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: maps/enterprise-session-recovery.bs
external: https://pwright.github.io/skupper-okf/generated/enterprise-session-recovery/session-expiry-window
tags:
  - skupper
  - enterprise-session-recovery
  - protocol-state
related:
  - failure-detection
  - logical-session-resume
---

# Session Resume Window

This is protocol or application state. Skupper does not store it, but it can keep the required endpoints reachable after a path or site change.

## Skupper Suitability

Skupper can be part of a design with a session expiry window, but it does not extend that window. The expiry value must be long enough for failure detection, reconnect, authentication, and protocol resume over the Skupper path.

## Appears in

- Enterprise TCP Sessions and Recovery / State Above TCP

## Dependency Check

The map dependency check resolved all declared dependencies for this topic: Failure Detection.

Dependencies:

- [Failure Detection](./failure-detection.md)

Used by:

- [Session Resumption](./logical-session-resume.md)

## Related Skupper Docs

- [Recovery procedure](../skupper-docs-landscape/recovery-procedure.md)
- [Layered checks](../skupper-docs-landscape/layered-checks.md)
- [Health checks](../skupper-docs-landscape/health-checks.md)
- [Client-listener-router-connector reconnects](../concepts/client-listener-router-connector-reconnects.md)
- [Restored connectivity](../skupper-docs-landscape/restored-connectivity.md)
- [Fault isolation](../skupper-docs-landscape/fault-isolation.md)
- [Flow metrics](../skupper-docs-landscape/flow-metrics.md)

## Draft Notes

- Validate the workload by breaking the TCP path and observing client-visible behavior, not just by checking that Skupper reconnects.
- Document whether the application requires same-socket continuity, logical session resume, durable progress, or ordinary retry.
