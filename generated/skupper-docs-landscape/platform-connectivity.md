---
type: DocumentationLandscapePage
title: "Platform-to-Platform Connectivity"
id: platform-connectivity
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/platform-connectivity
tags:
  - skupper
  - docs-landscape
  - integrate
related:
  - kubernetes-integration
  - host-integration
timestamp: 2026-07-23T21:45:00Z
---

# Platform-to-Platform Connectivity

Platform-to-platform connectivity uses Skupper sites and links to connect workloads across Kubernetes clusters, local-system platforms, or mixed environments.

## Appears in

- [Integrate Skupper](./integrate-skupper.md) / Integration Outcomes

## Dependencies

- [Kubernetes Integration](./kubernetes-integration.md)
- [Linux Host Integration](./host-integration.md)

## Sources

- [generated/skupper-ansible/skupper-ansible-workflow-mixed-sites.md](../skupper-ansible/skupper-ansible-workflow-mixed-sites.md) - Generated source for mixed Kubernetes and system site automation.
- [human/skupper-docs/input/kube-cli/site-linking.md](../../human/skupper-docs/input/kube-cli/site-linking.md) - Local CLI source for linking Kubernetes sites.
- [human/skupper-docs/input/system-cli/site-linking.md](../../human/skupper-docs/input/system-cli/site-linking.md) - Local CLI source for linking system sites.
- [human/skupper-docs/input/refdog/topics/site-linking.md](../../human/skupper-docs/input/refdog/topics/site-linking.md) - Refdog topic source for site linking concepts.
- [generated/concepts/network-deployment-concerns.md](../concepts/network-deployment-concerns.md) - Generated source for deployment and link-access concerns.

## Website Links

- [Site linking with the Skupper CLI](https://skupper.io/docs/kube-cli/site-linking.html)
- [System site linking](https://skupper.io/docs/system-cli/site-linking.html)
- [Site linking topic](https://skupperproject.github.io/refdog/topics/site-linking.html)
- [Skupper Ansible repository](https://github.com/skupperproject/skupper-ansible)

## Draft Notes

- Expand with separate Kubernetes-to-Kubernetes, system-to-system, and mixed-platform flows.
- Keep link credential handling and platform prerequisites explicit.
- Add validation checks for sites, links, listeners, connectors, and application traffic.
