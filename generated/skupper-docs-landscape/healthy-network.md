---
type: DocumentationLandscapePage
title: "Healthy Application Network"
id: healthy-network
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/healthy-network
tags:
  - skupper
  - docs-landscape
  - administer
related:
  - site-operations
  - link-operations
  - service-operations
timestamp: 2026-07-23T20:10:12Z
---

# Healthy Application Network

Healthy Application Network is the operational outcome where sites, links, and exposed services report usable status and representative application traffic succeeds. This page defines health as observable checks rather than a vague steady state.

## Appears in

- [Administer Skupper](./administer-skupper.md) / Operational Outcomes

## Dependencies

- [Site Operations](./site-operations.md)
- [Link Operations](./link-operations.md)
- [Service Operations](./service-operations.md)

## Sources

- [Troubleshooting guide](../../human/skupper-docs/input/troubleshooting/index.md): Primary local source for checking sites, links, connectors, listeners, and collecting debug evidence.
- [Network deployment concerns](../concepts/network-deployment-concerns.md): Generated local source for operational checks, link constraints, resources, and traffic direction.
- [Network Observer API concept](../concepts/network-observer-api.md): Generated local source for read-only runtime state, services, connections, and traffic flows.
- [Site status command](../../human/skupper-docs/input/refdog/commands/site/status.md): Local command reference for site status.
- [Link status command](../../human/skupper-docs/input/refdog/commands/link/status.md): Local command reference for link status.

## Website Links

- [Skupper troubleshooting guide](https://skupper.io/docs/troubleshooting/index.html)
- [Refdog site status command](https://skupperproject.github.io/refdog/commands/site/status.html)
- [Refdog link status command](https://skupperproject.github.io/refdog/commands/link/status.html)

## Draft Notes

- Define health checks by resource type: site, link, listener, connector, and application request.
- Keep remediation details in troubleshooting pages.
- Include namespace or platform context with every status check.
