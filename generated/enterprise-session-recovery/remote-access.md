---
type: EnterpriseSessionRecoveryPage
title: "Remote Access"
id: remote-access
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: maps/enterprise-session-recovery.bs
external: https://pwright.github.io/skupper-okf/generated/enterprise-session-recovery/remote-access
tags:
  - skupper
  - enterprise-session-recovery
  - uses
related:
  - rdp
  - ssh-sftp
---

# Remote Access

This is an enterprise traffic use case. Skupper fit depends on whether the workload can run over TCP and tolerate connection replacement.

## Skupper Suitability

Skupper can expose selected TCP remote-access services, but this is not its strongest use case. Interactive protocols such as SSH, SFTP, and RDP are sensitive to socket loss and user experience; use Skupper only when private reachability is the main goal and session interruption is acceptable.

## Appears in

- Enterprise Traffic Patterns / Enterprise Uses

## Dependency Check

The map dependency check resolved all declared dependencies for this topic: SSH (and SFTP), RDP.

Dependencies:

- [SSH (and SFTP)](./ssh-sftp.md)
- [RDP](./rdp.md)

## Related Skupper Docs

- [Service exposure](../skupper-docs-landscape/service-exposure.md)
- [Service routing](../skupper-docs-landscape/service-routing.md)
- [Connector configuration](../skupper-docs-landscape/connector-config.md)
- [Skupper multi-site connectivity](../skupper-docs-landscape/multi-site-connectivity.md)
- [Private connectivity](../skupper-docs-landscape/private-connectivity.md)
- [Firewall and egress controls](../skupper-docs-landscape/network-controls.md)

## Draft Notes

- Validate the workload by breaking the TCP path and observing client-visible behavior, not just by checking that Skupper reconnects.
- Document whether the application requires same-socket continuity, logical session resume, durable progress, or ordinary retry.
