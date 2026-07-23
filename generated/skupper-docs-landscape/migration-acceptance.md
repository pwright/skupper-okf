---
type: DocumentationLandscapePage
title: "Migration Acceptance"
id: migration-acceptance
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/migration-acceptance
tags:
  - skupper
  - docs-landscape
  - migrate
related:
  - migrated-connectivity
  - acceptance-tests
timestamp: 2026-07-23T20:07:08Z
---

# Migration Acceptance

Migration Acceptance is the formal checkpoint where the migrated connectivity is accepted by application and platform owners. It should combine Skupper health checks, traffic validation, known limitations, and rollback decision status.

## Appears in

- [Migrate to or Between Skupper Deployments](./migrate-skupper.md) / Migration Outcome

## Dependencies

- [Migrated Application Connectivity](./migrated-connectivity.md)
- [Acceptance Tests](./acceptance-tests.md)

## Sources

- [Troubleshooting guide](../../human/skupper-docs/input/troubleshooting/index.md): Primary local source for operational validation commands.
- [Skupper example applications](../workflows/skupper-examples.md): Generated local source for application-level connectivity tests.
- [Network Observer API concept](../concepts/network-observer-api.md): Generated local source for runtime state, services, connections, and traffic-flow visibility.
- [Migrating from Skupper v1](../../human/skupper-docs/input/overview/migrating.md): Local source for migration-specific terminology and constraints.
- [Acceptance Tests](./acceptance-tests.md): Local landscape source for the test suite that gates acceptance.

## Website Links

- [Skupper troubleshooting guide](https://skupper.io/docs/troubleshooting/index.html)
- [Migrating from Skupper v1](https://skupper.io/docs/overview/migrating.html)
- [Skupper examples](https://skupper.io/examples/index.html)

## Draft Notes

- Capture who accepts the migration and which evidence they reviewed.
- Include rollback status: still available, no longer available, or no rollback path.
- Keep unresolved deviations visible rather than folding them into a generic success statement.
