---
type: DocumentationLandscapePage
title: "Host Service Binding"
id: host-service-binding
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/host-service-binding
tags:
  - skupper
  - docs-landscape
  - integrate
timestamp: 2026-07-23T21:45:00Z
---

# Host Service Binding

Host service binding connects a service running on a local system to a Skupper connector so it can be reached from the application network.

## Appears in

- [Integrate Skupper](./integrate-skupper.md) / Platform Interfaces

## Sources

- [human/skupper-docs/input/system-cli/service-exposure.md](../../human/skupper-docs/input/system-cli/service-exposure.md) - Local CLI source for exposing system services.
- [human/skupper-docs/input/system-yaml/service-exposure.md](../../human/skupper-docs/input/system-yaml/service-exposure.md) - Local YAML source for system service exposure.
- [human/skupper-docs/input/refdog/resources/connector.md](../../human/skupper-docs/input/refdog/resources/connector.md) - Connector resource reference.
- [generated/skupper/skupper-crd-connectors-skupper-io.md](../skupper/skupper-crd-connectors-skupper-io.md) - Generated CRD source for Connector fields including host and port behavior.
- [generated/skupper-ansible/skupper-ansible-workflow-non-kubernetes.md](../skupper-ansible/skupper-ansible-workflow-non-kubernetes.md) - Generated source for non-Kubernetes workflow.

## Website Links

- [System service exposure](https://skupper.io/docs/system-cli/service-exposure.html)
- [System YAML service exposure](https://skupper.io/docs/system-yaml/service-exposure.html)
- [Connector resource reference](https://skupperproject.github.io/refdog/resources/connector.html)
- [Skupper Ansible repository](https://github.com/skupperproject/skupper-ansible)

## Draft Notes

- Keep host, port, TLS, and routing-key fields explicit in future examples.
- Separate binding to a local service from exposing that service through a remote listener.
- Include checks for connector status and application reachability.
