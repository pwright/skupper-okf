---
type: DocumentationLandscapePage
title: "Traffic Flow Requirements"
id: traffic-flows
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/traffic-flows
tags:
  - skupper
  - docs-landscape
  - plan
related:
  - application-inventory
timestamp: 2026-07-23T19:54:51Z
---

# Traffic Flow Requirements

Traffic Flow Requirements records which application clients need to reach which services, from which sites, and over which ports or protocols. For Skupper planning, this becomes the basis for listener, connector, routing-key, and link-path decisions.

## Appears in

- [Plan a Skupper Deployment](./plan-skupper.md) / Requirements and Constraints

## Dependencies

- [Application and Service Inventory](./application-inventory.md)

## Sources

- [Connector concept](../concepts/connector.md): Generated local concept source for exposing local workloads to remote listeners.
- [Listener concept](../concepts/listener.md): Generated local concept source for client-facing endpoints and routing-key matching.
- [Routing key concept](../concepts/routing-key.md): Generated local concept source for how listeners and connectors match service traffic.
- [Service exposure with the CLI](../../human/skupper-docs/input/kube-cli/service-exposure.md): Local source for connector/listener examples and status checks.
- [Network deployment concerns](../concepts/network-deployment-concerns.md): Generated local source for traffic direction, link cost, and multi-key listener planning.

## Website Links

- [Skupper service exposure guide](https://skupper.io/docs/kube-cli/service-exposure.html)
- [Refdog connector concept](https://skupperproject.github.io/refdog/concepts/connector.html)
- [Refdog listener concept](https://skupperproject.github.io/refdog/concepts/listener.html)

## Draft Notes

- Inventory each required service as client site, server site, service name, port, and routing-key candidate.
- Identify traffic that needs failover or weighted distribution separately from simple reachability.
- Do not assume all network paths need Skupper; document why each flow belongs in the application network.
