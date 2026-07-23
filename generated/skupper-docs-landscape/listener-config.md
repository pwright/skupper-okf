---
type: DocumentationLandscapePage
title: "Listener Configuration"
id: listener-config
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/listener-config
tags:
  - skupper
  - docs-landscape
  - configure
related:
  - service-address
timestamp: 2026-07-23T20:17:03Z
---

# Listener Configuration

Listener configuration defines the local endpoint that client applications use and the routing key that Skupper uses to match that endpoint to one or more connectors.

## Appears in

- [Configure Skupper](./configure-skupper.md) / Configuration Resources

## Dependencies

- [Service Address](./service-address.md)

## Sources

- [generated/concepts/listener.md](../concepts/listener.md) - Listener concept, core fields, status signals, and platform notes.
- [human/skupper-docs/input/kube-cli/service-exposure.md](../../human/skupper-docs/input/kube-cli/service-exposure.md) - CLI listener creation and status checks.
- [human/skupper-docs/input/kube-yaml/service-exposure.md](../../human/skupper-docs/input/kube-yaml/service-exposure.md) - Kubernetes Listener YAML examples and MultiKeyListener examples.
- [human/skupper-docs/input/system-cli/service-exposure.md](../../human/skupper-docs/input/system-cli/service-exposure.md) - Local-system listener creation flow.
- [human/skupper-docs/input/refdog/resources/listener.md](../../human/skupper-docs/input/refdog/resources/listener.md) - Listener resource field reference.

## Website Links

- [Listener resource reference](https://skupperproject.github.io/refdog/resources/listener.html)
- [Listener command reference](https://skupperproject.github.io/refdog/commands/listener/create.html)
- [Service exposure with YAML](https://skupper.io/docs/kube-yaml/service-exposure.html)
- [Service exposure with CLI](https://skupper.io/docs/kube-cli/service-exposure.html)

## Draft Notes

- Add a field table later for host, port, routing key, TLS credentials, and status conditions after confirming the exact source field names.
- Explain the platform difference carefully: Kubernetes listeners are implemented as services, while local-system listeners bind local sockets.
- Keep multi-key behavior linked to service routing unless this page grows a dedicated subtype section.
