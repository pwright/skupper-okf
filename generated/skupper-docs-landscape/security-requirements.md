---
type: DocumentationLandscapePage
title: "Security Requirements"
id: security-requirements
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/security-requirements
tags:
  - skupper
  - docs-landscape
  - plan
related:
  - trust-boundaries
  - identity-policy
timestamp: 2026-07-23T19:54:51Z
---

# Security Requirements

Security Requirements captures the constraints that shape a Skupper deployment: private service access, mutual TLS expectations, link credential handling, certificate policy, and which network boundaries the application network must cross.

## Appears in

- [Plan a Skupper Deployment](./plan-skupper.md) / Requirements and Constraints

## Dependencies

- [Trust Boundaries](./trust-boundaries.md)
- [Identity and Certificate Policy](./identity-policy.md)

## Sources

- [Skupper security overview](../../human/skupper-docs/input/overview/security.md): Primary local overview for mutual TLS, private CA, router identity, and network isolation claims.
- [Network deployment concerns](../concepts/network-deployment-concerns.md): Generated local planning source for token behavior, link constraints, and custom certificates for links.
- [Site linking with the CLI](../../human/skupper-docs/input/kube-cli/site-linking.md): Local source for token handling and link credential protection.
- [Skupper resources overview](../../human/skupper-docs/input/overview/resources.md): Local source for Kubernetes secrets and certificates created by Skupper.
- [Access token concept](../../human/skupper-docs/input/refdog/concepts/access-token.md): Local concept source for access token terminology and linking context.

## Website Links

- [Skupper security overview](https://skupper.io/docs/overview/security.html)
- [Linking sites with the Skupper CLI](https://skupper.io/docs/kube-cli/site-linking.html)
- [Refdog access token concept](https://skupperproject.github.io/refdog/concepts/access-token.html)

## Draft Notes

- Distinguish product defaults from site-specific security requirements.
- Record who may issue, transfer, redeem, store, and delete token files.
- Capture any custom certificate requirement as a planning input for secure-link expansion.
