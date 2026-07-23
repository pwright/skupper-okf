---
type: DocumentationLandscapePage
title: "New Service Reachable"
id: new-service-reachable
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/new-service-reachable
tags:
  - skupper
  - docs-landscape
  - extend
related:
  - new-site-connected
  - service-onboarding
timestamp: 2026-07-23T20:01:23Z
---

# New Service Reachable

New Service Reachable is the expansion outcome where a service has been added to the application network and can be consumed from the intended site or sites. The page should connect service definition, routing policy, and validation status.

## Appears in

- [Extend a Skupper Application Network](./extend-skupper.md) / Expansion Outcomes

## Dependencies

- [New Site Connected](./new-site-connected.md)
- [Onboard a Service](./service-onboarding.md)

## Sources

- [Service exposure with the CLI](../../human/skupper-docs/input/kube-cli/service-exposure.md): Primary local source for creating connectors and listeners and checking their status.
- [Connector concept](../concepts/connector.md): Generated local concept source for exposing workloads to the application network.
- [Listener concept](../concepts/listener.md): Generated local concept source for client-facing endpoints.
- [Routing key concept](../concepts/routing-key.md): Generated local concept source for listener/connector matching and service binding.
- [Skupper example applications](../workflows/skupper-examples.md): Generated local examples for validating service reachability across sites.

## Website Links

- [Skupper service exposure guide](https://skupper.io/docs/kube-cli/service-exposure.html)
- [Refdog connector concept](https://skupperproject.github.io/refdog/concepts/connector.html)
- [Refdog listener concept](https://skupperproject.github.io/refdog/concepts/listener.html)

## Draft Notes

- Define reachability in user terms: which client reaches which service endpoint.
- Require a matching listener and connector before declaring the service available.
- Record routing key, host, port, and validation command for each onboarded service.
