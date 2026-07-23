---
type: DocumentationLandscapePage
title: "Kubernetes Integration"
id: kubernetes-integration
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/kubernetes-integration
tags:
  - skupper
  - docs-landscape
  - integrate
related:
  - service-discovery
  - resource-automation
timestamp: 2026-07-23T21:45:00Z
---

# Kubernetes Integration

Kubernetes integration uses Skupper custom resources and CLI workflows to connect services across namespaces and clusters without changing application code.

## Appears in

- [Integrate Skupper](./integrate-skupper.md) / Integration Patterns

## Dependencies

- [Service Discovery Interface](./service-discovery.md)
- [Resource Automation Interface](./resource-automation.md)

## Sources

- [human/skupper-docs/input/kube-yaml/site-configuration.md](../../human/skupper-docs/input/kube-yaml/site-configuration.md) - Local source for Kubernetes Site resources.
- [human/skupper-docs/input/kube-yaml/service-exposure.md](../../human/skupper-docs/input/kube-yaml/service-exposure.md) - Local source for Kubernetes listener, connector, and attached-connector workflows.
- [human/skupper-docs/input/overview/resources.md](../../human/skupper-docs/input/overview/resources.md) - Local overview of Skupper-managed Kubernetes resources.
- [human/skupper-docs/input/refdog/resources/index.md](../../human/skupper-docs/input/refdog/resources/index.md) - Resource reference index.
- [generated/skupper-ansible/skupper-ansible-workflow-kubernetes.md](../skupper-ansible/skupper-ansible-workflow-kubernetes.md) - Generated source for Kubernetes automation with Ansible.

## Website Links

- [Site configuration with YAML](https://skupper.io/docs/kube-yaml/site-configuration.html)
- [Service exposure with YAML](https://skupper.io/docs/kube-yaml/service-exposure.html)
- [Skupper resources overview](https://skupper.io/docs/overview/resources.html)
- [Refdog resource reference](https://skupperproject.github.io/refdog/resources/index.html)

## Draft Notes

- Include namespace ownership, attached connectors, and Kubernetes resource status in future expansion.
- Keep operator installation and platform-specific prerequisites in platform-guide pages.
- Add examples that pair YAML resource application with status checks.
