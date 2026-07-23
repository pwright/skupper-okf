---
type: DocumentationLandscapePage
title: "Migrated Application Connectivity"
id: migrated-connectivity
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/migrated-connectivity
tags:
  - skupper
  - docs-landscape
  - migrate
related:
  - migration-wave
  - cutover
timestamp: 2026-07-23T20:07:08Z
---

# Migrated Application Connectivity

Migrated Application Connectivity is the migration outcome where the intended application traffic has moved to the target Skupper deployment or design while remaining reachable for users. This page should define the accepted end state with evidence from status checks and application-level tests.

## Appears in

- [Migrate to or Between Skupper Deployments](./migrate-skupper.md) / Migration Outcome

## Dependencies

- [Migration Waves](./migration-wave.md)
- [Traffic Cutover](./cutover.md)

## Sources

- [Migrating from Skupper v1](../../human/skupper-docs/input/overview/migrating.md): Primary local source for v1-to-v2 migration constraints and terminology changes.
- [Skupper connectivity overview](../../human/skupper-docs/input/overview/connectivity.md): Local source for the target application-network connectivity model.
- [Service exposure with the CLI](../../human/skupper-docs/input/kube-cli/service-exposure.md): Local source for recreating service reachability using connectors and listeners.
- [Troubleshooting guide](../../human/skupper-docs/input/troubleshooting/index.md): Local source for validating site, link, connector, and listener status.
- [Skupper example applications](../workflows/skupper-examples.md): Generated local source for representative application connectivity validation.

## Website Links

- [Migrating from Skupper v1](https://skupper.io/docs/overview/migrating.html)
- [Skupper connectivity overview](https://skupper.io/docs/overview/connectivity.html)
- [Skupper troubleshooting guide](https://skupper.io/docs/troubleshooting/index.html)

## Draft Notes

- Treat migration success as application reachability plus healthy Skupper status, not simply resource creation.
- Record source and target deployment identifiers so the accepted end state is unambiguous.
- For v1-to-v2 migration, avoid implying in-place compatibility; the local source says to create a new network.
