---
type: VmsLandscapePage
title: "Instant Eviction"
id: instant-eviction
status: generated
owner: agent
generated_by: generate-vms-landscape-pages.py
reviewed: false
confidence: stub
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/vms/instant-eviction
tags:
  - vms
  - vms-landscape
timestamp: 2026-08-26T16:01:08Z
---
# Instant Eviction

Remove entire VANs or individual members in one operation via certificate revocation - no per-site cleanup

## Appears in

- [Skupper VMS - Multi-tenant VAN Management System](./vms-overview.md) / VMS Automation Value

## Topics

### Dependencies

- [Security & PKI](./vms-security-pki.md)
- [Application Network Lifecycle](./vms-application-lifecycle.md)


## Instant Eviction

Remove entire VANs or individual members in one operation via certificate revocation - no per-site cleanup coordination required.

### VAN Eviction

**Single operation removes entire VAN:**

1. Admin evicts VAN via console or CLI
2. Management controller revokes VAN CA
3. VAN CA subtree invalidated - all invitation and member certificates become invalid
4. Routers reject connections using revoked certificates
5. All member sites lose VAN access immediately

**No per-site cleanup:**
- No need to contact each member
- No manual certificate revocation per site
- No coordination across distributed sites
- Instant enforcement via certificate validation

### Member Eviction

**Remove individual member:**

1. VAN owner evicts member via console or CLI
2. Management controller revokes member certificate
3. Routers reject connections from that member
4. Member loses VAN access immediately
5. Other members unaffected

### Certificate-based Enforcement

Eviction is enforced through PKI:

- **Revoked certificates** - Marked as invalid in VMS database
- **Router validation** - Routers check certificate validity on every connection
- **Immediate effect** - No waiting for CRL propagation
- **No bypass** - Certificate-based security cannot be circumvented

### Contrast with Manual Skupper

**Manual Skupper teardown** (VMS eliminates):
- Contact each site owner
- Coordinate removal timing
- Delete Skupper resources at each site
- Verify cleanup at each location
- Manual tracking of who's been removed

**VMS eviction**:
- One API call
- Instant effect across all sites
- No coordination required
- Centrally verifiable

### Use Cases

**Security incident:**
- Compromised member can be evicted immediately
- No time for attacker to move laterally
- Instant access revocation

**End of collaboration:**
- VAN no longer needed - evict entire VAN
- Project complete - remove all members at once
- Clean shutdown without coordination overhead

**Temporal access:**
- Time-boxed VANs automatically evict at end time
- Invitation deadlines prevent late joins
- Automatic expiration without manual cleanup

## Source

Based on `human/vms/README.md`
