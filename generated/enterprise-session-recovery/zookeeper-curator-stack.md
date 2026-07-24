---
type: EnterpriseSessionRecoveryPage
title: "ZooKeeper (Curator)"
id: zookeeper-curator-stack
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: maps/enterprise-session-recovery.bs
external: https://pwright.github.io/skupper-okf/generated/enterprise-session-recovery/zookeeper-curator-stack
tags:
  - skupper
  - enterprise-session-recovery
  - software-stacks
related:
  - bounded-session-resumption
  - logical-session-resume
---

# ZooKeeper (Curator)

This stack can use Skupper as private TCP reachability between client and service endpoints; recovery semantics remain owned by the client library, broker, or database.

## Skupper Suitability

Skupper can fit ZooKeeper Curator clients when the session timeout, retry policy, and ensemble endpoint exposure are designed carefully. It is not a substitute for ZooKeeper quorum connectivity or session semantics; Curator and ZooKeeper decide whether the logical session survives.

## Appears in

- Enterprise TCP Sessions and Recovery / Enterprise Software and Java Clients

## Dependency Check

The map dependency check resolved all declared dependencies for this topic: Session Resumption.

Dependencies:

- [Session Resumption](./logical-session-resume.md)

Used by:

- [Bounded Resumption](./bounded-session-resumption.md)

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
