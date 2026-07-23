---
type: DocumentationLandscapePage
title: "Automated Application Connectivity"
id: automated-connectivity
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/automated-connectivity
tags:
  - skupper
  - docs-landscape
  - develop
related:
  - declarative-resources
  - pipeline-integration
timestamp: 2026-07-23T21:30:00Z
---

# Automated Application Connectivity

Automated application connectivity uses Skupper commands, YAML resources, or automation modules to create sites, links, listeners, and connectors repeatably.

## Appears in

- [Develop with Skupper](./develop-skupper.md) / Developer Outcomes

## Dependencies

- [Declarative Resources](./declarative-resources.md)
- [CI/CD Integration](./pipeline-integration.md)

## Sources

- [human/skupper-docs/input/kube-yaml/site-configuration.md](../../human/skupper-docs/input/kube-yaml/site-configuration.md) - Local YAML source for site definitions.
- [human/skupper-docs/input/kube-yaml/site-linking.md](../../human/skupper-docs/input/kube-yaml/site-linking.md) - Local YAML source for link and token resources.
- [human/skupper-docs/input/kube-yaml/service-exposure.md](../../human/skupper-docs/input/kube-yaml/service-exposure.md) - Local YAML source for listeners and connectors.
- [generated/skupper-ansible/skupper-ansible-overview.md](../skupper-ansible/skupper-ansible-overview.md) - Generated source for Skupper Ansible automation.
- [generated/skupper-ansible/skupper-ansible-workflow-kubernetes.md](../skupper-ansible/skupper-ansible-workflow-kubernetes.md) - Generated source for Kubernetes automation workflow.

## Website Links

- [Site configuration with YAML](https://skupper.io/docs/kube-yaml/site-configuration.html)
- [Site linking with YAML](https://skupper.io/docs/kube-yaml/site-linking.html)
- [Service exposure with YAML](https://skupper.io/docs/kube-yaml/service-exposure.html)
- [Skupper Ansible repository](https://github.com/skupperproject/skupper-ansible)

## Draft Notes

- Expand around a pipeline-safe sequence: apply site, establish link, expose service, validate status.
- Keep imperative CLI automation and declarative YAML automation as separate paths.
- Include idempotency and secret-handling notes where source coverage supports them.
