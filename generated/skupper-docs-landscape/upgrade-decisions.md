---
type: DocumentationLandscapePage
title: "Upgrade Decisions"
id: upgrade-decisions
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/upgrade-decisions
tags:
  - skupper
  - docs-landscape
  - whats-new
related:
  - behavior-changes
  - deprecations
timestamp: 2026-07-23T19:40:56Z
---

# Upgrade Decisions

Upgrade decisions convert release information into a go/no-go assessment for a specific Skupper deployment. The page should summarize why a team would upgrade now, what compatibility or deprecation risks exist, and what validation evidence is needed before rollout.

## Appears in

- [What's New in Skupper](./skupper-whats-new.md) / Adoption Impact

## Dependencies

- [Behavior Changes](./behavior-changes.md)
- [Deprecations](./deprecations.md)

## Sources

- [Behavior changes](./behavior-changes.md): Input for expected workflow and runtime differences.
- [Deprecations](./deprecations.md): Input for features, APIs, or procedures that may need replacement.
- [Install guide upgrade section](../../human/skupper-docs/input/install/index.md#skupper-upgrading-sites): Local source for site upgrade flow.
- [Console upgrade section](../../human/skupper-docs/input/console/index.md#console-upgrade): Local source for Network Observer upgrade and rollback flow.

## Website Links

- [Skupper releases](https://skupper.io/releases/index.html)
- [GitHub releases](https://github.com/skupperproject/skupper/releases)

## Draft Notes

- Treat the decision as deployment-specific: platform, topology, automation, security policy, and support window all matter.
- Capture rollback readiness alongside upgrade benefits.
