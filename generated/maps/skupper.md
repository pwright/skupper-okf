---
title: "Skupper Blockscape maps"
type: BlockscapeMap
status: generated
source_path: maps/skupper.bs
tags:
  - skupper
  - blockscape
---

# Skupper Blockscape maps

Edit: [Blockscape](https://pwright.github.io/blockscape/?load=https://raw.githubusercontent.com/pwright/skupper-okf/refs/heads/main/maps/skupper.bs)

```bs full
[
  {
    "id": "skupper-application-network-map",
    "title": "Skupper Application Network",
    "abstract": "How Skupper uses listeners and connectors to let distributed application services communicate across sites.",
    "status": "generated",
    "reviewed": false,
    "source_paths": [
      "human/skupper-docs/input/overview/index.md",
      "human/skupper-docs/input/overview/connectivity.md",
      "human/skupper-docs/input/system-yaml/service-exposure.md",
      "generated/concepts/listener.md",
      "generated/concepts/connector.md"
    ],
    "categories": [
      {
        "id": "user-outcomes",
        "title": "User outcomes",
        "items": [
          {
            "id": "distributed-applications-communicate",
            "name": "Distributed applications communicate",
            "deps": [
              "skupper-listeners-map",
              "skupper-connectors-map"
            ],
            "source": "human/skupper-docs/input/overview/index.md",
            "external": "https://pwright.github.io/skupper-okf/human/skupper-docs/input/overview/index"
          },
          {
            "id": "services-feel-local-across-sites",
            "name": "Services feel local across sites",
            "deps": [
              "skupper-listeners-map",
              "skupper-connectors-map"
            ],
            "source": "human/skupper-docs/input/system-yaml/service-exposure.md",
            "external": "https://pwright.github.io/skupper-okf/human/skupper-docs/input/system-yaml/service-exposure"
          },
          {
            "id": "secure-hybrid-cloud-connectivity",
            "name": "Secure hybrid cloud connectivity",
            "deps": [
              "skupper-listeners-map",
              "skupper-connectors-map"
            ],
            "source": "human/skupper-docs/input/overview/connectivity.md",
            "external": "https://pwright.github.io/skupper-okf/human/skupper-docs/input/overview/connectivity"
          }
        ]
      },
      {
        "id": "service-exposure-primitives",
        "title": "Service exposure primitives",
        "items": [
          {
            "id": "skupper-listeners-map",
            "name": "Listeners",
            "source": "generated/concepts/listener.md",
            "external": "https://pwright.github.io/skupper-okf/generated/concepts/listener",
            "deps": []
          },
          {
            "id": "skupper-connectors-map",
            "name": "Connectors",
            "source": "generated/concepts/connector.md",
            "external": "https://pwright.github.io/skupper-okf/generated/concepts/connector",
            "deps": []
          }
        ]
      }
    ],
    "source_base_url": "https://pwright.github.io/skupper-okf/"
  },
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
  },
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
]
```
