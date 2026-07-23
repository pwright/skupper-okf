---
type: DocumentationLandscapePage
title: "Secrets Interface"
id: secrets-interface
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/secrets-interface
tags:
  - skupper
  - docs-landscape
  - integrate
timestamp: 2026-07-23T21:45:00Z
---

# Secrets Interface

The secrets interface covers the token, access grant, certificate, and generated secret material that delivery and operations tools must handle carefully.

## Appears in

- [Integrate Skupper](./integrate-skupper.md) / Operations Interfaces

## Sources

- [human/skupper-docs/input/kube-cli/site-linking.md](../../human/skupper-docs/input/kube-cli/site-linking.md) - Local CLI source for issuing and redeeming tokens.
- [human/skupper-docs/input/kube-yaml/site-linking.md](../../human/skupper-docs/input/kube-yaml/site-linking.md) - Local YAML source for AccessGrant, AccessToken, and Link resources.
- [human/skupper-docs/input/refdog/resources/access-token.md](../../human/skupper-docs/input/refdog/resources/access-token.md) - AccessToken resource reference.
- [human/skupper-docs/input/refdog/resources/access-grant.md](../../human/skupper-docs/input/refdog/resources/access-grant.md) - AccessGrant resource reference.
- [generated/skupper-ansible/skupper-ansible-module-token.md](../skupper-ansible/skupper-ansible-module-token.md) - Generated source for token automation.

## Website Links

- [Site linking with the Skupper CLI](https://skupper.io/docs/kube-cli/site-linking.html)
- [Site linking with YAML](https://skupper.io/docs/kube-yaml/site-linking.html)
- [AccessToken resource reference](https://skupperproject.github.io/refdog/resources/access-token.html)
- [AccessGrant resource reference](https://skupperproject.github.io/refdog/resources/access-grant.html)
- [Skupper Ansible repository](https://github.com/skupperproject/skupper-ansible)

## Draft Notes

- Include lifecycle notes for generation, transfer, redemption, storage, and redaction.
- Keep token limits and expiration windows tied to source examples.
- Add boundaries for CI logs, artifact stores, and debug bundles.
