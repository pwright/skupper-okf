---
type: Guide
title: Using NodePort Access for Skupper Sites
id: skupper-nodeport-access-guide
status: generated
owner: agent
generated_by: claude
reviewed: false
confidence: high
source_file: ../human/skupper/internal/kube/securedaccess/nodeport.go
tags:
  - skupper
  - nodeport
  - access-type
  - kubernetes
  - kind
  - minikube
related:
  - skupper-crd-sites-skupper-io
  - skupper-crd-routeraccesses-skupper-io
  - skupper-crd-securedaccesses-skupper-io
timestamp: 2026-08-12
---

# Using NodePort Access for Skupper Sites

## Overview

NodePort is a Skupper access type that enables site-to-site connectivity using Kubernetes NodePort services. Unlike LoadBalancer or Route access types, NodePort works in any Kubernetes environment, making it ideal for local development clusters (kind, Minikube), bare-metal deployments, and environments where LoadBalancers aren't available.

### When to Use NodePort

**Use nodeport when:**
- Running Skupper on kind, Minikube, or other local development clusters
- Deploying on bare-metal Kubernetes without LoadBalancer support
- Working in environments where OpenShift Routes aren't available
- You need predictable port ranges (30000-32767) for firewall configuration
- Testing Skupper functionality in constrained environments

**Use alternative access types when:**
- **route**: Running on OpenShift with external access requirements
- **loadbalancer**: Running on cloud Kubernetes (GKE, EKS, AKS) with cloud load balancer support
- **local**: Testing in a single cluster with no inter-cluster connectivity needed
- **ingress/ingress-nginx**: Using Kubernetes Ingress controllers for external access

### How NodePort Works

When you configure a Skupper site with nodeport access:

1. The controller creates a Kubernetes Service with `type: NodePort`
2. Kubernetes allocates a port in the NodePort range (typically 30000-32767)
3. The `NodeportAccessType.RealiseAndResolve` implementation builds connection endpoints using:
   - **Host**: The value of `SKUPPER_CLUSTER_HOST` (configured on the controller)
   - **Port**: The allocated NodePort from the Service

Remote sites connect to `<SKUPPER_CLUSTER_HOST>:<NodePort>` to establish links.

**Source**: `~/repos/sk/skupper-okf/human/skupper/internal/kube/securedaccess/nodeport.go` (lines 23-35)

## Prerequisites

Before using nodeport access, ensure:

1. **NodePort enabled on controller**: The Skupper controller must have `nodeport` in its enabled access types list
2. **ClusterHost configured**: The controller must know the hostname or IP address through which cluster nodes are reachable
3. **Network accessibility**: Remote sites must be able to route to the NodePort range on your cluster nodes
4. **Kubernetes NodePort understanding**: Familiarity with how Kubernetes NodePort services work

## Controller Configuration

The Skupper controller reads its access type configuration from environment variables. NodePort is **not enabled by default**—you must explicitly add it to the enabled access types list and configure the cluster host.

### Required Environment Variables

**`SKUPPER_ENABLED_ACCESS_TYPES`**
- **Purpose**: Comma-separated list of enabled access types
- **Default**: `local,loadbalancer,route` (does **not** include nodeport)
- **Required value**: Must include `nodeport`
- **Example**: `"nodeport,local,loadbalancer,route"`

**`SKUPPER_CLUSTER_HOST`**
- **Purpose**: Hostname or IP address of a reachable cluster node
- **Required when**: `nodeport` is in `SKUPPER_ENABLED_ACCESS_TYPES`
- **Validation**: Controller's `Verify()` function returns an error if nodeport is enabled without this setting
- **Examples**:
  - `"192.168.1.100"` (node IP address)
  - `"mycluster.example.com"` (hostname)
  - `"127.0.0.1"` or `"localhost"` (for kind with extraPortMappings)

**`SKUPPER_DEFAULT_ACCESS_TYPE` (Optional)**
- **Purpose**: Sets the default access type for sites that don't specify one
- **Validation**: Must be included in `SKUPPER_ENABLED_ACCESS_TYPES` if set
- **Example**: `"nodeport"`

**Source**: `~/repos/sk/skupper-okf/human/skupper/internal/kube/securedaccess/config.go` (lines 76-78, 88-94)

### Configuration via Deployment YAML

To enable nodeport on the Skupper controller, add these environment variables to the `skupper-controller` Deployment:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: skupper-controller
  namespace: skupper-system
spec:
  template:
    spec:
      containers:
      - name: controller
        image: quay.io/skupper/controller:latest
        env:
        - name: SKUPPER_ENABLED_ACCESS_TYPES
          value: "nodeport,local,loadbalancer,route"
        - name: SKUPPER_CLUSTER_HOST
          value: "192.168.1.100"  # Replace with your node IP or hostname
        - name: SKUPPER_DEFAULT_ACCESS_TYPE  # Optional
          value: "nodeport"
```

### Configuration via Helm Chart

If you're deploying Skupper via Helm, use the following values:

```yaml
# values.yaml
clusterHost: "192.168.1.100"  # Required for nodeport
enabledAccessTypes: "nodeport,local,loadbalancer,route"
defaultAccessType: "nodeport"  # Optional
```

These Helm values are rendered into the corresponding environment variables on the controller Deployment.

**Source**: `~/repos/sk/skupper-okf/human/skupper/scripts/skupper-helm-chart-generator.sh` (lines 44-57, 128-146)

### Validation

The controller validates the configuration on startup:

- **Error if nodeport enabled without clusterHost**:
  ```
  Error: nodeport access type requires cluster-host to be set
  ```
  **Solution**: Set `SKUPPER_CLUSTER_HOST` environment variable

- **Error if default access type not in enabled list**:
  ```
  Error: default access type must be in enabled access types
  ```
  **Solution**: Ensure `SKUPPER_DEFAULT_ACCESS_TYPE` value is included in `SKUPPER_ENABLED_ACCESS_TYPES`

**Source**: `~/repos/sk/skupper-okf/human/skupper/internal/kube/securedaccess/config.go` (lines 43-57)

## Using NodePort with Sites

Once nodeport is enabled on the controller, you can configure it on your sites using one of three methods:

### Method 1: Site linkAccess

The simplest approach is to set `linkAccess: nodeport` on the Site resource. This implies a RouterAccess resource with `accessType: nodeport`.

```yaml
apiVersion: skupper.io/v2alpha1
kind: Site
metadata:
  name: my-site
  namespace: default
spec:
  linkAccess: nodeport
```

**When to use**: Simple site configuration where you want link access enabled with nodeport and don't need fine-grained RouterAccess control.

### Method 2: RouterAccess Resource

For more control over router access configuration, create a RouterAccess resource explicitly:

```yaml
apiVersion: skupper.io/v2alpha1
kind: RouterAccess
metadata:
  name: my-router-access
  namespace: default
spec:
  accessType: nodeport
  roles:
    - name: inter-router
      port: 55671
  tlsCredentials: my-tls-secret
  generateTlsCredentials: true
  issuer: skupper-site-ca
```

**When to use**: You need to configure custom roles, ports, or TLS settings for router access.

**Source**: `~/repos/sk/skupper-okf/human/skupper/internal/kube/site/site_test.go` (lines 243-245, 1188-1190)

### Method 3: SecuredAccess Resource

For securing application services with nodeport access:

```yaml
apiVersion: skupper.io/v2alpha1
kind: SecuredAccess
metadata:
  name: my-secured-access
  namespace: default
spec:
  accessType: nodeport
  selector:
    app: my-app
  ports:
    - name: http
      port: 8080
      targetPort: 8080
      protocol: TCP
  certificate: my-cert
  issuer: skupper-site-ca
  generateTlsCredentials: true
```

**When to use**: You're exposing application services (not just router links) with mutual TLS and need nodeport accessibility.

**Source**: `~/repos/sk/skupper-okf/human/skupper/internal/kube/securedaccess/access_test.go` (lines 1108-1123)

## Kind-Specific Considerations

Kind (Kubernetes in Docker) clusters require special attention because kind nodes run inside Docker containers. By default, NodePort services inside the container aren't accessible from your host machine or other clusters.

### The Problem

When Skupper creates a NodePort service inside kind:
- Kubernetes allocates a port in the range 30000-32767
- The service binds to the kind node's network namespace (inside the Docker container)
- The `SKUPPER_CLUSTER_HOST` points to the kind node's IP or hostname
- **Remote sites cannot reach this address unless you map the ports**

### Solution 1: extraPortMappings (Recommended for Development)

Map specific NodePort ranges from the kind container to your host when creating the cluster:

```yaml
kind: Cluster
apiVersion: kind.x-k8s.io/v1alpha4
nodes:
  - role: control-plane
    extraPortMappings:
      # Map a range of ports for Skupper NodePort services
      - containerPort: 30001
        hostPort: 30001
        protocol: TCP
      - containerPort: 30002
        hostPort: 30002
        protocol: TCP
      # Add more port mappings as needed
```

Then configure the Skupper controller with:

```yaml
env:
  - name: SKUPPER_CLUSTER_HOST
    value: "localhost"  # or "127.0.0.1" or your host's external IP
```

**Pros**: Simple, works for single-node kind clusters, allows other sites to connect via your host IP  
**Cons**: Requires knowing port numbers in advance, limited to specific ports

### Solution 2: Container Network Routing

If your remote sites can route to the Docker network directly (e.g., other kind clusters on the same Docker network), use the kind container's IP:

```bash
# Get the kind container's IP
docker inspect kind-control-plane | grep IPAddress
```

Configure the controller with the container IP:

```yaml
env:
  - name: SKUPPER_CLUSTER_HOST
    value: "172.18.0.2"  # Replace with actual container IP
```

**Pros**: All NodePort allocations work automatically  
**Cons**: Only works if remote sites can route to the Docker network (uncommon across separate machines)

### Solution 3: Docker Network Sharing

For multi-kind-cluster scenarios on the same host, create clusters on a shared Docker network:

```bash
# Create a shared network
docker network create skupper-test

# Create kind clusters on this network
kind create cluster --name site1 --config site1-config.yaml
kind create cluster --name site2 --config site2-config.yaml

# In each cluster config, specify the network
# (kind doesn't directly support this; use docker network connect after creation)
docker network connect skupper-test kind-site1-control-plane
docker network connect skupper-test kind-site2-control-plane
```

**Pros**: Multiple kind clusters can reach each other via container IPs  
**Cons**: More complex setup, still container-scoped

## Minikube Considerations

Minikube has similar considerations to kind, though it typically runs in a VM rather than a container:

```bash
# Get the Minikube node IP
minikube ip
```

Configure the controller with the Minikube IP:

```yaml
env:
  - name: SKUPPER_CLUSTER_HOST
    value: "192.168.49.2"  # Replace with actual minikube ip output
```

If remote sites are on the same host network, this IP should be accessible. Otherwise, use `minikube tunnel` or port forwarding.

## Troubleshooting

### Error: "nodeport access type requires cluster-host to be set"

**Cause**: `SKUPPER_CLUSTER_HOST` is not configured on the controller  
**Solution**: Set the environment variable as shown in [Controller Configuration](#controller-configuration)

### Error: "default access type must be in enabled access types"

**Cause**: `SKUPPER_DEFAULT_ACCESS_TYPE` is set to a value not in `SKUPPER_ENABLED_ACCESS_TYPES`  
**Solution**: Add the default access type to the enabled list or remove the default setting

### Site endpoints not resolving

**Symptom**: Site status shows `Resolved: False` or endpoints array is empty

**Causes and solutions**:
1. **NodePort not enabled**: Check controller logs for access type validation errors
2. **ClusterHost not set**: Verify `SKUPPER_CLUSTER_HOST` environment variable on controller
3. **Service not created**: Check that a NodePort service exists for the site:
   ```bash
   kubectl get svc -l skupper.io/site=<site-name>
   ```
4. **NodePort not allocated**: Verify the service has a NodePort assigned:
   ```bash
   kubectl get svc <service-name> -o jsonpath='{.spec.ports[*].nodePort}'
   ```

### Remote site cannot connect

**Symptom**: Links remain in `Pending` or `Error` state

**Causes and solutions**:
1. **Network unreachable**: Verify remote site can reach `SKUPPER_CLUSTER_HOST`:
   ```bash
   # From remote site
   nc -zv <SKUPPER_CLUSTER_HOST> <NodePort>
   ```
2. **Firewall blocking**: Ensure NodePort range (30000-32767) is open in firewall rules
3. **Kind port mapping missing**: For kind clusters, verify `extraPortMappings` includes the allocated NodePort
4. **Wrong ClusterHost**: Double-check that `SKUPPER_CLUSTER_HOST` is the correct, externally-reachable address

### Verifying NodePort Configuration

Check that nodeport is properly configured:

```bash
# 1. Verify controller environment
kubectl get deploy skupper-controller -n skupper-system -o yaml | grep -A 10 "env:"

# 2. Check Site status for endpoints
kubectl get site my-site -o jsonpath='{.status.endpoints[*]}' | jq .

# 3. Verify Service type
kubectl get svc -l skupper.io/site=my-site -o jsonpath='{.spec.type}'
# Should output: NodePort

# 4. Get allocated NodePort
kubectl get svc -l skupper.io/site=my-site -o jsonpath='{.spec.ports[*].nodePort}'

# 5. Test connectivity from external host
curl -k https://<SKUPPER_CLUSTER_HOST>:<NodePort>
# Should connect (may get TLS or auth error, but connection proves network path works)
```

## References

### Related Documentation

- [Skupper Site CRD](./skupper-crd-sites-skupper-io.md) - Site resource specification including linkAccess configuration
- [Skupper RouterAccess CRD](./skupper-crd-routeraccesses-skupper-io.md) - RouterAccess resource specification
- [Skupper SecuredAccess CRD](./skupper-crd-securedaccesses-skupper-io.md) - SecuredAccess resource specification

### Source Code References

- **Configuration**: `~/repos/sk/skupper-okf/human/skupper/internal/kube/securedaccess/config.go`
  - Lines 22-32: `Config` struct definition
  - Lines 43-57: `Verify()` function validating nodeport requirements
  - Lines 74-86: `BoundConfig()` function binding environment variables
  - Lines 88-94: `defaultEnabledAccessTypes()` function

- **Implementation**: `~/repos/sk/skupper-okf/human/skupper/internal/kube/securedaccess/nodeport.go`
  - Lines 23-35: `NodeportAccessType.RealiseAndResolve()` implementation

- **Helm Chart**: `~/repos/sk/skupper-okf/human/skupper/scripts/skupper-helm-chart-generator.sh`
  - Lines 44-57: Helm values definition
  - Lines 128-146: Environment variable injection

- **Tests**:
  - `~/repos/sk/skupper-okf/human/skupper/internal/kube/securedaccess/config_test.go` (lines 29-51, 124-147)
  - `~/repos/sk/skupper-okf/human/skupper/internal/kube/securedaccess/access_test.go` (lines 1088-1170)
  - `~/repos/sk/skupper-okf/human/skupper/internal/kube/site/site_test.go` (lines 243-245, 1188-1190)

### External Resources

- [Kubernetes NodePort Service](https://kubernetes.io/docs/concepts/services-networking/service/#type-nodeport) - Official Kubernetes documentation
- [Kind ExtraPortMappings](https://kind.sigs.k8s.io/docs/user/configuration/#extra-port-mappings) - Kind documentation on port mapping
- [Minikube Networking](https://minikube.sigs.k8s.io/docs/handbook/accessing/) - Minikube documentation on accessing services

## Summary

NodePort access type enables Skupper site connectivity in any Kubernetes environment, making it essential for local development and bare-metal deployments. Key takeaways:

1. **Enable explicitly**: NodePort is not in the default access types list—add it to `SKUPPER_ENABLED_ACCESS_TYPES`
2. **Configure ClusterHost**: Always set `SKUPPER_CLUSTER_HOST` when using nodeport
3. **Three configuration methods**: Site.linkAccess, RouterAccess, or SecuredAccess
4. **Kind/Minikube**: Requires extra port mapping configuration for host accessibility
5. **Validation**: Use kubectl and network tools to verify configuration before troubleshooting link issues

For production deployments, consider LoadBalancer (cloud) or Route (OpenShift) access types. NodePort remains ideal for development, testing, and environments where other access types aren't available.
