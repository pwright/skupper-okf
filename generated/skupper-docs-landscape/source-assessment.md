---
type: DocumentationLandscapePage
title: "Source Deployment Assessment"
id: source-assessment
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/source-assessment
tags:
  - skupper
  - docs-landscape
  - migrate
timestamp: 2026-07-23T20:07:08Z
---

# Source Deployment Assessment

Source Deployment Assessment records the current application-network design, versions, sites, links, exposed services, operational owners, and validation signals before a migration begins. For v1-to-v2 migration, it must also capture terminology and command differences.

## Appears in

- [Migrate to or Between Skupper Deployments](./migrate-skupper.md) / Migration Readiness

## Sources

- [Migrating from Skupper v1](../../human/skupper-docs/input/overview/migrating.md): Primary local source for v1 compatibility limits and command changes.
- [Troubleshooting guide](../../human/skupper-docs/input/troubleshooting/index.md): Local source for collecting current site, link, connector, and listener status.
- [Skupper API resources](../../human/skupper-docs/input/refdog/resources/index.md): Local source for desired-state resources and platform differences.
- [Application and Service Inventory](./application-inventory.md): Local landscape source for cataloging services and consumers.
- [Site Inventory](./site-inventory.md): Local landscape source for cataloging source sites and environments.

## Website Links

- [Migrating from Skupper v1](https://skupper.io/docs/overview/migrating.html)
- [Skupper troubleshooting guide](https://skupper.io/docs/troubleshooting/index.html)
- [Refdog resource reference](https://skupperproject.github.io/refdog/resources/index.html)

## Draft Notes

- Capture current commands, resources, versions, and traffic paths before changing anything.
- For v1 sources, map service sync or expose behavior to v2 connector/listener/routing-key concepts.
- Identify unsupported or unknown source behavior explicitly.
