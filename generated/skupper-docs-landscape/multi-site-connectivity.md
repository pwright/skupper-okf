---
type: DocumentationLandscapePage
title: "Connect Applications Across Sites"
id: multi-site-connectivity
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/multi-site-connectivity
tags:
  - skupper
  - docs-landscape
  - discover
related:
  - application-network
  - service-exposure
timestamp: 2026-07-23T19:44:12Z
---

# Connect Applications Across Sites

Multi-site connectivity is the user outcome where application components in different clusters, hosts, clouds, or network domains communicate as one application. In Skupper documentation, this topic should explain the value before the implementation details: users can connect services across sites without making private backends publicly reachable.

## Appears in

- [Discover Skupper](./discover-skupper.md) / User Value

## Dependencies

- [Application Network](./application-network.md)
- [Service Exposure](./service-exposure.md)

## Sources

- [Skupper overview](../../human/skupper-docs/input/overview/index.md): Primary local introduction to what Skupper does for distributed applications.
- [Connectivity overview](../../human/skupper-docs/input/overview/connectivity.md): Local source for cross-site connectivity concepts.
- [Application network concept](./application-network.md): Dependency topic that explains the network model.
- [Skupper example applications](../workflows/skupper-examples.md): Generated local examples showing frontend-to-backend and multi-service connectivity across sites.

## Website Links

- [Skupper overview](https://skupper.io/docs/overview/index.html)
- [Skupper examples on GitHub](https://github.com/skupperproject/skupper-example-hello-world)

## Draft Notes

- Frame this as an outcome: application traffic works across sites without a flat network.
- Point readers to service exposure when they need the listener/connector mechanics.
