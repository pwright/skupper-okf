---
type: DocumentationLandscapePage
title: "Site Status"
id: site-status
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/site-status
tags:
  - skupper
  - docs-landscape
  - administer
timestamp: 2026-07-23T20:10:12Z
---

# Site Status

Site Status records whether a Skupper site is configured, ready, and running in the expected namespace or local-system context. It is the first operational check before investigating links or services.

## Appears in

- [Administer Skupper](./administer-skupper.md) / Operational State

## Sources

- [Site status command](../../human/skupper-docs/input/refdog/commands/site/status.md): Primary local command reference for site status.
- [Troubleshooting guide](../../human/skupper-docs/input/troubleshooting/index.md): Primary local source for checking sites, links, connectors, listeners, and collecting debug evidence.
- [Site resource](../../human/skupper-docs/input/refdog/resources/site.md): Local resource reference for status fields.
- [Network deployment concerns](../concepts/network-deployment-concerns.md): Generated local source for operational checks, link constraints, resources, and traffic direction.
- [Site concept](../../human/skupper-docs/input/refdog/concepts/site.md): Local concept source for site meaning and platform association.

## Website Links

- [Refdog site status command](https://skupperproject.github.io/refdog/commands/site/status.html)
- [Skupper troubleshooting guide](https://skupper.io/docs/troubleshooting/index.html)
- [Refdog site resource](https://skupperproject.github.io/refdog/resources/site.html)

## Draft Notes

- Capture command output with namespace and platform context.
- On Kubernetes, pair CLI status with resource status when diagnosing issues.
- Check controller state when site status fails unexpectedly.
