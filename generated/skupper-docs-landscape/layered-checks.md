---
type: DocumentationLandscapePage
title: "Site, Link, Route, and Service Checks"
id: layered-checks
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/layered-checks
tags:
  - skupper
  - docs-landscape
  - troubleshoot
timestamp: 2026-07-23T21:15:00Z
---

# Site, Link, Route, and Service Checks

Layered checks verify Skupper from the bottom up: site readiness, link state, routing-key matching, listener and connector status, and application reachability.

## Appears in

- [Troubleshoot Skupper](./troubleshoot-skupper.md) / Diagnostic Evidence

## Sources

- [human/skupper-docs/input/troubleshooting/index.md](../../human/skupper-docs/input/troubleshooting/index.md) - Local troubleshooting guide for site, link, listener, and connector checks.
- [human/skupper-docs/input/refdog/commands/site/status.md](../../human/skupper-docs/input/refdog/commands/site/status.md) - Site status command reference.
- [human/skupper-docs/input/refdog/commands/link/status.md](../../human/skupper-docs/input/refdog/commands/link/status.md) - Link status command reference.
- [human/skupper-docs/input/refdog/commands/listener/status.md](../../human/skupper-docs/input/refdog/commands/listener/status.md) - Listener status command reference.
- [human/skupper-docs/input/refdog/commands/connector/status.md](../../human/skupper-docs/input/refdog/commands/connector/status.md) - Connector status command reference.

## Website Links

- [Troubleshooting](https://skupper.io/docs/troubleshooting/index.html)
- [Site status command](https://skupperproject.github.io/refdog/commands/site/status.html)
- [Link status command](https://skupperproject.github.io/refdog/commands/link/status.html)
- [Listener status command](https://skupperproject.github.io/refdog/commands/listener/status.html)
- [Connector status command](https://skupperproject.github.io/refdog/commands/connector/status.html)

## Draft Notes

- Build the expanded page as ordered checks with expected evidence and next action.
- Include routing-key matching because listener and connector readiness depend on matching definitions.
- Keep platform-specific command variants separate if Kubernetes and local-system outputs differ.
