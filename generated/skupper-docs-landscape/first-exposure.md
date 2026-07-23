---
type: DocumentationLandscapePage
title: "Expose a Service"
id: first-exposure
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/first-exposure
tags:
  - skupper
  - docs-landscape
  - get-started
related:
  - first-sites
  - service-selection
timestamp: 2026-07-23T19:49:37Z
---

# Expose a Service

Expose a Service covers the starter step where an application endpoint becomes available through the Skupper application network. In the current local docs, the CLI path uses connectors and listeners matched by routing key, so this page should teach the minimal pairing needed for a first working service.

## Appears in

- [Get Started with Skupper](./get-started.md) / Starter Workflow

## Dependencies

- [Create Two Sites](./first-sites.md)
- [Choose a Test Service](./service-selection.md)

## Sources

- [Service exposure with the CLI](../../human/skupper-docs/input/kube-cli/service-exposure.md): Primary local source for creating connectors and listeners and checking their status.
- [Connector create command](../../human/skupper-docs/input/refdog/commands/connector/create.md): Local command reference for creating a connector to a local workload or host/port.
- [Listener create command](../../human/skupper-docs/input/refdog/commands/listener/create.md): Local command reference for creating a listener endpoint for clients.
- [Connector concept](../../human/skupper-docs/input/refdog/concepts/connector.md): Local concept source for connector behavior.
- [Listener concept](../../human/skupper-docs/input/refdog/concepts/listener.md): Local concept source for listener behavior.

## Website Links

- [Exposing services with the Skupper CLI](https://skupper.io/docs/kube-cli/service-exposure.html)
- [Refdog connector create command](https://skupperproject.github.io/refdog/commands/connector/create.html)
- [Refdog listener create command](https://skupperproject.github.io/refdog/commands/listener/create.html)

## Draft Notes

- Use one simple workload and one listener/connector pair for the first draft.
- Explain routing keys only as far as needed to match the listener and connector.
- Include status checks that confirm a matching listener or connector exists before moving to application validation.
