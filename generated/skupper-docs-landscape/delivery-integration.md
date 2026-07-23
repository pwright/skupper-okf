---
type: DocumentationLandscapePage
title: "CI/CD Integration"
id: delivery-integration
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/delivery-integration
tags:
  - skupper
  - docs-landscape
  - integrate
related:
  - automation-interface
  - secrets-interface
timestamp: 2026-07-23T21:45:00Z
---

# CI/CD Integration

CI/CD integration uses Skupper automation and secret-handling interfaces to create, update, test, and tear down connectivity as part of delivery workflows.

## Appears in

- [Integrate Skupper](./integrate-skupper.md) / Integration Patterns

## Dependencies

- [Automation Interface](./automation-interface.md)
- [Secrets Interface](./secrets-interface.md)

## Sources

- [generated/skupper-ansible/skupper-ansible-overview.md](../skupper-ansible/skupper-ansible-overview.md) - Generated source for Skupper Ansible automation.
- [generated/skupper-ansible/skupper-ansible-module-resource.md](../skupper-ansible/skupper-ansible-module-resource.md) - Generated source for applying resource YAML.
- [generated/skupper-ansible/skupper-ansible-module-token.md](../skupper-ansible/skupper-ansible-module-token.md) - Generated source for retrieving link token material.
- [human/skupper-docs/input/kube-cli/site-linking.md](../../human/skupper-docs/input/kube-cli/site-linking.md) - Local CLI source for link tokens.
- [human/skupper-docs/input/refdog/commands/debug/check.md](../../human/skupper-docs/input/refdog/commands/debug/check.md) - Debug check command reference for validation gates.

## Website Links

- [Skupper Ansible repository](https://github.com/skupperproject/skupper-ansible)
- [Site linking with the Skupper CLI](https://skupper.io/docs/kube-cli/site-linking.html)
- [Command reference](https://skupperproject.github.io/refdog/commands/index.html)
- [Debug check command](https://skupperproject.github.io/refdog/commands/debug/check.html)

## Draft Notes

- Model delivery integration as stages: configure, link, expose, validate, and collect diagnostics.
- Keep pipeline secrets short-lived and avoid storing generated link material in build logs.
- Add examples only after selecting a CI system or generic script format.
