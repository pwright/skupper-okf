---
type: EnterpriseSessionRecoveryPage
title: "Network Path"
id: network-path
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source: maps/enterprise-session-recovery.bs
external: https://pwright.github.io/skupper-okf/generated/enterprise-session-recovery/network-path
tags:
  - skupper
  - enterprise-session-recovery
  - transport
related:
  - broker-database-endpoints
  - dhcp
  - dns
  - endpoint-discovery
  - independent-request
  - load-balancer-proxy-timeout
  - middleboxes
  - nat-firewall-state
  - reconnect-retry
  - tcp
  - tcp-connection
  - tls
  - udp
---

# Network Path

This is transport or path behavior. Skupper is relevant where the workload speaks TCP through a listener and connector.

## Skupper Suitability

Skupper is useful when the network-path problem is private TCP reachability between sites, clusters, or hosts. It is not a general substitute for routing every enterprise protocol, especially foundational DNS, DHCP, UDP, or real-time media traffic.

## Appears in

- Enterprise TCP Sessions and Recovery / TCP and Network Path
- Enterprise Traffic Patterns / Transport and Path

## Dependency Check

This topic has no dependencies in the map and acts as a base assumption for dependent topics.

Used by:

- [Broker (and database endpoints)](./broker-database-endpoints.md)
- [DHCP](./dhcp.md)
- [DNS](./dns.md)
- [Endpoint Discovery](./endpoint-discovery.md)
- [Independent Exchange](./independent-request.md)
- [Idle Timeout (load balancer or proxy)](./load-balancer-proxy-timeout.md)
- [Middleboxes (NAT, firewall, LB)](./middleboxes.md)
- [NAT (and firewall state)](./nat-firewall-state.md)
- [Reconnect (and Retry)](./reconnect-retry.md)
- [TCP](./tcp.md)
- [TCP Connection](./tcp-connection.md)
- [TLS](./tls.md)
- [UDP](./udp.md)

## Related Skupper Docs

- [Skupper multi-site connectivity](../skupper-docs-landscape/multi-site-connectivity.md)
- [Private connectivity](../skupper-docs-landscape/private-connectivity.md)
- [Firewall and egress controls](../skupper-docs-landscape/network-controls.md)
- [Links](../skupper-docs-landscape/links.md)
- [Link status](../skupper-docs-landscape/link-status.md)
- [Secure links](../skupper-docs-landscape/secure-links.md)

## Draft Notes

- Validate the workload by breaking the TCP path and observing client-visible behavior, not just by checking that Skupper reconnects.
- Document whether the application requires same-socket continuity, logical session resume, durable progress, or ordinary retry.
