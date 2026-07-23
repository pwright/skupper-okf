---
type: DocumentationLandscapePage
title: "Site Upgrade Sequence"
id: upgrade-sequence
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/upgrade-sequence
tags:
  - skupper
  - docs-landscape
  - upgrade
related:
  - compatibility-review
  - maintenance-plan
timestamp: 2026-07-23T20:03:45Z
---

# Site Upgrade Sequence

Site Upgrade Sequence describes the order in which sites and components should be upgraded. Local sources do not provide a full multi-site sequencing policy, so this page should capture a practical plan: review compatibility, schedule maintenance, upgrade a limited scope, validate, then continue.

## Appears in

- [Upgrade Skupper](./upgrade-skupper.md) / Upgrade Execution

## Dependencies

- [Compatibility Review](./compatibility-review.md)
- [Maintenance and Communication Plan](./maintenance-plan.md)

## Sources

- [Skupper installation guide](../../human/skupper-docs/input/install/index.md): Local source for controller and local-site upgrade mechanisms.
- [Network deployment concerns](../concepts/network-deployment-concerns.md): Generated local source for sites, links, validation checks, and operational concerns.
- [Troubleshooting guide](../../human/skupper-docs/input/troubleshooting/index.md): Local source for validation checks between upgrade stages.
- [Version Compatibility](./version-compatibility.md): Local landscape source candidate for allowed version combinations.
- [Release Differences](./release-differences.md): Local landscape source candidate for behavior changes that affect sequencing.

## Website Links

- [Skupper installation docs](https://skupper.io/docs/install/index.html)
- [Skupper troubleshooting guide](https://skupper.io/docs/troubleshooting/index.html)
- [Skupper releases](https://skupper.io/releases/index.html)

## Draft Notes

- Start with a small, observable scope before upgrading every site.
- Record planned pauses and validation gates after each component or site group.
- Do not imply a universal safe order until supported by explicit release or upgrade guidance.
