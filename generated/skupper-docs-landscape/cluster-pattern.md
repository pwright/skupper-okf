---
type: DocumentationLandscapePage
title: "Kubernetes Cluster Pattern"
id: cluster-pattern
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/cluster-pattern
tags:
  - skupper
  - docs-landscape
  - platform
related:
  - platform-profile
  - operator-or-cli
timestamp: 2026-07-23T22:00:00Z
---

# Kubernetes Cluster Pattern

The Kubernetes cluster pattern deploys Skupper in a namespace and uses Kubernetes resources, CLI commands, or YAML to configure sites, links, and service exposure.

## Appears in

- [Skupper Platform and Managed-Environment Guides](./platform-guides.md) / Platform Patterns

## Dependencies

- [Platform Compatibility Profile](./platform-profile.md)
- [Operator or CLI Choice](./operator-or-cli.md)

## Sources

- [human/skupper-docs/input/kube-cli/index.md](../../human/skupper-docs/input/kube-cli/index.md) - Kubernetes CLI workflow index.
- [human/skupper-docs/input/kube-yaml/index.md](../../human/skupper-docs/input/kube-yaml/index.md) - Kubernetes YAML workflow index.
- [human/skupper-docs/input/overview/resources.md](../../human/skupper-docs/input/overview/resources.md) - Local overview of Kubernetes resources.
- [human/skupper-docs/input/refdog/resources/site.md](../../human/skupper-docs/input/refdog/resources/site.md) - Site resource reference.
- [generated/skupper-ansible/skupper-ansible-workflow-kubernetes.md](../skupper-ansible/skupper-ansible-workflow-kubernetes.md) - Generated Kubernetes automation workflow.

## Website Links

- [Kubernetes CLI workflows](https://skupper.io/docs/kube-cli/index.html)
- [Kubernetes YAML workflows](https://skupper.io/docs/kube-yaml/index.html)
- [Skupper resources overview](https://skupper.io/docs/overview/resources.html)
- [Site resource reference](https://skupperproject.github.io/refdog/resources/site.html)

## Draft Notes

- Cover namespace choice, installation method, site configuration, link access, and service exposure.
- Add RBAC and managed-platform caveats only where source-backed.
- Keep cluster pattern separate from local-system host integration.
