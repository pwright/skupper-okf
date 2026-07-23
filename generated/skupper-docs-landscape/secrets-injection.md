---
type: DocumentationLandscapePage
title: "Secrets Injection"
id: secrets-injection
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/secrets-injection
tags:
  - skupper
  - docs-landscape
  - develop
timestamp: 2026-07-23T21:30:00Z
---

# Secrets Injection

Secrets injection covers how automation supplies Skupper link tokens, generated link material, credentials, and platform access without committing sensitive data to long-lived configuration.

## Appears in

- [Develop with Skupper](./develop-skupper.md) / Developer Foundations

## Sources

- [human/skupper-docs/input/kube-cli/site-linking.md](../../human/skupper-docs/input/kube-cli/site-linking.md) - Local CLI source for issuing and redeeming link tokens.
- [human/skupper-docs/input/kube-yaml/site-linking.md](../../human/skupper-docs/input/kube-yaml/site-linking.md) - Local YAML source for access tokens and links.
- [human/skupper-docs/input/refdog/resources/access-token.md](../../human/skupper-docs/input/refdog/resources/access-token.md) - AccessToken resource reference.
- [human/skupper-docs/input/refdog/resources/access-grant.md](../../human/skupper-docs/input/refdog/resources/access-grant.md) - AccessGrant resource reference.
- [generated/skupper-ansible/skupper-ansible-module-token.md](../skupper-ansible/skupper-ansible-module-token.md) - Generated source for retrieving token material in automation.

## Website Links

- [Site linking with the Skupper CLI](https://skupper.io/docs/kube-cli/site-linking.html)
- [Site linking with YAML](https://skupper.io/docs/kube-yaml/site-linking.html)
- [AccessToken resource reference](https://skupperproject.github.io/refdog/resources/access-token.html)
- [AccessGrant resource reference](https://skupperproject.github.io/refdog/resources/access-grant.html)
- [Skupper Ansible repository](https://github.com/skupperproject/skupper-ansible)

## Draft Notes

- Keep link tokens and generated link credentials out of ordinary examples unless the example is clearly local or temporary.
- Document expiration, redemption limits, and handling boundaries only where source docs provide them.
- Add redaction guidance for logs and debug bundles that may contain sensitive material.
