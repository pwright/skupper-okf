---
type: DocumentationLandscapePage
title: "Network Health View"
id: network-health-view
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/network-health-view
tags:
  - skupper
  - docs-landscape
  - observe
related:
  - site-metrics
  - link-metrics
  - service-metrics
timestamp: 2026-07-23T20:45:00Z
---

# Network Health View

A network health view combines site, link, and service signals so operators can see whether the Skupper application network is connected and carrying the expected traffic.

## Appears in

- [Observe Skupper](./observe-skupper.md) / Operational Visibility

## Dependencies

- [Site Metrics](./site-metrics.md)
- [Link Metrics](./link-metrics.md)
- [Service Metrics](./service-metrics.md)

## Sources

- [generated/concepts/network-observer-api.md](../concepts/network-observer-api.md) - Generated source for observer API resources, topology, services, connections, and flows.
- [generated/skupper-console/console.md](../skupper-console/console.md) - Generated source describing console API calls and metrics queries.
- [human/skupper-docs/input/console/index.md](../../human/skupper-docs/input/console/index.md) - Local documentation for installing and using the network console.
- [human/skupper-docs/input/troubleshooting/index.md](../../human/skupper-docs/input/troubleshooting/index.md) - Local troubleshooting source for status and diagnostic workflows.
- [human/skupper-docs/input/refdog/topics/resource-status.md](../../human/skupper-docs/input/refdog/topics/resource-status.md) - Local source candidate for resource readiness and conditions.

## Website Links

- [Network console](https://skupper.io/docs/console/index.html)
- [Troubleshooting](https://skupper.io/docs/troubleshooting/index.html)
- [Resource status topic](https://skupperproject.github.io/refdog/topics/resource-status.html)
- [Skupper console repository](https://github.com/skupperproject/skupper-console)

## Draft Notes

- Expand into a triage page that starts with site health, then link health, then exposed service readiness.
- Keep console UI details separate from API-backed signal definitions.
- Add example checks only where the source docs provide stable commands or endpoints.
