---
type: EnterpriseSessionRecoveryPage
title: "Oracle TAC (JDBC Replay + UCP)"
id: oracle-tac-stack
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: maps/enterprise-session-recovery.bs
external: https://pwright.github.io/skupper-okf/generated/enterprise-session-recovery/oracle-tac-stack
tags:
  - skupper
  - enterprise-session-recovery
  - software-stacks
related:
  - seamless-work-continuity
  - transparent-work-replay
---

# Oracle TAC (JDBC Replay + UCP)

This stack can use Skupper as private TCP reachability between client and service endpoints; recovery semantics remain owned by the client library, broker, or database.

## Skupper Suitability

Skupper can be a good transport fit for Oracle TAC because TAC is specifically designed to replay work after recoverable database outages. Skupper supplies private TCP reachability to database endpoints; TAC, FAN, service configuration, and transaction outcome handling supply continuity.

## Appears in

- Enterprise TCP Sessions and Recovery / Enterprise Software and Java Clients

## Dependency Check

The map dependency check resolved all declared dependencies for this topic: Transparent Replay (session and work).

Dependencies:

- [Transparent Replay (session and work)](./transparent-work-replay.md)

Used by:

- [Seamless Continuity](./seamless-work-continuity.md)

## Related Skupper Docs

- [Service exposure](../skupper-docs-landscape/service-exposure.md)
- [Service routing](../skupper-docs-landscape/service-routing.md)
- [Connector configuration](../skupper-docs-landscape/connector-config.md)
- [Client-listener-router-connector reconnects](../concepts/client-listener-router-connector-reconnects.md)
- [Restored connectivity](../skupper-docs-landscape/restored-connectivity.md)
- [Fault isolation](../skupper-docs-landscape/fault-isolation.md)

## Draft Notes

- Validate the workload by breaking the TCP path and observing client-visible behavior, not just by checking that Skupper reconnects.
- Document whether the application requires same-socket continuity, logical session resume, durable progress, or ordinary retry.
