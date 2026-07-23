---
type: DocumentationLandscapePage
title: "Event Collection"
id: event-collection
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/event-collection
tags:
  - skupper
  - docs-landscape
  - observe
timestamp: 2026-07-23T20:45:00Z
---

# Event Collection

Event collection is the process of gathering discrete Skupper resource and observer signals so changes in network state can be reviewed alongside metrics and logs.

## Appears in

- [Observe Skupper](./observe-skupper.md) / Collection and Presentation

## Sources

- [human/skupper-docs/input/troubleshooting/index.md](../../human/skupper-docs/input/troubleshooting/index.md) - Local source for diagnostic collection.
- [human/skupper-docs/input/refdog/topics/resource-status.md](../../human/skupper-docs/input/refdog/topics/resource-status.md) - Local source candidate for resource conditions and status events.
- [generated/concepts/network-observer-api.md](../concepts/network-observer-api.md) - Generated source for observer resource state.
- [generated/skupper-console/console.md](../skupper-console/console.md) - Generated source for console API calls and error handling.
- [generated/skupper-docs-landscape/event-codes.md](./event-codes.md) - Related landscape page for event code material.

## Website Links

- [Troubleshooting](https://skupper.io/docs/troubleshooting/index.html)
- [Resource status topic](https://skupperproject.github.io/refdog/topics/resource-status.html)
- [Network console](https://skupper.io/docs/console/index.html)
- [Skupper console repository](https://github.com/skupperproject/skupper-console)

## Draft Notes

- Confirm whether events are exposed through Kubernetes events, observer APIs, console views, or debug bundles before adding procedure text.
- Add examples that pair an event with the affected resource and likely next check.
- Keep event collection scoped to observation; remediation belongs in troubleshooting pages.
