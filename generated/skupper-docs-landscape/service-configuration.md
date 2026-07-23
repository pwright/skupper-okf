---
type: DocumentationLandscapePage
title: "Service Configuration"
id: service-configuration
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/service-configuration
tags:
  - skupper
  - docs-landscape
  - administer
timestamp: 2026-07-23T20:10:12Z
---

# Service Configuration

Service Configuration is the desired listener and connector setup for an exposed service. It includes routing keys, ports, workload selectors or host endpoints, and any declarative resource definitions used to manage the service.

## Appears in

- [Administer Skupper](./administer-skupper.md) / Operational State

## Sources

- [Service exposure with the CLI](../../human/skupper-docs/input/kube-cli/service-exposure.md): Local source for connector/listener creation and status checks.
- [Connector concept](../concepts/connector.md): Generated local concept source for connector fields and behavior.
- [Listener concept](../concepts/listener.md): Generated local concept source for listener fields and behavior.
- [Connector resource](../../human/skupper-docs/input/refdog/resources/connector.md): Local resource reference for declarative connector configuration.
- [Listener resource](../../human/skupper-docs/input/refdog/resources/listener.md): Local resource reference for declarative listener configuration.

## Website Links

- [Skupper service exposure guide](https://skupper.io/docs/kube-cli/service-exposure.html)
- [Refdog connector resource](https://skupperproject.github.io/refdog/resources/connector.html)
- [Refdog listener resource](https://skupperproject.github.io/refdog/resources/listener.html)

## Draft Notes

- Track one service definition per routed service and port.
- Keep routing-key changes under controlled change because they can alter reachability.
- For local-system platforms, remember configuration changes may require reload.
