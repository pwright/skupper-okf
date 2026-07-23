---
type: DocumentationLandscapePage
title: "Choose a Test Service"
id: service-selection
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/service-selection
tags:
  - skupper
  - docs-landscape
  - get-started
timestamp: 2026-07-23T19:49:37Z
---

# Choose a Test Service

Choose a Test Service helps new users pick a small workload for their first Skupper validation. The current local examples support a simple frontend/backend HTTP path and a larger gRPC scenario; the starter page should begin with the simpler service shape.

## Appears in

- [Get Started with Skupper](./get-started.md) / Starter Setup

## Sources

- [Skupper example applications](../workflows/skupper-examples.md): Generated local source comparing the Hello World and gRPC examples and identifying Hello World as the minimal pattern.
- [Skupper Hello World source entry](../../sources/skupper-example-hello-world.md): Local source record for the Hello World example snapshot.
- [Service exposure with the CLI](../../human/skupper-docs/input/kube-cli/service-exposure.md): Local source that uses a backend deployment example when creating a connector.
- [Connector concept](../../human/skupper-docs/input/refdog/concepts/connector.md): Local concept source for the workload side of service exposure.
- [Listener concept](../../human/skupper-docs/input/refdog/concepts/listener.md): Local concept source for the client-facing side of service exposure.

## Website Links

- [Skupper Hello World example](https://github.com/skupperproject/skupper-example-hello-world)
- [Skupper examples](https://skupper.io/examples/index.html)
- [Exposing services with the Skupper CLI](https://skupper.io/docs/kube-cli/service-exposure.html)

## Draft Notes

- Prefer a service with an obvious request/response test and minimal infrastructure dependencies.
- Capture service name, port, namespace, and expected client command before exposing it.
- Use the gRPC example later when the starter path needs a richer multi-service validation.
