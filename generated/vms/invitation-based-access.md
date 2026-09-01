---
type: VmsLandscapePage
title: "Invitation-based Access"
id: invitation-based-access
status: generated
owner: agent
generated_by: generate-vms-landscape-pages.py
reviewed: false
confidence: stub
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/vms/invitation-based-access
tags:
  - vms
  - vms-landscape
timestamp: 2026-08-26T16:01:08Z
---
# Invitation-based Access

Participants join VANs with invitation YAML - video-conference workflow eliminates manual site coordination

## Appears in

- [Skupper VMS - Multi-tenant VAN Management System](./vms-overview.md) / VMS Automation Value

## Topics

### Dependencies

- [Application Network Lifecycle](./vms-application-lifecycle.md)


## Invitation-based Access

Participants join VANs with invitation YAML - video-conference workflow eliminates manual site coordination.

### Video Conference Analogy

VMS applies the video-conference meeting model to application networks:

**Video conference:**
- Host schedules meeting
- Sends invitation link via email
- Participants click link to join
- No IT coordination required

**VMS VAN:**
- Owner creates VAN
- Generates invitation YAML, distributes via any channel
- Participants apply YAML to join
- No distributed configuration coordination required

### Workflow Simplicity

**Traditional Skupper** (VMS eliminates):
1. Site A owner creates Skupper site
2. Generates link token
3. Sends token to Site B owner (secure channel)
4. Site B owner creates Skupper site
5. Applies token to create link
6. Repeat for each additional site
7. Manual coordination across all owners

**VMS invitation workflow:**
1. VAN owner creates VAN
2. Generates invitation(s)
3. Distributes invitation YAML (email, docs, chat, repo)
4. Participants apply YAML
5. Automatic join via claim redemption
6. No per-site coordination

### Invitation Properties

**Access controls:**
- **Claim access** - How participant initially connects
- **Primary access** - Main VAN access after join
- **Instance limit** - Single-use or multi-instance
- **Join deadline** - Optional time limit for redemption
- **Site class** - Optional grouping for similar sites

**Interactive mode:**
- Participant must approve configuration before deployment
- Review access points before they're created
- Local control over what gets deployed

### Distribution Flexibility

Invitations can be distributed via **any channel:**

- Email attachment
- Shared document
- Git repository
- Chat message
- Internal wiki
- Configuration management system

**No secure channel required** - invitation contains claim certificate that grants only claim redemption access, not full VAN access.

### No Central Authentication

**Participants don't need:**
- VMS account
- Keycloak authentication
- Central credentials
- Permission grants

**Invitation is the credential:**
- Claim certificate embedded in YAML
- Certificate signed by VAN CA
- Validates participant's right to join
- Exchange for member certificate after validation

### Scalability

**One-to-many distribution:**
- Create one invitation
- Distribute to many participants (if multi-instance)
- Each applies independently
- No coordination between participants

**Asynchronous joining:**
- Participants join when ready
- No need to schedule coordination
- Join deadline optional
- VAN owner monitors membership

### Security Model

**Controlled access:**
- Only those with invitation YAML can join
- VAN owner controls invitation creation
- Instance limits prevent unlimited sharing
- Join deadlines limit exposure window
- VAN owner can evict unauthorized members

**Audit trail:**
- Every member tracked with join time
- Invitation source recorded
- VAN owner sees all members
- Management controller logs all joins

## Source

Based on `human/vms/README.md`
