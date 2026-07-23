---
type: DocumentationLandscapePage
title: "Connected Service Across Sites"
id: first-connected-service
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/first-connected-service
tags:
  - skupper
  - docs-landscape
  - get-started
related:
  - first-sites
  - first-link
  - first-exposure
timestamp: 2026-07-23T19:49:37Z
---

# Connected Service Across Sites

Connected Service Across Sites is the starter outcome: a user has two Skupper sites, a link between them, and a service that can be reached through the application network. This page should stay focused on the end-to-end success path and point deeper setup, linking, and exposure details to the dependency topics.

## Appears in

- [Get Started with Skupper](./get-started.md) / First Working Network

## Dependencies

- [Create Two Sites](./first-sites.md)
- [Link the Sites](./first-link.md)
- [Expose a Service](./first-exposure.md)

## Sources

- [Kubernetes CLI overview](../../human/skupper-docs/input/kube-cli/index.md): Local source that frames the starter CLI flow as site creation, site linking, and service exposure.
- [Site configuration with the CLI](../../human/skupper-docs/input/kube-cli/site-configuration.md): Local source for creating a site before the network can carry application traffic.
- [Site linking with the CLI](../../human/skupper-docs/input/kube-cli/site-linking.md): Local source for linking sites and confirming link status before exposing services.
- [Service exposure with the CLI](../../human/skupper-docs/input/kube-cli/service-exposure.md): Local source for using connectors and listeners after sites are linked.
- [Skupper example applications](../workflows/skupper-examples.md): Generated local source showing Hello World and gRPC examples as connected application scenarios.

## Website Links

- [Skupper Kubernetes CLI overview](https://skupper.io/docs/kube-cli/index.html)
- [Skupper Hello World example](https://github.com/skupperproject/skupper-example-hello-world)
- [Skupper examples](https://skupper.io/examples/index.html)

## Draft Notes

- Keep this page outcome-oriented; avoid duplicating every command from the setup pages.
- Include a small success checklist: both sites ready, link ready, listener and connector matched, and application request succeeds.
- Use Hello World as the first example unless a broader multi-service walkthrough is needed.
