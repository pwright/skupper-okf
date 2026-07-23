---
type: DocumentationLandscapePage
title: "Upgrade Validation"
id: upgrade-validation
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/upgrade-validation
tags:
  - skupper
  - docs-landscape
  - upgrade
related:
  - upgraded-network
  - post-upgrade-tests
timestamp: 2026-07-23T20:03:45Z
---

# Upgrade Validation

Upgrade Validation confirms that the upgraded deployment still behaves correctly. It should combine component version checks, Skupper resource status checks, and application-level smoke tests selected before the upgrade begins.

## Appears in

- [Upgrade Skupper](./upgrade-skupper.md) / Upgrade Outcome

## Dependencies

- [Upgraded Application Network](./upgraded-network.md)
- [Post-upgrade Test Suite](./post-upgrade-tests.md)

## Sources

- [Troubleshooting guide](../../human/skupper-docs/input/troubleshooting/index.md): Primary local source for site, connector, listener, and link validation commands.
- [Site status command](../../human/skupper-docs/input/refdog/commands/site/status.md): Local command reference for site readiness.
- [Link status command](../../human/skupper-docs/input/refdog/commands/link/status.md): Local command reference for link readiness.
- [Version command](../../human/skupper-docs/input/refdog/commands/version.md): Local command reference for checking installed versions.
- [Skupper example applications](../workflows/skupper-examples.md): Generated local source for application-level validation patterns.

## Website Links

- [Skupper troubleshooting guide](https://skupper.io/docs/troubleshooting/index.html)
- [Refdog site status command](https://skupperproject.github.io/refdog/commands/site/status.html)
- [Refdog link status command](https://skupperproject.github.io/refdog/commands/link/status.html)

## Draft Notes

- Run validation after each staged change, not only after the last site.
- Preserve pre-upgrade expected results so regressions are easy to detect.
- Keep full incident diagnosis in troubleshoot pages; this page should define pass/fail gates.
