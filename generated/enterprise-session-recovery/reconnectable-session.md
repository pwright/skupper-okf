---
type: EnterpriseSessionRecoveryPage
title: "Reconnectable Session"
id: reconnectable-session
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: maps/enterprise-session-recovery.bs
external: https://pwright.github.io/skupper-okf/generated/enterprise-session-recovery/reconnectable-session
tags:
  - skupper
  - enterprise-session-recovery
  - session-behaviour
related:
  - amqp-jms
  - mqtt
  - nfs
  - rdp
  - reconnect-retry
  - sip-rtp
  - smb
---

# Reconnectable Session

This behavior describes how much state survives connection loss. Skupper does not convert socket-bound state into resumable state.

## Skupper Suitability

Skupper is a good fit for reconnectable sessions over TCP when the protocol expects a new connection after interruption. Validate how much state is resumed, how much must be rebuilt, and whether users or callers see the interruption.

## Appears in

- Enterprise Traffic Patterns / Session Behaviour

## Dependency Check

The map dependency check resolved all declared dependencies for this topic: Reconnect (and Retry).

Dependencies:

- [Reconnect (and Retry)](./reconnect-retry.md)

Used by:

- [AMQP (and JMS)](./amqp-jms.md)
- [MQTT](./mqtt.md)
- [NFS](./nfs.md)
- [RDP](./rdp.md)
- [SIP (and RTP)](./sip-rtp.md)
- [SMB (Samba)](./smb.md)

## Related Skupper Docs

- [Client-listener-router-connector reconnects](../concepts/client-listener-router-connector-reconnects.md)
- [Restored connectivity](../skupper-docs-landscape/restored-connectivity.md)
- [Fault isolation](../skupper-docs-landscape/fault-isolation.md)
- [Recovery procedure](../skupper-docs-landscape/recovery-procedure.md)
- [Layered checks](../skupper-docs-landscape/layered-checks.md)
- [Health checks](../skupper-docs-landscape/health-checks.md)

## Draft Notes

- Validate the workload by breaking the TCP path and observing client-visible behavior, not just by checking that Skupper reconnects.
- Document whether the application requires same-socket continuity, logical session resume, durable progress, or ordinary retry.
