---
title: Cluster Administrators
type: SkupperPersona
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
persona_order: 0
coverage: Partial — installation and RBAC pages exist, no consolidated admin guide
missing_target_count: 2
openshift_alignment: Cluster Administrator
audience_message: >-
  You control what runs on the cluster and who can do what. Skupper installs as a controller with its own CRDs and requires RBAC decisions about which namespaces and users can create sites, establish links, and issue access grants. You own the installation, upgrade lifecycle, certificate policy, and cluster-wide governance of Skupper resources.
tags:
  - skupper
  - personas
  - cluster-administration
  - rbac
  - missing-targets
---

# Cluster Administrators

> You control what runs on the cluster and who can do what. Skupper installs as a controller with its own CRDs and requires RBAC decisions about which namespaces and users can create sites, establish links, and issue access grants. You own the installation, upgrade lifecycle, certificate policy, and cluster-wide governance of Skupper resources.

For this audience, Skupper is infrastructure that must be installed, secured, and governed like any other cluster-scoped controller. The key decisions are: who can create Skupper resources, which namespaces are permitted to participate, what certificate and trust policies apply, and how upgrades are sequenced across a multi-site network.

This persona aligns with the OpenShift **Cluster Administrator** role — the user with elevated cluster-admin privileges who manages control plane components, global RBAC configuration, and cluster-wide policies.

## Responsibilities

- **Installation and upgrades** — deploying the Skupper controller, managing CRD versions, and coordinating upgrade sequences across linked sites.
- **Cluster-wide RBAC** — defining ClusterRoles and ClusterRoleBindings that govern which users and service accounts can create Site, Link, AccessGrant, Listener, and Connector resources.
- **Certificate and trust policy** — configuring the certificate manager, trust bundles, and rotation policies for mTLS across sites.
- **Namespace governance** — deciding which namespaces are permitted to host Skupper sites and setting policies that constrain resource owners.
- **Operational integration** — connecting Skupper's metrics, health checks, and network observer to the cluster's monitoring and alerting stack.

## Boundary with Resource Owners

Cluster Administrators establish the policies and permissions. Resource Owners (Platform Engineers / Namespace Admins) operate within those boundaries — creating sites, managing links, and provisioning services for application developers. The Cluster Administrator does not typically create individual listeners or connectors; they ensure the platform allows the right people to do so.

## Relevant existing pages

- [Install Skupper](../skupper-docs-landscape/install-skupper.md) — installation paths and prerequisites.
- [Operator Installation](../skupper-docs-landscape/operator-installation.md) — operator-based deployment for cluster-scoped management.
- [Role-Based Access Control](../skupper-docs-landscape/rbac.md) — platform authorization for Skupper resources.
- [Certificate Manager](../concepts/certificate-manager.md) — mTLS certificate issuance and management.
- [Site Controller](../concepts/site-controller.md) and [System Controller](../concepts/system-controller.md) — the controllers that reconcile Skupper CRDs.
- [Upgrade Sequence](../skupper-docs-landscape/upgrade-sequence.md) — coordinating upgrades across sites.
- [Network Isolation](../skupper-docs-landscape/network-isolation.md) — namespace scope, selected exposure, and link access policies.
- [Service Exposure Policy](../skupper-docs-landscape/service-policy.md) — cluster-wide constraints on addresses, ports, and workloads.
