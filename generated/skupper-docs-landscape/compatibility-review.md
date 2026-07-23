---
type: DocumentationLandscapePage
title: "Compatibility Review"
id: compatibility-review
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/compatibility-review
tags:
  - skupper
  - docs-landscape
  - upgrade
related:
  - version-compatibility
  - release-differences
timestamp: 2026-07-23T20:03:45Z
---

# Compatibility Review

Compatibility Review is the pre-upgrade checkpoint where target versions, component combinations, platform support, and behavior changes are checked before any environment is changed. Use release material first and keep assumptions explicit when source coverage is incomplete.

## Appears in

- [Upgrade Skupper](./upgrade-skupper.md) / Upgrade Readiness

## Dependencies

- [Version Compatibility](./version-compatibility.md)
- [Release Differences](./release-differences.md)

## Sources

- [Release Notes](./release-notes.md): Local landscape source for release-level changes.
- [Compatibility Matrix](./compatibility-matrix.md): Local landscape source candidate for supported version combinations.
- [Skupper installation guide](../../human/skupper-docs/input/install/index.md): Local source for current install and upgrade mechanisms.
- [Version command](../../human/skupper-docs/input/refdog/commands/version.md): Local command reference for identifying current component versions.
- [Skupper releases source](../../sources/skupper.md): Local source record for upstream release verification.

## Website Links

- [Skupper releases](https://skupper.io/releases/index.html)
- [Skupper GitHub releases](https://github.com/skupperproject/skupper/releases)
- [Refdog version command](https://skupperproject.github.io/refdog/commands/version.html)

## Draft Notes

- Capture current version, target version, platform, install method, and affected resources.
- Review release differences before scheduling the change.
- Flag any unverified mixed-version state as a risk, not as supported behavior.
