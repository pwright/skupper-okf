---
type: EnterpriseSessionRecoveryPage
title: "File Sharing"
id: file-sharing
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: maps/enterprise-session-recovery.bs
external: https://pwright.github.io/skupper-okf/generated/enterprise-session-recovery/file-sharing
tags:
  - skupper
  - enterprise-session-recovery
  - uses
related:
  - nfs
  - smb
---

# File Sharing

This is an enterprise traffic use case. Skupper fit depends on whether the workload can run over TCP and tolerate connection replacement.

## Skupper Suitability

Skupper is a cautious fit for file sharing. SMB or NFS over TCP may be reachable, but file-locking, mount recovery, DNS dependence, and latency sensitivity make this a workload that needs explicit failure testing rather than a default recommendation.

## Appears in

- Enterprise Traffic Patterns / Enterprise Uses

## Dependency Check

The map dependency check resolved all declared dependencies for this topic: SMB (Samba), NFS.

Dependencies:

- [SMB (Samba)](./smb.md)
- [NFS](./nfs.md)

## Related Skupper Docs

- No direct Skupper documentation link is specific enough yet; use the map dependencies above to navigate to related topics.

## Draft Notes

- Validate the workload by breaking the TCP path and observing client-visible behavior, not just by checking that Skupper reconnects.
- Document whether the application requires same-socket continuity, logical session resume, durable progress, or ordinary retry.
