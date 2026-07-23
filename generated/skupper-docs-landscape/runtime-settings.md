---
type: DocumentationLandscapePage
title: "Runtime Settings"
id: runtime-settings
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/runtime-settings
tags:
  - skupper
  - docs-landscape
  - configure
related:
  - resource-limits
  - logging-settings
timestamp: 2026-07-23T20:17:03Z
---

# Runtime Settings

Runtime settings are the operational configuration choices that affect how a site runs after creation, including resource allocation, reload behavior on local systems, and diagnostic logging.

## Appears in

- [Configure Skupper](./configure-skupper.md) / Configuration Resources

## Dependencies

- [Resource Limits](./resource-limits.md)
- [Logging Settings](./logging-settings.md)

## Sources

- [generated/concepts/network-deployment-concerns.md](../concepts/network-deployment-concerns.md) - Site performance and resource allocation notes.
- [human/skupper-docs/input/kube-yaml/site-configuration.md](../../human/skupper-docs/input/kube-yaml/site-configuration.md) - Site resource configuration examples.
- [human/skupper-docs/input/system-cli/site-configuration.md](../../human/skupper-docs/input/system-cli/site-configuration.md) - Local-system site configuration flow.
- [human/skupper-docs/input/troubleshooting/index.md](../../human/skupper-docs/input/troubleshooting/index.md) - Troubleshooting checks, logs, and debug dump guidance.
- [generated/skupper-ansible/skupper-ansible-module-system.md](../skupper-ansible/skupper-ansible-module-system.md) - System module actions including reload/start/stop for local-system sites.

## Website Links

- [Site configuration with YAML](https://skupper.io/docs/kube-yaml/site-configuration.html)
- [Troubleshooting](https://skupper.io/docs/troubleshooting/index.html)
- [Debug command reference](https://skupperproject.github.io/refdog/commands/debug/index.html)
- [Skupper Ansible repository](https://github.com/skupperproject/skupper-ansible)

## Draft Notes

- Treat this as a bridge page from configuration to operations; avoid duplicating full troubleshooting procedures.
- Separate Kubernetes resource requests and limits from local-system reload behavior in future expansion.
- Logging coverage is thin in the current local source set, so keep claims focused on diagnostic commands and collected logs.
