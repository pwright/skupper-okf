---
type: DocumentationLandscapePage
title: "Symptom Capture"
id: symptom-capture
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/symptom-capture
tags:
  - skupper
  - docs-landscape
  - troubleshoot
timestamp: 2026-07-23T21:15:00Z
---

# Symptom Capture

Symptom capture records what failed, when it failed, which application or Skupper resources were affected, and what evidence is available before changes are made.

## Appears in

- [Troubleshoot Skupper](./troubleshoot-skupper.md) / Diagnostic Evidence

## Sources

- [human/skupper-docs/input/troubleshooting/index.md](../../human/skupper-docs/input/troubleshooting/index.md) - Local troubleshooting source for collecting diagnostic context.
- [generated/concepts/network-observer-api.md](../concepts/network-observer-api.md) - Generated source for observable services, connections, and flows.
- [generated/skupper-console/console.md](../skupper-console/console.md) - Generated source for console errors, traffic views, and time-series queries.
- [human/skupper-docs/input/console/index.md](../../human/skupper-docs/input/console/index.md) - Local source for using the network console.
- [generated/skupper-docs-landscape/runtime-logs.md](./runtime-logs.md) - Related landscape page for runtime log evidence.

## Website Links

- [Troubleshooting](https://skupper.io/docs/troubleshooting/index.html)
- [Network console](https://skupper.io/docs/console/index.html)
- [Skupper console repository](https://github.com/skupperproject/skupper-console)
- [Skupper project](https://skupper.io/)

## Draft Notes

- Capture the first failing request, expected route, affected sites, and recent changes.
- Record whether the symptom is total outage, partial outage, latency, incorrect destination, or missing observability.
- Avoid changing resources before capturing enough evidence to compare post-remediation behavior.
