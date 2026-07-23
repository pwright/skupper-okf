---
type: DocumentationLandscapePage
title: "Service Status"
id: service-status
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/service-status
tags:
  - skupper
  - docs-landscape
  - administer
timestamp: 2026-07-23T20:10:12Z
---

# Service Status

Service Status records whether listeners and connectors are configured and matched so application traffic can flow. It should include both Skupper resource status and a lightweight application check when possible.

## Appears in

- [Administer Skupper](./administer-skupper.md) / Operational State

## Sources

- [Service exposure with the CLI](../../human/skupper-docs/input/kube-cli/service-exposure.md): Local source for connector/listener creation and status checks.
- [Connector status command](../../human/skupper-docs/input/refdog/commands/connector/status.md): Local command reference for connector status.
- [Listener status command](../../human/skupper-docs/input/refdog/commands/listener/status.md): Local command reference for listener status.
- [Routing key concept](../concepts/routing-key.md): Generated local source for matching and binding status.
- [Troubleshooting guide](../../human/skupper-docs/input/troubleshooting/index.md): Primary local source for checking sites, links, connectors, listeners, and collecting debug evidence.

## Website Links

- [Skupper service exposure guide](https://skupper.io/docs/kube-cli/service-exposure.html)
- [Refdog connector status command](https://skupperproject.github.io/refdog/commands/connector/status.html)
- [Refdog listener status command](https://skupperproject.github.io/refdog/commands/listener/status.html)

## Draft Notes

- Check listener and connector status together.
- Record routing key and matching status with every service check.
- Escalate to application tests when Skupper status is healthy but traffic still fails.
