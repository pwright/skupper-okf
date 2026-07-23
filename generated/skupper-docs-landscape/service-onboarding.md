---
type: DocumentationLandscapePage
title: "Onboard a Service"
id: service-onboarding
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/service-onboarding
tags:
  - skupper
  - docs-landscape
  - extend
related:
  - service-definition
  - routing-policy
timestamp: 2026-07-23T20:01:23Z
---

# Onboard a Service

Onboard a Service describes how to add another application service to the Skupper network after the relevant sites are connected. The current docs frame this as creating connectors for local workloads and listeners for remote consumers, matched by routing key.

## Appears in

- [Extend a Skupper Application Network](./extend-skupper.md) / Expansion Workflow

## Dependencies

- [Service Definition](./service-definition.md)
- [Routing Policy](./routing-policy.md)

## Sources

- [Service exposure with the CLI](../../human/skupper-docs/input/kube-cli/service-exposure.md): Primary local source for connector and listener creation and status checks.
- [Kubernetes YAML service exposure](../../human/skupper-docs/input/kube-yaml/service-exposure.md): Local source candidate for declarative service onboarding.
- [Connector create command](../../human/skupper-docs/input/refdog/commands/connector/create.md): Local command reference for adding a connector.
- [Listener create command](../../human/skupper-docs/input/refdog/commands/listener/create.md): Local command reference for adding a listener.
- [Routing key concept](../concepts/routing-key.md): Generated local source for matching listeners and connectors.

## Website Links

- [Skupper service exposure guide](https://skupper.io/docs/kube-cli/service-exposure.html)
- [Skupper YAML service exposure guide](https://skupper.io/docs/kube-yaml/service-exposure.html)
- [Refdog routing key concept](https://skupperproject.github.io/refdog/concepts/routing-key.html)

## Draft Notes

- Capture service owner approval before publishing a new service endpoint.
- Choose routing keys deliberately so future services do not collide or become ambiguous.
- Add status and application-level checks as part of the onboarding checklist.
