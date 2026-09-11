---
title: Enterprise Architects
type: SkupperPersona
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
persona_order: 4
coverage: Partial — strong patterns, no decision framework
missing_target_count: 2
audience_message: >-
  Skupper helps separate service relationships from deployment locations. Components can communicate across different environments, giving you more freedom to choose placement according to workload requirements and to change parts of the architecture independently.
tags:
  - skupper
  - personas
  - enterprise-architecture
  - missing-targets
---

# Enterprise Architects

> Skupper helps separate service relationships from deployment locations. Components can communicate across different environments, giving you more freedom to choose placement according to workload requirements and to change parts of the architecture independently.

For this audience, Skupper is a mechanism for preventing service relationships from silently becoming platform-placement requirements. Placement still has to account for latency, data gravity, cost, compliance, availability, and operational ownership.

## Relevant existing pages

- [Independent Microservice Placement Pattern](../architecture/independent-service-placement.md) — deployment topology should not dictate application topology.
- [Integration Layer Pattern](../architecture/integration-layer.md) — Skupper’s scoped role in connectivity, routing, and secure transport.
- [Legacy Modernization / Wrapper Pattern](../architecture/legacy-modernization.md) — incremental change without relocating the legacy system.
- [Hybrid-Cloud Elasticity Pattern](../architecture/hybrid-cloud-elasticity.md) — location preference, spillover, and failover across environments.
- [Network Deployment Concerns](../concepts/network-deployment-concerns.md) — practical constraints that remain after connectivity is available.
