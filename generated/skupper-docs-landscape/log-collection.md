---
type: DocumentationLandscapePage
title: "Log Collection"
id: log-collection
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/log-collection
tags:
  - skupper
  - docs-landscape
  - observe
timestamp: 2026-07-23T20:45:00Z
---

# Log Collection

Log collection gathers Skupper component, observer, and related platform logs for troubleshooting and post-incident analysis.

## Appears in

- [Observe Skupper](./observe-skupper.md) / Collection and Presentation

## Sources

- [human/skupper-docs/input/troubleshooting/index.md](../../human/skupper-docs/input/troubleshooting/index.md) - Local troubleshooting source for logs and debug bundles.
- [human/skupper-docs/input/console/configuration.md](../../human/skupper-docs/input/console/configuration.md) - Local observer configuration source including logging profile options.
- [generated/skupper-console/console.md](../skupper-console/console.md) - Generated source for console errors and API behavior.
- [generated/concepts/network-observer-api.md](../concepts/network-observer-api.md) - Generated source for observer API behavior.
- [generated/skupper-docs-landscape/logging-interface.md](./logging-interface.md) - Related landscape page for logging interfaces.

## Website Links

- [Troubleshooting](https://skupper.io/docs/troubleshooting/index.html)
- [Network console configuration](https://skupper.io/docs/console/configuration.html)
- [Network console](https://skupper.io/docs/console/index.html)
- [Skupper console repository](https://github.com/skupperproject/skupper-console)

## Draft Notes

- Separate routine log collection from emergency debug capture.
- Document platform-specific commands only after confirming Kubernetes, Podman, Docker, and Linux differences.
- Add guidance for redacting secrets and endpoint details before sharing debug bundles.
