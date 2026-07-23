---
type: DocumentationLandscapePage
title: "Upgraded Application Network"
id: upgraded-network
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/upgraded-network
tags:
  - skupper
  - docs-landscape
  - upgrade
related:
  - upgrade-sequence
  - component-upgrades
timestamp: 2026-07-23T20:03:45Z
---

# Upgraded Application Network

Upgraded Application Network is the upgrade outcome where the selected Skupper components have moved to the target version and the application network still reports healthy site, link, and service state. Keep this page evidence-based: version checks, status checks, and application validation should back the outcome.

## Appears in

- [Upgrade Skupper](./upgrade-skupper.md) / Upgrade Outcome

## Dependencies

- [Site Upgrade Sequence](./upgrade-sequence.md)
- [CLI, Operator, and Router Upgrades](./component-upgrades.md)

## Sources

- [Skupper installation guide](../../human/skupper-docs/input/install/index.md): Primary local source for controller, CLI, and local-site upgrade commands.
- [Troubleshooting guide](../../human/skupper-docs/input/troubleshooting/index.md): Local source for checking controller, site, connector, listener, and link status.
- [Version command](../../human/skupper-docs/input/refdog/commands/version.md): Local command reference for component version checks.
- [Release Notes](./release-notes.md): Local landscape source for release-level changes that may affect the outcome.
- [Compatibility Matrix](./compatibility-matrix.md): Local landscape source candidate for version compatibility checks.

## Website Links

- [Skupper installation docs](https://skupper.io/docs/install/index.html)
- [Skupper troubleshooting guide](https://skupper.io/docs/troubleshooting/index.html)
- [Skupper releases](https://skupper.io/releases/index.html)

## Draft Notes

- Define the upgraded state with concrete evidence, not just completed commands.
- Include site, link, listener, connector, and application checks when those resources are in use.
- Record any version skew intentionally left in place for a staged upgrade.
