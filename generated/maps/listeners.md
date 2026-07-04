---
title: "Skupper Listeners in the Application Network"
type: BlockscapeMap
status: generated
source_path: maps/listeners.bs
tags:
  - skupper
  - blockscape
---

# Skupper Listeners in the Application Network

Edit: [Blockscape](https://pwright.github.io/blockscape/?load=https://raw.githubusercontent.com/pwright/skupper-okf/refs/heads/main/maps/listeners.bs)

```bs full
{
  "id": "skupper-listeners-map",
  "title": "Skupper Listeners in the Application Network",
  "abstract": "How listeners help Skupper make remote services feel local across a secure application network.",
  "status": "generated",
  "reviewed": false,
  "source_paths": [
    "human/skupper-docs/input/overview/index.md",
    "human/skupper-docs/input/overview/connectivity.md",
    "human/skupper-docs/input/system-yaml/service-exposure.md",
    "human/skupper-docs/input/kube-yaml/service-exposure.md",
    "generated/concepts/listener.md"
  ],
  "categories": [
    {
      "id": "application-outcomes",
      "title": "Application outcomes",
      "items": [
        {
          "id": "distributed-services-communicate",
          "name": "Distributed services communicate",
          "deps": [
            "remote-service-consumption",
            "secure-application-network"
          ],
          "source": "human/skupper-docs/input/overview/index.md",
          "external": "https://pwright.github.io/skupper-okf/human/skupper-docs/input/overview/index"
        },
        {
          "id": "hybrid-cloud-reachability",
          "name": "Hybrid cloud reachability",
          "deps": [
            "secure-application-network",
            "local-service-endpoint"
          ],
          "source": "human/skupper-docs/input/overview/connectivity.md",
          "external": "https://pwright.github.io/skupper-okf/human/skupper-docs/input/overview/connectivity"
        },
        {
          "id": "avoid-public-internet-or-vpn",
          "name": "Avoid public exposure or VPN setup",
          "deps": [
            "secure-application-network"
          ],
          "source": "human/skupper-docs/input/overview/connectivity.md",
          "external": "https://pwright.github.io/skupper-okf/human/skupper-docs/input/overview/connectivity"
        }
      ]
    },
    {
      "id": "service-consumption",
      "title": "Service consumption",
      "items": [
        {
          "id": "remote-service-consumption",
          "name": "Consume remote service locally",
          "deps": [
            "local-service-endpoint",
            "matching-connector"
          ],
          "source": "human/skupper-docs/input/system-yaml/service-exposure.md",
          "external": "https://pwright.github.io/skupper-okf/human/skupper-docs/input/system-yaml/service-exposure"
        },
        {
          "id": "local-service-endpoint",
          "name": "Local service endpoint",
          "deps": [
            "listener-host-port"
          ],
          "source": "human/skupper-docs/input/kube-yaml/service-exposure.md",
          "external": "https://pwright.github.io/skupper-okf/human/skupper-docs/input/kube-yaml/service-exposure"
        },
        {
          "id": "client-stable-address",
          "name": "Stable client address",
          "deps": [
            "listener-host-port"
          ],
          "source": "generated/concepts/listener.md",
          "external": "https://pwright.github.io/skupper-okf/generated/concepts/listener#outcome"
        }
      ]
    },
    {
      "id": "listener-role",
      "title": "Listener role",
      "items": [
        {
          "id": "listener",
          "name": "Listener",
          "deps": [
            "listener-host-port",
            "routing-key-match"
          ],
          "source": "generated/concepts/listener.md",
          "external": "https://pwright.github.io/skupper-okf/generated/concepts/listener#listener"
        },
        {
          "id": "listener-host-port",
          "name": "Host and port",
          "deps": [
            "listener-resource"
          ],
          "source": "human/skupper-docs/input/kube-yaml/service-exposure.md",
          "external": "https://pwright.github.io/skupper-okf/human/skupper-docs/input/kube-yaml/service-exposure"
        },
        {
          "id": "routing-key-match",
          "name": "Routing key match",
          "deps": [
            "matching-connector"
          ],
          "source": "human/skupper-docs/input/system-yaml/service-exposure.md",
          "external": "https://pwright.github.io/skupper-okf/human/skupper-docs/input/system-yaml/service-exposure"
        },
        {
          "id": "matching-connector",
          "name": "Matching connector",
          "deps": [
            "connector-exposed-workload"
          ],
          "source": "human/skupper-docs/input/system-yaml/service-exposure.md",
          "external": "https://pwright.github.io/skupper-okf/human/skupper-docs/input/system-yaml/service-exposure"
        }
      ]
    },
    {
      "id": "traffic-path",
      "title": "Traffic path",
      "items": [
        {
          "id": "client-connection",
          "name": "Client connection",
          "deps": [
            "listener"
          ],
          "source": "generated/concepts/listener.md",
          "external": "https://pwright.github.io/skupper-okf/generated/concepts/listener"
        },
        {
          "id": "skupper-router-forwarding",
          "name": "Skupper router forwarding",
          "deps": [
            "secure-application-network",
            "routing-key-match"
          ],
          "source": "human/skupper-docs/input/overview/index.md",
          "external": "https://pwright.github.io/skupper-okf/human/skupper-docs/input/overview/index"
        },
        {
          "id": "connector-exposed-workload",
          "name": "Connector-exposed workload",
          "deps": [
            "secure-application-network"
          ],
          "source": "human/skupper-docs/input/system-yaml/service-exposure.md",
          "external": "https://pwright.github.io/skupper-okf/human/skupper-docs/input/system-yaml/service-exposure"
        }
      ]
    },
    {
      "id": "network-foundation",
      "title": "Network foundation",
      "items": [
        {
          "id": "secure-application-network",
          "name": "Secure application network",
          "deps": [
            "linked-sites",
            "skupper-routers"
          ],
          "source": "human/skupper-docs/input/overview/connectivity.md",
          "external": "https://pwright.github.io/skupper-okf/human/skupper-docs/input/overview/connectivity"
        },
        {
          "id": "linked-sites",
          "name": "Linked sites",
          "deps": [
            "skupper-instances"
          ],
          "source": "human/skupper-docs/input/system-yaml/service-exposure.md",
          "external": "https://pwright.github.io/skupper-okf/human/skupper-docs/input/system-yaml/service-exposure"
        },
        {
          "id": "skupper-routers",
          "name": "Skupper routers",
          "source": "human/skupper-docs/input/overview/index.md",
          "external": "https://pwright.github.io/skupper-okf/human/skupper-docs/input/overview/index"
        },
        {
          "id": "skupper-instances",
          "name": "Skupper instances",
          "source": "human/skupper-docs/input/overview/index.md",
          "external": "https://pwright.github.io/skupper-okf/human/skupper-docs/input/overview/index"
        }
      ]
    },
    {
      "id": "listener-control-plane",
      "title": "Listener control plane",
      "items": [
        {
          "id": "listener-resource",
          "name": "Listener resource",
          "deps": [
            "listener-spec-routing-key",
            "listener-spec-host",
            "listener-spec-port"
          ],
          "source": "human/skupper-docs/input/kube-yaml/service-exposure.md",
          "external": "https://pwright.github.io/skupper-okf/human/skupper-docs/input/kube-yaml/service-exposure"
        },
        {
          "id": "listener-spec-routing-key",
          "name": "spec.routingKey",
          "source": "generated/concepts/listener.md",
          "external": "https://pwright.github.io/skupper-okf/generated/concepts/listener#common-fields"
        },
        {
          "id": "listener-spec-host",
          "name": "spec.host",
          "source": "generated/concepts/listener.md",
          "external": "https://pwright.github.io/skupper-okf/generated/concepts/listener#common-fields"
        },
        {
          "id": "listener-spec-port",
          "name": "spec.port",
          "source": "generated/concepts/listener.md",
          "external": "https://pwright.github.io/skupper-okf/generated/concepts/listener#common-fields"
        },
        {
          "id": "multi-key-listener",
          "name": "Multi-key listener",
          "deps": [
            "listener",
            "routing-key-match"
          ],
          "source": "human/skupper-docs/input/kube-yaml/service-exposure.md",
          "external": "https://pwright.github.io/skupper-okf/human/skupper-docs/input/kube-yaml/service-exposure"
        },
        {
          "id": "listener-ready-status",
          "name": "Ready with matching connector",
          "deps": [
            "listener-resource",
            "matching-connector"
          ],
          "source": "human/skupper-docs/input/kube-yaml/service-exposure.md",
          "external": "https://pwright.github.io/skupper-okf/human/skupper-docs/input/kube-yaml/service-exposure"
        }
      ]
    }
  ],
  "source_base_url": "https://pwright.github.io/skupper-okf/"
}
```
