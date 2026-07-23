---
type: DocumentationLandscapePage
title: "Backend Endpoint"
id: backend-endpoint
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/backend-endpoint
tags:
  - skupper
  - docs-landscape
  - configure
related: []
timestamp: 2026-07-23T20:17:03Z
---

# Backend Endpoint

A backend endpoint is the workload target described by a connector, such as selected Kubernetes pods, a workload reference, or a host and port on a local system.

## Appears in

- [Configure Skupper](./configure-skupper.md) / Configuration Inputs

## Sources

- [generated/concepts/connector.md](../concepts/connector.md) - Connector fields for selector, workload, host, port, and routing key.
- [human/skupper-docs/input/kube-cli/service-exposure.md](../../human/skupper-docs/input/kube-cli/service-exposure.md) - CLI examples for workload and selector based connectors.
- [human/skupper-docs/input/kube-yaml/service-exposure.md](../../human/skupper-docs/input/kube-yaml/service-exposure.md) - YAML examples for standard and attached connectors.
- [human/skupper-docs/input/system-cli/service-exposure.md](../../human/skupper-docs/input/system-cli/service-exposure.md) - Local-system host and port connector examples.
- [human/skupper-docs/input/refdog/concepts/workload.md](../../human/skupper-docs/input/refdog/concepts/workload.md) - Workload concept reference.

## Website Links

- [Connector resource reference](https://skupperproject.github.io/refdog/resources/connector.html)
- [Connector concept](https://skupperproject.github.io/refdog/concepts/connector.html)
- [Workload concept](https://skupperproject.github.io/refdog/concepts/workload.html)
- [Service exposure with YAML](https://skupper.io/docs/kube-yaml/service-exposure.html)

## Draft Notes

- Add decision guidance for selector, workload reference, attached connector, and host-based endpoint choices.
- Include status examples showing selected pods and matching listeners once the status source is normalized.
- Keep backend endpoint wording service-agnostic so it works for Kubernetes and local-system platforms.
