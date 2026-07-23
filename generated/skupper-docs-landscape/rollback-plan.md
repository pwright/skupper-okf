---
type: DocumentationLandscapePage
title: "Rollback Plan"
id: rollback-plan
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/rollback-plan
tags:
  - skupper
  - docs-landscape
  - upgrade
related:
  - backup-state
  - version-compatibility
timestamp: 2026-07-23T20:03:45Z
---

# Rollback Plan

Rollback Plan records how the team will return to the previous working state if an upgrade does not pass validation. Source coverage for Skupper-specific rollback is thin, so this page should remain a readiness checklist until release-specific rollback instructions are available.

## Appears in

- [Upgrade Skupper](./upgrade-skupper.md) / Upgrade Execution

## Dependencies

- [Configuration and State Backup](./backup-state.md)
- [Version Compatibility](./version-compatibility.md)

## Sources

- [Skupper installation guide](../../human/skupper-docs/input/install/index.md): Local source for reinstalling controllers and updating CLI or local systems.
- [Network console guide](../../human/skupper-docs/input/console/index.md): Local source with Helm rollback examples for the Network Observer component.
- [Troubleshooting guide](../../human/skupper-docs/input/troubleshooting/index.md): Local source for identifying failed post-upgrade state.
- [Version Compatibility](./version-compatibility.md): Local landscape source candidate for downgrade or mixed-version constraints.
- [Release Notes](./release-notes.md): Local landscape source candidate for release-specific rollback warnings.

## Website Links

- [Skupper installation docs](https://skupper.io/docs/install/index.html)
- [Skupper network console](https://skupper.io/docs/console/index.html)
- [Skupper releases](https://skupper.io/releases/index.html)

## Draft Notes

- Define rollback triggers before starting the upgrade.
- Keep backup artifacts, previous versions, and commands available before changing components.
- Do not promise downgrade safety without release-specific compatibility evidence.
