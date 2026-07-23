---
type: DocumentationLandscapePage
title: "Fault Isolation"
id: fault-isolation
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/fault-isolation
tags:
  - skupper
  - docs-landscape
  - troubleshoot
related:
  - symptom-capture
  - layered-checks
timestamp: 2026-07-23T21:15:00Z
---

# Fault Isolation

Fault isolation narrows a Skupper problem from a broad symptom to the layer most likely responsible: site, link, route, service exposure, workload, observer, or platform.

## Appears in

- [Troubleshoot Skupper](./troubleshoot-skupper.md) / Diagnostic Workflow

## Dependencies

- [Symptom Capture](./symptom-capture.md)
- [Site, Link, Route, and Service Checks](./layered-checks.md)

## Sources

- [human/skupper-docs/input/troubleshooting/index.md](../../human/skupper-docs/input/troubleshooting/index.md) - Local troubleshooting source for layered diagnostic checks.
- [human/skupper-docs/input/refdog/commands/debug/check.md](../../human/skupper-docs/input/refdog/commands/debug/check.md) - Debug check command reference.
- [generated/concepts/listener.md](../concepts/listener.md) - Generated source for listener readiness and matching signals.
- [generated/concepts/connector.md](../concepts/connector.md) - Generated source for connector readiness and matching signals.
- [generated/concepts/routing-key.md](../concepts/routing-key.md) - Generated source for routing-key matching and service status.

## Website Links

- [Troubleshooting](https://skupper.io/docs/troubleshooting/index.html)
- [Debug check command](https://skupperproject.github.io/refdog/commands/debug/check.html)
- [Listener command reference](https://skupperproject.github.io/refdog/commands/listener/status.html)
- [Connector command reference](https://skupperproject.github.io/refdog/commands/connector/status.html)

## Draft Notes

- Organize future content as a decision tree from symptom to evidence to next check.
- Include routing-key mismatch as a common service-layer isolation path.
- Keep remediation out of this page except for links to the appropriate recovery procedure.
