---
type: DocumentationLandscapePage
title: "Topology Analysis"
id: topology-analysis
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/topology-analysis
tags:
  - skupper
  - docs-landscape
  - optimize
timestamp: 2026-07-23T21:00:00Z
---

# Topology Analysis

Topology analysis identifies the sites, links, service endpoints, and traffic paths that affect performance and reliability.

## Appears in

- [Optimize Skupper](./optimize-skupper.md) / Analysis Inputs

## Sources

- [generated/concepts/network-deployment-concerns.md](../concepts/network-deployment-concerns.md) - Generated source for site links, link access, and topology considerations.
- [generated/concepts/network-observer-api.md](../concepts/network-observer-api.md) - Generated source for observer topology and connection data.
- [generated/skupper-console/console.md](../skupper-console/console.md) - Generated source for console topology views.
- [human/skupper-docs/input/refdog/concepts/link.md](../../human/skupper-docs/input/refdog/concepts/link.md) - Link concept source.
- [human/skupper-docs/input/refdog/topics/large-networks.md](../../human/skupper-docs/input/refdog/topics/large-networks.md) - Large-network source candidate.

## Website Links

- [Network console](https://skupper.io/docs/console/index.html)
- [Link concept](https://skupperproject.github.io/refdog/concepts/link.html)
- [Large networks topic](https://skupperproject.github.io/refdog/topics/large-networks.html)
- [Skupper console repository](https://github.com/skupperproject/skupper-console)

## Draft Notes

- Start with a current topology inventory before recommending route or resource changes.
- Capture both configured topology and observed traffic topology; they can differ during partial outages.
- Add a future diagram template for site, link, listener, connector, and workload placement.
