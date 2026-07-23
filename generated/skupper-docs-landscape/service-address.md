---
type: DocumentationLandscapePage
title: "Service Address"
id: service-address
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/service-address
tags:
  - skupper
  - docs-landscape
  - configure
related: []
timestamp: 2026-07-23T20:17:03Z
---

# Service Address

A service address is the client-facing endpoint configured on a listener: the host and port that local clients use, plus the routing key that connects that endpoint to matching backend connectors.

## Appears in

- [Configure Skupper](./configure-skupper.md) / Configuration Inputs

## Sources

- [generated/concepts/listener.md](../concepts/listener.md) - Listener fields for host, port, and routing key.
- [generated/concepts/routing-key.md](../concepts/routing-key.md) - Routing key behavior and listener-to-connector matching.
- [human/skupper-docs/input/kube-cli/service-exposure.md](../../human/skupper-docs/input/kube-cli/service-exposure.md) - CLI examples that create listener endpoints.
- [human/skupper-docs/input/kube-yaml/service-exposure.md](../../human/skupper-docs/input/kube-yaml/service-exposure.md) - Listener YAML examples.
- [human/skupper-docs/input/refdog/resources/listener.md](../../human/skupper-docs/input/refdog/resources/listener.md) - Listener resource reference.

## Website Links

- [Listener resource reference](https://skupperproject.github.io/refdog/resources/listener.html)
- [Listener concept](https://skupperproject.github.io/refdog/concepts/listener.html)
- [Routing key concept](https://skupperproject.github.io/refdog/concepts/routing-key.html)
- [Service exposure with CLI](https://skupper.io/docs/kube-cli/service-exposure.html)

## Draft Notes

- Add one Kubernetes example and one local-system example because the local address is implemented differently by platform.
- Distinguish the user-facing host and port from the routing key used inside the Skupper network.
- Include a note that multiple service ports normally need separate listener definitions unless future source docs describe a different model.
