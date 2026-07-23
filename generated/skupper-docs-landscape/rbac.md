---
type: DocumentationLandscapePage
title: "Role-Based Access Control"
id: rbac
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/rbac
tags:
  - skupper
  - docs-landscape
  - secure
timestamp: 2026-07-23T20:30:00Z
---

# Role-Based Access Control

Role-based access control is the platform authorization layer that controls who can create, update, view, and delete Skupper resources in a Kubernetes namespace or cluster.

## Appears in

- [Secure Skupper](./secure-skupper.md) / Identity Foundations

## Sources

- [human/skupper-docs/input/overview/resources.md](../../human/skupper-docs/input/overview/resources.md) - Local overview of Skupper Kubernetes resources.
- [human/skupper-docs/input/kube-cli/site-configuration.md](../../human/skupper-docs/input/kube-cli/site-configuration.md) - CLI source that assumes access to the target namespace.
- [human/skupper-docs/input/kube-yaml/site-configuration.md](../../human/skupper-docs/input/kube-yaml/site-configuration.md) - YAML source for applying site resources.
- [human/skupper-docs/input/console/configuration.md](../../human/skupper-docs/input/console/configuration.md) - Local console configuration source with authentication and delegated RBAC notes.
- [human/skupper-docs/refdog/crds/skupper_cluster_policy_crd.yaml](../../human/skupper-docs/refdog/crds/skupper_cluster_policy_crd.yaml) - Local CRD source candidate for cluster-level policy controls.

## Website Links

- [Skupper resources overview](https://skupper.io/docs/overview/resources.html)
- [Site configuration with the Skupper CLI](https://skupper.io/docs/kube-cli/site-configuration.html)
- [Site configuration with YAML](https://skupper.io/docs/kube-yaml/site-configuration.html)
- [Network console configuration](https://skupper.io/docs/console/configuration.html)

## Draft Notes

- Document prerequisite permissions without over-specifying cluster role names unless source docs provide them.
- Separate operator permissions, application namespace ownership, and console authentication permissions.
- Validate cluster policy examples before presenting them as a primary user-facing RBAC workflow.
