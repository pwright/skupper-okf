---
title: Database Engineers
type: SkupperPersona
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
persona_order: 2
coverage: Partial — database cautions exist, but no placement tutorial
missing_target_count: 2
audience_message: >-
  Moving an application to Kubernetes does not automatically require moving its database. Skupper lets applications in other environments connect to the database where you operate it. You retain responsibility for its deployment, recovery, and maintenance.
tags:
  - skupper
  - personas
  - databases
  - missing-targets
---

# Database Engineers

> Moving an application to Kubernetes does not automatically require moving its database. Skupper lets applications in other environments connect to the database where you operate it. You retain responsibility for its deployment, recovery, and maintenance.

For this audience, the important boundary is between network reachability and database correctness. Skupper can carry TCP connections to the database; it does not preserve an in-flight transaction or replace database authentication, recovery, pooling, and failover design.

## Relevant existing pages

- [Database Access](../enterprise-session-recovery/database-access.md) — suitability and production concerns for remote database access.
- [Direct DB (JDBC/native)](../enterprise-session-recovery/direct-db.md) — explicit limits around socket-bound sessions and transactions.
- [Connection Pool](../enterprise-session-recovery/connection-pool.md) — client-side detection and replacement of unhealthy connections.
- [Connector](../concepts/connector.md) — how a database host and port can be offered without relocating the database.
- [Network Deployment Concerns](../concepts/network-deployment-concerns.md) — placement, capacity, network, and operational considerations.
