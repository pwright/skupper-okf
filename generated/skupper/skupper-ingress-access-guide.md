---
type: Guide
title: Using Ingress Access for Skupper Sites
id: skupper-ingress-access-guide
status: generated
owner: agent
generated_by: claude
reviewed: false
confidence: high
source_file: ../human/skupper/internal/kube/securedaccess/ingress.go
tags:
  - skupper
  - ingress
  - ingress-nginx
  - access-type
  - kubernetes
related:
  - skupper-crd-sites-skupper-io
  - skupper-crd-routeraccesses-skupper-io
  - skupper-crd-securedaccesses-skupper-io
  - skupper-nodeport-access-guide
timestamp: 2026-08-13
---

# Using Ingress Access for Skupper Sites

## Overview

Skupper supports two ingress-based access types that create Kubernetes Ingress resources for site-to-site connectivity:

- **`ingress`**: Creates standard Kubernetes Ingress resources for generic ingress controllers
- **`ingress-nginx`**: Creates Ingress resources with NGINX-specific annotations for TLS passthrough

Both access types work with Kubernetes Ingress controllers but differ in their annotation strategy. The `ingress-nginx` variant adds controller-specific annotations that enable TLS passthrough with the NGINX Ingress Controller.

### When to Use Ingress Access

**Use ingress/ingress-nginx when:**
- You have a Kubernetes Ingress controller deployed (NGINX, HAProxy, Traefik, etc.)
- You want to reuse existing ingress infrastructure for Skupper connectivity
- Your cluster doesn't support LoadBalancer services
- You need hostname-based routing through a centralized ingress point
- Running on cloud Kubernetes without OpenShift Routes

**Use alternative access types when:**
- **route**: Running on OpenShift (routes are the native OpenShift ingress mechanism)
- **loadbalancer**: Cloud Kubernetes with direct LoadBalancer support (simpler than ingress)
- **nodeport**: Local development (kind, Minikube) or bare-metal without ingress controller
- **local**: Single-cluster testing with no external access needed

### Difference Between `ingress` and `ingress-nginx`

| Feature | `ingress` | `ingress-nginx` |
|---------|-----------|-----------------|
| Target controller | Any Kubernetes ingress controller | NGINX Ingress Controller |
| TLS passthrough | Requires manual configuration | Automatic via annotations |
| Annotations | None (generic) | `ssl-passthrough: true`, `ssl-redirect: true` |
| Default IngressClass | None (must be configured) | `"nginx"` (if not otherwise set) |
| Use case | Generic ingress controllers | NGINX-specific deployments |

**Source**: `/home/paulwright/repos/sk/skupper-okf/human/skupper/internal/kube/securedaccess/ingress.go` (lines 17-33, 195-198)

## Prerequisites

Before using ingress access, ensure:

1. **Ingress controller deployed**: A Kubernetes ingress controller must be running in your cluster
2. **Ingress enabled on controller**: The Skupper controller must have `ingress` or `ingress-nginx` in its enabled access types
3. **Ingress domain configured**: The controller must know the base domain for constructing FQDNs
4. **TLS passthrough support**: Your ingress controller must support TLS passthrough (for mutual TLS between routers)
5. **DNS resolution**: The generated ingress hostnames must resolve to your ingress controller

## Controller Configuration

The Skupper controller requires specific environment variables to enable and configure ingress access types.

### Required Environment Variables

**`SKUPPER_ENABLED_ACCESS_TYPES`**
- **Purpose**: Comma-separated list of enabled access types
- **Default**: `local,loadbalancer,route` (does **not** include ingress variants)
- **Required value**: Must include `ingress` and/or `ingress-nginx`
- **Example**: `"ingress-nginx,local,loadbalancer,route"`

**`SKUPPER_INGRESS_DOMAIN`**
- **Purpose**: Base domain for constructing fully qualified hostnames for Ingress resources
- **Required when**: Using `ingress` or `ingress-nginx` access types
- **How it works**: Combined with access name to form FQDN (e.g., `<port-name>.<domain>`)
- **Examples**:
  - `"ingress.example.com"` → generates hostnames like `inter-router.ingress.example.com`
  - `"apps.cluster.local"` → generates hostnames like `edge.apps.cluster.local`

**Source**: `/home/paulwright/repos/sk/skupper-okf/human/skupper/internal/kube/securedaccess/config.go` (line 79)

### Optional Environment Variables

**`SKUPPER_INGRESS_CLASS_NAME`**
- **Purpose**: Sets the default `ingressClassName` for Skupper-managed Ingress resources
- **Default behavior**:
  - `ingress`: No default (empty string)
  - `ingress-nginx`: Defaults to `"nginx"` if not set
- **Per-resource override**: Can be overridden via `RouterAccess.spec.settings.ingressClassName`
- **Examples**:
  - `"nginx"` (NGINX Ingress Controller)
  - `"haproxy"` (HAProxy Ingress Controller)
  - `"traefik"` (Traefik Ingress Controller)

**Source**: `/home/paulwright/repos/sk/skupper-okf/human/skupper/internal/kube/securedaccess/config.go` (line 80), `ingress.go` (lines 35-50)

**`SKUPPER_DEFAULT_ACCESS_TYPE` (Optional)**
- **Purpose**: Sets the default access type for sites that don't specify one
- **Validation**: Must be included in `SKUPPER_ENABLED_ACCESS_TYPES` if set
- **Example**: `"ingress-nginx"`

### Configuration via Deployment YAML

#### For NGINX Ingress Controller

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
          value: "ingress-nginx,local,loadbalancer,route"
        - name: SKUPPER_INGRESS_DOMAIN
          value: "ingress.example.com"
        - name: SKUPPER_INGRESS_CLASS_NAME  # Optional: defaults to "nginx" for ingress-nginx
          value: "nginx"
        - name: SKUPPER_DEFAULT_ACCESS_TYPE  # Optional
          value: "ingress-nginx"
```

#### For Generic Ingress Controller

```yaml
env:
  - name: SKUPPER_ENABLED_ACCESS_TYPES
    value: "ingress,local,loadbalancer,route"
  - name: SKUPPER_INGRESS_DOMAIN
    value: "apps.cluster.local"
  - name: SKUPPER_INGRESS_CLASS_NAME
    value: "haproxy"  # Or your ingress controller's class name
```

### Configuration via Helm Chart

```yaml
# values.yaml
enabledAccessTypes: "ingress-nginx,local,loadbalancer,route"
ingressDomain: "ingress.example.com"
ingressClassName: "nginx"  # Optional
defaultAccessType: "ingress-nginx"  # Optional
```

**Note**: The Helm chart variables `ingressDomain` and `ingressClassName` would map to `SKUPPER_INGRESS_DOMAIN` and `SKUPPER_INGRESS_CLASS_NAME` respectively. Check your Helm chart documentation for availability.

## Using Ingress with Sites

Once ingress access is enabled on the controller, configure it on your sites using one of three methods:

### Method 1: Site linkAccess

Set `linkAccess: ingress-nginx` or `linkAccess: ingress` on the Site resource:

```yaml
apiVersion: skupper.io/v2alpha1
kind: Site
metadata:
  name: my-site
  namespace: default
spec:
  linkAccess: ingress-nginx
```

**When to use**: Simple site configuration where you want link access enabled with ingress and don't need fine-grained control.

### Method 2: RouterAccess Resource

For more control, create a RouterAccess resource explicitly:

```yaml
apiVersion: skupper.io/v2alpha1
kind: RouterAccess
metadata:
  name: my-router-access
  namespace: default
spec:
  accessType: ingress-nginx
  roles:
    - name: inter-router
      port: 55671
  tlsCredentials: my-tls-secret
  generateTlsCredentials: true
  issuer: skupper-site-ca
  settings:
    ingressClassName: "nginx"  # Optional: override controller default
```

**When to use**: You need custom roles, ports, TLS settings, or want to override the ingress class name per-resource.

**Per-resource IngressClass override**: The `spec.settings.ingressClassName` field overrides the controller-wide `SKUPPER_INGRESS_CLASS_NAME` for this specific RouterAccess.

**Source**: `/home/paulwright/repos/sk/skupper-okf/human/skupper/internal/kube/securedaccess/ingress.go` (lines 35-50)

### Method 3: SecuredAccess Resource

For securing application services with ingress access:

```yaml
apiVersion: skupper.io/v2alpha1
kind: SecuredAccess
metadata:
  name: my-secured-access
  namespace: default
spec:
  accessType: ingress-nginx
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
  settings:
    ingressClassName: "nginx"
```

**When to use**: Exposing application services (not just router links) with mutual TLS through ingress.

## How Ingress Access Works

### Hostname Generation

When you configure ingress access, Skupper generates fully qualified hostnames by combining:

1. **Port name** from the RouterAccess/SecuredAccess spec
2. **Ingress domain** from `SKUPPER_INGRESS_DOMAIN`

**Example**:
- Port name: `inter-router`
- Ingress domain: `ingress.example.com`
- Generated FQDN: `inter-router.ingress.example.com`

**Source**: `/home/paulwright/repos/sk/skupper-okf/human/skupper/internal/kube/securedaccess/ingress.go` (lines 147-189)

### Ingress Resource Structure

Skupper creates Ingress resources with:

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: my-router-access
  annotations:
    # For ingress-nginx only:
    nginx.ingress.kubernetes.io/ssl-passthrough: "true"
    nginx.ingress.kubernetes.io/ssl-redirect: "true"
spec:
  ingressClassName: "nginx"  # Based on configuration
  rules:
    - host: inter-router.ingress.example.com
      http:
        paths:
          - path: /
            pathType: Prefix
            backend:
              service:
                name: my-router-access
                port:
                  number: 55671
```

**Key points**:
- `ingressClassName` set based on controller default or per-resource override
- `ingress-nginx` variant includes `ssl-passthrough` and `ssl-redirect` annotations
- Each port gets its own ingress rule with a unique hostname
- All traffic routes to port `443` (standard HTTPS)

**Source**: `/home/paulwright/repos/sk/skupper-okf/human/skupper/internal/kube/securedaccess/ingress.go` (lines 195-198)

### Endpoint Resolution

After creating the Ingress, Skupper generates connection endpoints:

```yaml
endpoints:
  - name: inter-router
    host: inter-router.ingress.example.com
    port: "443"
```

Remote sites connect to these endpoints to establish links.

**Source**: `/home/paulwright/repos/sk/skupper-okf/human/skupper/internal/kube/securedaccess/ingress.go` (lines 68-76)

## NGINX Ingress Controller Configuration

If using `ingress-nginx` access type, ensure your NGINX Ingress Controller supports TLS passthrough:

### Enable TLS Passthrough

TLS passthrough must be explicitly enabled on the NGINX Ingress Controller. Check your controller deployment:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: ingress-nginx-controller
  namespace: ingress-nginx
spec:
  template:
    spec:
      containers:
      - name: controller
        image: registry.k8s.io/ingress-nginx/controller:latest
        args:
          - /nginx-ingress-controller
          - --enable-ssl-passthrough  # Required for Skupper
```

**Verification**:

```bash
# Check if SSL passthrough is enabled
kubectl get deployment ingress-nginx-controller -n ingress-nginx -o yaml | grep enable-ssl-passthrough
```

### Annotations Added by Skupper

When using `ingress-nginx`, Skupper automatically adds these annotations:

```yaml
annotations:
  nginx.ingress.kubernetes.io/ssl-passthrough: "true"
  nginx.ingress.kubernetes.io/ssl-redirect: "true"
```

- **ssl-passthrough**: Tells NGINX to pass TLS traffic directly to the backend without terminating it
- **ssl-redirect**: Forces HTTP traffic to redirect to HTTPS

**Source**: `/home/paulwright/repos/sk/skupper-okf/human/skupper/internal/kube/securedaccess/ingress.go` (lines 195-198)

## DNS Configuration

For ingress access to work, DNS must resolve the generated hostnames to your ingress controller's load balancer or IP address.

### Option 1: Wildcard DNS

Create a wildcard DNS record pointing to your ingress controller:

```
*.ingress.example.com. IN A 203.0.113.10
```

This allows any subdomain (e.g., `inter-router.ingress.example.com`) to resolve to the ingress controller.

### Option 2: Specific DNS Records

Create individual DNS records for each generated hostname:

```
inter-router.ingress.example.com. IN A 203.0.113.10
edge.ingress.example.com. IN A 203.0.113.10
```

### Option 3: nip.io (Development/Testing)

If your ingress controller has a public IP, you can use the `nip.io` service:

```yaml
env:
  - name: SKUPPER_INGRESS_DOMAIN
    value: "203.0.113.10.nip.io"
```

Skupper will generate hostnames like `inter-router.203.0.113.10.nip.io`, which automatically resolve to `203.0.113.10`.

**Note**: Skupper can auto-deduce the domain from the ingress controller's LoadBalancer status and use nip.io if an IP address is available. See **Source**: `/home/paulwright/repos/sk/skupper-okf/human/skupper/internal/kube/securedaccess/ingress.go` (lines 200-212)

## Troubleshooting

### Ingress not created

**Symptom**: No Ingress resource appears after configuring RouterAccess

**Causes and solutions**:
1. **Access type not enabled**: Verify `ingress` or `ingress-nginx` is in `SKUPPER_ENABLED_ACCESS_TYPES`
2. **Missing domain**: Check `SKUPPER_INGRESS_DOMAIN` is set on controller
3. **Check controller logs**:
   ```bash
   kubectl logs -n skupper-system deployment/skupper-controller | grep ingress
   ```

### Endpoints not resolving

**Symptom**: Site status shows `Resolved: False` or endpoints array is empty

**Causes and solutions**:
1. **Ingress domain not configured**: Verify `SKUPPER_INGRESS_DOMAIN` environment variable
2. **Ingress controller not running**: Check ingress controller pods are healthy
3. **LoadBalancer not assigned**: Check ingress controller service has an external IP:
   ```bash
   kubectl get svc -n ingress-nginx
   ```

### Remote site cannot connect

**Symptom**: Links remain in `Pending` or `Error` state

**Causes and solutions**:
1. **DNS not resolving**: Verify DNS resolution from remote site:
   ```bash
   nslookup inter-router.ingress.example.com
   dig inter-router.ingress.example.com
   ```
2. **TLS passthrough not enabled**: For NGINX, verify `--enable-ssl-passthrough` flag
3. **Wrong IngressClass**: Check `spec.ingressClassName` matches your controller:
   ```bash
   kubectl get ingress -A -o jsonpath='{.items[*].spec.ingressClassName}'
   kubectl get ingressclass
   ```
4. **Ingress controller not routing traffic**: Check ingress controller logs:
   ```bash
   kubectl logs -n ingress-nginx deployment/ingress-nginx-controller
   ```

### SSL passthrough not working (NGINX)

**Symptom**: Connection fails with TLS errors

**Causes and solutions**:
1. **Passthrough not enabled on controller**: Add `--enable-ssl-passthrough` to controller args
2. **Annotation missing**: Verify Ingress has the passthrough annotation:
   ```bash
   kubectl get ingress <name> -o yaml | grep ssl-passthrough
   ```
3. **Check NGINX config**: Inspect the generated NGINX configuration:
   ```bash
   kubectl exec -n ingress-nginx deployment/ingress-nginx-controller -- cat /etc/nginx/nginx.conf | grep -A 10 "server_name inter-router"
   ```

### Wrong IngressClass used

**Symptom**: Ingress created but no traffic routing

**Causes and solutions**:
1. **Verify IngressClass configuration priority**:
   - Check per-resource setting: `RouterAccess.spec.settings.ingressClassName`
   - Check controller default: `SKUPPER_INGRESS_CLASS_NAME`
   - For `ingress-nginx`, defaults to `"nginx"` if neither is set
2. **List available IngressClasses**:
   ```bash
   kubectl get ingressclass
   ```
3. **Update controller or RouterAccess** to use correct class name

## Verification Commands

### Check Controller Configuration

```bash
# Verify controller environment
kubectl get deploy skupper-controller -n skupper-system -o yaml | grep -A 5 "env:"

# Check for SKUPPER_INGRESS_DOMAIN
kubectl get deploy skupper-controller -n skupper-system -o jsonpath='{.spec.template.spec.containers[0].env[?(@.name=="SKUPPER_INGRESS_DOMAIN")].value}'
```

### Check Ingress Resources

```bash
# List Skupper-managed Ingress resources
kubectl get ingress -l internal.skupper.io/secured-access=true

# Check specific ingress details
kubectl get ingress <name> -o yaml

# Verify hostname and IngressClass
kubectl get ingress <name> -o jsonpath='{.spec.rules[*].host}'
kubectl get ingress <name> -o jsonpath='{.spec.ingressClassName}'
```

### Check Site Endpoints

```bash
# View site endpoints
kubectl get site my-site -o jsonpath='{.status.endpoints[*]}' | jq .

# Should show endpoints with host/port like:
# {"name":"inter-router","host":"inter-router.ingress.example.com","port":"443"}
```

### Test Connectivity

```bash
# Test DNS resolution
nslookup inter-router.ingress.example.com

# Test TLS connection
openssl s_client -connect inter-router.ingress.example.com:443 -servername inter-router.ingress.example.com

# Should establish TLS connection (may show cert details or fail auth, but connection proves routing works)
```

## Comparison: ingress vs ingress-nginx

| Aspect | `ingress` | `ingress-nginx` |
|--------|-----------|-----------------|
| **Annotations** | None | `ssl-passthrough: true`, `ssl-redirect: true` |
| **Default IngressClass** | `""` (empty) | `"nginx"` |
| **Target controllers** | Generic (HAProxy, Traefik, etc.) | NGINX Ingress Controller |
| **TLS passthrough config** | Must configure manually on controller | Enabled via annotation |
| **Use when** | Non-NGINX ingress controllers | NGINX Ingress Controller deployed |
| **Configuration complexity** | Requires manual TLS passthrough setup | Automatic via annotations |

**Recommendation**: Use `ingress-nginx` if you're running the NGINX Ingress Controller. Use `ingress` for other controllers and manually configure TLS passthrough per controller's requirements.

## References

### Related Documentation

- [Skupper Site CRD](./skupper-crd-sites-skupper-io.md) - Site resource specification including linkAccess configuration
- [Skupper RouterAccess CRD](./skupper-crd-routeraccesses-skupper-io.md) - RouterAccess resource specification
- [Skupper SecuredAccess CRD](./skupper-crd-securedaccesses-skupper-io.md) - SecuredAccess resource specification
- [Skupper NodePort Access Guide](./skupper-nodeport-access-guide.md) - Alternative access type for local development

### Source Code References

- **Implementation**: `/home/paulwright/repos/sk/skupper-okf/human/skupper/internal/kube/securedaccess/ingress.go`
  - Lines 17-33: `IngressAccessType` struct with nginx flag
  - Lines 35-50: `ingressClassNameForDesiredIngress` function (IngressClass selection logic)
  - Lines 147-189: `toIngress` function (Ingress resource creation)
  - Lines 195-198: `addNginxIngressAnnotations` function (NGINX-specific annotations)
  - Lines 68-76: Endpoint resolution

- **Configuration**: `/home/paulwright/repos/sk/skupper-okf/human/skupper/internal/kube/securedaccess/config.go`
  - Lines 15-16: Access type constants
  - Line 17: `SettingIngressClassName` constant
  - Line 79: `SKUPPER_INGRESS_DOMAIN` binding
  - Line 80: `SKUPPER_INGRESS_CLASS_NAME` binding

- **Access Type Registration**: `/home/paulwright/repos/sk/skupper-okf/human/skupper/internal/kube/securedaccess/access.go`
  - Lines 73-76: Ingress access type initialization

### External Resources

- [Kubernetes Ingress](https://kubernetes.io/docs/concepts/services-networking/ingress/) - Official Kubernetes Ingress documentation
- [NGINX Ingress Controller](https://kubernetes.github.io/ingress-nginx/) - NGINX Ingress Controller documentation
- [NGINX TLS Passthrough](https://kubernetes.github.io/ingress-nginx/user-guide/tls/#ssl-passthrough) - Enabling SSL passthrough
- [Kubernetes IngressClass](https://kubernetes.io/docs/concepts/services-networking/ingress/#ingress-class) - IngressClass resource documentation

## Summary

Ingress access types enable Skupper site connectivity through Kubernetes ingress controllers, reusing existing ingress infrastructure:

1. **Two variants**: `ingress` (generic) and `ingress-nginx` (NGINX-specific with automatic TLS passthrough)
2. **Enable explicitly**: Neither is in the default access types—add to `SKUPPER_ENABLED_ACCESS_TYPES`
3. **Configure domain**: Always set `SKUPPER_INGRESS_DOMAIN` for hostname generation
4. **IngressClass control**: Three-level priority: per-resource > controller default > nginx default
5. **DNS requirement**: Generated hostnames must resolve to ingress controller
6. **TLS passthrough**: NGINX variant enables automatically; other controllers require manual configuration
7. **Three configuration methods**: Site.linkAccess, RouterAccess, or SecuredAccess

For cloud deployments with ingress controllers, ingress access types provide a production-ready alternative to LoadBalancer and Route access types. Use `ingress-nginx` for NGINX deployments and `ingress` for other controllers.
