---
type: DocumentationLandscapePage
title: "Identity and Certificate Policy"
id: identity-policy
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/identity-policy
tags:
  - skupper
  - docs-landscape
  - plan
timestamp: 2026-07-23T19:54:51Z
---

# Identity and Certificate Policy

Identity and Certificate Policy records how the deployment will handle Skupper-generated identity, link credentials, token lifetime, and any externally supplied certificate requirements. Local sources support mutual TLS and private CA defaults, plus token restrictions for link creation.

## Appears in

- [Plan a Skupper Deployment](./plan-skupper.md) / Planning Inputs

## Sources

- [Skupper security overview](../../human/skupper-docs/input/overview/security.md): Local source for mutual TLS, private CA, and router certificate identity.
- [Network deployment concerns](../concepts/network-deployment-concerns.md): Generated local source for access token characteristics and custom certificates for links.
- [Skupper resources overview](../../human/skupper-docs/input/overview/resources.md): Local source for site CA, local CA, and link-related Kubernetes secrets.
- [Token issue command](../../human/skupper-docs/input/refdog/commands/token/issue.md): Local command reference for token expiration and redemption options.
- [Access token concept](../../human/skupper-docs/input/refdog/concepts/access-token.md): Local concept source for token-based linking terminology.

## Website Links

- [Skupper security overview](https://skupper.io/docs/overview/security.html)
- [Refdog token issue command](https://skupperproject.github.io/refdog/commands/token/issue.html)
- [Refdog access token concept](https://skupperproject.github.io/refdog/concepts/access-token.html)

## Draft Notes

- Capture default token limits and any required overrides in the rollout plan.
- Record whether custom certificates are required before selecting link access and deployment automation.
- Define ownership for certificate rotation or credential cleanup if those responsibilities are outside the Skupper docs.
