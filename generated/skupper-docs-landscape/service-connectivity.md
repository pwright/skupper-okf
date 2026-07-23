---
type: DocumentationLandscapePage
title: "Configured Service Connectivity"
id: service-connectivity
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/service-connectivity
tags:
  - skupper
  - docs-landscape
  - configure
related:
  - listener-config
  - connector-config
  - service-routing
timestamp: 2026-07-23T20:17:03Z
---

# Configured Service Connectivity

Configured service connectivity is the outcome where clients at one site can reach a selected backend through a listener, a matching connector, and routing settings that identify the service path.

## Appears in

- [Configure Skupper](./configure-skupper.md) / Configured Behavior

## Dependencies

- [Listener Configuration](./listener-config.md)
- [Connector Configuration](./connector-config.md)
- [Service Routing Configuration](./service-routing.md)

## Sources

- [human/skupper-docs/input/kube-cli/service-exposure.md](../../human/skupper-docs/input/kube-cli/service-exposure.md) - CLI workflow for creating listeners and connectors and checking their status.
- [human/skupper-docs/input/kube-yaml/service-exposure.md](../../human/skupper-docs/input/kube-yaml/service-exposure.md) - Kubernetes YAML examples for Listener, Connector, MultiKeyListener, and attached connector resources.
- [generated/concepts/listener.md](../concepts/listener.md) - Concept page describing listeners as local service endpoints matched by routing key.
- [generated/concepts/connector.md](../concepts/connector.md) - Concept page describing connectors as workload-facing service endpoints.
- [generated/concepts/routing-key.md](../concepts/routing-key.md) - Concept page explaining how routing keys match listeners and connectors.

## Website Links

- [Service exposure with CLI](https://skupper.io/docs/kube-cli/service-exposure.html)
- [Service exposure with YAML](https://skupper.io/docs/kube-yaml/service-exposure.html)
- [Listener resource reference](https://skupperproject.github.io/refdog/resources/listener.html)
- [Connector resource reference](https://skupperproject.github.io/refdog/resources/connector.html)

## Draft Notes

- Expand this page into an operator checklist: create listener, create connector, confirm matching routing key, and verify status from both sides.
- Keep the outcome wording platform-neutral, then branch into Kubernetes and local-system details only where the source docs differ.
- Include a future diagram showing client, listener endpoint, Skupper router network, connector, and backend workload.
