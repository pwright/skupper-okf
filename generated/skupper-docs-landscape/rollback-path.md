---
type: DocumentationLandscapePage
title: "Rollback Path"
id: rollback-path
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/rollback-path
tags:
  - skupper
  - docs-landscape
  - migrate
timestamp: 2026-07-23T20:07:08Z
---

# Rollback Path

Rollback Path defines how a migration wave can return traffic to the source deployment if validation fails. Source coverage is mostly indirect, so this page should capture prerequisites, triggers, and evidence rather than promising product-managed rollback behavior.

## Appears in

- [Migrate to or Between Skupper Deployments](./migrate-skupper.md) / Migration Readiness

## Sources

- [Skupper load balancing and failover](../../human/skupper-docs/input/overview/load-balancing.md): Local source for failover behavior and the stateful-application orchestration caveat.
- [Troubleshooting guide](../../human/skupper-docs/input/troubleshooting/index.md): Local source for identifying failed site, link, or service status.
- [Source Deployment Assessment](./source-assessment.md): Local landscape source for preserving source-state evidence.
- [Configuration and State Backup](./backup-state.md): Local landscape source for backup expectations.
- [Rollback Plan](./rollback-plan.md): Local landscape source for upgrade rollback planning patterns that can inform migration rollback.

## Website Links

- [Skupper load balancing and failover](https://skupper.io/docs/overview/load-balancing.html)
- [Skupper troubleshooting guide](https://skupper.io/docs/troubleshooting/index.html)
- [Refdog resource reference](https://skupperproject.github.io/refdog/resources/index.html)

## Draft Notes

- Define rollback triggers before cutover starts.
- Keep source connectivity intact until acceptance criteria are met, where possible.
- For stateful services, coordinate rollback outside Skupper if ordering or data consistency matters.
