---
type: DocumentationLandscapePage
title: "Host Identity"
id: host-identity
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/host-identity
tags:
  - skupper
  - docs-landscape
  - integrate
timestamp: 2026-07-23T21:45:00Z
---

# Host Identity

Host identity is the site and credential material that lets a local-system Skupper site participate in secure links and service routing.

## Appears in

- [Integrate Skupper](./integrate-skupper.md) / Platform Interfaces

## Sources

- [human/skupper-docs/input/system-cli/site-configuration.md](../../human/skupper-docs/input/system-cli/site-configuration.md) - Local CLI source for system site setup.
- [human/skupper-docs/input/system-cli/site-linking.md](../../human/skupper-docs/input/system-cli/site-linking.md) - Local CLI source for system site linking.
- [human/skupper-docs/input/refdog/topics/system-namespaces.md](../../human/skupper-docs/input/refdog/topics/system-namespaces.md) - Local source candidate for system namespace behavior.
- [human/skupper-docs/input/refdog/topics/system-tls-credentials.md](../../human/skupper-docs/input/refdog/topics/system-tls-credentials.md) - Local source for system TLS credential handling.
- [generated/skupper-ansible/skupper-ansible-module-system.md](../skupper-ansible/skupper-ansible-module-system.md) - Generated source for system-site lifecycle and bundles.

## Website Links

- [System site configuration](https://skupper.io/docs/system-cli/site-configuration.html)
- [System site linking](https://skupper.io/docs/system-cli/site-linking.html)
- [System namespaces topic](https://skupperproject.github.io/refdog/topics/system-namespaces.html)
- [System TLS credentials topic](https://skupperproject.github.io/refdog/topics/system-tls-credentials.html)

## Draft Notes

- Clarify which identity material is generated, applied, or supplied by users.
- Keep namespace directory details platform-specific and source-backed.
- Add guidance for rotating or replacing host identity only after explicit source coverage is identified.
