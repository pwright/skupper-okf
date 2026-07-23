---
type: DocumentationLandscapePage
title: "Connectivity Validation"
id: first-validation
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/first-validation
tags:
  - skupper
  - docs-landscape
  - get-started
related:
  - first-connected-service
  - basic-observation
timestamp: 2026-07-23T19:49:37Z
---

# Connectivity Validation

Connectivity Validation confirms that the starter Skupper network is doing useful work. It should cover practical checks for site readiness, link readiness, matched service exposure, and an application-level request, while leaving detailed troubleshooting for later maps.

## Appears in

- [Get Started with Skupper](./get-started.md) / First Working Network

## Dependencies

- [Connected Service Across Sites](./first-connected-service.md)
- [Check Network Status](./basic-observation.md)

## Sources

- [Site linking with the CLI](../../human/skupper-docs/input/kube-cli/site-linking.md): Local source for checking `skupper link status` after redeeming a token or applying a link resource.
- [Service exposure with the CLI](../../human/skupper-docs/input/kube-cli/service-exposure.md): Local source for checking connector and listener status and matching routing keys.
- [Site status command](../../human/skupper-docs/input/refdog/commands/site/status.md): Local command reference for checking whether the current site reports ready status.
- [Link status command](../../human/skupper-docs/input/refdog/commands/link/status.md): Local command reference for displaying current site links.
- [Skupper example applications](../workflows/skupper-examples.md): Generated local source for application-level validation examples.

## Website Links

- [Skupper site linking guide](https://skupper.io/docs/kube-cli/site-linking.html)
- [Skupper service exposure guide](https://skupper.io/docs/kube-cli/service-exposure.html)
- [Refdog link status command](https://skupperproject.github.io/refdog/commands/link/status.html)

## Draft Notes

- Separate infrastructure checks from application checks so readers can isolate where validation failed.
- Capture expected ready states conservatively; link and service status can be transient immediately after creation.
- Add example curl or client commands only when sourced from a chosen starter example.
