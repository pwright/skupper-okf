---
type: DocumentationLandscapePage
title: "Certificate Issuance"
id: issuance
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/issuance
tags:
  - skupper
  - docs-landscape
  - secure
timestamp: 2026-07-23T20:30:00Z
---

# Certificate Issuance

Certificate issuance is the part of secure linking where Skupper creates or exchanges credential material needed by a site or link.

## Appears in

- [Secure Skupper](./secure-skupper.md) / Isolation Foundations

## Sources

- [human/skupper-docs/input/kube-cli/site-linking.md](../../human/skupper-docs/input/kube-cli/site-linking.md) - CLI token issue and redeem workflow.
- [human/skupper-docs/input/kube-yaml/site-linking.md](../../human/skupper-docs/input/kube-yaml/site-linking.md) - YAML source for access grants, access tokens, and links.
- [human/skupper-docs/input/refdog/resources/access-grant.md](../../human/skupper-docs/input/refdog/resources/access-grant.md) - AccessGrant resource reference.
- [human/skupper-docs/input/refdog/resources/access-token.md](../../human/skupper-docs/input/refdog/resources/access-token.md) - AccessToken resource reference.
- [generated/skupper-ansible/skupper-ansible-module-token.md](../skupper-ansible/skupper-ansible-module-token.md) - Generated Ansible source for retrieving token material.

## Website Links

- [Site linking with the Skupper CLI](https://skupper.io/docs/kube-cli/site-linking.html)
- [Site linking with YAML](https://skupper.io/docs/kube-yaml/site-linking.html)
- [AccessGrant resource reference](https://skupperproject.github.io/refdog/resources/access-grant.html)
- [AccessToken resource reference](https://skupperproject.github.io/refdog/resources/access-token.html)
- [Skupper Ansible repository](https://github.com/skupperproject/skupper-ansible)

## Draft Notes

- Describe issuance through user-visible objects: token issue, access grant, access token, link, and generated secrets.
- Keep token restrictions such as expiration and redemption count tied to the CLI and YAML source examples.
- Add a future note for non-Kubernetes token redemption once the system CLI and Ansible flows are reconciled.
