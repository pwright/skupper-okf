---
title: "skupper-series series"
type: BlockscapeMap
status: generated
source_path: maps/skupper-value-perspectives.bs
tags:
  - skupper
  - blockscape
---

# skupper-series series

Edit: [Blockscape](https://pwright.github.io/blockscape/?load=https://raw.githubusercontent.com/pwright/skupper-okf/refs/heads/main/maps/skupper-value-perspectives.bs)

```bs full
{
  "blockscapeVersion": 1,
  "title": "skupper-series series",
  "settings": {
    "theme": "light",
    "hoverScale": 1.6,
    "selectionDimOpacity": 0.2,
    "selectionDimEnabled": true,
    "tileCompactness": 1,
    "titleWrapMode": "wrap",
    "titleHoverWidthMultiplier": 1.3,
    "titleHoverTextPortion": 0.25,
    "obsidianLinksEnabled": false,
    "obsidianLinkMode": "title",
    "obsidianVault": "",
    "autoIdFromName": false,
    "seriesNavDoubleClickMs": 700,
    "showSecondaryLinks": true,
    "centerItems": true,
    "centerNoStageItems": false,
    "showReusedInMap": false,
    "colorPresets": [
      {
        "name": "Black",
        "value": "#111111"
      },
      {
        "name": "White",
        "value": "#ffffff"
      },
      {
        "name": "Red",
        "value": "#ef4444"
      },
      {
        "name": "Green",
        "value": "#22c55e"
      },
      {
        "name": "Blue",
        "value": "#2563eb"
      }
    ],
    "depColor": "#2563eb",
    "revdepColor": "#ef4444",
    "linkThickness": "l",
    "stripParentheticalNames": true
  },
  "maps": [
    {
      "id": "skupper-business-value",
      "title": "Skupper Business Value Chain",
      "abstract": "Skupper enables organizations to connect application services securely across clusters, clouds, data centers, and local systems while reducing the need for applications to understand network location. From a business perspective, this supports faster cloud migration, greater workload-placement freedom, improved resilience, regional expansion, and better infrastructure utilization. These outcomes are enabled by location-independent service connectivity, cross-site routing and failover, secure application networks, and Skupper's underlying sites, links, listeners, connectors, and routers.",
      "categories": [
        {
          "id": "business-value",
          "title": "Business Value",
          "items": [
            {
              "id": "faster-change",
              "name": "Faster Business & Technology Change",
              "deps": [
                "migration-flexibility",
                "delivery-velocity"
              ],
              "source": "generated/skupper-value-perspectives/faster-change.md",
              "external": "https://pwright.github.io/skupper-okf/generated/skupper-value-perspectives/faster-change"
            },
            {
              "id": "business-continuity",
              "name": "Business Continuity",
              "deps": [
                "cross-site-resilience",
                "multi-site-services"
              ],
              "source": "generated/skupper-value-perspectives/business-continuity.md",
              "external": "https://pwright.github.io/skupper-okf/generated/skupper-value-perspectives/business-continuity"
            },
            {
              "id": "cloud-cost-flexibility",
              "name": "Cloud Cost & Capacity Flexibility",
              "deps": [
                "workload-placement",
                "capacity-spillover"
              ],
              "source": "generated/skupper-value-perspectives/cloud-cost-flexibility.md",
              "external": "https://pwright.github.io/skupper-okf/generated/skupper-value-perspectives/cloud-cost-flexibility"
            },
            {
              "id": "market-reach",
              "name": "Faster Regional & Market Expansion",
              "deps": [
                "regional-deployment",
                "multi-site-services"
              ],
              "source": "generated/skupper-value-perspectives/market-reach.md",
              "external": "https://pwright.github.io/skupper-okf/generated/skupper-value-perspectives/market-reach"
            },
            {
              "id": "reduced-integration-risk",
              "name": "Reduced Integration Risk",
              "deps": [
                "secure-connectivity",
                "location-independence"
              ],
              "source": "generated/skupper-value-perspectives/reduced-integration-risk.md",
              "external": "https://pwright.github.io/skupper-okf/generated/skupper-value-perspectives/reduced-integration-risk"
            }
          ]
        },
        {
          "id": "strategic-use-cases",
          "title": "Strategic Use Cases",
          "items": [
            {
              "id": "migration-flexibility",
              "name": "Incremental Cloud Migration",
              "deps": [
                "location-independence",
                "skupper-network-engineering-pov"
              ],
              "source": "generated/skupper-value-perspectives/migration-flexibility.md",
              "external": "https://pwright.github.io/skupper-okf/generated/skupper-value-perspectives/migration-flexibility"
            },
            {
              "id": "delivery-velocity",
              "name": "Faster Application Delivery",
              "deps": [
                "service-connectivity",
                "skupper-application-engineering-pov"
              ],
              "source": "generated/skupper-value-perspectives/delivery-velocity.md",
              "external": "https://pwright.github.io/skupper-okf/generated/skupper-value-perspectives/delivery-velocity"
            },
            {
              "id": "cross-site-resilience",
              "name": "Cross-Site Resilience & Failover",
              "deps": [
                "adaptive-routing",
                "service-failover"
              ],
              "source": "generated/skupper-value-perspectives/cross-site-resilience.md",
              "external": "https://pwright.github.io/skupper-okf/generated/skupper-value-perspectives/cross-site-resilience"
            },
            {
              "id": "workload-placement",
              "name": "Workload Placement Freedom",
              "deps": [
                "location-independence",
                "skupper-network-engineering-pov"
              ],
              "source": "generated/skupper-value-perspectives/workload-placement.md",
              "external": "https://pwright.github.io/skupper-okf/generated/skupper-value-perspectives/workload-placement"
            },
            {
              "id": "capacity-spillover",
              "name": "Hybrid-Cloud Capacity Spillover",
              "deps": [
                "adaptive-routing",
                "multi-site-services"
              ],
              "source": "generated/skupper-value-perspectives/capacity-spillover.md",
              "external": "https://pwright.github.io/skupper-okf/generated/skupper-value-perspectives/capacity-spillover"
            },
            {
              "id": "regional-deployment",
              "name": "Distributed Regional Deployment",
              "deps": [
                "multi-site-services",
                "secure-connectivity"
              ],
              "source": "generated/skupper-value-perspectives/regional-deployment.md",
              "external": "https://pwright.github.io/skupper-okf/generated/skupper-value-perspectives/regional-deployment"
            }
          ]
        },
        {
          "id": "application-capabilities",
          "title": "Application Connectivity Capabilities",
          "items": [
            {
              "id": "location-independence",
              "name": "Location-Independent Applications",
              "deps": [
                "service-connectivity",
                "routing-keys"
              ],
              "external": "[https://skupper.io/docs/refdog/concepts/index.html](https://skupper.io/docs/refdog/concepts/index.html)",
              "source": "generated/skupper-value-perspectives/location-independence.md"
            },
            {
              "id": "multi-site-services",
              "name": "Multi-Site Application Services",
              "deps": [
                "adaptive-routing",
                "listeners-connectors"
              ],
              "external": "[https://skupper.io/docs/overview/routing.html](https://skupper.io/docs/overview/routing.html)",
              "source": "generated/skupper-value-perspectives/multi-site-services.md"
            },
            {
              "id": "service-connectivity",
              "name": "Transparent Service-to-Service Connectivity",
              "deps": [
                "listeners-connectors",
                "site-links"
              ],
              "external": "[https://skupper.io/docs/kube-cli/service-exposure.html](https://skupper.io/docs/kube-cli/service-exposure.html)",
              "source": "generated/skupper-value-perspectives/service-connectivity.md"
            },
            {
              "id": "service-failover",
              "name": "Cross-Site Load Balancing & Failover",
              "deps": [
                "adaptive-routing",
                "skupper-router"
              ],
              "external": "[https://skupper.io/docs/overview/load-balancing.html](https://skupper.io/docs/overview/load-balancing.html)",
              "source": "generated/skupper-value-perspectives/service-failover.md"
            },
            {
              "id": "secure-connectivity",
              "name": "Secure Private Application Connectivity",
              "deps": [
                "mtls",
                "access-tokens",
                "site-links"
              ],
              "external": "[https://skupper.io/docs/kube-cli/site-linking.html](https://skupper.io/docs/kube-cli/site-linking.html)",
              "source": "generated/skupper-value-perspectives/secure-connectivity.md"
            },
            {
              "id": "skupper-network-engineering-pov",
              "name": "Cross-Platform Connectivity",
              "deps": [
                "skupper-sites",
                "site-links"
              ],
              "external": "[https://skupper.io/docs/refdog/concepts/index.html](https://skupper.io/docs/refdog/concepts/index.html)",
              "source": "generated/skupper-value-perspectives/skupper-network-engineering-pov.md"
            }
          ]
        },
        {
          "id": "platform-services",
          "title": "Platform & Operating Model",
          "items": [
            {
              "id": "adaptive-routing",
              "name": "Application-Aware Routing",
              "deps": [
                "routing-keys",
                "skupper-router"
              ],
              "external": "[https://skupper.io/docs/overview/routing.html](https://skupper.io/docs/overview/routing.html)",
              "source": "generated/skupper-value-perspectives/adaptive-routing.md"
            },
            {
              "id": "skupper-application-engineering-pov",
              "name": "Declarative Application Networking",
              "deps": [
                "skupper-sites",
                "listeners-connectors",
                "site-links"
              ],
              "external": "[https://skupper.io/docs/](https://skupper.io/docs/)",
              "source": "generated/skupper-value-perspectives/skupper-application-engineering-pov.md"
            },
            {
              "id": "listeners-connectors",
              "name": "Listeners & Connectors",
              "deps": [
                "routing-keys",
                "skupper-router"
              ],
              "external": "[https://skupper.io/docs/kube-cli/service-exposure.html](https://skupper.io/docs/kube-cli/service-exposure.html)",
              "source": "generated/skupper-value-perspectives/listeners-connectors.md"
            },
            {
              "id": "routing-keys",
              "name": "Application-Layer Service Addressing",
              "deps": [
                "skupper-router"
              ],
              "external": "[https://skupper.io/docs/overview/routing.html](https://skupper.io/docs/overview/routing.html)",
              "source": "generated/skupper-value-perspectives/routing-keys.md"
            },
            {
              "id": "mtls",
              "name": "Mutual TLS Protection",
              "deps": [
                "skupper-router"
              ],
              "external": "[https://skupper.io/docs/kube-cli/site-linking.html](https://skupper.io/docs/kube-cli/site-linking.html)",
              "source": "generated/skupper-value-perspectives/mtls.md"
            },
            {
              "id": "access-tokens",
              "name": "Controlled Site Enrollment",
              "deps": [
                "skupper-sites"
              ],
              "external": "[https://skupper.io/docs/kube-cli/site-linking.html](https://skupper.io/docs/kube-cli/site-linking.html)",
              "source": "generated/skupper-value-perspectives/access-tokens.md"
            }
          ]
        },
        {
          "id": "foundation",
          "title": "Skupper Foundation",
          "items": [
            {
              "id": "skupper-sites",
              "name": "Skupper Sites",
              "deps": [],
              "external": "[https://skupper.io/docs/refdog/concepts/index.html](https://skupper.io/docs/refdog/concepts/index.html)",
              "source": "generated/skupper-value-perspectives/skupper-sites.md"
            },
            {
              "id": "site-links",
              "name": "Secure Site-to-Site Links",
              "deps": [
                "skupper-sites",
                "skupper-router"
              ],
              "external": "[https://skupper.io/docs/kube-cli/site-linking.html](https://skupper.io/docs/kube-cli/site-linking.html)",
              "source": "generated/skupper-value-perspectives/site-links.md"
            },
            {
              "id": "skupper-router",
              "name": "Skupper Router",
              "deps": [],
              "external": "[https://skupper.io/docs/overview/resources.html](https://skupper.io/docs/overview/resources.html)",
              "source": "generated/skupper-value-perspectives/skupper-router.md"
            },
            {
              "id": "kubernetes",
              "name": "Kubernetes",
              "deps": [],
              "source": "generated/skupper-value-perspectives/kubernetes.md",
              "external": "https://pwright.github.io/skupper-okf/generated/skupper-value-perspectives/kubernetes"
            },
            {
              "id": "local-platforms",
              "name": "Docker, Podman & Linux Systems",
              "deps": [],
              "source": "generated/skupper-value-perspectives/local-platforms.md",
              "external": "https://pwright.github.io/skupper-okf/generated/skupper-value-perspectives/local-platforms"
            }
          ]
        }
      ],
      "seriesId": "skupper-series"
    },
    {
      "id": "skupper-application-engineering-pov",
      "title": "Application Engineering POV - Skupper Layered Connectivity",
      "abstract": "Application engineers see Skupper as a way to connect clients and servers through familiar listener and connector abstractions without coupling applications to network location. The application-facing Client, Listener, Connector, and Server remain at the top, with routing keys, service routing, sites, routers, secure inter-site links, and mutual TLS providing the underlying connectivity.",
      "categories": [
        {
          "id": "application-endpoints",
          "title": "Application Endpoints",
          "items": [
            {
              "id": "connector",
              "name": "Connector",
              "deps": [
                "routing-key",
                "skupper-site"
              ],
              "source": "generated/skupper-value-perspectives/connector.md",
              "external": "https://pwright.github.io/skupper-okf/generated/skupper-value-perspectives/connector"
            },
            {
              "id": "server",
              "name": "Server",
              "deps": [
                "connector"
              ],
              "source": "generated/skupper-value-perspectives/server.md",
              "external": "https://pwright.github.io/skupper-okf/generated/skupper-value-perspectives/server"
            },
            {
              "id": "client",
              "name": "Client",
              "deps": [
                "listener"
              ],
              "source": "generated/skupper-value-perspectives/client.md",
              "external": "https://pwright.github.io/skupper-okf/generated/skupper-value-perspectives/client"
            },
            {
              "id": "listener",
              "name": "Listener",
              "deps": [
                "routing-key",
                "skupper-site"
              ],
              "source": "generated/skupper-value-perspectives/listener.md",
              "external": "https://pwright.github.io/skupper-okf/generated/skupper-value-perspectives/listener"
            }
          ]
        },
        {
          "id": "service-layer",
          "title": "Skupper Service Layer",
          "items": [
            {
              "id": "routing-key",
              "name": "Routing Key",
              "deps": [
                "service-routing"
              ],
              "source": "generated/skupper-value-perspectives/routing-key.md",
              "external": "https://pwright.github.io/skupper-okf/generated/skupper-value-perspectives/routing-key"
            },
            {
              "id": "service-routing",
              "name": "Service Routing",
              "deps": [
                "router"
              ],
              "source": "generated/skupper-value-perspectives/service-routing.md",
              "external": "https://pwright.github.io/skupper-okf/generated/skupper-value-perspectives/service-routing"
            },
            {
              "id": "service-binding",
              "name": "Service Binding",
              "deps": [
                "routing-key",
                "skupper-config"
              ],
              "source": "generated/skupper-value-perspectives/service-binding.md",
              "external": "https://pwright.github.io/skupper-okf/generated/skupper-value-perspectives/service-binding"
            }
          ]
        },
        {
          "id": "site-layer",
          "title": "Skupper Site Layer",
          "items": [
            {
              "id": "skupper-site",
              "name": "Skupper Site",
              "deps": [
                "router",
                "skupper-config"
              ],
              "source": "generated/skupper-value-perspectives/skupper-site.md",
              "external": "https://pwright.github.io/skupper-okf/generated/skupper-value-perspectives/skupper-site"
            },
            {
              "id": "skupper-config",
              "name": "Skupper Configuration",
              "deps": [
                "site-identity"
              ],
              "source": "generated/skupper-value-perspectives/skupper-config.md",
              "external": "https://pwright.github.io/skupper-okf/generated/skupper-value-perspectives/skupper-config"
            },
            {
              "id": "site-identity",
              "name": "Site Identity",
              "deps": [
                "credentials"
              ],
              "source": "generated/skupper-value-perspectives/site-identity.md",
              "external": "https://pwright.github.io/skupper-okf/generated/skupper-value-perspectives/site-identity"
            }
          ]
        },
        {
          "id": "routing-layer",
          "title": "Routing Layer",
          "items": [
            {
              "id": "router",
              "name": "Skupper Router",
              "deps": [
                "inter-site-link"
              ],
              "source": "generated/skupper-value-perspectives/router.md",
              "external": "https://pwright.github.io/skupper-okf/generated/skupper-value-perspectives/router"
            },
            {
              "id": "inter-site-link",
              "name": "Inter-site Link",
              "deps": [
                "secure-transport"
              ],
              "source": "generated/skupper-value-perspectives/inter-site-link.md",
              "external": "https://pwright.github.io/skupper-okf/generated/skupper-value-perspectives/inter-site-link"
            },
            {
              "id": "route-discovery",
              "name": "Route Discovery",
              "deps": [
                "router"
              ],
              "source": "generated/skupper-value-perspectives/route-discovery.md",
              "external": "https://pwright.github.io/skupper-okf/generated/skupper-value-perspectives/route-discovery"
            }
          ]
        },
        {
          "id": "transport-layer",
          "title": "Secure Transport",
          "items": [
            {
              "id": "secure-transport",
              "name": "Secure Transport",
              "deps": [
                "mutual-tls",
                "network-reachability"
              ],
              "source": "generated/skupper-value-perspectives/secure-transport.md",
              "external": "https://pwright.github.io/skupper-okf/generated/skupper-value-perspectives/secure-transport"
            },
            {
              "id": "mutual-tls",
              "name": "Mutual TLS",
              "deps": [
                "credentials"
              ],
              "source": "generated/skupper-value-perspectives/mutual-tls.md",
              "external": "https://pwright.github.io/skupper-okf/generated/skupper-value-perspectives/mutual-tls"
            },
            {
              "id": "credentials",
              "name": "Link Credentials",
              "deps": [],
              "source": "generated/skupper-value-perspectives/credentials.md",
              "external": "https://pwright.github.io/skupper-okf/generated/skupper-value-perspectives/credentials"
            },
            {
              "id": "network-reachability",
              "name": "Network Reachability",
              "deps": [],
              "source": "generated/skupper-value-perspectives/network-reachability.md",
              "external": "https://pwright.github.io/skupper-okf/generated/skupper-value-perspectives/network-reachability"
            }
          ]
        }
      ],
      "seriesId": "skupper-series"
    },
    {
      "id": "skupper-network-engineering-pov",
      "title": "Network Engineering POV - Site Platform Choices",
      "abstract": "Network engineers manage Skupper sites as platform-aware connectivity endpoints. West site runs on Kubernetes while East site runs directly on Podman, and both paths converge on shared host, control-plane, adaptor, container-runtime, and routing capabilities. This view emphasizes platform implementation choices and the network infrastructure required to realize site connectivity.",
      "categories": [
        {
          "id": "sites",
          "title": "Sites",
          "items": [
            {
              "id": "platform1",
              "name": "Platform",
              "deps": [
                "kubernetes-platform"
              ],
              "source": "generated/skupper-value-perspectives/platform1.md",
              "external": "https://pwright.github.io/skupper-okf/generated/skupper-value-perspectives/platform1"
            },
            {
              "id": "west-site",
              "name": "West site",
              "deps": [
                "platform1",
                "kubernetes-platform",
                "kube-adaptor"
              ],
              "source": "generated/skupper-value-perspectives/west-site.md",
              "external": "https://pwright.github.io/skupper-okf/generated/skupper-value-perspectives/west-site"
            },
            {
              "id": "east-site",
              "name": "East site",
              "deps": [
                "platform",
                "podman",
                "container-host-platform"
              ],
              "source": "generated/skupper-value-perspectives/east-site.md",
              "external": "https://pwright.github.io/skupper-okf/generated/skupper-value-perspectives/east-site"
            },
            {
              "id": "platform",
              "name": "Platform",
              "deps": [
                "container-host-platform"
              ],
              "source": "generated/skupper-value-perspectives/platform.md",
              "external": "https://pwright.github.io/skupper-okf/generated/skupper-value-perspectives/platform"
            }
          ]
        },
        {
          "id": "platform-management",
          "title": "Platform Choice & Management",
          "items": [
            {
              "id": "skupper-platform-choices",
              "name": "Site Platform Choice",
              "deps": [
                "kubernetes-platform",
                "container-host-platform"
              ],
              "source": "generated/skupper-value-perspectives/skupper-platform-choices.md",
              "external": "https://pwright.github.io/skupper-okf/generated/skupper-value-perspectives/skupper-platform-choices"
            },
            {
              "id": "site-control-plane",
              "name": "Site Control Plane",
              "deps": [
                "skupper-platform-choices",
                "kube-adaptor",
                "network-intent"
              ],
              "source": "generated/skupper-value-perspectives/site-control-plane.md",
              "external": "https://pwright.github.io/skupper-okf/generated/skupper-value-perspectives/site-control-plane"
            },
            {
              "id": "desired-state",
              "name": "Desired Network State",
              "deps": [
                "site-control-plane"
              ],
              "source": "generated/skupper-value-perspectives/desired-state.md",
              "external": "https://pwright.github.io/skupper-okf/generated/skupper-value-perspectives/desired-state"
            }
          ]
        },
        {
          "id": "platform-options",
          "title": "Platform Implementations",
          "items": [
            {
              "id": "kubernetes-platform",
              "name": "Kubernetes",
              "deps": [
                "kube-api",
                "kubelet",
                "container-runtime",
                "systemd"
              ],
              "source": "generated/skupper-value-perspectives/kubernetes-platform.md",
              "external": "https://pwright.github.io/skupper-okf/generated/skupper-value-perspectives/kubernetes-platform"
            },
            {
              "id": "ocp-platform",
              "name": "OpenShift Container Platform",
              "deps": [
                "kubernetes-platform",
                "crio-runtime",
                "systemd"
              ],
              "source": "generated/skupper-value-perspectives/ocp-platform.md",
              "external": "https://pwright.github.io/skupper-okf/generated/skupper-value-perspectives/ocp-platform"
            },
            {
              "id": "container-host-platform",
              "name": "Container Host",
              "deps": [
                "podman",
                "systemd",
                "linux-host"
              ],
              "source": "generated/skupper-value-perspectives/container-host-platform.md",
              "external": "https://pwright.github.io/skupper-okf/generated/skupper-value-perspectives/container-host-platform"
            }
          ]
        },
        {
          "id": "adaptors",
          "title": "Platform Adaptors",
          "items": [
            {
              "id": "kube-adaptor",
              "name": "Kubernetes Adaptor",
              "deps": [
                "kube-api",
                "network-intent"
              ],
              "source": "generated/skupper-value-perspectives/kube-adaptor.md",
              "external": "https://pwright.github.io/skupper-okf/generated/skupper-value-perspectives/kube-adaptor"
            },
            {
              "id": "network-intent",
              "name": "Network Intent Translation",
              "deps": [
                "router-api"
              ],
              "source": "generated/skupper-value-perspectives/network-intent.md",
              "external": "https://pwright.github.io/skupper-okf/generated/skupper-value-perspectives/network-intent"
            },
            {
              "id": "kube-api",
              "name": "Kubernetes API",
              "deps": [
                "kubelet"
              ],
              "source": "generated/skupper-value-perspectives/kube-api.md",
              "external": "https://pwright.github.io/skupper-okf/generated/skupper-value-perspectives/kube-api"
            }
          ]
        },
        {
          "id": "container-platform",
          "title": "Containers & Workload Runtime",
          "items": [
            {
              "id": "kubelet",
              "name": "Kubelet",
              "deps": [
                "container-runtime",
                "systemd"
              ],
              "source": "generated/skupper-value-perspectives/kubelet.md",
              "external": "https://pwright.github.io/skupper-okf/generated/skupper-value-perspectives/kubelet"
            },
            {
              "id": "container-runtime",
              "name": "Container Runtime Interface",
              "deps": [
                "containerd-runtime",
                "crio-runtime"
              ],
              "source": "generated/skupper-value-perspectives/container-runtime.md",
              "external": "https://pwright.github.io/skupper-okf/generated/skupper-value-perspectives/container-runtime"
            },
            {
              "id": "podman",
              "name": "Podman",
              "deps": [
                "oci-runtime",
                "systemd",
                "linux-host"
              ],
              "source": "generated/skupper-value-perspectives/podman.md",
              "external": "https://pwright.github.io/skupper-okf/generated/skupper-value-perspectives/podman"
            },
            {
              "id": "docker",
              "name": "Docker",
              "deps": [
                "containerd-runtime",
                "oci-runtime",
                "systemd"
              ],
              "source": "generated/skupper-value-perspectives/docker.md",
              "external": "https://pwright.github.io/skupper-okf/generated/skupper-value-perspectives/docker"
            },
            {
              "id": "containerd-runtime",
              "name": "containerd",
              "deps": [
                "oci-runtime",
                "systemd"
              ],
              "source": "generated/skupper-value-perspectives/containerd-runtime.md",
              "external": "https://pwright.github.io/skupper-okf/generated/skupper-value-perspectives/containerd-runtime"
            },
            {
              "id": "crio-runtime",
              "name": "CRI-O",
              "deps": [
                "oci-runtime",
                "systemd"
              ],
              "source": "generated/skupper-value-perspectives/crio-runtime.md",
              "external": "https://pwright.github.io/skupper-okf/generated/skupper-value-perspectives/crio-runtime"
            }
          ]
        },
        {
          "id": "host-services",
          "title": "Host & Service Management",
          "items": [
            {
              "id": "systemd",
              "name": "systemd",
              "deps": [
                "linux-host"
              ],
              "source": "generated/skupper-value-perspectives/systemd.md",
              "external": "https://pwright.github.io/skupper-okf/generated/skupper-value-perspectives/systemd"
            },
            {
              "id": "oci-runtime",
              "name": "OCI Runtime",
              "deps": [
                "linux-host"
              ],
              "source": "generated/skupper-value-perspectives/oci-runtime.md",
              "external": "https://pwright.github.io/skupper-okf/generated/skupper-value-perspectives/oci-runtime"
            },
            {
              "id": "linux-host",
              "name": "Linux Host",
              "deps": [],
              "source": "generated/skupper-value-perspectives/linux-host.md",
              "external": "https://pwright.github.io/skupper-okf/generated/skupper-value-perspectives/linux-host"
            }
          ]
        },
        {
          "id": "network-routing",
          "title": "Routing & Network Infrastructure",
          "items": [
            {
              "id": "router-api",
              "name": "Router API",
              "deps": [
                "site-router"
              ],
              "source": "generated/skupper-value-perspectives/router-api.md",
              "external": "https://pwright.github.io/skupper-okf/generated/skupper-value-perspectives/router-api"
            },
            {
              "id": "site-router",
              "name": "Site Router",
              "deps": [
                "routing-stack",
                "linux-host"
              ],
              "source": "generated/skupper-value-perspectives/site-router.md",
              "external": "https://pwright.github.io/skupper-okf/generated/skupper-value-perspectives/site-router"
            },
            {
              "id": "routing-stack",
              "name": "Routing Stack",
              "deps": [
                "linux-host"
              ],
              "source": "generated/skupper-value-perspectives/routing-stack.md",
              "external": "https://pwright.github.io/skupper-okf/generated/skupper-value-perspectives/routing-stack"
            }
          ]
        }
      ],
      "seriesId": "skupper-series"
    },
    {
      "id": "skupper-platform-choices",
      "title": "Skupper Platform Choices",
      "abstract": "Skupper helps teams connect services across environments, so the main user-facing decision is which platform hosts a Skupper site: systemd, podman, docker, kubernetes, or openshift. Each choice relies on common Skupper site capabilities for exposing services and creating links, plus underlying security, networking, and runtime primitives that make the application network work reliably.",
      "categories": [
        {
          "id": "platforms",
          "title": "Platform Choices",
          "items": [
            {
              "id": "systemd",
              "name": "Systemd",
              "deps": [
                "site-runtime",
                "site-linking",
                "host-network",
                "tls-identity"
              ],
              "source": "generated/skupper-value-perspectives/systemd.md",
              "external": "https://pwright.github.io/skupper-okf/generated/skupper-value-perspectives/systemd"
            },
            {
              "id": "podman",
              "name": "Podman",
              "deps": [
                "site-runtime",
                "site-linking",
                "container-runtime",
                "host-network",
                "tls-identity"
              ],
              "source": "generated/skupper-value-perspectives/podman.md",
              "external": "https://pwright.github.io/skupper-okf/generated/skupper-value-perspectives/podman"
            },
            {
              "id": "docker",
              "name": "Docker",
              "deps": [
                "site-runtime",
                "site-linking",
                "container-runtime",
                "bridge-network",
                "tls-identity"
              ],
              "source": "generated/skupper-value-perspectives/docker.md",
              "external": "https://pwright.github.io/skupper-okf/generated/skupper-value-perspectives/docker"
            },
            {
              "id": "kubernetes",
              "name": "Kubernetes",
              "deps": [
                "site-controller",
                "service-exposure",
                "site-linking",
                "cluster-network",
                "tls-identity"
              ],
              "source": "generated/skupper-value-perspectives/kubernetes.md",
              "external": "https://pwright.github.io/skupper-okf/generated/skupper-value-perspectives/kubernetes"
            },
            {
              "id": "openshift",
              "name": "OpenShift",
              "deps": [
                "site-controller",
                "service-exposure",
                "site-linking",
                "route-scc",
                "tls-identity"
              ],
              "source": "generated/skupper-value-perspectives/openshift.md",
              "external": "https://pwright.github.io/skupper-okf/generated/skupper-value-perspectives/openshift"
            }
          ]
        },
        {
          "id": "site-capabilities",
          "title": "Skupper Site Capabilities",
          "items": [
            {
              "id": "site-controller",
              "name": "Site Controller",
              "deps": [
                "router-core",
                "secret-store"
              ],
              "source": "generated/skupper-value-perspectives/site-controller.md",
              "external": "https://pwright.github.io/skupper-okf/generated/skupper-value-perspectives/site-controller"
            },
            {
              "id": "site-runtime",
              "name": "Site Runtime",
              "deps": [
                "router-core",
                "listener-connector"
              ],
              "source": "generated/skupper-value-perspectives/site-runtime.md",
              "external": "https://pwright.github.io/skupper-okf/generated/skupper-value-perspectives/site-runtime"
            },
            {
              "id": "service-exposure",
              "name": "Service Exposure",
              "deps": [
                "service-sync",
                "listener-connector"
              ],
              "source": "generated/skupper-value-perspectives/service-exposure.md",
              "external": "https://pwright.github.io/skupper-okf/generated/skupper-value-perspectives/service-exposure"
            },
            {
              "id": "site-linking",
              "name": "Site Linking",
              "deps": [
                "link-token",
                "tls-identity"
              ],
              "source": "generated/skupper-value-perspectives/site-linking.md",
              "external": "https://pwright.github.io/skupper-okf/generated/skupper-value-perspectives/site-linking"
            },
            {
              "id": "console",
              "name": "Console & Status",
              "deps": [
                "metrics",
                "router-core"
              ],
              "source": "generated/skupper-value-perspectives/console.md",
              "external": "https://pwright.github.io/skupper-okf/generated/skupper-value-perspectives/console"
            }
          ]
        },
        {
          "id": "security-networking",
          "title": "Security & Networking",
          "items": [
            {
              "id": "tls-identity",
              "name": "TLS Identity",
              "deps": [
                "secret-store"
              ],
              "source": "generated/skupper-value-perspectives/tls-identity.md",
              "external": "https://pwright.github.io/skupper-okf/generated/skupper-value-perspectives/tls-identity"
            },
            {
              "id": "link-token",
              "name": "Link Token",
              "deps": [
                "secret-store"
              ],
              "source": "generated/skupper-value-perspectives/link-token.md",
              "external": "https://pwright.github.io/skupper-okf/generated/skupper-value-perspectives/link-token"
            },
            {
              "id": "cluster-network",
              "name": "Cluster Networking",
              "deps": [],
              "source": "generated/skupper-value-perspectives/cluster-network.md",
              "external": "https://pwright.github.io/skupper-okf/generated/skupper-value-perspectives/cluster-network"
            },
            {
              "id": "host-network",
              "name": "Host Networking",
              "deps": [],
              "source": "generated/skupper-value-perspectives/host-network.md",
              "external": "https://pwright.github.io/skupper-okf/generated/skupper-value-perspectives/host-network"
            },
            {
              "id": "bridge-network",
              "name": "Bridge Networking",
              "deps": [
                "host-network"
              ],
              "source": "generated/skupper-value-perspectives/bridge-network.md",
              "external": "https://pwright.github.io/skupper-okf/generated/skupper-value-perspectives/bridge-network"
            },
            {
              "id": "route-scc",
              "name": "Routes & SCC",
              "deps": [
                "cluster-network"
              ],
              "source": "generated/skupper-value-perspectives/route-scc.md",
              "external": "https://pwright.github.io/skupper-okf/generated/skupper-value-perspectives/route-scc"
            }
          ]
        },
        {
          "id": "runtime-primitives",
          "title": "Runtime Primitives",
          "items": [
            {
              "id": "router-core",
              "name": "Router Core",
              "deps": [],
              "source": "generated/skupper-value-perspectives/router-core.md",
              "external": "https://pwright.github.io/skupper-okf/generated/skupper-value-perspectives/router-core"
            },
            {
              "id": "service-sync",
              "name": "Service Sync",
              "deps": [
                "router-core"
              ],
              "source": "generated/skupper-value-perspectives/service-sync.md",
              "external": "https://pwright.github.io/skupper-okf/generated/skupper-value-perspectives/service-sync"
            },
            {
              "id": "listener-connector",
              "name": "Listeners & Connectors",
              "deps": [
                "router-core"
              ],
              "source": "generated/skupper-value-perspectives/listener-connector.md",
              "external": "https://pwright.github.io/skupper-okf/generated/skupper-value-perspectives/listener-connector"
            },
            {
              "id": "secret-store",
              "name": "Secret Store",
              "deps": [],
              "source": "generated/skupper-value-perspectives/secret-store.md",
              "external": "https://pwright.github.io/skupper-okf/generated/skupper-value-perspectives/secret-store"
            },
            {
              "id": "container-runtime",
              "name": "Container Runtime",
              "deps": [],
              "source": "generated/skupper-value-perspectives/container-runtime.md",
              "external": "https://pwright.github.io/skupper-okf/generated/skupper-value-perspectives/container-runtime"
            },
            {
              "id": "metrics",
              "name": "Metrics",
              "deps": [],
              "source": "generated/skupper-value-perspectives/metrics.md",
              "external": "https://pwright.github.io/skupper-okf/generated/skupper-value-perspectives/metrics"
            }
          ]
        }
      ],
      "seriesId": "skupper-series"
    }
  ]
}
```
