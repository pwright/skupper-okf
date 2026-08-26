---
type: VmsLandscapePage
title: "Backbone Provisioning"
id: backbone-provisioning
status: generated
owner: agent
generated_by: generate-vms-landscape-pages.py
reviewed: false
confidence: stub
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/vms/backbone-provisioning
tags:
  - vms
  - vms-landscape
timestamp: 2026-08-26T16:01:08Z
---
# Backbone Provisioning

Define backbone, add sites at strategic locations, create cost-weighted links - centralized infrastructure setup

## Appears in

- [VMS Network Topology Management](./vms-overview.md) / Topology Workflows

## Topics

### Dependencies

- [Backbone Network](./backbone-network.md)
- [Backbone Site](./backbone-site.md)
- [Backbone Links](./backbone-links.md)


## Backbone Provisioning

Define backbone, add sites at strategic locations, create cost-weighted links - centralized infrastructure setup via VMS management controller.

### Provisioning Steps

**1. Create Backbone**
- Define new multi-tenant backbone network
- Name and optionally configure as single-tenant (`--no-multitenant`)
- Backbone CA created automatically

**2. Add Backbone Sites**
- Create sites at strategic network locations
- Consider geography, network boundaries, and DMZ placement
- Each site gets a site controller deployment
- Site certificates signed by backbone CA

**3. Configure Access Points**
- Add "manage" access point for management traffic
- Add "peer" access points for inter-router connections
- Add "van" access points for VAN traffic
- Optionally add "claim" and "member" access points

**4. Create Links**
- Connect sites with cost-weighted links
- Lower cost = preferred path
- Design topology for performance and redundancy
- Links use peer access points

**5. Bootstrap Sites**
- Three-step process per site:
  - Download and apply bootstrap YAML
  - Upload ingress data
  - Apply final configuration YAML

### Design Considerations

**Geographic Distribution**
- Place sites near application deployments
- Reduce latency by using local backbone sites
- Consider data sovereignty and compliance requirements

**Network Boundaries**
- Use DMZ sites to bridge restricted networks
- Backbone can relay across firewalls and NAT
- No need for direct connectivity between all sites

**Performance**
- High-bandwidth links get low cost
- Low-latency paths preferred for critical traffic
- Multiple paths provide failover

**Cost Planning**
- Assign costs based on link characteristics:
  - 1 = high-bandwidth, low-latency (preferred)
  - 5 = moderate quality
  - 10+ = backup/expensive paths

### Centralized vs. Distributed

**Traditional Skupper** (VMS eliminates):
- Plan topology manually across sites
- Coordinate router configuration
- Distribute certificates to each site
- Manual link creation at each location

**VMS Backbone Provisioning**:
- Define topology centrally in management controller
- Configuration distributed automatically to sites
- Certificates generated and synced automatically
- Links created via API calls

## Source

Based on `human/vms/README.md` and `human/vms/cli/vms`
