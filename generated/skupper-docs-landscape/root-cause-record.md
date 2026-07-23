---
type: DocumentationLandscapePage
title: "Root Cause Record"
id: root-cause-record
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/root-cause-record
tags:
  - skupper
  - docs-landscape
  - troubleshoot
related:
  - fault-isolation
  - evidence-bundle
timestamp: 2026-07-23T21:15:00Z
---

# Root Cause Record

A root cause record captures the diagnosed cause of a Skupper incident, the evidence supporting it, the affected resources, and the follow-up actions needed to prevent recurrence.

## Appears in

- [Troubleshoot Skupper](./troubleshoot-skupper.md) / Diagnostic Workflow

## Dependencies

- [Fault Isolation](./fault-isolation.md)
- [Logs, Events, Metrics, and Configuration](./evidence-bundle.md)

## Sources

- [human/skupper-docs/input/troubleshooting/index.md](../../human/skupper-docs/input/troubleshooting/index.md) - Local troubleshooting guide for diagnostic evidence and checks.
- [human/skupper-docs/input/refdog/commands/debug/dump.md](../../human/skupper-docs/input/refdog/commands/debug/dump.md) - Debug dump command reference.
- [generated/concepts/network-observer-api.md](../concepts/network-observer-api.md) - Generated source for observer evidence from services, connections, and flows.
- [generated/skupper-console/console.md](../skupper-console/console.md) - Generated source for console errors, traffic views, and API behavior.
- [generated/skupper-docs-landscape/evidence-bundle.md](./evidence-bundle.md) - Related landscape page for evidence collection.

## Website Links

- [Troubleshooting](https://skupper.io/docs/troubleshooting/index.html)
- [Debug dump command](https://skupperproject.github.io/refdog/commands/debug/dump.html)
- [Network console](https://skupper.io/docs/console/index.html)
- [Skupper console repository](https://github.com/skupperproject/skupper-console)

## Draft Notes

- Use this page as a template for incident documentation rather than a troubleshooting command reference.
- Include timeline, observed symptom, isolated layer, changed resources, validation evidence, and corrective actions.
- Keep unproven hypotheses separate from confirmed root cause.
