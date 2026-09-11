---
title: Platform Engineers
type: SkupperPersona
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
persona_order: 3
coverage: Partial — cross-platform patterns and automation exist
missing_target_count: 2
audience_message: >-
  A platform can support applications whose dependencies live elsewhere. Skupper gives you a consistent way to expose and consume services across environments, allowing your Kubernetes platform to work with existing databases, VM workloads, and independently managed systems.
tags:
  - skupper
  - personas
  - platform-engineering
  - missing-targets
---

# Platform Engineers

> A platform can support applications whose dependencies live elsewhere. Skupper gives you a consistent way to expose and consume services across environments, allowing your Kubernetes platform to work with existing databases, VM workloads, and independently managed systems.

For this audience, Skupper is a platform capability with an ownership boundary: the platform can provide consistent application-networking primitives without absorbing operation of every connected dependency.

## Relevant existing pages

- [Hybrid Environment Connectivity](../skupper-docs-landscape/hybrid-environment.md) — connecting Kubernetes and local-system sites.
- [Kubernetes Cluster Pattern](../skupper-docs-landscape/cluster-pattern.md) — namespace and Kubernetes resource model.
- [Linux Host Pattern](../skupper-docs-landscape/host-pattern.md) — Podman, Docker, and Linux-hosted sites.
- [Declarative Resources](../skupper-docs-landscape/declarative-resources.md) — versionable site, link, listener, and connector definitions.
- [Mixed Kubernetes and System Workflow](../skupper-ansible/skupper-ansible-workflow-mixed-sites.md) — an existing automation path across environments.
