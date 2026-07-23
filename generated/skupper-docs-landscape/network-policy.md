---
type: DocumentationLandscapePage
title: "Network Policy"
id: network-policy
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/network-policy
tags:
  - skupper
  - docs-landscape
  - extend
timestamp: 2026-07-23T20:01:23Z
---

# Network Policy

Network Policy captures the connectivity and access constraints that affect adding a site or link. In this landscape page, use the term broadly for firewall, proxy, ingress, link direction, and external access decisions rather than assuming Kubernetes NetworkPolicy unless a source explicitly does so.

## Appears in

- [Extend a Skupper Application Network](./extend-skupper.md) / Expansion Controls

## Sources

- [Site linking with the CLI](../../human/skupper-docs/input/kube-cli/site-linking.md): Local source for link direction, link access, HTTP CONNECT proxy support with link resources, and status checks.
- [Network deployment concerns](../concepts/network-deployment-concerns.md): Generated local source for link constraints, link access defaults, and firewall-aware console placement.
- [Skupper connectivity overview](../../human/skupper-docs/input/overview/connectivity.md): Local source for public/private cluster and edge connectivity examples.
- [Skupper security overview](../../human/skupper-docs/input/overview/security.md): Local source for private connectivity and mutual TLS security framing.
- [Link resource](../../human/skupper-docs/input/refdog/resources/link.md): Local resource reference candidate for link endpoint and settings fields.

## Website Links

- [Linking sites with the Skupper CLI](https://skupper.io/docs/kube-cli/site-linking.html)
- [Skupper connectivity overview](https://skupper.io/docs/overview/connectivity.html)
- [Skupper security overview](https://skupper.io/docs/overview/security.html)

## Draft Notes

- Define allowed directions and who can open inbound access before generating credentials.
- Use link resources for proxy scenarios because token redemption does not cover every proxy case.
- Avoid Kubernetes NetworkPolicy specifics until a dedicated source is selected.
