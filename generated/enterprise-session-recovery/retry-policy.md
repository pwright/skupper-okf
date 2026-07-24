---
type: EnterpriseSessionRecoveryPage
title: "Bounded Retry (and backoff)"
id: retry-policy
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: maps/enterprise-session-recovery.bs
external: https://pwright.github.io/skupper-okf/generated/enterprise-session-recovery/retry-policy
tags:
  - skupper
  - enterprise-session-recovery
  - connection-management
related:
  - failure-detection
  - reconnect-and-retry
---

# Bounded Retry (and backoff)

This is client-side connection behavior. Skupper helps by providing service addresses and links, while the client detects failures and reconnects.

## Skupper Suitability

Skupper benefits from bounded retry policies because temporary link or endpoint failures can recover. Retries still need backoff, deadlines, and idempotency rules so recovery does not amplify load or duplicate work.

## Appears in

- Enterprise TCP Sessions and Recovery / Client Connection Management

## Dependency Check

The map dependency check resolved all declared dependencies for this topic: Failure Detection.

Dependencies:

- [Failure Detection](./failure-detection.md)

Used by:

- [Reconnect (and retry)](./reconnect-and-retry.md)

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
