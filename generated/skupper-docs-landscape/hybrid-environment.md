---
type: DocumentationLandscapePage
title: "Hybrid Environment Connectivity"
id: hybrid-environment
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/hybrid-environment
tags:
  - skupper
  - docs-landscape
  - platform
related:
  - cluster-pattern
  - host-pattern
  - network-controls
timestamp: 2026-07-23T22:00:00Z
---

# Hybrid Environment Connectivity

Hybrid environment connectivity joins Kubernetes sites and local-system sites so application services can communicate across clusters, hosts, and network boundaries.

## Appears in

- [Skupper Platform and Managed-Environment Guides](./platform-guides.md) / Platform Outcomes

## Dependencies

- [Kubernetes Cluster Pattern](./cluster-pattern.md)
- [Linux Host Pattern](./host-pattern.md)
- [Firewall and Egress Controls](./network-controls.md)

## Sources

- [generated/skupper-ansible/skupper-ansible-workflow-mixed-sites.md](../skupper-ansible/skupper-ansible-workflow-mixed-sites.md) - Generated source for mixed Kubernetes and system workflows.
- [human/skupper-docs/input/kube-cli/site-linking.md](../../human/skupper-docs/input/kube-cli/site-linking.md) - Kubernetes site linking source.
- [human/skupper-docs/input/system-cli/site-linking.md](../../human/skupper-docs/input/system-cli/site-linking.md) - System site linking source.
- [generated/concepts/network-deployment-concerns.md](../concepts/network-deployment-concerns.md) - Generated source for link access and firewall placement.
- [human/skupper-docs/input/refdog/topics/site-linking.md](../../human/skupper-docs/input/refdog/topics/site-linking.md) - Refdog site linking topic.

## Website Links

- [Kubernetes site linking](https://skupper.io/docs/kube-cli/site-linking.html)
- [System site linking](https://skupper.io/docs/system-cli/site-linking.html)
- [Site linking topic](https://skupperproject.github.io/refdog/topics/site-linking.html)
- [Skupper Ansible repository](https://github.com/skupperproject/skupper-ansible)

## Draft Notes

- Include examples for cluster-to-host and host-to-cluster link direction.
- Keep platform networking prerequisites and credential exchange visible in every workflow.
- Add application validation after both sites report link status.
