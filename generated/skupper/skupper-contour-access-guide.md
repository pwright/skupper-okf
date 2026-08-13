---
type: Guide
title: Using Contour HTTPProxy Access for Skupper Sites
id: skupper-contour-access-guide
status: generated
owner: agent
generated_by: claude
reviewed: false
confidence: high
source_file: ../human/skupper/internal/kube/securedaccess/contour.go
tags:
  - skupper
  - contour
  - httpproxy
  - access-type
  - kubernetes
  - projectcontour
related:
  - skupper-crd-sites-skupper-io
  - skupper-crd-routeraccesses-skupper-io
  - skupper-crd-securedaccesses-skupper-io
  - skupper-ingress-access-guide
timestamp: 2026-08-13
---

# Using Contour HTTPProxy Access for Skupper Sites

## Overview

The `contour-http-proxy` access type enables Skupper site connectivity using Contour's HTTPProxy custom resource instead of standard Kubernetes Ingress. Contour is a Kubernetes ingress controller built on the Envoy proxy that provides advanced routing capabilities.

Unlike standard Ingress resources, HTTPProxy offers native support for TLS passthrough and TCP routing without requiring controller-specific annotations, making it a natural fit for Skupper's router-to-router mutual TLS connections.

### When to Use Contour HTTPProxy Access

**Use contour-http-proxy when:**
- You have Contour deployed as your ingress controller
- You want native TLS passthrough support (no annotations required)
- You need advanced routing capabilities that Contour provides
- You prefer Contour's HTTPProxy CRD over standard Ingress resources
- Running on cloud Kubernetes or on-premise clusters with Contour

**Use alternative access types when:**
- **route**: Running on OpenShift (routes are the native mechanism)
- **loadbalancer**: Cloud Kubernetes with direct LoadBalancer support (simpler)
- **ingress/ingress-nginx**: Using NGINX or other ingress controllers
- **nodeport**: Local development (kind, Minikube) without ingress controller
- **local**: Single-cluster testing with no external access

### How HTTPProxy Differs from Ingress

| Feature | Standard Ingress | Contour HTTPProxy |
|---------|------------------|-------------------|
| Resource type | Native Kubernetes | Custom Resource (CRD) |
| TLS passthrough | Requires annotations | Native `spec.virtualhost.tls.passthrough` |
| TCP routing | Limited support | Native `spec.tcpproxy` |
| Controller | Multiple options | Contour only |
| Complexity | Generic, widely supported | Contour-specific, more powerful |

**Key advantage**: HTTPProxy's `spec.tcpproxy` enables direct TCP routing with TLS passthrough, which is exactly what Skupper needs for router-to-router connections.

**Source**: `/home/paulwright/repos/sk/skupper-okf/human/skupper/internal/kube/securedaccess/contour.go` (lines 192-212)

## Prerequisites

Before using contour-http-proxy access, ensure:

1. **Contour deployed**: Contour ingress controller must be running in your cluster
2. **HTTPProxy CRD installed**: The `projectcontour.io/v1` HTTPProxy CRD must be available
3. **HTTPProxy enabled on controller**: Skupper controller must have `contour-http-proxy` in enabled access types
4. **HTTPProxy domain configured**: The controller must know the base domain for constructing FQDNs
5. **DNS resolution**: Generated HTTPProxy hostnames must resolve to Contour's Envoy service

## Controller Configuration

The Skupper controller requires specific environment variables to enable and configure contour-http-proxy access.

### Required Environment Variables

**`SKUPPER_ENABLED_ACCESS_TYPES`**
- **Purpose**: Comma-separated list of enabled access types
- **Default**: `local,loadbalancer,route` (does **not** include contour-http-proxy)
- **Required value**: Must include `contour-http-proxy`
- **Example**: `"contour-http-proxy,local,loadbalancer,route"`

**`SKUPPER_HTTP_PROXY_DOMAIN`**
- **Purpose**: Base domain for constructing fully qualified hostnames for HTTPProxy resources
- **Required when**: Using `contour-http-proxy` access type
- **How it works**: Combined with proxy name to form FQDN
- **Examples**:
  - `"contour.example.com"` → generates `my-router-inter-router.contour.example.com`
  - `"apps.cluster.local"` → generates `my-router-edge.apps.cluster.local`

**Source**: `/home/paulwright/repos/sk/skupper-okf/human/skupper/internal/kube/securedaccess/config.go` (line 81)

### Optional Environment Variables

**`SKUPPER_DEFAULT_ACCESS_TYPE` (Optional)**
- **Purpose**: Sets the default access type for sites that don't specify one
- **Validation**: Must be included in `SKUPPER_ENABLED_ACCESS_TYPES` if set
- **Example**: `"contour-http-proxy"`

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
          value: "contour-http-proxy,local,loadbalancer,route"
        - name: SKUPPER_HTTP_PROXY_DOMAIN
          value: "contour.example.com"
        - name: SKUPPER_DEFAULT_ACCESS_TYPE  # Optional
          value: "contour-http-proxy"
```

### Configuration via Helm Chart

```yaml
# values.yaml
enabledAccessTypes: "contour-http-proxy,local,loadbalancer,route"
httpProxyDomain: "contour.example.com"
defaultAccessType: "contour-http-proxy"  # Optional
```

**Note**: Check your Skupper Helm chart documentation for the exact Helm value names that map to `SKUPPER_HTTP_PROXY_DOMAIN`.

## Using Contour HTTPProxy with Sites

Once contour-http-proxy is enabled on the controller, configure it on your sites using one of three methods:

### Method 1: Site linkAccess

Set `linkAccess: contour-http-proxy` on the Site resource:

```yaml
apiVersion: skupper.io/v2alpha1
kind: Site
metadata:
  name: my-site
  namespace: default
spec:
  linkAccess: contour-http-proxy
```

**When to use**: Simple site configuration where you want link access enabled with Contour and don't need fine-grained control.

### Method 2: RouterAccess Resource

For more control, create a RouterAccess resource explicitly:

```yaml
apiVersion: skupper.io/v2alpha1
kind: RouterAccess
metadata:
  name: my-router-access
  namespace: default
spec:
  accessType: contour-http-proxy
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

For securing application services with HTTPProxy:

```yaml
apiVersion: skupper.io/v2alpha1
kind: SecuredAccess
metadata:
  name: my-secured-access
  namespace: default
spec:
  accessType: contour-http-proxy
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

**When to use**: Exposing application services (not just router links) with mutual TLS through Contour.

## How Contour HTTPProxy Access Works

### HTTPProxy Naming and Hostname Generation

Skupper creates one HTTPProxy resource **per port** in the RouterAccess or SecuredAccess spec. The naming follows the pattern:

**HTTPProxy Name**: `<service-name>-<port-name>`  
**Hostname (FQDN)**: `<service-name>-<port-name>.<domain>`

**Example**:
- Service name: `my-router-access`
- Port 1: `inter-router`
- Port 2: `edge`
- Domain: `contour.example.com`

**Generated HTTPProxies**:
1. Name: `my-router-access-inter-router`, FQDN: `my-router-access-inter-router.contour.example.com`
2. Name: `my-router-access-edge`, FQDN: `my-router-access-edge.contour.example.com`

**Source**: `/home/paulwright/repos/sk/skupper-okf/human/skupper/internal/kube/securedaccess/contour.go` (lines 139-151)

### HTTPProxy Resource Structure

Skupper creates HTTPProxy resources using the Contour `projectcontour.io/v1` API:

```yaml
apiVersion: projectcontour.io/v1
kind: HTTPProxy
metadata:
  name: my-router-access-inter-router
  namespace: default
  labels:
    internal.skupper.io/secured-access: "true"
  annotations:
    internal.skupper.io/controlled: "true"
spec:
  virtualhost:
    fqdn: my-router-access-inter-router.contour.example.com
    tls:
      passthrough: true
  tcpproxy:
    services:
      - name: my-router-access
        port: 55671
```

**Key fields**:
- **`spec.virtualhost.fqdn`**: The fully qualified hostname for routing
- **`spec.virtualhost.tls.passthrough: true`**: Enables TLS passthrough (no termination at Envoy)
- **`spec.tcpproxy.services`**: Routes TCP traffic directly to the Skupper service
  - `name`: The Kubernetes Service backing the RouterAccess/SecuredAccess
  - `port`: The service port number

**Source**: `/home/paulwright/repos/sk/skupper-okf/human/skupper/internal/kube/securedaccess/contour.go` (lines 192-212)

### How TLS Passthrough Works

With `tls.passthrough: true`:

1. Client initiates TLS connection to `my-router-access-inter-router.contour.example.com:443`
2. DNS resolves to Contour's Envoy service (LoadBalancer or NodePort)
3. Envoy receives the TLS ClientHello with SNI (Server Name Indication)
4. Envoy matches the SNI hostname to the HTTPProxy's `spec.virtualhost.fqdn`
5. Envoy routes the **encrypted** TCP stream to the backend service without decrypting
6. The Skupper router terminates TLS and authenticates the mutual TLS certificate

This preserves Skupper's end-to-end mutual TLS authentication between routers.

### Endpoint Resolution

After creating HTTPProxy resources, Skupper generates connection endpoints:

```yaml
endpoints:
  - name: inter-router
    host: my-router-access-inter-router.contour.example.com
    port: "443"
  - name: edge
    host: my-router-access-edge.contour.example.com
    port: "443"
```

Remote sites connect to these endpoints (via Contour/Envoy on port 443) to establish links.

**Source**: `/home/paulwright/repos/sk/skupper-okf/human/skupper/internal/kube/securedaccess/contour.go` (lines 32-55)

## Contour Deployment Considerations

### Verify Contour is Running

```bash
# Check Contour pods
kubectl get pods -n projectcontour

# Check Envoy service (the ingress entry point)
kubectl get svc -n projectcontour envoy
```

**Expected output**:
```
NAME    TYPE           CLUSTER-IP      EXTERNAL-IP      PORT(S)
envoy   LoadBalancer   10.96.123.45    203.0.113.50     80:30080/TCP,443:30443/TCP
```

The `EXTERNAL-IP` is what your DNS should point to.

### Verify HTTPProxy CRD

```bash
# Check HTTPProxy CRD is installed
kubectl get crd httpproxies.projectcontour.io

# Check API version
kubectl explain httpproxy --api-version=projectcontour.io/v1
```

### Contour Configuration for TLS Passthrough

Contour supports TLS passthrough by default—no special configuration needed. However, verify:

```bash
# Check Contour ConfigMap for TLS settings
kubectl get configmap contour -n projectcontour -o yaml
```

Contour's Envoy will automatically handle SNI-based routing when `tls.passthrough: true` is set on HTTPProxy resources.

## DNS Configuration

For contour-http-proxy access to work, DNS must resolve the generated HTTPProxy hostnames to Contour's Envoy service.

### Option 1: Wildcard DNS

Create a wildcard DNS record pointing to the Envoy LoadBalancer:

```
*.contour.example.com. IN A 203.0.113.50
```

This allows any subdomain to resolve to Contour's Envoy.

### Option 2: Specific DNS Records

Create individual DNS records for each generated HTTPProxy hostname:

```
my-router-access-inter-router.contour.example.com. IN A 203.0.113.50
my-router-access-edge.contour.example.com. IN A 203.0.113.50
```

### Option 3: nip.io (Development/Testing)

If Envoy has a public IP, you can use the `nip.io` service:

```yaml
env:
  - name: SKUPPER_HTTP_PROXY_DOMAIN
    value: "203.0.113.50.nip.io"
```

Skupper will generate hostnames like `my-router-access-inter-router.203.0.113.50.nip.io`, which automatically resolve to `203.0.113.50`.

## Dynamic Client and Resource Management

Skupper uses Kubernetes' **dynamic client** to create and manage HTTPProxy resources because HTTPProxy is a Custom Resource (not a native Kubernetes type like Ingress).

**Implementation details**:
- **GroupVersionResource**: `projectcontour.io/v1/httpproxies`
- **GroupVersionKind**: `projectcontour.io/v1/HTTPProxy`
- Resources are created, updated, and deleted using `unstructured.Unstructured` objects

**Source**: `/home/paulwright/repos/sk/skupper-okf/human/skupper/internal/kube/securedaccess/contour.go` (lines 121-130, 214-227)

## Troubleshooting

### HTTPProxy not created

**Symptom**: No HTTPProxy resource appears after configuring RouterAccess

**Causes and solutions**:
1. **Access type not enabled**: Verify `contour-http-proxy` is in `SKUPPER_ENABLED_ACCESS_TYPES`
2. **Missing domain**: Check `SKUPPER_HTTP_PROXY_DOMAIN` is set on controller
3. **CRD not installed**: Verify HTTPProxy CRD exists:
   ```bash
   kubectl get crd httpproxies.projectcontour.io
   ```
4. **Check controller logs**:
   ```bash
   kubectl logs -n skupper-system deployment/skupper-controller | grep -i contour
   ```

### HTTPProxy created but no routing

**Symptom**: HTTPProxy exists but traffic doesn't reach backend

**Causes and solutions**:
1. **Contour not processing HTTPProxy**: Check Contour logs:
   ```bash
   kubectl logs -n projectcontour deployment/contour
   ```
2. **Invalid HTTPProxy spec**: Check HTTPProxy status:
   ```bash
   kubectl get httpproxy <name> -o yaml
   ```
   Look for `status.conditions` indicating errors
3. **Backend service doesn't exist**: Verify the service is created:
   ```bash
   kubectl get svc <service-name>
   ```

### Endpoints not resolving

**Symptom**: Site status shows `Resolved: False` or endpoints array is empty

**Causes and solutions**:
1. **HTTPProxy domain not configured**: Verify `SKUPPER_HTTP_PROXY_DOMAIN` environment variable
2. **Contour not running**: Check Contour and Envoy pods are healthy:
   ```bash
   kubectl get pods -n projectcontour
   ```
3. **Envoy service has no external IP**: Check Envoy service:
   ```bash
   kubectl get svc -n projectcontour envoy
   ```

### Remote site cannot connect

**Symptom**: Links remain in `Pending` or `Error` state

**Causes and solutions**:
1. **DNS not resolving**: Verify DNS resolution from remote site:
   ```bash
   nslookup my-router-access-inter-router.contour.example.com
   dig my-router-access-inter-router.contour.example.com
   ```
2. **Firewall blocking port 443**: Ensure remote site can reach Envoy on port 443
3. **TLS passthrough not working**: Check HTTPProxy has `tls.passthrough: true`:
   ```bash
   kubectl get httpproxy <name> -o jsonpath='{.spec.virtualhost.tls.passthrough}'
   # Should output: true
   ```
4. **Check Envoy routing**: Verify Envoy has routes for the HTTPProxy:
   ```bash
   kubectl exec -n projectcontour deployment/envoy -- curl localhost:9001/config_dump | jq '.configs[] | select(.name == "routes")'
   ```

### TLS errors

**Symptom**: Connection established but TLS handshake fails

**Causes and solutions**:
1. **Certificate mismatch**: Verify TLS credentials match on both sites
2. **SNI mismatch**: Check client is sending correct SNI hostname
3. **Passthrough not enabled**: Verify HTTPProxy has `tls.passthrough: true`
4. **Test with openssl**:
   ```bash
   openssl s_client -connect my-router-access-inter-router.contour.example.com:443 \
     -servername my-router-access-inter-router.contour.example.com
   ```

## Verification Commands

### Check Controller Configuration

```bash
# Verify controller environment
kubectl get deploy skupper-controller -n skupper-system -o yaml | grep -A 5 "env:"

# Check for SKUPPER_HTTP_PROXY_DOMAIN
kubectl get deploy skupper-controller -n skupper-system \
  -o jsonpath='{.spec.template.spec.containers[0].env[?(@.name=="SKUPPER_HTTP_PROXY_DOMAIN")].value}'
```

### Check HTTPProxy Resources

```bash
# List Skupper-managed HTTPProxy resources
kubectl get httpproxy -l internal.skupper.io/secured-access=true

# Check specific HTTPProxy details
kubectl get httpproxy <name> -o yaml

# Verify hostname and TLS passthrough
kubectl get httpproxy <name> -o jsonpath='{.spec.virtualhost.fqdn}'
kubectl get httpproxy <name> -o jsonpath='{.spec.virtualhost.tls.passthrough}'
```

### Check HTTPProxy Status

```bash
# Check if Contour accepted the HTTPProxy
kubectl get httpproxy <name> -o jsonpath='{.status.conditions[?(@.type=="Valid")].status}'
# Should output: True

# Check for error conditions
kubectl get httpproxy <name> -o jsonpath='{.status.conditions[*].message}'
```

### Check Site Endpoints

```bash
# View site endpoints
kubectl get site my-site -o jsonpath='{.status.endpoints[*]}' | jq .

# Should show endpoints with host/port like:
# {"name":"inter-router","host":"my-router-access-inter-router.contour.example.com","port":"443"}
```

### Test Connectivity

```bash
# Test DNS resolution
nslookup my-router-access-inter-router.contour.example.com

# Test TCP connection to Envoy
nc -zv my-router-access-inter-router.contour.example.com 443

# Test TLS handshake (should connect even if auth fails)
openssl s_client -connect my-router-access-inter-router.contour.example.com:443 \
  -servername my-router-access-inter-router.contour.example.com
```

### Check Envoy Configuration

```bash
# Get Envoy pod name
ENVOY_POD=$(kubectl get pod -n projectcontour -l app=envoy -o jsonpath='{.items[0].metadata.name}')

# Dump Envoy listener configuration
kubectl exec -n projectcontour $ENVOY_POD -- curl -s localhost:9001/config_dump \
  | jq '.configs[] | select(.name == "listener_manager")'

# Check for HTTPProxy routes
kubectl exec -n projectcontour $ENVOY_POD -- curl -s localhost:9001/config_dump \
  | jq '.configs[] | select(.name == "route_configuration_0")'
```

## Comparison: HTTPProxy vs Ingress

| Feature | Kubernetes Ingress (ingress-nginx) | Contour HTTPProxy |
|---------|-----------------------------------|-------------------|
| **Resource Type** | Native Kubernetes | Custom Resource (CRD) |
| **Controller** | NGINX (annotations required) | Contour (native support) |
| **TLS Passthrough** | Annotation: `ssl-passthrough: true` | Native: `spec.virtualhost.tls.passthrough: true` |
| **TCP Routing** | Limited (HTTP-focused) | Native: `spec.tcpproxy` |
| **Configuration** | Annotations for advanced features | Declarative spec fields |
| **Multi-controller** | Yes (generic Ingress API) | No (Contour only) |
| **Skupper Integration** | Works (with nginx variant) | Works (native support) |

**Recommendation**: Use `contour-http-proxy` if Contour is your ingress controller. The native TLS passthrough and TCP routing support make it a cleaner fit for Skupper than annotated Ingress resources.

## References

### Related Documentation

- [Skupper Site CRD](./skupper-crd-sites-skupper-io.md) - Site resource specification including linkAccess configuration
- [Skupper RouterAccess CRD](./skupper-crd-routeraccesses-skupper-io.md) - RouterAccess resource specification
- [Skupper SecuredAccess CRD](./skupper-crd-securedaccesses-skupper-io.md) - SecuredAccess resource specification
- [Skupper Ingress Access Guide](./skupper-ingress-access-guide.md) - Alternative ingress-based access type

### Source Code References

- **Implementation**: `/home/paulwright/repos/sk/skupper-okf/human/skupper/internal/kube/securedaccess/contour.go`
  - Lines 18-30: `ContourHttpProxyAccessType` struct
  - Lines 32-46: `RealiseAndResolve` implementation
  - Lines 132-151: `desiredHttpProxies` function (HTTPProxy generation)
  - Lines 192-212: `writeToContourProxy` function (HTTPProxy spec construction)
  - Lines 121-130: HTTPProxy GroupVersionResource/Kind
  - Lines 214-227: HTTPProxy creation and update functions

- **Configuration**: `/home/paulwright/repos/sk/skupper-okf/human/skupper/internal/kube/securedaccess/config.go`
  - Line 18: `ACCESS_TYPE_CONTOUR_HTTP_PROXY` constant
  - Line 81: `SKUPPER_HTTP_PROXY_DOMAIN` binding

- **Access Type Registration**: `/home/paulwright/repos/sk/skupper-okf/human/skupper/internal/kube/securedaccess/access.go`
  - Lines 77-78: Contour HTTPProxy access type initialization

### External Resources

- [Contour Documentation](https://projectcontour.io/) - Official Contour project documentation
- [HTTPProxy API](https://projectcontour.io/docs/main/config/api/) - HTTPProxy CRD reference
- [TLS Passthrough Guide](https://projectcontour.io/docs/main/config/tls-termination/#tls-passthrough) - Contour TLS passthrough configuration
- [Envoy SNI Routing](https://www.envoyproxy.io/docs/envoy/latest/faq/configuration/sni) - Understanding SNI-based routing

## Summary

The contour-http-proxy access type provides native Skupper integration with Contour's HTTPProxy resources:

1. **Contour-specific**: Only works with Contour ingress controller (not generic like Ingress)
2. **Enable explicitly**: Not in default access types—add to `SKUPPER_ENABLED_ACCESS_TYPES`
3. **Configure domain**: Always set `SKUPPER_HTTP_PROXY_DOMAIN` for hostname generation
4. **One HTTPProxy per port**: Skupper creates separate HTTPProxy resources for each defined port
5. **Native TLS passthrough**: Uses `spec.virtualhost.tls.passthrough: true` (no annotations)
6. **TCP routing**: Leverages `spec.tcpproxy.services` for direct TCP traffic routing
7. **DNS requirement**: Generated hostnames must resolve to Contour's Envoy service
8. **Dynamic client**: Uses Kubernetes dynamic client to manage HTTPProxy custom resources

For deployments using Contour as the ingress controller, contour-http-proxy provides cleaner integration than generic Ingress resources, with native support for the TLS passthrough and TCP routing requirements of Skupper's router-to-router connections.
