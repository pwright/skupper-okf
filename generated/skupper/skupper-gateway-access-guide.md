---
type: Guide
title: Using Gateway API Access for Skupper Sites
id: skupper-gateway-access-guide
status: generated
owner: agent
generated_by: claude
reviewed: false
confidence: high
source_file: ../human/skupper/internal/kube/securedaccess/gateway.go
tags:
  - skupper
  - gateway
  - gateway-api
  - tlsroute
  - access-type
  - kubernetes
related:
  - skupper-crd-sites-skupper-io
  - skupper-crd-routeraccesses-skupper-io
  - skupper-crd-securedaccesses-skupper-io
  - skupper-ingress-access-guide
  - skupper-contour-access-guide
timestamp: 2026-08-13
---

# Using Gateway API Access for Skupper Sites

## Overview

The `gateway` access type enables Skupper site connectivity using the Kubernetes Gateway API, a next-generation ingress standard that provides expressive, extensible, and role-oriented APIs for network traffic management.

Skupper creates **TLSRoute** resources that attach to a shared **Gateway** resource, enabling TLS passthrough routing based on SNI (Server Name Indication). This approach provides a modern, standardized alternative to Ingress or HTTPProxy resources.

### When to Use Gateway API Access

**Use gateway when:**
- You have Gateway API controllers deployed (Istio, Envoy Gateway, Cilium, Kong, etc.)
- You want to use modern Kubernetes networking standards
- You need advanced traffic management capabilities
- Your organization is migrating from Ingress to Gateway API
- Running on cloud Kubernetes or on-premise clusters with Gateway API support

**Use alternative access types when:**
- **route**: Running on OpenShift (routes are the native mechanism)
- **loadbalancer**: Cloud Kubernetes with direct LoadBalancer support (simpler)
- **ingress/ingress-nginx**: Already using Ingress controllers without Gateway API
- **contour-http-proxy**: Using Contour without Gateway API support
- **nodeport**: Local development (kind, Minikube) without Gateway API
- **local**: Single-cluster testing with no external access

### Gateway API Architecture

The Gateway API separates concerns into three resources:

1. **GatewayClass**: Defines the controller implementation (Istio, Envoy Gateway, etc.)
2. **Gateway**: Shared infrastructure for routing (listeners, ports, TLS)
3. **TLSRoute**: Per-service routing rules (SNI matching, backend references)

**Skupper's approach**:
- Creates **one shared Gateway** for the entire Skupper installation (in the controller namespace)
- Creates **one TLSRoute per port** in each SecuredAccess/RouterAccess

**Source**: `/home/paulwright/repos/sk/skupper-okf/human/skupper/internal/kube/securedaccess/gateway.go` (lines 76-105, 114-163)

## Prerequisites

Before using gateway access, ensure:

1. **Gateway API CRDs installed**: Gateway, GatewayClass, and TLSRoute CRDs must be available
2. **Gateway controller deployed**: A Gateway API implementation must be running (Istio, Envoy Gateway, Cilium, etc.)
3. **GatewayClass available**: A GatewayClass matching your controller must exist
4. **Gateway enabled on Skupper controller**: Must have `gateway` in enabled access types **and** GatewayClass configured
5. **DNS resolution**: Generated TLSRoute hostnames must resolve to the Gateway's load balancer

## Controller Configuration

The Skupper controller requires specific environment variables to enable and configure gateway access. Unlike other access types, gateway requires **mandatory** configuration of the GatewayClass.

### Required Environment Variables

**`SKUPPER_ENABLED_ACCESS_TYPES`**
- **Purpose**: Comma-separated list of enabled access types
- **Default**: `local,loadbalancer,route` (does **not** include gateway)
- **Required value**: Must include `gateway`
- **Example**: `"gateway,local,loadbalancer,route"`

**`SKUPPER_GATEWAY_CLASS`** (Required for gateway)
- **Purpose**: The GatewayClass name that the shared Gateway should use
- **Required**: Gateway access type cannot be enabled without this setting
- **Validation**: Controller's `Verify()` function returns an error if gateway is enabled without this
- **Examples**:
  - `"istio"` (Istio Gateway controller)
  - `"envoy-gateway"` (Envoy Gateway)
  - `"cilium"` (Cilium Gateway)
  - `"kong"` (Kong Gateway)

**Source**: `/home/paulwright/repos/sk/skupper-okf/human/skupper/internal/kube/securedaccess/config.go` (lines 52-55, 83)

### Optional Environment Variables

**`SKUPPER_GATEWAY_DOMAIN`**
- **Purpose**: Base domain for constructing fully qualified hostnames for TLSRoutes
- **Default**: Auto-deduced from Gateway status if not set
- **How auto-deduction works**: Reads `status.addresses[].value` from Gateway (Hostname or IPAddress + nip.io)
- **Examples**:
  - `"gateway.example.com"` → generates `my-router-inter-router.default.gateway.example.com`
  - Auto-deduced: `"34.123.45.67.nip.io"` (from Gateway LoadBalancer IP)

**Source**: `/home/paulwright/repos/sk/skupper-okf/human/skupper/internal/kube/securedaccess/config.go` (line 82), `gateway.go` (lines 96-103, 165-184)

**`SKUPPER_GATEWAY_PORT`**
- **Purpose**: The port the Gateway should listen on for TLS traffic
- **Default**: `8443`
- **Valid range**: 1-65535
- **Example**: `"443"` (standard HTTPS port)

**Source**: `/home/paulwright/repos/sk/skupper-okf/human/skupper/internal/kube/securedaccess/config.go` (line 84)

**`SKUPPER_DEFAULT_ACCESS_TYPE` (Optional)**
- **Purpose**: Sets the default access type for sites that don't specify one
- **Validation**: Must be included in `SKUPPER_ENABLED_ACCESS_TYPES` if set
- **Example**: `"gateway"`

### Configuration via Deployment YAML

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
          value: "gateway,local,loadbalancer,route"
        - name: SKUPPER_GATEWAY_CLASS
          value: "istio"  # REQUIRED
        - name: SKUPPER_GATEWAY_DOMAIN  # Optional: auto-deduced if not set
          value: "gateway.example.com"
        - name: SKUPPER_GATEWAY_PORT  # Optional: defaults to 8443
          value: "443"
        - name: SKUPPER_DEFAULT_ACCESS_TYPE  # Optional
          value: "gateway"
```

### Configuration via Helm Chart

```yaml
# values.yaml
enabledAccessTypes: "gateway,local,loadbalancer,route"
gatewayClass: "istio"  # REQUIRED
gatewayDomain: "gateway.example.com"  # Optional
gatewayPort: 443  # Optional, defaults to 8443
defaultAccessType: "gateway"  # Optional
```

**Note**: Check your Skupper Helm chart documentation for exact Helm value names.

### Validation

The controller validates the configuration on startup:

- **Error if gateway enabled without gatewayClass**:
  ```
  Error: Gateway class must be set to enable gateway access type.
  ```
  **Solution**: Set `SKUPPER_GATEWAY_CLASS` environment variable

- **Error if default access type not in enabled list**:
  ```
  Error: default access type must be in enabled access types
  ```
  **Solution**: Ensure `SKUPPER_DEFAULT_ACCESS_TYPE` is in `SKUPPER_ENABLED_ACCESS_TYPES`

**Source**: `/home/paulwright/repos/sk/skupper-okf/human/skupper/internal/kube/securedaccess/config.go` (lines 52-55)

## Using Gateway API with Sites

Once gateway is enabled on the controller, configure it on your sites using one of three methods:

### Method 1: Site linkAccess

Set `linkAccess: gateway` on the Site resource:

```yaml
apiVersion: skupper.io/v2alpha1
kind: Site
metadata:
  name: my-site
  namespace: default
spec:
  linkAccess: gateway
```

**When to use**: Simple site configuration where you want link access enabled with Gateway API.

### Method 2: RouterAccess Resource

For more control, create a RouterAccess resource explicitly:

```yaml
apiVersion: skupper.io/v2alpha1
kind: RouterAccess
metadata:
  name: my-router-access
  namespace: default
spec:
  accessType: gateway
  roles:
    - name: inter-router
      port: 55671
    - name: edge
      port: 45671
  tlsCredentials: my-tls-secret
  generateTlsCredentials: true
  issuer: skupper-site-ca
```

**When to use**: You need custom roles, multiple ports, or specific TLS settings.

### Method 3: SecuredAccess Resource

For securing application services with Gateway API:

```yaml
apiVersion: skupper.io/v2alpha1
kind: SecuredAccess
metadata:
  name: my-secured-access
  namespace: default
spec:
  accessType: gateway
  selector:
    app: my-app
  ports:
    - name: http
      port: 8080
      targetPort: 8080
      protocol: TCP
    - name: grpc
      port: 9090
      targetPort: 9090
      protocol: TCP
  certificate: my-cert
  issuer: skupper-site-ca
  generateTlsCredentials: true
```

**When to use**: Exposing application services (not just router links) through Gateway API.

## How Gateway API Access Works

### Gateway Creation

Skupper creates **one shared Gateway** resource in the controller namespace (typically `skupper-system`) when gateway access is first enabled:

```yaml
apiVersion: gateway.networking.k8s.io/v1
kind: Gateway
metadata:
  name: skupper
  namespace: skupper-system
spec:
  gatewayClassName: istio  # From SKUPPER_GATEWAY_CLASS
  listeners:
    - name: tls
      protocol: TLS
      port: 8443  # From SKUPPER_GATEWAY_PORT
      tls:
        mode: Passthrough
```

**Key fields**:
- **`gatewayClassName`**: Links to the GatewayClass (controller implementation)
- **`listeners[].protocol: TLS`**: Accepts TLS connections
- **`listeners[].port`**: Port to listen on (default 8443)
- **`listeners[].tls.mode: Passthrough`**: TLS traffic is passed through without termination

**Source**: `/home/paulwright/repos/sk/skupper-okf/human/skupper/internal/kube/securedaccess/gateway.go` (lines 76-105)

### TLSRoute Creation

Skupper creates **one TLSRoute per port** in each RouterAccess/SecuredAccess:

**TLSRoute Naming**: `<access-name>-<port-name>`  
**Hostname (FQDN)**: `<access-name>-<port-name>.<namespace>.<domain>`

**Example**:
- Access name: `my-router-access`
- Namespace: `default`
- Port 1: `inter-router` (port 55671)
- Port 2: `edge` (port 45671)
- Domain: `gateway.example.com`

**Generated TLSRoutes**:
1. Name: `my-router-access-inter-router`, Hostname: `my-router-access-inter-router.default.gateway.example.com`
2. Name: `my-router-access-edge`, Hostname: `my-router-access-edge.default.gateway.example.com`

**Source**: `/home/paulwright/repos/sk/skupper-okf/human/skupper/internal/kube/securedaccess/gateway.go` (lines 120-122)

### TLSRoute Resource Structure

```yaml
apiVersion: gateway.networking.k8s.io/v1alpha2
kind: TLSRoute
metadata:
  name: my-router-access-inter-router
  namespace: default
  ownerReferences:
    - apiVersion: skupper.io/v2alpha1
      kind: SecuredAccess
      name: my-router-access
      uid: <access-uid>
spec:
  parentRefs:
    - name: skupper
      namespace: skupper-system
  hostnames:
    - my-router-access-inter-router.default.gateway.example.com
  rules:
    - backendRefs:
        - name: my-router-access
          port: 55671
```

**Key fields**:
- **`parentRefs`**: References the shared Gateway in the controller namespace
- **`hostnames`**: SNI hostname for routing (TLS passthrough uses SNI)
- **`rules[].backendRefs`**: Routes to the Kubernetes Service backing the access

**Source**: `/home/paulwright/repos/sk/skupper-okf/human/skupper/internal/kube/securedaccess/gateway.go` (lines 131-151)

### How TLS Passthrough Works with Gateway API

1. Client initiates TLS connection to `my-router-access-inter-router.default.gateway.example.com:<gateway-port>`
2. DNS resolves to the Gateway's load balancer
3. Gateway listener receives TLS ClientHello with SNI hostname
4. Gateway matches SNI to TLSRoute's `spec.hostnames`
5. Gateway routes **encrypted** TLS stream to the backend service (no termination)
6. Skupper router terminates TLS and authenticates the mutual TLS certificate

This preserves end-to-end mutual TLS between Skupper routers.

### Endpoint Resolution

After creating TLSRoutes, Skupper generates connection endpoints:

```yaml
endpoints:
  - name: inter-router
    host: my-router-access-inter-router.default.gateway.example.com
    port: "8443"  # Or configured SKUPPER_GATEWAY_PORT
  - name: edge
    host: my-router-access-edge.default.gateway.example.com
    port: "8443"
```

Remote sites connect to these endpoints (via the Gateway) to establish links.

**Source**: `/home/paulwright/repos/sk/skupper-okf/human/skupper/internal/kube/securedaccess/gateway.go` (lines 156-160)

### Domain Auto-Deduction

If `SKUPPER_GATEWAY_DOMAIN` is not set, Skupper attempts to auto-deduce the domain from the Gateway's status:

```go
// Reads status.addresses[] from Gateway
// Priority 1: Type "Hostname" → use value
// Priority 2: Type "IPAddress" → use value + ".nip.io"
```

**Example Gateway status**:
```yaml
status:
  addresses:
    - type: Hostname
      value: gateway-lb.us-east-1.elb.amazonaws.com
```
**Deduced domain**: `gateway-lb.us-east-1.elb.amazonaws.com`

**Source**: `/home/paulwright/repos/sk/skupper-okf/human/skupper/internal/kube/securedaccess/gateway.go` (lines 165-184)

## Gateway API Deployment Considerations

### Verify Gateway API CRDs

```bash
# Check Gateway API CRDs are installed
kubectl get crd gateways.gateway.networking.k8s.io
kubectl get crd gatewayclasses.gateway.networking.k8s.io
kubectl get crd tlsroutes.gateway.networking.k8s.io

# Check API versions
kubectl explain gateway --api-version=gateway.networking.k8s.io/v1
kubectl explain tlsroute --api-version=gateway.networking.k8s.io/v1alpha2
```

**Note**: TLSRoute is in `v1alpha2` as of this writing. The API may evolve.

### Verify GatewayClass Exists

```bash
# List available GatewayClasses
kubectl get gatewayclass

# Example output:
NAME            CONTROLLER                      ACCEPTED
istio           istio.io/gateway-controller     True
envoy-gateway   gateway.envoyproxy.io/v1        True
```

The value you set in `SKUPPER_GATEWAY_CLASS` must match one of these names.

### Verify Gateway Controller

Ensure the Gateway API controller is running:

```bash
# For Istio
kubectl get pods -n istio-system

# For Envoy Gateway
kubectl get pods -n envoy-gateway-system

# For Cilium
kubectl get pods -n kube-system -l k8s-app=cilium
```

### Check Skupper-Created Gateway

```bash
# Verify Skupper created the Gateway
kubectl get gateway skupper -n skupper-system

# Check Gateway status
kubectl get gateway skupper -n skupper-system -o yaml

# Look for status.addresses[] (should have LoadBalancer IP or hostname)
kubectl get gateway skupper -n skupper-system -o jsonpath='{.status.addresses[*]}'
```

## DNS Configuration

For gateway access to work, DNS must resolve the generated TLSRoute hostnames to the Gateway's load balancer.

### Option 1: Wildcard DNS

Create a wildcard DNS record pointing to the Gateway LoadBalancer:

```
*.gateway.example.com. IN A 203.0.113.100
```

This allows any subdomain to resolve to the Gateway.

### Option 2: Specific DNS Records

Create individual DNS records for each generated TLSRoute hostname:

```
my-router-access-inter-router.default.gateway.example.com. IN A 203.0.113.100
my-router-access-edge.default.gateway.example.com. IN A 203.0.113.100
```

### Option 3: Auto-Deduced Domain

If you don't set `SKUPPER_GATEWAY_DOMAIN`, Skupper will attempt to deduce it from the Gateway's `status.addresses[]`. If the Gateway has:

- **Hostname**: Uses that hostname directly
- **IPAddress**: Appends `.nip.io` (e.g., `203.0.113.100.nip.io`)

This works automatically without additional DNS configuration when using nip.io.

## Troubleshooting

### Gateway not created

**Symptom**: No Gateway resource appears in skupper-system namespace

**Causes and solutions**:
1. **Access type not enabled**: Verify `gateway` is in `SKUPPER_ENABLED_ACCESS_TYPES`
2. **GatewayClass not set**: Check `SKUPPER_GATEWAY_CLASS` environment variable is configured
3. **Invalid GatewayClass**: Verify the class exists:
   ```bash
   kubectl get gatewayclass <class-name>
   ```
4. **Gateway API CRDs missing**: Install Gateway API CRDs:
   ```bash
   kubectl apply -f https://github.com/kubernetes-sigs/gateway-api/releases/latest/download/standard-install.yaml
   ```
5. **Check controller logs**:
   ```bash
   kubectl logs -n skupper-system deployment/skupper-controller | grep -i gateway
   ```

### TLSRoute not created

**Symptom**: No TLSRoute resources appear after configuring RouterAccess

**Causes and solutions**:
1. **Gateway not ready**: Check Gateway status:
   ```bash
   kubectl get gateway skupper -n skupper-system -o jsonpath='{.status.conditions[?(@.type=="Ready")].status}'
   # Should output: True
   ```
2. **Domain not resolved**: If auto-deducing domain, Gateway must have `status.addresses[]` populated
3. **Check SecuredAccess status**:
   ```bash
   kubectl get securedaccess <name> -o yaml
   ```

### Endpoints not resolving

**Symptom**: Site status shows `Resolved: False` or endpoints array is empty

**Causes and solutions**:
1. **Gateway domain not resolved**: Check if domain was auto-deduced or manually set
2. **Gateway not ready**: Verify Gateway has `status.addresses[]`:
   ```bash
   kubectl get gateway skupper -n skupper-system -o jsonpath='{.status.addresses[*]}'
   ```
3. **TLSRoute not accepted**: Check TLSRoute status:
   ```bash
   kubectl get tlsroute <name> -o jsonpath='{.status.parents[*].conditions[*]}'
   ```

### Remote site cannot connect

**Symptom**: Links remain in `Pending` or `Error` state

**Causes and solutions**:
1. **DNS not resolving**: Verify DNS resolution from remote site:
   ```bash
   nslookup my-router-access-inter-router.default.gateway.example.com
   ```
2. **Wrong port**: Ensure connecting to `SKUPPER_GATEWAY_PORT` (default 8443, not 443)
3. **Gateway LoadBalancer not ready**: Check Gateway service:
   ```bash
   kubectl get svc -n <gateway-controller-namespace> | grep gateway
   ```
4. **TLSRoute not routing**: Check TLSRoute parent status:
   ```bash
   kubectl get tlsroute <name> -o jsonpath='{.status.parents[?(@.parentRef.name=="skupper")].conditions[?(@.type=="Accepted")].status}'
   # Should output: True
   ```

### TLS errors

**Symptom**: Connection established but TLS handshake fails

**Causes and solutions**:
1. **SNI mismatch**: Verify client sends correct SNI hostname
2. **TLS passthrough not working**: Check Gateway listener mode:
   ```bash
   kubectl get gateway skupper -n skupper-system -o jsonpath='{.spec.listeners[?(@.name=="tls")].tls.mode}'
   # Should output: Passthrough
   ```
3. **Test with openssl**:
   ```bash
   openssl s_client -connect my-router-access-inter-router.default.gateway.example.com:8443 \
     -servername my-router-access-inter-router.default.gateway.example.com
   ```

### Gateway controller not accepting resources

**Symptom**: Gateway or TLSRoute created but status shows errors

**Causes and solutions**:
1. **Check Gateway status conditions**:
   ```bash
   kubectl get gateway skupper -n skupper-system -o jsonpath='{.status.conditions[*].message}'
   ```
2. **Check TLSRoute status conditions**:
   ```bash
   kubectl get tlsroute <name> -o jsonpath='{.status.parents[*].conditions[*].message}'
   ```
3. **Verify Gateway controller logs**:
   ```bash
   # For Istio
   kubectl logs -n istio-system deployment/istiod | grep gateway
   
   # For Envoy Gateway
   kubectl logs -n envoy-gateway-system deployment/envoy-gateway
   ```

## Verification Commands

### Check Controller Configuration

```bash
# Verify controller environment
kubectl get deploy skupper-controller -n skupper-system -o yaml | grep -A 10 "env:"

# Check specific env vars
kubectl get deploy skupper-controller -n skupper-system \
  -o jsonpath='{.spec.template.spec.containers[0].env[?(@.name=="SKUPPER_GATEWAY_CLASS")].value}'
kubectl get deploy skupper-controller -n skupper-system \
  -o jsonpath='{.spec.template.spec.containers[0].env[?(@.name=="SKUPPER_GATEWAY_DOMAIN")].value}'
```

### Check Gateway Resources

```bash
# Check Skupper Gateway
kubectl get gateway skupper -n skupper-system

# Check Gateway status
kubectl get gateway skupper -n skupper-system -o yaml

# Check Gateway addresses (LoadBalancer IP/hostname)
kubectl get gateway skupper -n skupper-system -o jsonpath='{.status.addresses[*]}'

# Check Gateway listeners
kubectl get gateway skupper -n skupper-system -o jsonpath='{.spec.listeners[*]}'
```

### Check TLSRoute Resources

```bash
# List Skupper-managed TLSRoutes
kubectl get tlsroute -A

# Check specific TLSRoute
kubectl get tlsroute <name> -o yaml

# Verify hostname and backend
kubectl get tlsroute <name> -o jsonpath='{.spec.hostnames[*]}'
kubectl get tlsroute <name> -o jsonpath='{.spec.rules[*].backendRefs[*]}'

# Check TLSRoute parent status
kubectl get tlsroute <name> -o jsonpath='{.status.parents[*].conditions[?(@.type=="Accepted")]}'
```

### Check Site Endpoints

```bash
# View site endpoints
kubectl get site my-site -o jsonpath='{.status.endpoints[*]}' | jq .

# Should show endpoints with host/port like:
# {"name":"inter-router","host":"my-router-access-inter-router.default.gateway.example.com","port":"8443"}
```

### Test Connectivity

```bash
# Test DNS resolution
nslookup my-router-access-inter-router.default.gateway.example.com

# Test TCP connection to Gateway
nc -zv my-router-access-inter-router.default.gateway.example.com 8443

# Test TLS handshake
openssl s_client -connect my-router-access-inter-router.default.gateway.example.com:8443 \
  -servername my-router-access-inter-router.default.gateway.example.com
```

## Comparison: Gateway API vs Alternatives

| Feature | Gateway API | Ingress (NGINX) | Contour HTTPProxy |
|---------|-------------|-----------------|-------------------|
| **Standard** | Kubernetes SIG standard | Kubernetes native | Contour-specific CRD |
| **TLS Passthrough** | Native (`tls.mode: Passthrough`) | Annotation required | Native (`tls.passthrough: true`) |
| **Routing** | TLSRoute (SNI-based) | Ingress rules | HTTPProxy rules |
| **Architecture** | Shared Gateway + per-service TLSRoute | Per-service Ingress | Per-port HTTPProxy |
| **Controllers** | Multiple (Istio, Envoy, Cilium, Kong) | Multiple generic | Contour only |
| **Maturity** | Evolving (TLSRoute in alpha/beta) | Stable (GA) | Stable (Contour v1) |
| **Skupper Integration** | Full support | Full support (nginx variant) | Full support |

**Recommendation**: Use `gateway` if:
- Your organization is adopting Gateway API as the ingress standard
- You're running a Gateway API controller (Istio, Envoy Gateway, Cilium)
- You want modern, role-oriented traffic management APIs

Use alternatives if Gateway API is not yet available or your controller doesn't support it.

## References

### Related Documentation

- [Skupper Site CRD](./skupper-crd-sites-skupper-io.md) - Site resource specification
- [Skupper RouterAccess CRD](./skupper-crd-routeraccesses-skupper-io.md) - RouterAccess resource specification
- [Skupper SecuredAccess CRD](./skupper-crd-securedaccesses-skupper-io.md) - SecuredAccess resource specification
- [Skupper Ingress Access Guide](./skupper-ingress-access-guide.md) - Alternative ingress-based access
- [Skupper Contour Access Guide](./skupper-contour-access-guide.md) - Alternative HTTPProxy-based access

### Source Code References

- **Implementation**: `/home/paulwright/repos/sk/skupper-okf/human/skupper/internal/kube/securedaccess/gateway.go`
  - Lines 44-54: `GatewayAccessType` struct
  - Lines 76-105: Gateway creation (`init` function)
  - Lines 114-163: TLSRoute creation (`RealiseAndResolve`)
  - Lines 165-184: Domain auto-deduction (`getBaseDomain`)

- **Configuration**: `/home/paulwright/repos/sk/skupper-okf/human/skupper/internal/kube/securedaccess/config.go`
  - Line 19: `ACCESS_TYPE_GATEWAY` constant
  - Lines 52-55: Gateway validation (GatewayClass required)
  - Line 82: `SKUPPER_GATEWAY_DOMAIN` binding
  - Line 83: `SKUPPER_GATEWAY_CLASS` binding
  - Line 84: `SKUPPER_GATEWAY_PORT` binding

- **Access Type Registration**: `/home/paulwright/repos/sk/skupper-okf/human/skupper/internal/kube/securedaccess/access.go`
  - Lines 79-86: Gateway access type initialization

### External Resources

- [Kubernetes Gateway API](https://gateway-api.sigs.k8s.io/) - Official Gateway API documentation
- [TLSRoute Reference](https://gateway-api.sigs.k8s.io/reference/spec/#gateway.networking.k8s.io/v1alpha2.TLSRoute) - TLSRoute specification
- [Gateway API Implementations](https://gateway-api.sigs.k8s.io/implementations/) - List of Gateway API controllers
- [Istio Gateway](https://istio.io/latest/docs/tasks/traffic-management/ingress/gateway-api/) - Istio's Gateway API implementation
- [Envoy Gateway](https://gateway.envoyproxy.io/) - Envoy Gateway project

## Summary

The gateway access type provides modern Kubernetes Gateway API integration for Skupper:

1. **Gateway API standard**: Uses official Kubernetes SIG Gateway API (next-gen ingress)
2. **Mandatory GatewayClass**: Must set `SKUPPER_GATEWAY_CLASS` environment variable (validation enforced)
3. **Enable explicitly**: Not in default access types—add to `SKUPPER_ENABLED_ACCESS_TYPES`
4. **Shared Gateway**: Creates one Gateway in controller namespace (skupper-system)
5. **One TLSRoute per port**: Each port gets its own TLSRoute with unique hostname
6. **Domain handling**: Auto-deduces from Gateway status or uses `SKUPPER_GATEWAY_DOMAIN`
7. **Configurable port**: Defaults to 8443, override via `SKUPPER_GATEWAY_PORT`
8. **TLS passthrough**: Native support via `tls.mode: Passthrough` on Gateway listener
9. **SNI routing**: TLSRoute matches on `spec.hostnames` for routing decisions
10. **Controller choice**: Works with any Gateway API controller (Istio, Envoy Gateway, Cilium, Kong)

For deployments adopting the Gateway API standard, the gateway access type provides future-proof integration with Skupper while leveraging modern, role-oriented traffic management capabilities.
