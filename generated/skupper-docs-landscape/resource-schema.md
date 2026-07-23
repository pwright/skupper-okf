---
type: DocumentationLandscapePage
title: "Resource Schemas"
id: resource-schema
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/resource-schema
tags:
  - skupper
  - docs-landscape
  - develop
timestamp: 2026-07-23T21:30:00Z
---

# Resource Schemas

Resource schemas define the fields, status, and relationships for Skupper custom resources used in declarative workflows.

## Appears in

- [Develop with Skupper](./develop-skupper.md) / Developer Foundations

## Sources

- [human/skupper-docs/input/refdog/resources/index.md](../../human/skupper-docs/input/refdog/resources/index.md) - Local resource reference index.
- [human/skupper-docs/refdog/crds/skupper_site_crd.yaml](../../human/skupper-docs/refdog/crds/skupper_site_crd.yaml) - Local CRD source for Site.
- [human/skupper-docs/refdog/crds/skupper_link_crd.yaml](../../human/skupper-docs/refdog/crds/skupper_link_crd.yaml) - Local CRD source for Link.
- [human/skupper-docs/refdog/crds/skupper_listener_crd.yaml](../../human/skupper-docs/refdog/crds/skupper_listener_crd.yaml) - Local CRD source for Listener.
- [human/skupper-docs/refdog/crds/skupper_connector_crd.yaml](../../human/skupper-docs/refdog/crds/skupper_connector_crd.yaml) - Local CRD source for Connector.

## Website Links

- [Refdog resource reference](https://skupperproject.github.io/refdog/resources/index.html)
- [Site resource reference](https://skupperproject.github.io/refdog/resources/site.html)
- [Link resource reference](https://skupperproject.github.io/refdog/resources/link.html)
- [Listener resource reference](https://skupperproject.github.io/refdog/resources/listener.html)
- [Connector resource reference](https://skupperproject.github.io/refdog/resources/connector.html)

## Draft Notes

- Use refdog resource pages as the first user-facing schema source and CRD YAML as implementation evidence.
- Add schema tables by resource type only after verifying current generated fields.
- Include status fields where they are useful for automation validation.
