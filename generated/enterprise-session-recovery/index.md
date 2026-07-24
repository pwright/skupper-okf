---
title: "Enterprise Session Recovery"
id: enterprise-session-recovery-index
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: maps/enterprise-session-recovery.bs
external: https://pwright.github.io/skupper-okf/generated/enterprise-session-recovery
tags:
  - skupper
  - enterprise-session-recovery
---

# Enterprise Session Recovery

Generated topic pages from `maps/enterprise-session-recovery.bs`, with dependency checks and Skupper suitability notes.

## Map

- [Blockscape map wrapper](../maps/enterprise-session-recovery.md)

## Dependency Check

- All 183 dependency references resolve to generated topic pages.

## Topics

### Enterprise TCP Sessions and Recovery

A value-chain map distinguishing continuity of one TCP connection from recovery above TCP. Green items preserve or reconstruct substantial logical state; amber items reconnect and rebuild selected state; red items replace the connection and require explicit application recovery.

**Application Outcomes**

- [Seamless Continuity](./seamless-work-continuity.md)
- [Bounded Resumption](./bounded-session-resumption.md)
- [Durable Progress](./durable-processing-progress.md)
- [Recoverable Topology](./recoverable-messaging-topology.md)
- [Application Recovery](./explicit-application-recovery.md)

**Enterprise Software and Java Clients**

- [Oracle TAC (JDBC Replay + UCP)](./oracle-tac-stack.md)
- [IBM MQ (JMS)](./ibm-mq-jms-stack.md)
- [ZooKeeper (Curator)](./zookeeper-curator-stack.md)
- [Kafka (Java Client or Spring)](./kafka-java-stack.md)
- [MQTT (Paho Java)](./mqtt-paho-stack.md)
- [AMQP (RabbitMQ or Qpid JMS)](./rabbitmq-qpid-stack.md)
- [JDBC (PostgreSQL or MySQL + HikariCP)](./ordinary-jdbc-stack.md)

**Recovery Semantics**

- [Transparent Replay (session and work)](./transparent-work-replay.md)
- [Session Resumption](./logical-session-resume.md)
- [Durable-Position Recovery](./durable-position-recovery.md)
- [Topology Reconstruction (and subscriptions)](./topology-reconstruction.md)
- [Reconnect (and retry)](./reconnect-and-retry.md)
- [Connection Replacement](./connection-replacement.md)
- [Same TCP Connection](./same-tcp-continuity.md)

**State Above TCP**

- [Tracked Session State](./tracked-session-state.md)
- [Known Transaction Outcome](./transaction-outcome.md)
- [Session Identity](./session-identity.md)
- [Session Resume Window](./session-expiry-window.md)
- [Durable Checkpoint (offset or cursor)](./durable-checkpoint.md)
- [Durable Delivery State (and topology)](./durable-delivery-topology.md)
- [Idempotency (deduplication and fencing)](./idempotency-and-fencing.md)

**Client Connection Management**

- [Automatic Reconnect (and failover)](./automatic-reconnect-failover.md)
- [Failure Detection](./failure-detection.md)
- [Bounded Retry (and backoff)](./retry-policy.md)
- [Connection Pool](./connection-pool.md)
- [Heartbeats (and TCP keepalive)](./heartbeat-and-keepalive.md)
- [Endpoint Discovery](./endpoint-discovery.md)

**TCP and Network Path**

- [TCP Connection](./tcp-connection.md)
- [Network Path](./network-path.md)
- [NAT (and firewall state)](./nat-firewall-state.md)
- [Idle Timeout (load balancer or proxy)](./load-balancer-proxy-timeout.md)
- [Broker (and database endpoints)](./broker-database-endpoints.md)

### Enterprise Traffic Patterns

A companion map for common office and enterprise traffic. It distinguishes independent exchanges, pooled connections, multiplexed streams, socket-bound sessions, reconnectable sessions, and durable recovery. Colours indicate the dominant behaviour: blue for request or pooled traffic, purple for multiplexing, red for socket-bound sessions, amber for resumable sessions, and green for durable progress.

**Enterprise Uses**

- [Web (and APIs)](./web-api-access.md)
- [Remote Access](./remote-access.md)
- [Database Access](./database-access.md)
- [Events (and Messaging)](./events-messaging.md)
- [File Sharing](./file-sharing.md)
- [Identity (and Naming)](./identity-naming.md)
- [Office Operations](./office-operations.md)

**Web and Interactive**

- [HTTP/1.1](./http1.md)
- [HTTP/2 (and gRPC)](./http2-grpc.md)
- [HTTP/3 (QUIC)](./http3-quic.md)
- [WebSocket](./websocket.md)
- [SSH (and SFTP)](./ssh-sftp.md)
- [RDP](./rdp.md)

**Data and Messaging**

- [Direct DB (JDBC/native)](./direct-db.md)
- [Kafka](./kafka.md)
- [AMQP (and JMS)](./amqp-jms.md)
- [MQTT](./mqtt.md)
- [Redis Protocol](./redis.md)

**File and Identity**

- [SMB (Samba)](./smb.md)
- [NFS](./nfs.md)
- [LDAP](./ldap.md)
- [Kerberos](./kerberos.md)

**Office and Operations**

- [DNS](./dns.md)
- [DHCP](./dhcp.md)
- [SMTP (and IMAP)](./mail.md)
- [IPP (Printing)](./ipp.md)
- [SIP (and RTP)](./sip-rtp.md)
- [SNMP](./snmp.md)
- [Syslog](./syslog.md)

**Session Behaviour**

- [Independent Exchange](./independent-request.md)
- [Pooled Reuse](./pooled-reuse.md)
- [Multiplexed Session](./multiplexed-session.md)
- [Socket-Bound Session](./socket-bound.md)
- [Reconnectable Session](./reconnectable-session.md)
- [Durable Position](./durable-position.md)
- [Reconnect (and Retry)](./reconnect-retry.md)

**Transport and Path**

- [TCP](./tcp.md)
- [UDP](./udp.md)
- [QUIC](./quic.md)
- [TLS](./tls.md)
- [Keepalive (and Timeouts)](./keepalive-timeouts.md)
- [Middleboxes (NAT, firewall, LB)](./middleboxes.md)
- [Network Path](./network-path.md)
