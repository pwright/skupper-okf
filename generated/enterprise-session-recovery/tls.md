---
type: EnterpriseSessionRecoveryPage
title: "TLS"
id: tls
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: maps/enterprise-session-recovery.bs
external: https://pwright.github.io/skupper-okf/generated/enterprise-session-recovery/tls
tags:
  - skupper
  - enterprise-session-recovery
  - transport
related:
  - amqp-jms
  - direct-db
  - http1
  - http2-grpc
  - http3-quic
  - ipp
  - kafka
  - ldap
  - mail
  - mqtt
  - network-path
  - redis
  - syslog
  - websocket
---

# TLS

This is transport or path behavior. Skupper is relevant where the workload speaks TCP through a listener and connector.

## Skupper Suitability

Skupper works well with TLS-protected TCP services, either carrying application TLS end to end or using Skupper link security for the site-to-site path. Certificate ownership and trust boundaries still need to be explicit.

## Appears in

- Enterprise Traffic Patterns / Transport and Path

## Dependency Check

The map dependency check resolved all declared dependencies for this topic: Network Path.

Dependencies:

- [Network Path](./network-path.md)

Used by:

- [AMQP (and JMS)](./amqp-jms.md)
- [Direct DB (JDBC/native)](./direct-db.md)
- [HTTP/1.1](./http1.md)
- [HTTP/2 (and gRPC)](./http2-grpc.md)
- [HTTP/3 (QUIC)](./http3-quic.md)
- [IPP (Printing)](./ipp.md)
- [Kafka](./kafka.md)
- [LDAP](./ldap.md)
- [SMTP (and IMAP)](./mail.md)
- [MQTT](./mqtt.md)
- [Redis Protocol](./redis.md)
- [Syslog](./syslog.md)
- [WebSocket](./websocket.md)

## Related Skupper Docs

- [Secure Skupper](../skupper-docs-landscape/secure-skupper.md)
- [Mutual authentication](../skupper-docs-landscape/mutual-authentication.md)
- [Trust boundaries](../skupper-docs-landscape/trust-boundaries.md)
- [Skupper multi-site connectivity](../skupper-docs-landscape/multi-site-connectivity.md)
- [Private connectivity](../skupper-docs-landscape/private-connectivity.md)
- [Firewall and egress controls](../skupper-docs-landscape/network-controls.md)
- [Links](../skupper-docs-landscape/links.md)

## Draft Notes

- Validate the workload by breaking the TCP path and observing client-visible behavior, not just by checking that Skupper reconnects.
- Document whether the application requires same-socket continuity, logical session resume, durable progress, or ordinary retry.
