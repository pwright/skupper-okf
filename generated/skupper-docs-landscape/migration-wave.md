---
type: DocumentationLandscapePage
title: "Migration Waves"
id: migration-wave
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/migration-wave
tags:
  - skupper
  - docs-landscape
  - migrate
related:
  - source-assessment
  - target-design
timestamp: 2026-07-23T20:07:08Z
---

# Migration Waves

Migration Waves break a migration into manageable groups of sites, services, or traffic paths. Local sources do not define a formal wave model, so this page should frame waves as a practical planning device built from source assessment, target design, validation, and rollback readiness.

## Appears in

- [Migrate to or Between Skupper Deployments](./migrate-skupper.md) / Migration Execution

## Dependencies

- [Source Deployment Assessment](./source-assessment.md)
- [Target Deployment Design](./target-design.md)

## Sources

- [Migrating from Skupper v1](../../human/skupper-docs/input/overview/migrating.md): Local source for migration constraints and command changes.
- [Network deployment concerns](../concepts/network-deployment-concerns.md): Generated local source for sites, links, service exposure, traffic direction, and validation checks.
- [Target Application Network Topology](./target-topology.md): Local landscape source for target site and traffic design.
- [Application and Service Inventory](./application-inventory.md): Local landscape source for selecting service groups.
- [Rollout Plan](./rollout-plan.md): Local landscape source for staged execution concepts.

## Website Links

- [Migrating from Skupper v1](https://skupper.io/docs/overview/migrating.html)
- [Skupper connectivity overview](https://skupper.io/docs/overview/connectivity.html)
- [Skupper service exposure guide](https://skupper.io/docs/kube-cli/service-exposure.html)

## Draft Notes

- Define each wave by services, sites, owners, validation tests, and rollback path.
- Start with a low-risk service path before migrating critical or stateful flows.
- Keep wave boundaries small enough that failures can be isolated.
