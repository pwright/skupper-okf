---
type: DocumentationLandscapePage
title: "Dual Connectivity Plan"
id: dual-connectivity
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/dual-connectivity
tags:
  - skupper
  - docs-landscape
  - migrate
related:
  - source-assessment
  - target-design
timestamp: 2026-07-23T20:07:08Z
---

# Dual Connectivity Plan

Dual Connectivity Plan describes how source and target connectivity coexist during migration. It should identify which clients and services can use both paths, how routing is separated or controlled, and how status and traffic are observed.

## Appears in

- [Migrate to or Between Skupper Deployments](./migrate-skupper.md) / Migration Readiness

## Dependencies

- [Source Deployment Assessment](./source-assessment.md)
- [Target Deployment Design](./target-design.md)

## Sources

- [Skupper load balancing and failover](../../human/skupper-docs/input/overview/load-balancing.md): Local source for multi-key listener strategies and link cost caveats.
- [Routing key concept](../concepts/routing-key.md): Generated local source for routing-key matching and many-to-many service relationships.
- [Network Observer API concept](../concepts/network-observer-api.md): Generated local source for observing active connections and traffic flows.
- [Skupper Ansible mixed Kubernetes and system workflow](../skupper-ansible/skupper-ansible-workflow-mixed-sites.md): Generated local source for mixed deployment link-resource patterns.
- [Network deployment concerns](../concepts/network-deployment-concerns.md): Generated local source for traffic direction and link planning.

## Website Links

- [Skupper load balancing and failover](https://skupper.io/docs/overview/load-balancing.html)
- [Refdog routing key concept](https://skupperproject.github.io/refdog/concepts/routing-key.html)
- [Skupper network console](https://skupper.io/docs/console/index.html)

## Draft Notes

- Keep source and target routing keys distinct unless intentional overlap has been reviewed.
- Decide whether dual connectivity is production traffic, canary traffic, or validation-only traffic.
- Use observer data where available to confirm which path traffic is actually using.
