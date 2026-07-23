---
type: DocumentationLandscapePage
title: "Runtime Logs"
id: runtime-logs
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/runtime-logs
tags:
  - skupper
  - docs-landscape
  - observe
related:
  - log-collection
timestamp: 2026-07-23T20:45:00Z
---

# Runtime Logs

Runtime logs are diagnostic records from Skupper components and related observer services that help explain failed setup, degraded connectivity, or unexpected traffic behavior.

## Appears in

- [Observe Skupper](./observe-skupper.md) / Observability Signals

## Dependencies

- [Log Collection](./log-collection.md)

## Sources

- [human/skupper-docs/input/troubleshooting/index.md](../../human/skupper-docs/input/troubleshooting/index.md) - Local troubleshooting source for logs and debug collection.
- [human/skupper-docs/input/console/configuration.md](../../human/skupper-docs/input/console/configuration.md) - Local source for observer logging profile configuration.
- [generated/skupper-console/console.md](../skupper-console/console.md) - Generated source for console behavior and error handling notes.
- [generated/concepts/network-observer-api.md](../concepts/network-observer-api.md) - Generated source for observer components and API behavior.
- [generated/skupper-docs-landscape/logging-settings.md](./logging-settings.md) - Related landscape page for logging configuration.

## Website Links

- [Troubleshooting](https://skupper.io/docs/troubleshooting/index.html)
- [Network console configuration](https://skupper.io/docs/console/configuration.html)
- [Network console](https://skupper.io/docs/console/index.html)
- [Skupper console repository](https://github.com/skupperproject/skupper-console)

## Draft Notes

- Separate component logs, observer logs, and generated debug bundles.
- Add source-backed examples for changing log verbosity only after confirming platform-specific commands.
- Keep log interpretation tied to concrete symptoms such as failed links, unmatched services, or missing metrics.
