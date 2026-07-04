---
title: "Skupper Connectors in the Application Network"
type: BlockscapeMap
status: generated
source_path: maps/connectors.bs
tags:
  - skupper
  - blockscape
---

# Skupper Connectors in the Application Network

Edit: [Blockscape](https://pwright.github.io/blockscape/?load=https://raw.githubusercontent.com/pwright/skupper-okf/refs/heads/main/maps/connectors.bs)

```bs full
{
  "id": "skupper-connectors-map",
  "title": "Skupper Connectors in the Application Network",
  "abstract": "How connectors help Skupper publish workloads into a secure application network so remote listeners can consume them.",
  "status": "generated",
  "reviewed": false,
  "source_paths": [
    "human/skupper-docs/input/overview/index.md",
    "human/skupper-docs/input/overview/connectivity.md",
    "human/skupper-docs/input/system-yaml/service-exposure.md",
    "human/skupper-docs/input/kube-yaml/service-exposure.md",
    "human/skupper-docs/input/refdog/topics/attached-connectors.md",
    "generated/concepts/connector.md"
  ],
  "categories": [
    {
      "id": "application-outcomes",
      "title": "Application outcomes",
      "items": [
        {
          "id": "distributed-application",
          "name": "Distributed application",
          "deps": [
            "service-exposed-to-network",
            "secure-application-network"
          ],
          "source": "human/skupper-docs/input/overview/index.md",
          "external": "https://pwright.github.io/skupper-okf/human/skupper-docs/input/overview/index"
        },
        {
          "id": "services-across-sites",
          "name": "Services across sites",
          "deps": [
            "service-exposed-to-network",
            "remote-listener-consumption"
          ],
          "source": "human/skupper-docs/input/overview/index.md",
          "external": "https://pwright.github.io/skupper-okf/human/skupper-docs/input/overview/index"
        },
        {
          "id": "private-public-cloud-composition",
          "name": "Private and public cloud composition",
          "deps": [
            "secure-application-network"
          ],
          "source": "human/skupper-docs/input/overview/connectivity.md",
          "external": "https://pwright.github.io/skupper-okf/human/skupper-docs/input/overview/connectivity"
        }
      ]
    },
    {
      "id": "service-publication",
      "title": "Service publication",
      "items": [
        {
          "id": "service-exposed-to-network",
          "name": "Service exposed to network",
          "deps": [
            "connector",
            "routing-key-match"
          ],
          "source": "human/skupper-docs/input/system-yaml/service-exposure.md",
          "external": "https://pwright.github.io/skupper-okf/human/skupper-docs/input/system-yaml/service-exposure"
        },
        {
          "id": "workload-selected",
          "name": "Workload selected",
          "deps": [
            "connector-selector-or-host"
          ],
          "source": "human/skupper-docs/input/kube-yaml/service-exposure.md",
          "external": "https://pwright.github.io/skupper-okf/human/skupper-docs/input/kube-yaml/service-exposure"
        },
        {
          "id": "remote-listener-consumption",
          "name": "Remote listener consumption",
          "deps": [
            "routing-key-match"
          ],
          "source": "human/skupper-docs/input/system-yaml/service-exposure.md",
          "external": "https://pwright.github.io/skupper-okf/human/skupper-docs/input/system-yaml/service-exposure"
        }
      ]
    },
    {
      "id": "connector-role",
      "title": "Connector role",
      "items": [
        {
          "id": "connector",
          "name": "Connector",
          "deps": [
            "connector-selector-or-host",
            "connector-port",
            "routing-key-match"
          ],
          "source": "generated/concepts/connector.md",
          "external": "https://pwright.github.io/skupper-okf/generated/concepts/connector#connector"
        },
        {
          "id": "connector-selector-or-host",
          "name": "Selector or host",
          "source": "generated/concepts/connector.md",
          "external": "https://pwright.github.io/skupper-okf/generated/concepts/connector#common-fields"
        },
        {
          "id": "connector-port",
          "name": "Target port",
          "source": "generated/concepts/connector.md",
          "external": "https://pwright.github.io/skupper-okf/generated/concepts/connector#common-fields"
        },
        {
          "id": "routing-key-match",
          "name": "Routing key match",
          "deps": [
            "matching-listener"
          ],
          "source": "human/skupper-docs/input/system-yaml/service-exposure.md",
          "external": "https://pwright.github.io/skupper-okf/human/skupper-docs/input/system-yaml/service-exposure"
        },
        {
          "id": "matching-listener",
          "name": "Matching listener",
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
          "id": "listener-to-connector-traffic",
          "name": "Listener-to-connector traffic",
          "deps": [
            "remote-listener-consumption",
            "connector"
          ],
          "source": "generated/concepts/connector.md",
          "external": "https://pwright.github.io/skupper-okf/generated/concepts/connector"
        },
        {
          "id": "router-message-forwarding",
          "name": "Router message forwarding",
          "deps": [
            "secure-application-network",
            "routing-key-match"
          ],
          "source": "human/skupper-docs/input/overview/index.md",
          "external": "https://pwright.github.io/skupper-okf/human/skupper-docs/input/overview/index"
        },
        {
          "id": "workload-server-delivery",
          "name": "Workload server delivery",
          "deps": [
            "workload-selected",
            "listener-to-connector-traffic"
          ],
          "source": "generated/concepts/connector.md",
          "external": "https://pwright.github.io/skupper-okf/generated/concepts/connector"
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
      "id": "connector-control-plane",
      "title": "Connector control plane",
      "items": [
        {
          "id": "connector-resource",
          "name": "Connector resource",
          "deps": [
            "connector-routing-key-field",
            "connector-selector-field",
            "connector-port-field"
          ],
          "source": "human/skupper-docs/input/kube-yaml/service-exposure.md",
          "external": "https://pwright.github.io/skupper-okf/human/skupper-docs/input/kube-yaml/service-exposure"
        },
        {
          "id": "connector-routing-key-field",
          "name": "spec.routingKey",
          "source": "generated/concepts/connector.md",
          "external": "https://pwright.github.io/skupper-okf/generated/concepts/connector#common-fields"
        },
        {
          "id": "connector-selector-field",
          "name": "spec.selector",
          "source": "generated/concepts/connector.md",
          "external": "https://pwright.github.io/skupper-okf/generated/concepts/connector#common-fields"
        },
        {
          "id": "connector-port-field",
          "name": "spec.port",
          "source": "generated/concepts/connector.md",
          "external": "https://pwright.github.io/skupper-okf/generated/concepts/connector#common-fields"
        },
        {
          "id": "attached-connector",
          "name": "Attached connector",
          "deps": [
            "connector",
            "peer-namespace-workload"
          ],
          "source": "human/skupper-docs/input/refdog/topics/attached-connectors.md",
          "external": "https://pwright.github.io/skupper-okf/human/skupper-docs/input/refdog/topics/attached-connectors"
        },
        {
          "id": "peer-namespace-workload",
          "name": "Peer namespace workload",
          "deps": [
            "cluster-wide-skupper"
          ],
          "source": "human/skupper-docs/input/kube-yaml/service-exposure.md",
          "external": "https://pwright.github.io/skupper-okf/human/skupper-docs/input/kube-yaml/service-exposure"
        },
        {
          "id": "cluster-wide-skupper",
          "name": "Cluster-wide Skupper",
          "source": "human/skupper-docs/input/kube-yaml/service-exposure.md",
          "external": "https://pwright.github.io/skupper-okf/human/skupper-docs/input/kube-yaml/service-exposure"
        },
        {
          "id": "connector-ready-status",
          "name": "Ready with matching listener",
          "deps": [
            "connector-resource",
            "matching-listener"
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
