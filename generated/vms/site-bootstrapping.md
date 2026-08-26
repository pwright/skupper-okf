---
type: VmsLandscapePage
title: "Site Bootstrapping"
id: site-bootstrapping
status: generated
owner: agent
generated_by: generate-vms-landscape-pages.py
reviewed: false
confidence: stub
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/vms/site-bootstrapping
tags:
  - vms
  - vms-landscape
timestamp: 2026-08-26T16:01:08Z
---
# Site Bootstrapping

Three-step process: deploy bootstrap YAML, upload actual ingress data, apply final access point config - automated coordination

## Appears in

- [VMS Network Topology Management](./vms-overview.md) / Topology Workflows

## Topics

### Dependencies

- [Bootstrap YAML Generation](./bootstrap-yaml.md)
- [Ingress Discovery](./ingress-discovery.md)


## Bootstrap Process

Router bootstrapping is required when deploying a new backbone network which has no routers currently reachable from the management controller.

### Eligibility

A backbone router is eligible for bootstrap deployment when:

1. Its TLS lifecycle is "ready", meaning it has an available TLS client certificate
2. It is configured with a "manage" access point (most likely in the "partial" TLS lifecycle state)
3. It does not have configured connections to other routers that are in the "deployed" state

Eligibility for bootstrap deployment is indicated by a deployment-state of "ready-bootstrap".

### Three-Step Process

**Step 1 - Initial Deployment YAML**

The management controller provides the initial deployment YAML using:

```
GET https://<hostport>/api/v1alpha1/backbonesite/<site-id>/kube
```

The user applies this YAML on the new backbone site.

**Step 2 - Upload Site's Ingress JSON**

The user obtains a small JSON text from the site that describes the site's ingress for management access. This text is posted to the management controller using:

```
POST https://<hostport>/api/v1alpha1/backbonesite/<site-id>/ingress
Content-Type: application/json
```

**Step 3 - Incoming Links YAML**

The final step generates the final YAML for site configuration:

```
GET https://<hostport>/api/v1alpga1/backbonesite/<site-id>/links/incoming/kube
```

Once the user applies this YAML text to the site, the bootstrap process is completed and the backbone site transitions to deployment-state "deployed".

## Source

Based on `human/vms/docs/notes/bootstrap.md`
