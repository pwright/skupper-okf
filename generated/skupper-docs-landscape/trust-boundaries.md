---
type: DocumentationLandscapePage
title: "Trust Boundaries"
id: trust-boundaries
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/trust-boundaries
tags:
  - skupper
  - docs-landscape
  - plan
timestamp: 2026-07-23T19:54:51Z
---

# Trust Boundaries

Trust Boundaries identifies which networks, clusters, namespaces, hosts, and operational teams must remain isolated or controlled when Skupper is introduced. This page should map those boundaries to link access, token handling, and service exposure decisions.

## Appears in

- [Plan a Skupper Deployment](./plan-skupper.md) / Planning Inputs

## Sources

- [Skupper security overview](../../human/skupper-docs/input/overview/security.md): Primary local source for built-in network isolation and mutual TLS security framing.
- [Skupper connectivity overview](../../human/skupper-docs/input/overview/connectivity.md): Local source for public/private cluster and hybrid communication examples.
- [Network deployment concerns](../concepts/network-deployment-concerns.md): Generated local source for link access, link constraints, and console placement across firewall boundaries.
- [Site linking with the CLI](../../human/skupper-docs/input/kube-cli/site-linking.md): Local source for link direction and token transfer considerations.
- [Skupper resources overview](../../human/skupper-docs/input/overview/resources.md): Local source for Skupper-created service accounts, roles, secrets, and services on Kubernetes.

## Website Links

- [Skupper security overview](https://skupper.io/docs/overview/security.html)
- [Skupper connectivity overview](https://skupper.io/docs/overview/connectivity.html)
- [Linking sites with the Skupper CLI](https://skupper.io/docs/kube-cli/site-linking.html)

## Draft Notes

- Describe boundaries in operational terms: who controls each side, what traffic is allowed, and where credentials may be handled.
- Use link direction to reduce inbound exposure where firewall constraints require it.
- Do not treat Skupper as a substitute for application authorization; keep application security requirements explicit.
