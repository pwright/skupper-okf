---
type: DocumentationLandscapePage
title: "Logs, Events, Metrics, and Configuration"
id: evidence-bundle
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/evidence-bundle
tags:
  - skupper
  - docs-landscape
  - troubleshoot
timestamp: 2026-07-23T21:15:00Z
---

# Logs, Events, Metrics, and Configuration

An evidence bundle gathers the logs, events, metrics, status output, and Skupper configuration needed to diagnose or escalate a problem.

## Appears in

- [Troubleshoot Skupper](./troubleshoot-skupper.md) / Diagnostic Evidence

## Sources

- [human/skupper-docs/input/troubleshooting/index.md](../../human/skupper-docs/input/troubleshooting/index.md) - Local troubleshooting source for diagnostic collection.
- [human/skupper-docs/input/refdog/commands/debug/dump.md](../../human/skupper-docs/input/refdog/commands/debug/dump.md) - Debug dump command reference.
- [human/skupper-docs/input/console/configuration.md](../../human/skupper-docs/input/console/configuration.md) - Local source for observer metrics, logs, and persistence settings.
- [generated/skupper-console/console.md](../skupper-console/console.md) - Generated source for console data, metrics, and error behavior.
- [generated/concepts/network-observer-api.md](../concepts/network-observer-api.md) - Generated source for observer API evidence.

## Website Links

- [Troubleshooting](https://skupper.io/docs/troubleshooting/index.html)
- [Debug dump command](https://skupperproject.github.io/refdog/commands/debug/dump.html)
- [Network console configuration](https://skupper.io/docs/console/configuration.html)
- [Network console](https://skupper.io/docs/console/index.html)

## Draft Notes

- Include redaction guidance for tokens, certificates, endpoints, and application identifiers before sharing bundles.
- Separate automatically collected debug dumps from manually captured metrics and console screenshots.
- Record the exact timestamp and topology state for every evidence bundle.
