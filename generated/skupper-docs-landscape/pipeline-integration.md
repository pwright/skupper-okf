---
type: DocumentationLandscapePage
title: "CI/CD Integration"
id: pipeline-integration
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/pipeline-integration
tags:
  - skupper
  - docs-landscape
  - develop
related:
  - cli-automation
  - secrets-injection
timestamp: 2026-07-23T21:30:00Z
---

# CI/CD Integration

CI/CD integration embeds Skupper setup, link material handling, service exposure, and validation into repeatable delivery workflows.

## Appears in

- [Develop with Skupper](./develop-skupper.md) / Development Interfaces

## Dependencies

- [CLI Automation](./cli-automation.md)
- [Secrets Injection](./secrets-injection.md)

## Sources

- [generated/skupper-ansible/skupper-ansible-workflow-kubernetes.md](../skupper-ansible/skupper-ansible-workflow-kubernetes.md) - Generated source for automated Kubernetes resource and token workflows.
- [generated/skupper-ansible/skupper-ansible-workflow-non-kubernetes.md](../skupper-ansible/skupper-ansible-workflow-non-kubernetes.md) - Generated source for local-system automation.
- [generated/skupper-ansible/skupper-ansible-module-token.md](../skupper-ansible/skupper-ansible-module-token.md) - Generated source for token retrieval automation.
- [human/skupper-docs/input/kube-cli/site-linking.md](../../human/skupper-docs/input/kube-cli/site-linking.md) - Local CLI source for token issue and redemption workflow.
- [human/skupper-docs/input/kube-yaml/site-linking.md](../../human/skupper-docs/input/kube-yaml/site-linking.md) - Local YAML source for declarative link material.

## Website Links

- [Site linking with the Skupper CLI](https://skupper.io/docs/kube-cli/site-linking.html)
- [Site linking with YAML](https://skupper.io/docs/kube-yaml/site-linking.html)
- [Skupper Ansible repository](https://github.com/skupperproject/skupper-ansible)
- [Command reference](https://skupperproject.github.io/refdog/commands/index.html)

## Draft Notes

- Separate build-time validation, deploy-time configuration, and runtime smoke tests.
- Treat token and secret material as short-lived pipeline inputs unless source docs state otherwise.
- Add example pipeline stages after choosing a supported automation surface.
