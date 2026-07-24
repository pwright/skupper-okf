---
type: EnterpriseSessionRecoveryPage
title: "Known Transaction Outcome"
id: transaction-outcome
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: maps/enterprise-session-recovery.bs
external: https://pwright.github.io/skupper-okf/generated/enterprise-session-recovery/transaction-outcome
tags:
  - skupper
  - enterprise-session-recovery
  - protocol-state
related:
  - idempotency-and-fencing
  - transparent-work-replay
---

# Known Transaction Outcome

This is protocol or application state. Skupper does not store it, but it can keep the required endpoints reachable after a path or site change.

## Skupper Suitability

Skupper does not determine transaction outcome. It can restore connectivity after a failure, but applications still need database, broker, or transaction-manager support to decide whether an interrupted operation committed, rolled back, or must be compensated.

## Appears in

- Enterprise TCP Sessions and Recovery / State Above TCP

## Dependency Check

The map dependency check resolved all declared dependencies for this topic: Idempotency (deduplication and fencing).

Dependencies:

- [Idempotency (deduplication and fencing)](./idempotency-and-fencing.md)

Used by:

- [Transparent Replay (session and work)](./transparent-work-replay.md)

## Related Skupper Docs

- [Recovery procedure](../skupper-docs-landscape/recovery-procedure.md)
- [Layered checks](../skupper-docs-landscape/layered-checks.md)
- [Health checks](../skupper-docs-landscape/health-checks.md)

## Draft Notes

- Validate the workload by breaking the TCP path and observing client-visible behavior, not just by checking that Skupper reconnects.
- Document whether the application requires same-socket continuity, logical session resume, durable progress, or ordinary retry.
