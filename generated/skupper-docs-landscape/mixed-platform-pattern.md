---
type: DocumentationLandscapePage
title: "Mixed Platform Pattern"
id: mixed-platform-pattern
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/mixed-platform-pattern
tags:
  - skupper
  - docs-landscape
  - platform
related:
  - cluster-pattern
  - host-pattern
timestamp: 2026-07-23T22:00:00Z
---

# Mixed Platform Pattern

The mixed platform pattern connects Kubernetes and local-system Skupper sites using link resources and shared service definitions.

## Appears in

- [Skupper Platform and Managed-Environment Guides](./platform-guides.md) / Platform Patterns

## Dependencies

- [Kubernetes Cluster Pattern](./cluster-pattern.md)
- [Linux Host Pattern](./host-pattern.md)

## Sources

- [generated/skupper-ansible/skupper-ansible-workflow-mixed-sites.md](../skupper-ansible/skupper-ansible-workflow-mixed-sites.md) - Generated source for mixed site workflows.
- [human/skupper-docs/input/kube-cli/site-linking.md](../../human/skupper-docs/input/kube-cli/site-linking.md) - Kubernetes link workflow source.
- [human/skupper-docs/input/system-cli/site-linking.md](../../human/skupper-docs/input/system-cli/site-linking.md) - System link workflow source.
- [human/skupper-docs/input/system-yaml/service-exposure.md](../../human/skupper-docs/input/system-yaml/service-exposure.md) - System service exposure source.
- [human/skupper-docs/input/kube-yaml/service-exposure.md](../../human/skupper-docs/input/kube-yaml/service-exposure.md) - Kubernetes service exposure source.

## Website Links

- [Kubernetes site linking](https://skupper.io/docs/kube-cli/site-linking.html)
- [System site linking](https://skupper.io/docs/system-cli/site-linking.html)
- [Kubernetes service exposure with YAML](https://skupper.io/docs/kube-yaml/service-exposure.html)
- [System service exposure with YAML](https://skupper.io/docs/system-yaml/service-exposure.html)

## Draft Notes

- Show both directions: Kubernetes site linking to system site and system site linking to Kubernetes site.
- Keep token redemption and static link resource behavior distinct.
- Add validation steps for both platform sides.
