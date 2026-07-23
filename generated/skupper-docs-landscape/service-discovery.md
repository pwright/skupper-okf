---
type: DocumentationLandscapePage
title: "Service Discovery Interface"
id: service-discovery
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/service-discovery
tags:
  - skupper
  - docs-landscape
  - integrate
timestamp: 2026-07-23T21:45:00Z
---

# Service Discovery Interface

The service discovery interface is the Skupper listener, connector, and routing-key model that makes a service reachable across sites.

## Appears in

- [Integrate Skupper](./integrate-skupper.md) / Platform Interfaces

## Sources

- [generated/concepts/routing-key.md](../concepts/routing-key.md) - Generated source for routing-key matching and service discovery.
- [generated/concepts/listener.md](../concepts/listener.md) - Generated source for listener behavior and status.
- [generated/concepts/connector.md](../concepts/connector.md) - Generated source for connector behavior and status.
- [human/skupper-docs/input/kube-yaml/service-exposure.md](../../human/skupper-docs/input/kube-yaml/service-exposure.md) - Local YAML source for service exposure resources.
- [human/skupper-docs/input/refdog/topics/service-exposure.md](../../human/skupper-docs/input/refdog/topics/service-exposure.md) - Refdog topic source for service exposure.

## Website Links

- [Service exposure with YAML](https://skupper.io/docs/kube-yaml/service-exposure.html)
- [Service exposure topic](https://skupperproject.github.io/refdog/topics/service-exposure.html)
- [Listener resource reference](https://skupperproject.github.io/refdog/resources/listener.html)
- [Connector resource reference](https://skupperproject.github.io/refdog/resources/connector.html)
- [Routing key concept](https://skupperproject.github.io/refdog/concepts/routing-key.html)

## Draft Notes

- Explain service discovery through configured Skupper resources rather than external DNS assumptions.
- Include attached connectors as a Kubernetes namespace integration case.
- Add status checks for listener and connector matching.
