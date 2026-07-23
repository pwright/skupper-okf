---
type: DocumentationLandscapePage
title: "Operational Ownership"
id: ownership-model
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/ownership-model
tags:
  - skupper
  - docs-landscape
  - plan
timestamp: 2026-07-23T19:54:51Z
---

# Operational Ownership

Operational Ownership identifies who owns the application, the Skupper sites, link credentials, resource configuration, validation, and ongoing observation. Source coverage is mostly indirect, so this page should remain a practical planning checklist.

## Appears in

- [Plan a Skupper Deployment](./plan-skupper.md) / Planning Inputs

## Sources

- [Network deployment concerns](../concepts/network-deployment-concerns.md): Generated local source for deployment responsibilities across sites, links, services, and observation choices.
- [Skupper resources overview](../../human/skupper-docs/input/overview/resources.md): Local source for Kubernetes resources created by the controller and by sites, useful for platform ownership discussions.
- [Network console guide](../../human/skupper-docs/input/console/index.md): Local source for observer placement and operational visibility considerations.
- [Site linking with the CLI](../../human/skupper-docs/input/kube-cli/site-linking.md): Local source for sensitive token handling and link status validation.
- [Service exposure with the CLI](../../human/skupper-docs/input/kube-cli/service-exposure.md): Local source for service owner actions around connectors and listeners.

## Website Links

- [Skupper network console](https://skupper.io/docs/console/index.html)
- [Skupper resources overview](https://skupper.io/docs/overview/resources.html)
- [Linking sites with the Skupper CLI](https://skupper.io/docs/kube-cli/site-linking.html)

## Draft Notes

- Keep this as a RACI-style planning page unless stronger product-owned guidance appears.
- Assign owners for issuing tokens, applying resources, validating links, exposing services, monitoring status, and handling incidents.
- Call out cross-team handoffs where one team owns the namespace and another owns the application service.
