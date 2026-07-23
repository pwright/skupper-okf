---
type: DocumentationLandscapePage
title: "Service Operations"
id: service-operations
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/service-operations
tags:
  - skupper
  - docs-landscape
  - administer
related:
  - service-status
  - service-configuration
timestamp: 2026-07-23T20:10:12Z
---

# Service Operations

Service Operations covers administering exposed application services: checking listener and connector status, confirming routing-key matches, and changing service definitions in a controlled way.

## Appears in

- [Administer Skupper](./administer-skupper.md) / Administrative Workflows

## Dependencies

- [Service Status](./service-status.md)
- [Service Configuration](./service-configuration.md)

## Sources

- [Service exposure with the CLI](../../human/skupper-docs/input/kube-cli/service-exposure.md): Local source for connector/listener creation and status checks.
- [Connector status command](../../human/skupper-docs/input/refdog/commands/connector/status.md): Local command reference for connector status.
- [Listener status command](../../human/skupper-docs/input/refdog/commands/listener/status.md): Local command reference for listener status.
- [Routing key concept](../concepts/routing-key.md): Generated local source for service binding and routing-key status.
- [Network Observer API concept](../concepts/network-observer-api.md): Generated local source for read-only runtime state, services, connections, and traffic flows.

## Website Links

- [Skupper service exposure guide](https://skupper.io/docs/kube-cli/service-exposure.html)
- [Refdog connector status command](https://skupperproject.github.io/refdog/commands/connector/status.html)
- [Refdog listener status command](https://skupperproject.github.io/refdog/commands/listener/status.html)

## Draft Notes

- Validate both sides of a service: connector and listener.
- Record routing keys because they are the primary service matching mechanism.
- Use application-level checks when status is ready but users report failures.
