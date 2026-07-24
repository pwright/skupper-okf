---
type: EnterpriseSessionRecoveryPage
title: "TCP"
id: tcp
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: maps/enterprise-session-recovery.bs
external: https://pwright.github.io/skupper-okf/generated/enterprise-session-recovery/tcp
tags:
  - skupper
  - enterprise-session-recovery
  - transport
related:
  - amqp-jms
  - direct-db
  - dns
  - http1
  - http2-grpc
  - ipp
  - kafka
  - keepalive-timeouts
  - kerberos
  - ldap
  - mail
  - mqtt
  - multiplexed-session
  - network-path
  - nfs
  - pooled-reuse
  - rdp
  - redis
  - sip-rtp
  - smb
  - snmp
  - socket-bound
  - ssh-sftp
  - syslog
  - websocket
---

# TCP

This is transport or path behavior. Skupper is relevant where the workload speaks TCP through a listener and connector.

## Skupper Suitability

Skupper is fundamentally a TCP service-connectivity tool, so TCP workloads are the natural baseline fit. The suitability question is not whether TCP can pass, but whether the application tolerates connection replacement, latency, and endpoint abstraction.

## Appears in

- Enterprise Traffic Patterns / Transport and Path

## Dependency Check

The map dependency check resolved all declared dependencies for this topic: Network Path.

Dependencies:

- [Network Path](./network-path.md)

Used by:

- [AMQP (and JMS)](./amqp-jms.md)
- [Direct DB (JDBC/native)](./direct-db.md)
- [DNS](./dns.md)
- [HTTP/1.1](./http1.md)
- [HTTP/2 (and gRPC)](./http2-grpc.md)
- [IPP (Printing)](./ipp.md)
- [Kafka](./kafka.md)
- [Keepalive (and Timeouts)](./keepalive-timeouts.md)
- [Kerberos](./kerberos.md)
- [LDAP](./ldap.md)
- [SMTP (and IMAP)](./mail.md)
- [MQTT](./mqtt.md)
- [Multiplexed Session](./multiplexed-session.md)
- [NFS](./nfs.md)
- [Pooled Reuse](./pooled-reuse.md)
- [RDP](./rdp.md)
- [Redis Protocol](./redis.md)
- [SIP (and RTP)](./sip-rtp.md)
- [SMB (Samba)](./smb.md)
- [SNMP](./snmp.md)
- [Socket-Bound Session](./socket-bound.md)
- [SSH (and SFTP)](./ssh-sftp.md)
- [Syslog](./syslog.md)
- [WebSocket](./websocket.md)

## Related Skupper Docs

- [Skupper multi-site connectivity](../skupper-docs-landscape/multi-site-connectivity.md)
- [Private connectivity](../skupper-docs-landscape/private-connectivity.md)
- [Firewall and egress controls](../skupper-docs-landscape/network-controls.md)
- [Service exposure](../skupper-docs-landscape/service-exposure.md)
- [Service routing](../skupper-docs-landscape/service-routing.md)
- [Connector configuration](../skupper-docs-landscape/connector-config.md)
- [Links](../skupper-docs-landscape/links.md)

## Draft Notes

- Validate the workload by breaking the TCP path and observing client-visible behavior, not just by checking that Skupper reconnects.
- Document whether the application requires same-socket continuity, logical session resume, durable progress, or ordinary retry.
