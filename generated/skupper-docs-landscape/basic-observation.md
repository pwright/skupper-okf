---
type: DocumentationLandscapePage
title: "Check Network Status"
id: basic-observation
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/basic-observation
tags:
  - skupper
  - docs-landscape
  - get-started
related:
  - first-sites
  - first-link
timestamp: 2026-07-23T19:49:37Z
---

# Check Network Status

Check Network Status gives new users the minimum observation loop for a starter network. It should cover site status, link status, and service exposure status without turning into a full observability or troubleshooting guide.

## Appears in

- [Get Started with Skupper](./get-started.md) / Starter Workflow

## Dependencies

- [Create Two Sites](./first-sites.md)
- [Link the Sites](./first-link.md)

## Sources

- [Site configuration with the CLI](../../human/skupper-docs/input/kube-cli/site-configuration.md): Local source that points readers to `skupper site status` after site creation.
- [Site linking with the CLI](../../human/skupper-docs/input/kube-cli/site-linking.md): Local source for using `skupper link status` and interpreting pending versus ready link states.
- [Service exposure with the CLI](../../human/skupper-docs/input/kube-cli/service-exposure.md): Local source for connector and listener status checks.
- [Site status command](../../human/skupper-docs/input/refdog/commands/site/status.md): Local command reference for site readiness.
- [Link status command](../../human/skupper-docs/input/refdog/commands/link/status.md): Local command reference for link readiness.

## Website Links

- [Creating a site with the Skupper CLI](https://skupper.io/docs/kube-cli/site-configuration.html)
- [Linking sites with the Skupper CLI](https://skupper.io/docs/kube-cli/site-linking.html)
- [Refdog site status command](https://skupperproject.github.io/refdog/commands/site/status.html)

## Draft Notes

- Keep this to basic CLI status commands; dashboards and metrics belong in later observation topics.
- Include a short sequence so users know which status to check first.
- Note that newly created resources can be pending briefly before they report ready.
