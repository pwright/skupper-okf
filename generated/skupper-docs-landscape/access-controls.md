---
type: DocumentationLandscapePage
title: "Administrative Access Controls"
id: access-controls
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/access-controls
tags:
  - skupper
  - docs-landscape
  - administer
timestamp: 2026-07-23T20:10:12Z
---

# Administrative Access Controls

Administrative Access Controls defines who can install, configure, link, expose services, collect diagnostics, and handle credentials. Local Skupper docs provide resource and credential behavior, while organization-specific authorization remains outside the product docs.

## Appears in

- [Administer Skupper](./administer-skupper.md) / Governance Controls

## Sources

- [Skupper installation guide](../../human/skupper-docs/input/install/index.md): Local source for cluster-admin requirements and controller scope notes.
- [Skupper resources overview](../../human/skupper-docs/input/overview/resources.md): Local source for service accounts, roles, role bindings, and secrets.
- [Site linking with the CLI](../../human/skupper-docs/input/kube-cli/site-linking.md): Local source for token, link-resource, proxy, and link-status workflows.
- [Skupper security overview](../../human/skupper-docs/input/overview/security.md): Local source for mutual TLS and network isolation framing.
- [Skupper API resources](../../human/skupper-docs/input/refdog/resources/index.md): Local source for desired resources, generated resources, and platform-specific operations.

## Website Links

- [Skupper installation docs](https://skupper.io/docs/install/index.html)
- [Skupper security overview](https://skupper.io/docs/overview/security.html)
- [Skupper resources overview](https://skupper.io/docs/overview/resources.html)

## Draft Notes

- Separate platform admin, Skupper operator, application owner, and credential handler roles.
- Record who may issue and redeem link credentials.
- Avoid inventing RBAC policy details beyond sourced resource and install requirements.
