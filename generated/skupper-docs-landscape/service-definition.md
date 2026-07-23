---
type: DocumentationLandscapePage
title: "Service Definition"
id: service-definition
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/service-definition
tags:
  - skupper
  - docs-landscape
  - extend
timestamp: 2026-07-23T20:01:23Z
---

# Service Definition

Service Definition records the workload endpoint and client-facing endpoint needed to expose a service on Skupper. It should capture connector details, listener details, routing key, port, and validation expectations before resources are created.

## Appears in

- [Extend a Skupper Application Network](./extend-skupper.md) / Expansion Controls

## Sources

- [Service exposure with the CLI](../../human/skupper-docs/input/kube-cli/service-exposure.md): Primary local source for connector/listener workflow and routing-key defaults.
- [Connector concept](../concepts/connector.md): Generated local concept source for workload endpoint and routing key.
- [Listener concept](../concepts/listener.md): Generated local concept source for local client endpoint and routing key.
- [Connector resource](../../human/skupper-docs/input/refdog/resources/connector.md): Local resource reference for declarative connector definitions.
- [Listener resource](../../human/skupper-docs/input/refdog/resources/listener.md): Local resource reference for declarative listener definitions.

## Website Links

- [Skupper service exposure guide](https://skupper.io/docs/kube-cli/service-exposure.html)
- [Refdog connector resource](https://skupperproject.github.io/refdog/resources/connector.html)
- [Refdog listener resource](https://skupperproject.github.io/refdog/resources/listener.html)

## Draft Notes

- Use one definition record per service/port pair unless multiple ports are intentionally grouped.
- Capture workload selector or host/port, listener host/port, routing key, and owning team.
- Mark whether the service is CLI-created or resource-managed.
