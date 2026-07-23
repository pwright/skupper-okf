---
type: DocumentationLandscapePage
title: "Create Two Sites"
id: first-sites
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/first-sites
tags:
  - skupper
  - docs-landscape
  - get-started
related:
  - starter-prerequisites
  - cli-install
timestamp: 2026-07-23T19:49:37Z
---

# Create Two Sites

Create Two Sites covers the first concrete Skupper setup step for a starter network. The page should explain that a site represents a place where application components run, then guide readers to create one site in each target namespace, cluster, or supported local platform.

## Appears in

- [Get Started with Skupper](./get-started.md) / Starter Workflow

## Dependencies

- [Cluster or Host Prerequisites](./starter-prerequisites.md)
- [Install the Skupper CLI](./cli-install.md)

## Sources

- [Site configuration with the CLI](../../human/skupper-docs/input/kube-cli/site-configuration.md): Primary local procedure for creating a simple Kubernetes site with `skupper site create`.
- [Skupper installation guide](../../human/skupper-docs/input/install/index.md): Local source for installing the controller before creating Kubernetes sites and for local-system CLI setup.
- [Site create command](../../human/skupper-docs/input/refdog/commands/site/create.md): Local command reference describing site creation, supported platforms, and link-access option.
- [Site concept](../../human/skupper-docs/input/refdog/concepts/site.md): Local concept source for the meaning of a Skupper site.

## Website Links

- [Creating a site with the Skupper CLI](https://skupper.io/docs/kube-cli/site-configuration.html)
- [Refdog site create command](https://skupperproject.github.io/refdog/commands/site/create.html)
- [Refdog site concept](https://skupperproject.github.io/refdog/concepts/site.html)

## Draft Notes

- Make namespace and context assumptions explicit for Kubernetes examples.
- Include the `--enable-link-access` decision, but keep detailed token issuance in the link credentials page.
- Mention local platforms only as a branch unless the starter workflow expands beyond Kubernetes.
