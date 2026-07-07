---
type: Concept
title: Network Deployment Concerns
id: skupper-concept-network-deployment-concerns
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source_repo: https://github.com/skupperproject/skupper-docs.git
source_branch: main
source_commit: fdfd4594ade939dd2d756215e5f3afdb54190c44
source_paths:
  - human/skupper-docs/input/refdog/concepts/site.md
  - human/skupper-docs/input/refdog/concepts/link.md
  - human/skupper-docs/input/refdog/concepts/access-token.md
  - human/skupper-docs/input/kube-yaml/site-configuration.md
  - human/skupper-docs/input/refdog/resources/site.md
  - human/skupper-docs/input/overview/load-balancing.md
  - human/skupper-docs/input/console/index.md
  - human/skupper-docs/input/kube-cli/site-linking.md
  - human/skupper-docs/input/kube-yaml/custom-labels.md
tags:
  - skupper
  - network
  - deployment
  - site
  - link
  - planning
related:
  - skupper-concept-connector
  - skupper-concept-listener
  - skupper-concept-routing-key
  - skupper-concept-network-observer-api
decision:
  setupStep:
    - identify-sites
    - join-sites
    - validate
  platform:
    - kubernetes
    - openshift
    - podman
    - docker
    - linux
timestamp: 2026-07-07T14:00:35Z
---

# Network Deployment Concerns

A network is a set of sites joined by links. A Skupper network is also known as an application network or virtual application network (VAN). 

This topic assumes that you have completed the Getting Started and understand the basics of creating and linking sites, exposing services using [connectors](./connector.md), consuming those services using [listeners](./listener.md) with matching [routing keys](./routing-key.md).

Consider the following topics when designing and implementing your application network.

## Outcome

Understanding deployment concerns helps you:

- Scale your network to handle production traffic
- Choose appropriate linking strategies for your topology
- Direct traffic efficiently across sites
- Observe and monitor network behavior

## Sites

A [site](../human/skupper-docs/input/refdog/concepts/site.md) is a place on the network where application workloads are running and services are consumed. You can create a site on Kubernetes, Podman, Docker or Linux.

Each site has a Skupper router which is responsible for communicating with the local workloads and forwarding traffic to routers in remote sites.

### Site Performance and Resource Allocation

By default, the router CPU allocation is BestEffort as described in [Pod Quality of Service Classes](https://kubernetes.io/docs/concepts/workloads/pods/pod-qos/), and this might affect performance under network load.

If your site handles a lot of traffic you can provide more resources (CPU/RAM) to improve the network performance. Consider the following CPU allocation options:

| Router CPU | Description |
|------------|-------------|
| 1 | Helps avoid issues with BestEffort on low resource clusters |
| 2 | Suitable for production environments |
| 5 | Maximum performance |

For configuration details, see [Setting site resources](../human/skupper-docs/input/kube-yaml/site-configuration.md#kube-site-resources-yaml).

**Note:** Increasing the number of routers does not improve network performance. An incoming router-to-router link is associated with just one active router. Additional routers do not receive traffic while that router is responding.

### High Availability Sites

High availability mode is intended to maintain service continuity during router restarts or pod rescheduling, but it does not provide failover if network connectivity between sites is lost. High availability mode deploys two router pods with anti-affinity rules to ensure service continuity during node failures.

To enable high availability on a site:

```yaml
apiVersion: skupper.io/v2alpha1
kind: Site
metadata:
  name: ha-site
  namespace: west
spec:
  ha: true
  linkAccess: default  # Optional: configure external access
```

When you create a high availability site, it generates two link resources to ensure both router pods can accept connections.

For more information, see [Creating a high availability site using YAML](../human/skupper-docs/input/kube-yaml/site-configuration.md#kube-ha-yaml).

## Links

[Links](../human/skupper-docs/input/refdog/concepts/link.md) connect sites. Application connections and requests flow across links in both directions. A linked site can communicate with any other site in the network, even if it is not linked directly.

### Link Access

You must create at least one listening site on your network. That is, you must enable link access on that site to allow other sites to create links to it.

To enable link access:

```yaml
apiVersion: skupper.io/v2alpha1
kind: Site
metadata:
  name: my-site
  namespace: west
spec:
  linkAccess: default
```

Link access provides an external access point for accepting links. On OpenShift, the default is `route`. For other Kubernetes flavors, the default is `loadbalancer`.

See [Site resource](../human/skupper-docs/input/refdog/resources/site.md) for more information on link access configuration.

### Linking Methods

When linking sites you can choose between:

1. **Creating tokens** on the listening site and redeeming that token from the linking site
2. **Creating link resources** on both the listening site and the linking site

Ultimately, a link resource is created on the linking site, but [access tokens](../human/skupper-docs/input/refdog/concepts/access-token.md) provide the ability to restrict redemption by time and usage.

#### Access Token Characteristics

- **Limited redemptions**: By default, tokens can be redeemed only once. You can set custom limits using the access grant configuration.
- **Limited lifespan**: Tokens expire 15 minutes after being issued by default. You can configure custom expiration windows.
- **Secure exchange**: All inter-site traffic is protected by mutual TLS using a private, dedicated certificate authority (CA). A token is not a certificate, but is securely exchanged for a certificate during the linking process.

Example token with custom restrictions:

```bash
# Time restriction: 1 hour expiration
skupper token issue build/west.yaml --expiration-window 60m

# Usage restriction: 3 redemptions allowed
skupper token issue output/west.yaml --redemptions-allowed 3
```

For more information on tokens, see [Site linking using tokens](../human/skupper-docs/input/kube-cli/site-linking.md#kube-token-cli).

### Link Constraints

- Linking through an HTTP proxy is not supported for token redemption
- High Availability sites generate two link resources (one for each router pod)
- Links can be added and removed dynamically

### Custom Certificates for Links

You can use custom TLS certificates to support linking by creating SecuredAccess resources. SecuredAccess resources allow you to provide your own CA and certificates for link authentication.

For details on propagating custom labels and annotations to SecuredAccess resources, see [Propagating custom labels and annotations using YAML](../human/skupper-docs/input/kube-yaml/custom-labels.md).

## Services 

After you expose an application workload on the application network using a [connector](./connector.md), that service can be consumed from any site on the network using a [listener](./listener.md) with a matching [routing key](./routing-key.md).

```text
remote client -> listener -> matching routing key -> connector -> local workload
```

### Observing Services

You can deploy the Network Observer on any site and collect service metrics or observe traffic using the Skupper console.

The Network console provides data and visualizations of the traffic flow between sites using the Network Observer component which also deploys an [API endpoint](./network-observer-api.md).

**Site Selection Criteria for Network Observer:**

1. Does the application network cross a firewall? If you want the console to be available only inside the firewall, you need to locate the Network console on a site inside the firewall.
2. Is there a site that processes more traffic than other sites? If you have a frontend component that calls a set of services from other sites, it might make sense to locate the Network console on that site to minimize data traffic.
3. Is there a site with more or cheaper resources that you want to use? If resources are more expensive on one site, you might want to locate the Network console on a less expensive site.

For installation and configuration details, see [Using the Skupper network console](../human/skupper-docs/input/console/index.md).

### Traffic Direction

Traffic can be directed using link cost or multi-key listeners.

#### Multi-key Listeners (Recommended)

A multi-key listener provides per-service control over load balancing and failover by binding a single endpoint to multiple routing keys (connectors). This is the recommended approach for most use cases because it offers:

- **Per-service configuration** — Each service can have its own distribution strategy, independent of network topology
- **Predictable behavior** — Traffic distribution is explicitly controlled by strategy, not influenced by connection timing or link metrics
- **Two strategies**:
  - **weighted** — Proportional distribution across routing keys (e.g., 25/75 split)
  - **priority** — Failover with preference order (uses first available, fails over to next)

For configuration details, see the multi-key listener section in [Service exposure](../human/skupper-docs/input/kube-yaml/service-exposure.md).

#### Link Cost

Link cost is a configurable integer value that influences how Skupper routes traffic across **all services** that traverse a link between two sites. The routing algorithm favors paths with the lowest total cost from client to target server.

**Key characteristics:**

- The default link cost is `1`. Local workloads have an implicit cost of `0`.
- If a connection traverses more than one link, the path cost is the sum of all link costs along the path.
- Link cost applies to **all services** on a link and cannot be set differently for individual services. For per-service control, use a multi-key listener instead.
- When multiple paths exist, traffic flows on the lowest-cost path until the number of open connections exceeds the cost of an alternative path. After that threshold is reached, new connections are spread across both paths.

For details on configuring link cost, see [Load balancing and failover](../human/skupper-docs/input/overview/load-balancing.md).

## Verify

Check site status:

```bash
kubectl get site
```

Expected output:

```text
NAME   STATUS   SITES IN NETWORK   MESSAGE
west   Ready    1                  OK
```

Check link status:

```bash
skupper link status
```

Expected output:

```text
NAME                                            STATUS  COST    MESSAGE
west-12f75bc8-5dda-4256-88f8-9df48150281a       Ready   1       OK
```

## References

- [Site concept](../human/skupper-docs/input/refdog/concepts/site.md)
- [Link concept](../human/skupper-docs/input/refdog/concepts/link.md)
- [Access token concept](../human/skupper-docs/input/refdog/concepts/access-token.md)
- [Site resource](../human/skupper-docs/input/refdog/resources/site.md)
- [Creating a site on Kubernetes using YAML](../human/skupper-docs/input/kube-yaml/site-configuration.md)
- [Linking sites on Kubernetes using the CLI](../human/skupper-docs/input/kube-cli/site-linking.md)
- [Load balancing and failover](../human/skupper-docs/input/overview/load-balancing.md)
- [Using the Skupper network console](../human/skupper-docs/input/console/index.md)
- [Connector concept](./connector.md)
- [Listener concept](./listener.md)
- [Routing key concept](./routing-key.md)
- [Network Observer API](./network-observer-api.md)
