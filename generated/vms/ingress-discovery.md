---
type: VmsLandscapePage
title: "Ingress Discovery"
id: ingress-discovery
status: generated
owner: agent
generated_by: generate-vms-landscape-pages.py
reviewed: false
confidence: stub
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/vms/ingress-discovery
tags:
  - vms
  - vms-landscape
timestamp: 2026-08-26T16:01:08Z
---
# Ingress Discovery

Bootstrap process captures actual ingress addresses from deployed site - adapts to cluster networking

## Appears in

- [VMS Network Topology Management](./vms-overview.md) / VMS Topology Automation

## Topics

- This item has no documented dependencies.


## Ingress Discovery

Bootstrap process captures actual ingress addresses from deployed site - adapts to cluster networking automatically.

### The Problem

When deploying a backbone site:

- Kubernetes may assign unpredictable ingress addresses
- LoadBalancer IPs allocated dynamically
- Routes may have cluster-specific hostnames
- Management controller needs these addresses to configure links

### Discovery Process

**Step 1 - Deploy with placeholder:**
- Bootstrap YAML deploys site controller and router
- Access points configured but actual addresses unknown

**Step 2 - Site reports ingress:**
- Site controller queries Kubernetes for actual ingress data
- Captures host and port for each access point
- Formats as JSON

**Step 3 - Upload to management:**
- User (or automation) retrieves ingress JSON from site
- Posts to management controller:
  ```
  POST /api/v1alpha1/backbonesite/<site-id>/ingress
  Content-Type: application/json
  ```
- Management controller stores host/port in database

**Step 4 - Links configured:**
- Management controller generates final YAML with real addresses
- Other sites can now connect to this site's access points

### Ingress Data Format

Site reports access point status with:

- **access-point-id** - Which access point this status belongs to
- **host** - Actual hostname or IP address
- **port** - Actual port number

### Automation Opportunity

The `vmshosts` command extracts ingress data:

```bash
kubectl exec -it <vms-site-pod> -c controller -- vmshosts
```

Output can be piped directly to management controller API.

### Why This Matters

**Without ingress discovery:**
- Admin must manually determine ingress addresses
- Error-prone transcription
- Breaks if cluster networking changes

**With ingress discovery:**
- Site reports actual addresses
- Adapts to any cluster networking
- Works with LoadBalancer, NodePort, Routes
- Reduces bootstrap errors

### Cluster Networking Adaptation

Ingress discovery works with:

- **OpenShift Routes** - Captures route hostname
- **Kubernetes LoadBalancer** - Captures assigned IP
- **Kubernetes NodePort** - Captures node IP and port
- **Ingress controllers** - Captures ingress addresses

Site controller queries the Kubernetes API to discover actual ingress, regardless of the mechanism.

## Source

Based on `human/vms/docs/notes/bootstrap.md` and `human/vms/docs/notes/getting-started.md`
