---
type: DocumentationLandscapePage
title: "Site Initialization"
id: site-initialization
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/site-initialization
tags:
  - skupper
  - docs-landscape
  - install
related:
  - installation-method
timestamp: 2026-07-23T19:57:36Z
---

# Site Initialization

Site Initialization is the step after selecting and completing an installation method where a Skupper site is created in the target namespace or local-system context. The starter path uses `skupper site create`, while YAML-driven paths use Skupper resources.

## Appears in

- [Install Skupper](./install-skupper.md) / Prerequisites and Validation

## Dependencies

- [Select Installation Method](./installation-method.md)

## Sources

- [Site configuration with the CLI](../../human/skupper-docs/input/kube-cli/site-configuration.md): Primary local source for creating a simple Kubernetes site.
- [Kubernetes YAML site configuration](../../human/skupper-docs/input/kube-yaml/site-configuration.md): Local source candidate for declarative site initialization.
- [Site create command](../../human/skupper-docs/input/refdog/commands/site/create.md): Local command reference for site creation and link-access option.
- [Site concept](../../human/skupper-docs/input/refdog/concepts/site.md): Local concept source for site meaning and platform association.
- [Skupper resources overview](../../human/skupper-docs/input/refdog/resources/index.md): Local source for Site as a primary resource.

## Website Links

- [Creating a site with the Skupper CLI](https://skupper.io/docs/kube-cli/site-configuration.html)
- [Creating a site with YAML](https://skupper.io/docs/kube-yaml/site-configuration.html)
- [Refdog site create command](https://skupperproject.github.io/refdog/commands/site/create.html)

## Draft Notes

- Separate site creation from controller installation; users often conflate the two.
- Include namespace or platform context before the create command.
- Mention link access only as an initialization option, with link setup covered elsewhere.
