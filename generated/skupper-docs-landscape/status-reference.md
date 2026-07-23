---
type: DocumentationLandscapePage
title: "Status and Condition Reference"
id: status-reference
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/status-reference
tags:
  - skupper
  - docs-landscape
  - reference
related:
  - resource-status
  - event-codes
timestamp: 2026-07-23T22:15:00Z
---

# Status and Condition Reference

The status and condition reference explains where Skupper reports readiness, matching, link health, service state, events, and diagnostic information.

## Appears in

- [Skupper Reference](./skupper-reference.md) / Runtime Reference

## Dependencies

- [Resource Status](./resource-status.md)
- [Event and Diagnostic Codes](./event-codes.md)

## Sources

- [human/skupper-docs/input/refdog/topics/resource-status.md](../../human/skupper-docs/input/refdog/topics/resource-status.md) - Local resource status topic.
- [human/skupper-docs/input/refdog/commands/site/status.md](../../human/skupper-docs/input/refdog/commands/site/status.md) - Site status command reference.
- [human/skupper-docs/input/refdog/commands/link/status.md](../../human/skupper-docs/input/refdog/commands/link/status.md) - Link status command reference.
- [human/skupper-docs/input/refdog/commands/listener/status.md](../../human/skupper-docs/input/refdog/commands/listener/status.md) - Listener status command reference.
- [human/skupper-docs/input/refdog/commands/connector/status.md](../../human/skupper-docs/input/refdog/commands/connector/status.md) - Connector status command reference.

## Website Links

- [Resource status topic](https://skupperproject.github.io/refdog/topics/resource-status.html)
- [Site status command](https://skupperproject.github.io/refdog/commands/site/status.html)
- [Link status command](https://skupperproject.github.io/refdog/commands/link/status.html)
- [Listener status command](https://skupperproject.github.io/refdog/commands/listener/status.html)
- [Connector status command](https://skupperproject.github.io/refdog/commands/connector/status.html)

## Draft Notes

- Add a cross-resource status table after field names are verified.
- Distinguish configured resource status from observer API runtime state.
- Include common readiness and matching conditions with source-backed meanings.
