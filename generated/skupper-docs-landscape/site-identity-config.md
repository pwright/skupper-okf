---
type: DocumentationLandscapePage
title: "Site Identity Settings"
id: site-identity-config
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/site-identity-config
tags:
  - skupper
  - docs-landscape
  - configure
related: []
timestamp: 2026-07-23T20:17:03Z
---

# Site Identity Settings

Site identity settings identify the local Skupper site and provide the context that other configuration resources use when they run in the site namespace or local-system namespace.

## Appears in

- [Configure Skupper](./configure-skupper.md) / Configuration Inputs

## Sources

- [human/skupper-docs/input/refdog/concepts/site.md](../../human/skupper-docs/input/refdog/concepts/site.md) - Site concept and role in the application network.
- [human/skupper-docs/input/refdog/resources/site.md](../../human/skupper-docs/input/refdog/resources/site.md) - Site resource reference and status fields.
- [human/skupper-docs/input/kube-cli/site-configuration.md](../../human/skupper-docs/input/kube-cli/site-configuration.md) - CLI site creation flow and status checks.
- [human/skupper-docs/input/kube-yaml/site-configuration.md](../../human/skupper-docs/input/kube-yaml/site-configuration.md) - YAML site examples with metadata and namespace context.
- [human/skupper-docs/input/overview/resources.md](../../human/skupper-docs/input/overview/resources.md) - Overview of Skupper-managed resource ownership.

## Website Links

- [Site concept](https://skupperproject.github.io/refdog/concepts/site.html)
- [Site resource reference](https://skupperproject.github.io/refdog/resources/site.html)
- [Site configuration with CLI](https://skupper.io/docs/kube-cli/site-configuration.html)
- [Site configuration with YAML](https://skupper.io/docs/kube-yaml/site-configuration.html)

## Draft Notes

- Clarify which identity values are operator-chosen metadata and which are controller-managed status or generated credentials.
- Link certificate and trust material to the security map rather than expanding it here.
- Add examples only after confirming the current Site resource fields in the refdog configuration source.
