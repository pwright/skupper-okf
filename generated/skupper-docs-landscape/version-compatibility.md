---
type: DocumentationLandscapePage
title: "Version Compatibility"
id: version-compatibility
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/version-compatibility
tags:
  - skupper
  - docs-landscape
  - upgrade
timestamp: 2026-07-23T20:03:45Z
---

# Version Compatibility

Version Compatibility records which Skupper versions and components are expected to work together during and after an upgrade. Because compatibility rules can change by release, this page should rely on current release artifacts and avoid unsupported mixed-version claims.

## Appears in

- [Upgrade Skupper](./upgrade-skupper.md) / Upgrade Readiness

## Sources

- [Compatibility Matrix](./compatibility-matrix.md): Local landscape source candidate for compatibility data.
- [Release Notes](./release-notes.md): Local landscape source for release-specific version notes.
- [Skupper installation guide](../../human/skupper-docs/input/install/index.md): Local source for current versioned install and upgrade commands.
- [Version command](../../human/skupper-docs/input/refdog/commands/version.md): Local command reference for discovering installed versions.
- [Skupper source entry](../../sources/skupper.md): Local source record for upstream release verification.

## Website Links

- [Skupper releases](https://skupper.io/releases/index.html)
- [Skupper GitHub releases](https://github.com/skupperproject/skupper/releases)
- [Refdog version command](https://skupperproject.github.io/refdog/commands/version.html)

## Draft Notes

- Capture CLI, controller, router, and console or observer versions separately.
- Mark unknown compatibility explicitly rather than filling gaps.
- Review this page for each release because compatibility information is time-sensitive.
