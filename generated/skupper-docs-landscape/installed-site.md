---
type: DocumentationLandscapePage
title: "Operational Skupper Site"
id: installed-site
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/installed-site
tags:
  - skupper
  - docs-landscape
  - install
related:
  - installation-method
  - site-initialization
timestamp: 2026-07-23T19:57:36Z
---

# Operational Skupper Site

Operational Skupper Site is the install outcome where the required controller or local-system runtime is present and a Skupper site can be created and reported as ready. Keep this page focused on what "installed enough to start using Skupper" means, not on every later linking or service-exposure step.

## Appears in

- [Install Skupper](./install-skupper.md) / Installed Environment

## Dependencies

- [Select Installation Method](./installation-method.md)
- [Site Initialization](./site-initialization.md)

## Sources

- [Skupper installation guide](../../human/skupper-docs/input/install/index.md): Primary local source for installing the Kubernetes controller, installing the CLI, and local-system controller setup.
- [Site configuration with the CLI](../../human/skupper-docs/input/kube-cli/site-configuration.md): Local source for creating a site and checking that it becomes ready.
- [Site create command](../../human/skupper-docs/input/refdog/commands/site/create.md): Local command reference for creating a site across supported platforms.
- [Site status command](../../human/skupper-docs/input/refdog/commands/site/status.md): Local command reference for verifying current site status.
- [Skupper resources overview](../../human/skupper-docs/input/refdog/resources/index.md): Local source for controller reconciliation and generated platform resources.

## Website Links

- [Skupper installation docs](https://skupper.io/docs/install/index.html)
- [Creating a site with the Skupper CLI](https://skupper.io/docs/kube-cli/site-configuration.html)
- [Refdog site status command](https://skupperproject.github.io/refdog/commands/site/status.html)

## Draft Notes

- Define the minimum ready state before moving readers to linking or service exposure.
- Separate Kubernetes controller readiness from local-system controller readiness.
- Include both CLI status and resource status checks when the target platform supports them.
