---
title: Platform Engineers (Resource Owners)
type: SkupperPersona
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
persona_order: 3
coverage: Partial — cross-platform patterns and automation exist
missing_target_count: 2
openshift_alignment: Resource Owner (Platform Engineer / Namespace Admin)
audience_message: >-
  You own the environments where applications run — Kubernetes namespaces, Linux hosts, or both — and the Skupper sites that connect them. You create sites, establish links across environments, manage access grants, and provision services that application developers consume.
tags:
  - skupper
  - personas
  - platform-engineering
  - resource-owner
  - missing-targets
---

# Platform Engineers (Resource Owners)

> You own the environments where applications run — Kubernetes namespaces, Linux hosts, or both — and the Skupper sites that connect them. You create sites, establish links across environments, manage access grants, and provision services that application developers consume.

For this audience, Skupper is a platform capability with an ownership boundary: the platform can provide consistent application-networking primitives without absorbing operation of every connected dependency.

This persona aligns with the OpenShift **Resource Owner** role — the namespace admin who creates local RoleBindings, delegates project ownership, and provisions shared resources for downstream consumers. On Linux hosts, the equivalent ownership is over the systemd units, Podman containers, or Docker processes that comprise a Skupper site.

## Responsibilities

- **Site lifecycle** — creating and configuring Skupper sites on Kubernetes (via CRDs) or Linux hosts (via Podman, Docker, or systemd), using declarative resources that can be versioned and automated.
- **Link management** — establishing inter-site links between any combination of Kubernetes and Linux-hosted sites, issuing and revoking access grants and tokens for other sites to connect.
- **Service provisioning** — defining listeners and connectors that expose services to or consume services from other environments, then delegating consumption to application developers.
- **Access control** — on Kubernetes, creating local RoleBindings that scope developer permissions; on Linux hosts, managing user access to Skupper configuration directories, tokens, and site definitions.
- **Cross-environment coordination** — connecting Kubernetes namespaces with Linux-hosted sites running on bare metal, VMs, or edge infrastructure, and independently managed systems.

## Relevant existing pages

- [Hybrid Environment Connectivity](../skupper-docs-landscape/hybrid-environment.md) — connecting Kubernetes and local-system sites.
- [Kubernetes Cluster Pattern](../skupper-docs-landscape/cluster-pattern.md) — namespace and Kubernetes resource model.
- [Linux Host Pattern](../skupper-docs-landscape/host-pattern.md) — Podman, Docker, and Linux-hosted sites.
- [Declarative Resources](../skupper-docs-landscape/declarative-resources.md) — versionable site, link, listener, and connector definitions.
- [Mixed Kubernetes and System Workflow](../skupper-ansible/skupper-ansible-workflow-mixed-sites.md) — an existing automation path across environments.
