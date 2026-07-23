---
type: DocumentationLandscapePage
title: "Service Exposure"
id: service-exposure
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/service-exposure
tags:
  - skupper
  - docs-landscape
  - discover
related:
  - sites
  - routing
timestamp: 2026-07-23T19:44:12Z
---

# Service Exposure

Service exposure describes how a workload becomes reachable through the Skupper application network. The core pattern is a listener for clients, a connector for the target workload, and a routing key that binds them across sites.

## Appears in

- [Discover Skupper](./discover-skupper.md) / Core Concepts

## Dependencies

- [Sites](./sites.md)
- [Service Routing](./routing.md)

## Sources

- [Service exposure topic](../../human/skupper-docs/input/refdog/topics/service-exposure.md): Local topic source for exposing services.
- [Kubernetes YAML service exposure](../../human/skupper-docs/input/kube-yaml/service-exposure.md): Local procedural source for Kubernetes listeners and connectors.
- [System YAML service exposure](../../human/skupper-docs/input/system-yaml/service-exposure.md): Local procedural source for Podman, Docker, and Linux service exposure.
- [Generated listener concept](../concepts/listener.md): Generated local note explaining listener behavior.
- [Generated connector concept](../concepts/connector.md): Generated local note explaining connector behavior.

## Website Links

- [Kubernetes service exposure](https://skupper.io/docs/kube-yaml/service-exposure.html)
- [System service exposure](https://skupper.io/docs/system-yaml/service-exposure.html)

## Draft Notes

- Explain listener, connector, and routing key together; none is enough alone for end-to-end service reachability.
- Separate Kubernetes service semantics from local-system host/port binding.
