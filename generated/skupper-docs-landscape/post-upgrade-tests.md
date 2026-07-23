---
type: DocumentationLandscapePage
title: "Post-upgrade Test Suite"
id: post-upgrade-tests
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/post-upgrade-tests
tags:
  - skupper
  - docs-landscape
  - upgrade
timestamp: 2026-07-23T20:03:45Z
---

# Post-upgrade Test Suite

Post-upgrade Test Suite is the set of checks run after each upgrade stage. It should include Skupper component version checks, site and link status, service matching, and application-level requests for representative services.

## Appears in

- [Upgrade Skupper](./upgrade-skupper.md) / Upgrade Readiness

## Sources

- [Troubleshooting guide](../../human/skupper-docs/input/troubleshooting/index.md): Primary local source for status checks across sites, connectors, listeners, and links.
- [Site status command](../../human/skupper-docs/input/refdog/commands/site/status.md): Local command reference for site checks.
- [Connector status command](../../human/skupper-docs/input/refdog/commands/connector/status.md): Local command reference for connector checks.
- [Listener status command](../../human/skupper-docs/input/refdog/commands/listener/status.md): Local command reference for listener checks.
- [Skupper example applications](../workflows/skupper-examples.md): Generated local source for representative application test shapes.

## Website Links

- [Skupper troubleshooting guide](https://skupper.io/docs/troubleshooting/index.html)
- [Refdog connector status command](https://skupperproject.github.io/refdog/commands/connector/status.html)
- [Refdog listener status command](https://skupperproject.github.io/refdog/commands/listener/status.html)

## Draft Notes

- Run the same test suite before and after upgrade so results can be compared.
- Include at least one application-level check for each critical traffic path.
- Store expected outputs and failure thresholds with the maintenance plan.
