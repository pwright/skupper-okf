---
type: DocumentationLandscapePage
title: "Site Operations"
id: site-operations
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/site-operations
tags:
  - skupper
  - docs-landscape
  - administer
related:
  - site-status
  - site-configuration
timestamp: 2026-07-23T20:10:12Z
---

# Site Operations

Site Operations covers recurring administration of Skupper sites: checking readiness, reviewing configuration, updating site settings, and collecting diagnostic evidence when site state is unexpected.

## Appears in

- [Administer Skupper](./administer-skupper.md) / Administrative Workflows

## Dependencies

- [Site Status](./site-status.md)
- [Site Configuration](./site-configuration.md)

## Sources

- [Site configuration with the CLI](../../human/skupper-docs/input/kube-cli/site-configuration.md): Local source for site create, update, HA, status, and delete workflows.
- [Site status command](../../human/skupper-docs/input/refdog/commands/site/status.md): Local command reference for checking site state.
- [Site resource](../../human/skupper-docs/input/refdog/resources/site.md): Local resource reference for declarative site configuration and status.
- [Troubleshooting guide](../../human/skupper-docs/input/troubleshooting/index.md): Primary local source for checking sites, links, connectors, listeners, and collecting debug evidence.
- [Network deployment concerns](../concepts/network-deployment-concerns.md): Generated local source for operational checks, link constraints, resources, and traffic direction.

## Website Links

- [Creating a site with the Skupper CLI](https://skupper.io/docs/kube-cli/site-configuration.html)
- [Refdog site resource](https://skupperproject.github.io/refdog/resources/site.html)
- [Refdog site status command](https://skupperproject.github.io/refdog/commands/site/status.html)

## Draft Notes

- Separate routine status checks from configuration changes.
- Record namespace, platform, and controller scope when documenting site operations.
- Use debug dumps for support evidence instead of manually copying partial state.
