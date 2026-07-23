---
type: DocumentationLandscapePage
title: "Acceptance Tests"
id: acceptance-tests
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/acceptance-tests
tags:
  - skupper
  - docs-landscape
  - migrate
timestamp: 2026-07-23T20:07:08Z
---

# Acceptance Tests

Acceptance Tests are the checks that prove a migration wave is ready to be accepted. They should include Skupper status checks, service binding checks, application requests, and any observer or metrics evidence needed for the migrated traffic path.

## Appears in

- [Migrate to or Between Skupper Deployments](./migrate-skupper.md) / Migration Readiness

## Sources

- [Troubleshooting guide](../../human/skupper-docs/input/troubleshooting/index.md): Primary local source for site, link, connector, and listener status checks.
- [Connector status command](../../human/skupper-docs/input/refdog/commands/connector/status.md): Local command reference for connector validation.
- [Listener status command](../../human/skupper-docs/input/refdog/commands/listener/status.md): Local command reference for listener validation.
- [Network Observer API concept](../concepts/network-observer-api.md): Generated local source for runtime and traffic-flow visibility.
- [Skupper example applications](../workflows/skupper-examples.md): Generated local source for application-level validation patterns.

## Website Links

- [Skupper troubleshooting guide](https://skupper.io/docs/troubleshooting/index.html)
- [Refdog connector status command](https://skupperproject.github.io/refdog/commands/connector/status.html)
- [Refdog listener status command](https://skupperproject.github.io/refdog/commands/listener/status.html)

## Draft Notes

- Reuse the same acceptance tests before migration, during parallel run, and after cutover.
- Include both control-plane status and application-level traffic checks.
- Store expected outputs and owner signoff with the migration wave record.
