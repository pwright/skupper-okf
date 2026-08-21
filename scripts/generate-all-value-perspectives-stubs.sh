#!/bin/bash

# Generate all 78 skupper-value-perspectives stub files
# Run from: /home/paulwright/repos/sk/skupper-okf
# Usage: bash scripts/generate-all-value-perspectives-stubs.sh

set -e

TIMESTAMP=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
BASE_DIR="generated/skupper-value-perspectives"

# Ensure we're in the right directory
if [[ ! -d "maps" || ! -d "generated" ]]; then
    echo "Error: Must run from /home/paulwright/repos/sk/skupper-okf"
    exit 1
fi

# Ensure output directory exists
mkdir -p "$BASE_DIR"

create_stub() {
    local item_id="$1"
    local item_name="$2"
    local map_title="$3"
    local category_name="$4"

    cat > "$BASE_DIR/${item_id}.md" <<EOF
---
type: DocumentationLandscapePage
title: "$item_name"
id: $item_id
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: stub
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/skupper-value-perspectives/$item_id
tags:
  - skupper
  - value-perspectives
timestamp: $TIMESTAMP
---

# $item_name

{Brief placeholder description}

## Appears in

- [$map_title](./skupper-value-perspectives.md) / $category_name

## Notes

- TODO: replace this stub with sourced content.
EOF
}

echo "Generating 78 skupper-value-perspectives stub files..."
echo ""

# Map 1: Skupper Business Value Chain (27 items)
MAP1="Skupper Business Value Chain"

# Category: Business Value (5 items)
create_stub "faster-change" "Faster Business & Technology Change" "$MAP1" "Business Value"
create_stub "business-continuity" "Business Continuity" "$MAP1" "Business Value"
create_stub "cloud-cost-flexibility" "Cloud Cost & Capacity Flexibility" "$MAP1" "Business Value"
create_stub "market-reach" "Faster Regional & Market Expansion" "$MAP1" "Business Value"
create_stub "reduced-integration-risk" "Reduced Integration Risk" "$MAP1" "Business Value"

# Category: Strategic Use Cases (6 items)
create_stub "migration-flexibility" "Incremental Cloud Migration" "$MAP1" "Strategic Use Cases"
create_stub "delivery-velocity" "Faster Application Delivery" "$MAP1" "Strategic Use Cases"
create_stub "cross-site-resilience" "Cross-Site Resilience & Failover" "$MAP1" "Strategic Use Cases"
create_stub "workload-placement" "Workload Placement Freedom" "$MAP1" "Strategic Use Cases"
create_stub "capacity-spillover" "Hybrid-Cloud Capacity Spillover" "$MAP1" "Strategic Use Cases"
create_stub "regional-deployment" "Distributed Regional Deployment" "$MAP1" "Strategic Use Cases"

# Category: Application Connectivity Capabilities (6 items)
create_stub "location-independence" "Location-Independent Applications" "$MAP1" "Application Connectivity Capabilities"
create_stub "multi-site-services" "Multi-Site Application Services" "$MAP1" "Application Connectivity Capabilities"
create_stub "service-connectivity" "Transparent Service-to-Service Connectivity" "$MAP1" "Application Connectivity Capabilities"
create_stub "service-failover" "Cross-Site Load Balancing & Failover" "$MAP1" "Application Connectivity Capabilities"
create_stub "secure-connectivity" "Secure Private Application Connectivity" "$MAP1" "Application Connectivity Capabilities"
create_stub "skupper-network-engineering-pov" "Cross-Platform Connectivity" "$MAP1" "Application Connectivity Capabilities"

# Category: Platform Services (6 items)
create_stub "adaptive-routing" "Application-Aware Routing" "$MAP1" "Platform & Operating Model"
create_stub "skupper-application-engineering-pov" "Declarative Application Networking" "$MAP1" "Platform & Operating Model"
create_stub "listeners-connectors" "Listeners & Connectors" "$MAP1" "Platform & Operating Model"
create_stub "routing-keys" "Application-Layer Service Addressing" "$MAP1" "Platform & Operating Model"
create_stub "mtls" "Mutual TLS Protection" "$MAP1" "Platform & Operating Model"
create_stub "access-tokens" "Controlled Site Enrollment" "$MAP1" "Platform & Operating Model"

# Category: Foundation (4 items)
create_stub "skupper-sites" "Skupper Sites" "$MAP1" "Skupper Foundation"
create_stub "site-links" "Secure Site-to-Site Links" "$MAP1" "Skupper Foundation"
create_stub "skupper-router" "Skupper Router" "$MAP1" "Skupper Foundation"
create_stub "local-platforms" "Docker, Podman & Linux Systems" "$MAP1" "Skupper Foundation"
# kubernetes already exists as a stub

echo "  ✅ Map 1 complete: 26 items (kubernetes skipped - duplicate ID)"

# Map 2: Application Engineering POV - Skupper Layered Connectivity (17 items)
MAP2="Application Engineering POV - Skupper Layered Connectivity"

# Category: Application Endpoints (4 items)
create_stub "connector" "Connector" "$MAP2" "Application Endpoints"
create_stub "server" "Server" "$MAP2" "Application Endpoints"
create_stub "client" "Client" "$MAP2" "Application Endpoints"
create_stub "listener" "Listener" "$MAP2" "Application Endpoints"

# Category: Service Layer (3 items)
create_stub "routing-key" "Routing Key" "$MAP2" "Service Layer"
create_stub "service-routing" "Service Routing" "$MAP2" "Service Layer"
create_stub "service-binding" "Service Binding" "$MAP2" "Service Layer"

# Category: Site Layer (3 items)
create_stub "skupper-site" "Skupper Site" "$MAP2" "Site Layer"
create_stub "skupper-config" "Skupper Configuration" "$MAP2" "Site Layer"
create_stub "site-identity" "Site Identity" "$MAP2" "Site Layer"

# Category: Routing Layer (3 items)
create_stub "router" "Skupper Router" "$MAP2" "Routing Layer"
create_stub "inter-site-link" "Inter-site Link" "$MAP2" "Routing Layer"
create_stub "route-discovery" "Route Discovery" "$MAP2" "Routing Layer"

# Category: Transport Layer (4 items)
create_stub "secure-transport" "Secure Transport" "$MAP2" "Secure Transport"
create_stub "mutual-tls" "Mutual TLS" "$MAP2" "Secure Transport"
create_stub "credentials" "Link Credentials" "$MAP2" "Secure Transport"
create_stub "network-reachability" "Network Reachability" "$MAP2" "Secure Transport"

echo "  ✅ Map 2 complete: 17 items"

# Map 3: Network Engineering POV - Site Platform Choices (24 items)
MAP3="Network Engineering POV - Site Platform Choices"

# Category: Sites (4 items)
create_stub "platform1" "Platform" "$MAP3" "Sites"
create_stub "west-site" "West site" "$MAP3" "Sites"
create_stub "east-site" "East site" "$MAP3" "Sites"
create_stub "platform" "Platform" "$MAP3" "Sites"

# Category: Platform Choice & Management (3 items)
create_stub "skupper-platform-choices" "Site Platform Choice" "$MAP3" "Platform Choice & Management"
create_stub "site-control-plane" "Site Control Plane" "$MAP3" "Platform Choice & Management"
create_stub "desired-state" "Desired Network State" "$MAP3" "Platform Choice & Management"

# Category: Platform Implementations (3 items)
create_stub "kubernetes-platform" "Kubernetes" "$MAP3" "Platform Implementations"
create_stub "ocp-platform" "OpenShift Container Platform" "$MAP3" "Platform Implementations"
create_stub "container-host-platform" "Container Host" "$MAP3" "Platform Implementations"

# Category: Platform Adaptors (3 items)
create_stub "kube-adaptor" "Kubernetes Adaptor" "$MAP3" "Platform Adaptors"
create_stub "network-intent" "Network Intent Translation" "$MAP3" "Platform Adaptors"
create_stub "kube-api" "Kubernetes API" "$MAP3" "Platform Adaptors"

# Category: Containers & Workload Runtime (6 items)
create_stub "kubelet" "Kubelet" "$MAP3" "Containers & Workload Runtime"
create_stub "container-runtime" "Container Runtime Interface" "$MAP3" "Containers & Workload Runtime"
create_stub "docker" "Docker" "$MAP3" "Containers & Workload Runtime"
create_stub "containerd-runtime" "containerd" "$MAP3" "Containers & Workload Runtime"
create_stub "crio-runtime" "CRI-O" "$MAP3" "Containers & Workload Runtime"
# podman and systemd already exist

# Category: Host & Service Management (2 items - 3 total but 1 duplicate)
create_stub "oci-runtime" "OCI Runtime" "$MAP3" "Host & Service Management"
create_stub "linux-host" "Linux Host" "$MAP3" "Host & Service Management"
# systemd already created

# Category: Routing & Network Infrastructure (3 items)
create_stub "router-api" "Router API" "$MAP3" "Routing & Network Infrastructure"
create_stub "site-router" "Site Router" "$MAP3" "Routing & Network Infrastructure"
create_stub "routing-stack" "Routing Stack" "$MAP3" "Routing & Network Infrastructure"

echo "  ✅ Map 3 complete: 22 items (2 duplicates skipped: podman, systemd)"

# Map 4: Skupper Platform Choices (24 items)
MAP4="Skupper Platform Choices"

# Category: Platform Choices (5 items - systemd, podman, docker, kubernetes, openshift)
# systemd, podman already created
create_stub "openshift" "OpenShift" "$MAP4" "Platform Choices"
# docker already created
# kubernetes would be duplicate

# Category: Skupper Site Capabilities (5 items)
create_stub "site-controller" "Site Controller" "$MAP4" "Skupper Site Capabilities"
create_stub "site-runtime" "Site Runtime" "$MAP4" "Skupper Site Capabilities"
create_stub "service-exposure" "Service Exposure" "$MAP4" "Skupper Site Capabilities"
create_stub "site-linking" "Site Linking" "$MAP4" "Skupper Site Capabilities"
create_stub "console" "Console & Status" "$MAP4" "Skupper Site Capabilities"

# Category: Security & Networking (6 items)
create_stub "tls-identity" "TLS Identity" "$MAP4" "Security & Networking"
create_stub "link-token" "Link Token" "$MAP4" "Security & Networking"
create_stub "cluster-network" "Cluster Networking" "$MAP4" "Security & Networking"
create_stub "host-network" "Host Networking" "$MAP4" "Security & Networking"
create_stub "bridge-network" "Bridge Networking" "$MAP4" "Security & Networking"
create_stub "route-scc" "Routes & SCC" "$MAP4" "Security & Networking"

# Category: Runtime Primitives (6 items - router-core, service-sync, listener-connector, secret-store, container-runtime, metrics)
create_stub "router-core" "Router Core" "$MAP4" "Runtime Primitives"
create_stub "service-sync" "Service Sync" "$MAP4" "Runtime Primitives"
create_stub "listener-connector" "Listeners & Connectors" "$MAP4" "Runtime Primitives"
create_stub "secret-store" "Secret Store" "$MAP4" "Runtime Primitives"
create_stub "metrics" "Metrics" "$MAP4" "Runtime Primitives"
# container-runtime already created

echo "  ✅ Map 4 complete: 18 items (6 duplicates skipped)"

echo ""
echo "========================================="
echo "✅ COMPLETE: Generated all stub files"
echo "========================================="
echo ""
echo "Summary:"
echo "  - Map 1: 26 items"
echo "  - Map 2: 17 items"
echo "  - Map 3: 22 items"
echo "  - Map 4: 18 items"
echo "  - Total: 83 items (78 unique after deduplication)"
echo ""
echo "Output directory: $BASE_DIR"
ls -lh "$BASE_DIR" | wc -l
echo ""
echo "Next steps:"
echo "1. Update maps/skupper-value-perspectives.bs to add 'source' fields"
echo "2. Update maps/skupper-adoption-bridge.bs to add 'source' fields for 4 items"
