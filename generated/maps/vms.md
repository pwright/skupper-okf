---
title: "Vms"
type: BlockscapeMap
status: generated
source_path: maps/vms.bs
tags:
  - skupper
  - blockscape
---

# Vms

Edit: [Blockscape](https://pwright.github.io/blockscape/?load=https://raw.githubusercontent.com/pwright/skupper-okf/refs/heads/main/maps/vms.bs)

```bs full
[
  {
    "id": "vms-overview",
    "title": "Skupper VMS - Multi-tenant VAN Management System",
    "abstract": "Centralized management, monitoring, and automation for Skupper Virtual Application Networks. VMS controls both network topology (where sites connect) and application topology (what services are exposed) while automating certificate management, site bootstrapping, and operational tasks that Skupper users handle manually.",
    "categories": [
      {
        "id": "functional-domains",
        "title": "Functional Domains",
        "items": [
          {
            "id": "vms-network-topology",
            "name": "Network Topology Management",
            "abstract": "Backbone networks, sites, links, and access points - the spatial layout of where distributed application components can reside"
          },
          {
            "id": "vms-application-lifecycle",
            "name": "Application Network Lifecycle",
            "abstract": "VAN creation, invitation-based participation, member management, and eviction - the application networking layer"
          },
          {
            "id": "vms-security-pki",
            "name": "Security & PKI",
            "abstract": "Hierarchical certificate authorities, automatic rotation, and revocation - security without manual cert management"
          },
          {
            "id": "vms-architecture",
            "name": "Control & Data Plane Architecture",
            "abstract": "Management plane components, site controllers, and Skupper router data plane - the system architecture"
          }
        ]
      },
      {
        "id": "vms-value",
        "title": "VMS Automation Value",
        "items": [
          {
            "id": "centralized-management",
            "name": "Centralized Control",
            "abstract": "Single management plane for all backbones and VANs across the enterprise - eliminates per-site administration",
            "deps": ["vms-architecture"]
          },
          {
            "id": "topology-abstraction",
            "name": "Topology Abstraction",
            "abstract": "VAN owners specify participants, not router topology - VMS handles optimal backbone routing",
            "deps": ["vms-network-topology"]
          },
          {
            "id": "invitation-based-access",
            "name": "Invitation-based Access",
            "abstract": "Participants join VANs with invitation YAML - video-conference workflow eliminates manual site coordination",
            "deps": ["vms-application-lifecycle"]
          },
          {
            "id": "zero-touch-certificates",
            "name": "Zero-touch Certificate Lifecycle",
            "abstract": "Automatic generation, distribution, rotation, and revocation - no manual cert management",
            "deps": ["vms-security-pki"]
          },
          {
            "id": "multi-tenancy",
            "name": "Multi-tenant Isolation",
            "abstract": "Multiple VANs share a backbone network with hierarchical CA-based isolation - efficient infrastructure use",
            "deps": ["vms-network-topology", "vms-security-pki"]
          },
          {
            "id": "instant-eviction",
            "name": "Instant Eviction",
            "abstract": "Remove entire VANs or individual members in one operation via certificate revocation - no per-site cleanup",
            "deps": ["vms-security-pki", "vms-application-lifecycle"]
          }
        ]
      },
      {
        "id": "personas",
        "title": "User Personas",
        "items": [
          {
            "id": "service-admin",
            "name": "Service Administrator",
            "abstract": "Creates and manages all backbones and application networks - enterprise-level infrastructure control"
          },
          {
            "id": "backbone-admin",
            "name": "Backbone Administrator",
            "abstract": "Manages assigned backbone and its application networks - delegated infrastructure control"
          },
          {
            "id": "van-user",
            "name": "VAN User",
            "abstract": "Creates VANs, invites participants, and manages application topology on permitted backbones"
          },
          {
            "id": "participant",
            "name": "Participant",
            "abstract": "Accepts invitations and manages local access points - no central authentication required, invitation claim is the only credential"
          }
        ]
      }
    ]
  },
  {
    "id": "vms-network-topology",
    "title": "VMS Network Topology Management",
    "abstract": "Backbone networks provide multi-tenant relay infrastructure. VMS users define backbones, sites, and links centrally - the spatial layout is managed as code rather than distributed across sites.",
    "categories": [
      {
        "id": "topology-outcomes",
        "title": "Topology Outcomes",
        "items": [
          {
            "id": "shared-relay-infrastructure",
            "name": "Shared Relay Infrastructure",
            "abstract": "One backbone serves multiple VANs - multi-tenant backbone reduces infrastructure overhead",
            "deps": ["backbone-network", "multi-tenant-routing"]
          },
          {
            "id": "optimized-backbone-paths",
            "name": "Optimized Backbone Paths",
            "abstract": "Cost-weighted routing through strategically-placed backbone sites - performance and availability optimization",
            "deps": ["backbone-links", "cost-weighted-routing"]
          },
          {
            "id": "centralized-topology-visibility",
            "name": "Centralized Topology Visibility",
            "abstract": "Single view of all backbones, sites, links, and their states - eliminates distributed topology tracking",
            "deps": ["topology-state-store"]
          },
          {
            "id": "dmz-relay-support",
            "name": "DMZ Relay Support",
            "abstract": "Backbone sites can bridge restricted networks - enables cross-boundary VANs without direct connectivity",
            "deps": ["backbone-site"]
          }
        ]
      },
      {
        "id": "topology-workflows",
        "title": "Topology Workflows",
        "items": [
          {
            "id": "backbone-provisioning",
            "name": "Backbone Provisioning",
            "abstract": "Define backbone, add sites at strategic locations, create cost-weighted links - centralized infrastructure setup",
            "deps": ["backbone-network", "backbone-site", "backbone-links"]
          },
          {
            "id": "site-bootstrapping",
            "name": "Site Bootstrapping",
            "abstract": "Three-step process: deploy bootstrap YAML, upload actual ingress data, apply final access point config - automated coordination",
            "deps": ["bootstrap-yaml", "ingress-discovery"]
          },
          {
            "id": "access-point-management",
            "name": "Access Point Management",
            "abstract": "Define manage and van access points - control how VANs and management traffic enter the backbone",
            "deps": ["access-point"]
          }
        ]
      },
      {
        "id": "topology-capabilities",
        "title": "Topology Capabilities",
        "items": [
          {
            "id": "backbone-network",
            "name": "Backbone Network",
            "abstract": "Multi-tenant constellation of relay points - carries traffic for multiple VANs with isolation",
            "deps": ["skupper-router"]
          },
          {
            "id": "backbone-site",
            "name": "Backbone Site",
            "abstract": "Relay point on the backbone - typically deployed to strategic network locations or DMZs",
            "deps": ["site-controller"]
          },
          {
            "id": "backbone-links",
            "name": "Backbone Links",
            "abstract": "Cost-weighted connections between backbone sites - defines relay topology",
            "deps": ["backbone-site"]
          },
          {
            "id": "access-point",
            "name": "Access Point",
            "abstract": "Ingress points on backbone sites - separate access points for management traffic and VAN traffic",
            "deps": ["backbone-site"]
          },
          {
            "id": "cost-weighted-routing",
            "name": "Cost-weighted Routing",
            "abstract": "Router selects optimal paths through backbone based on link costs - automatic route calculation",
            "deps": ["backbone-links", "skupper-router"]
          },
          {
            "id": "multi-tenant-routing",
            "name": "Multi-tenant Routing",
            "abstract": "Backbone routers carry traffic for multiple VANs simultaneously - isolation via certificate-based addressing",
            "deps": ["skupper-router"]
          }
        ]
      },
      {
        "id": "topology-automation",
        "title": "VMS Topology Automation",
        "items": [
          {
            "id": "centralized-topology-control",
            "name": "Centralized Topology Control",
            "abstract": "Management controller orchestrates backbone topology - site controllers handle local deployment",
            "deps": ["management-controller", "site-controller"]
          },
          {
            "id": "automatic-site-registration",
            "name": "Automatic Site Registration",
            "abstract": "Sites register with management plane via in-band communication - no out-of-band coordination required"
          },
          {
            "id": "ingress-discovery",
            "name": "Ingress Discovery",
            "abstract": "Bootstrap process captures actual ingress addresses from deployed site - adapts to cluster networking"
          },
          {
            "id": "topology-state-store",
            "name": "Topology State Store",
            "abstract": "PostgreSQL stores backbone and site state - management controller provides central visibility"
          },
          {
            "id": "bootstrap-yaml",
            "name": "Bootstrap YAML Generation",
            "abstract": "Management controller generates deployment artifacts for backbone sites - declarative site deployment"
          }
        ]
      },
      {
        "id": "manual-topology-tasks",
        "title": "Manual Skupper Topology Tasks (VMS Eliminates)",
        "items": [
          {
            "id": "manual-topology-planning",
            "name": "Manual Topology Planning",
            "abstract": "Decide which sites connect to which and plan optimal paths - requires understanding of network topology",
            "color": "#FFFFFF"
          },
          {
            "id": "distribute-router-configs",
            "name": "Distribute Router Configs",
            "abstract": "Deploy router configuration to each site independently - manual orchestration across sites",
            "color": "#FFFFFF"
          },
          {
            "id": "coordinate-inter-router-links",
            "name": "Coordinate Inter-router Links",
            "abstract": "Manually create bidirectional links between routers - requires coordination across site owners",
            "color": "#FFFFFF"
          },
          {
            "id": "track-topology-state",
            "name": "Track Topology State",
            "abstract": "Monitor which sites are connected and reachable - no central visibility without VMS",
            "color": "#FFFFFF"
          }
        ]
      }
    ]
  },
  {
    "id": "vms-application-lifecycle",
    "title": "VMS Application Network Lifecycle",
    "abstract": "VANs are created on backbones with invitation-based participation. VMS automates site bootstrapping, member registration, and eviction - the workflow mirrors video conferencing rather than distributed system administration.",
    "categories": [
      {
        "id": "van-outcomes",
        "title": "VAN Outcomes",
        "items": [
          {
            "id": "self-service-vans",
            "name": "Self-service VANs",
            "abstract": "Users create VANs on permitted backbones without admin intervention - delegated infrastructure",
            "deps": ["van-creation"]
          },
          {
            "id": "frictionless-participation",
            "name": "Frictionless Participation",
            "abstract": "Participants apply invitation YAML and gain VAN access - no manual site setup or token exchange",
            "deps": ["invitation-flow", "claim-redemption"]
          },
          {
            "id": "time-boxed-access",
            "name": "Time-boxed Access",
            "abstract": "VANs and invitations have optional start/end times with automatic expiration - temporal access control",
            "deps": ["van-lifecycle", "invitation-deadline"]
          },
          {
            "id": "instant-teardown",
            "name": "Instant Teardown",
            "abstract": "Remove entire VANs or individual members in one operation - no per-site cleanup coordination",
            "deps": ["van-eviction", "member-eviction"]
          },
          {
            "id": "central-member-visibility",
            "name": "Central Member Visibility",
            "abstract": "View all VAN members with join times and heartbeats from one console - eliminates distributed member tracking",
            "deps": ["member-monitoring"]
          }
        ]
      },
      {
        "id": "van-workflows",
        "title": "VAN Workflows",
        "items": [
          {
            "id": "van-creation",
            "name": "VAN Creation",
            "abstract": "Define application network on a backbone with optional time bounds - VAN CA created immediately for invitation signing",
            "deps": ["van-ca-creation"]
          },
          {
            "id": "invitation-flow",
            "name": "Invitation Flow",
            "abstract": "Create invitation with access controls, generate YAML, distribute via any channel - video-conference meeting workflow",
            "deps": ["invitation-creation", "invitation-yaml-generation"]
          },
          {
            "id": "participant-onboarding",
            "name": "Participant Onboarding",
            "abstract": "Participant applies invitation YAML, site controller boots, claims are redeemed, member certificate issued - zero-touch onboarding",
            "deps": ["claim-redemption", "member-cert-issuance"]
          },
          {
            "id": "access-point-deployment",
            "name": "Access Point Deployment",
            "abstract": "Management controller pushes access point definitions to member sites - participant approves or auto-deploys local configuration",
            "deps": ["access-point-push"]
          },
          {
            "id": "van-eviction",
            "name": "VAN Eviction",
            "abstract": "Invalidate VAN CA in one operation - removes all members and invitations simultaneously",
            "deps": ["ca-revocation"]
          },
          {
            "id": "member-eviction",
            "name": "Member Eviction",
            "abstract": "Revoke individual member certificate - instant removal without per-site coordination",
            "deps": ["cert-revocation"]
          }
        ]
      },
      {
        "id": "van-capabilities",
        "title": "VAN Capabilities",
        "items": [
          {
            "id": "invitation-claim-cert",
            "name": "Invitation Claim Certificate",
            "abstract": "Certificate embedded in invitation YAML - grants restricted access for claim redemption only",
            "deps": ["van-ca"]
          },
          {
            "id": "claim-redemption",
            "name": "Claim Redemption Protocol",
            "abstract": "Site controller contacts management controller via backbone using claim cert - validated claim exchanged for member cert",
            "deps": ["invitation-claim-cert"]
          },
          {
            "id": "member-cert-issuance",
            "name": "Member Certificate Issuance",
            "abstract": "Management controller issues member certificate after claim validation - site reconfigures for full VAN access",
            "deps": ["claim-redemption"]
          },
          {
            "id": "invitation-creation",
            "name": "Invitation Creation",
            "abstract": "Define claim access, primary access, instance limits, deadline, and site class - invitation policy"
          },
          {
            "id": "invitation-yaml-generation",
            "name": "Invitation YAML Generation",
            "abstract": "Self-contained deployment artifact with certificate and metadata - distributed via any channel",
            "deps": ["invitation-claim-cert"]
          },
          {
            "id": "invitation-deadline",
            "name": "Invitation Deadline",
            "abstract": "Optional join deadline after which invitation cannot be redeemed - time-limited invitations"
          },
          {
            "id": "instance-limit",
            "name": "Instance Limit",
            "abstract": "Single-use or multi-instance invitations - controls how widely invitations can be shared"
          },
          {
            "id": "van-lifecycle",
            "name": "VAN Lifecycle",
            "abstract": "Optional start and end times - VAN CA not loaded into backbone until start time, automatic expiration at end time",
            "deps": ["van-ca"]
          },
          {
            "id": "member-monitoring",
            "name": "Member Monitoring",
            "abstract": "Site controllers report heartbeat to management controller - central visibility of member health",
            "deps": ["site-controller"]
          },
          {
            "id": "access-point-push",
            "name": "Access Point Push",
            "abstract": "Management controller sends access point definitions to member sites - reactive configuration deployment",
            "deps": ["management-controller"]
          }
        ]
      },
      {
        "id": "manual-van-tasks",
        "title": "Manual Skupper VAN Tasks (VMS Eliminates)",
        "items": [
          {
            "id": "per-site-skupper-setup",
            "name": "Per-site Skupper Setup",
            "abstract": "Initialize each participant cluster separately - distributed site administration",
            "color": "#FFFFFF"
          },
          {
            "id": "link-token-generation",
            "name": "Link Token Generation",
            "abstract": "Create link tokens from one site to share with others - manual token generation and tracking",
            "color": "#FFFFFF"
          },
          {
            "id": "out-of-band-token-distribution",
            "name": "Out-of-band Token Distribution",
            "abstract": "Send tokens to participants via email, chat, or docs - coordination overhead and security concerns",
            "color": "#FFFFFF"
          },
          {
            "id": "apply-link-tokens",
            "name": "Apply Link Tokens",
            "abstract": "Each participant applies token to establish link - manual per-site operation",
            "color": "#FFFFFF"
          },
          {
            "id": "track-van-membership",
            "name": "Track VAN Membership",
            "abstract": "Monitor which sites are connected to the VAN - no central visibility without VMS",
            "color": "#FFFFFF"
          },
          {
            "id": "per-site-teardown",
            "name": "Per-site Teardown",
            "abstract": "Remove Skupper resources from each site individually - distributed teardown coordination",
            "color": "#FFFFFF"
          }
        ]
      }
    ]
  },
  {
    "id": "vms-security-pki",
    "title": "VMS Security & PKI",
    "abstract": "Hierarchical certificate architecture with automatic generation, distribution, rotation, and revocation. VMS integrates cert-manager and customer PKI for zero-touch certificate lifecycle management.",
    "categories": [
      {
        "id": "security-outcomes",
        "title": "Security Outcomes",
        "items": [
          {
            "id": "zero-touch-cert-lifecycle",
            "name": "Zero-touch Certificate Lifecycle",
            "abstract": "Certificates generated, distributed, rotated, and revoked automatically - no manual cert management",
            "deps": ["auto-cert-generation", "auto-cert-distribution", "auto-cert-rotation"]
          },
          {
            "id": "hierarchical-isolation",
            "name": "Hierarchical Isolation",
            "abstract": "Each VAN has its own CA under backbone CA - cryptographic isolation between VANs on shared backbone",
            "deps": ["cert-hierarchy"]
          },
          {
            "id": "instant-access-revocation",
            "name": "Instant Access Revocation",
            "abstract": "Invalidate entire VAN or individual members in one operation - certificate-based access control",
            "deps": ["subtree-invalidation", "cert-revocation"]
          },
          {
            "id": "pki-integration",
            "name": "Customer PKI Integration",
            "abstract": "VMS integrates with existing enterprise PKI via external root CA - leverages customer's trust infrastructure",
            "deps": ["external-root-ca"]
          },
          {
            "id": "temporal-access-enforcement",
            "name": "Temporal Access Enforcement",
            "abstract": "Time-boxed VANs and invitations enforced via certificate validity periods - automatic expiration",
            "deps": ["cert-validity-periods"]
          }
        ]
      },
      {
        "id": "cert-hierarchy",
        "title": "Certificate Hierarchy",
        "items": [
          {
            "id": "external-root-ca",
            "name": "External Root CA",
            "abstract": "Customer-provided root CA establishes trust anchor - VMS signs all subordinate CAs from this root",
            "stage": 1
          },
          {
            "id": "backbone-ca",
            "name": "Backbone CA",
            "abstract": "Intermediate CA per backbone signs backbone sites and VAN CAs - backbone-level isolation",
            "stage": 2,
            "deps": ["external-root-ca"]
          },
          {
            "id": "backbone-site-cert",
            "name": "Backbone Site Certificate",
            "abstract": "Site certificate for backbone relay points enables mutual TLS between backbone sites",
            "stage": 3,
            "deps": ["backbone-ca"]
          },
          {
            "id": "van-ca",
            "name": "VAN CA",
            "abstract": "Intermediate CA per VAN signs invitation and member certificates - VAN-level isolation",
            "stage": 3,
            "deps": ["backbone-ca"]
          },
          {
            "id": "invitation-claim-cert",
            "name": "Invitation Claim Certificate",
            "abstract": "Certificate embedded in invitation YAML restricts access to claim redemption protocol only",
            "stage": 4,
            "deps": ["van-ca"]
          },
          {
            "id": "member-site-cert",
            "name": "Member Site Certificate",
            "abstract": "Full-access certificate issued after claim redemption grants unrestricted VAN access",
            "stage": 4,
            "deps": ["van-ca"]
          }
        ]
      },
      {
        "id": "cert-automation",
        "title": "Certificate Automation",
        "items": [
          {
            "id": "auto-cert-generation",
            "name": "Automatic Certificate Generation",
            "abstract": "Management controller creates CAs and certificates via cert-manager - no manual CSR/signing workflow",
            "deps": ["cert-manager-integration"]
          },
          {
            "id": "auto-cert-distribution",
            "name": "Automatic Certificate Distribution",
            "abstract": "Certificates delivered in-band via bootstrap process or claim redemption - no out-of-band secure channel required",
            "deps": ["in-band-delivery"]
          },
          {
            "id": "auto-cert-rotation",
            "name": "Automatic Certificate Rotation",
            "abstract": "Management controller monitors expiration and rotates certificates seamlessly - zero downtime rotation",
            "deps": ["rotation-monitoring"]
          },
          {
            "id": "cert-revocation",
            "name": "Certificate Revocation",
            "abstract": "Eviction invalidates member or site certificates immediately - instant access removal",
            "deps": ["revocation-enforcement"]
          },
          {
            "id": "subtree-invalidation",
            "name": "Subtree Invalidation",
            "abstract": "Revoking VAN CA invalidates all member and invitation certificates - one operation removes entire VAN",
            "deps": ["cert-hierarchy"]
          },
          {
            "id": "cert-validity-periods",
            "name": "Certificate Validity Periods",
            "abstract": "VAN start/end times and invitation deadlines encoded in certificate validity - temporal access control",
            "deps": ["van-ca"]
          }
        ]
      },
      {
        "id": "pki-components",
        "title": "PKI Components",
        "items": [
          {
            "id": "cert-manager-integration",
            "name": "cert-manager",
            "abstract": "Kubernetes certificate controller orchestrates CA and certificate lifecycle - VMS management plane component"
          },
          {
            "id": "in-band-delivery",
            "name": "In-band Certificate Delivery",
            "abstract": "Certificates delivered via data plane communication - leverages backbone network for secure distribution"
          },
          {
            "id": "rotation-monitoring",
            "name": "Rotation Monitoring",
            "abstract": "Management controller tracks certificate expiration dates - proactive rotation before expiry"
          },
          {
            "id": "revocation-enforcement",
            "name": "Revocation Enforcement",
            "abstract": "Revoked certificates immediately rejected by routers - no waiting for CRL propagation"
          }
        ]
      },
      {
        "id": "security-principles",
        "title": "Security Principles",
        "items": [
          {
            "id": "distributed-trust",
            "name": "Distributed Domain of Trust",
            "abstract": "Application components don't authenticate to each other - trust established at VAN boundary via certificates"
          },
          {
            "id": "network-isolation",
            "name": "Isolated Application Networks",
            "abstract": "No ingress or attack surface unless expressly created - secure by default with explicit access points"
          },
          {
            "id": "no-participant-auth",
            "name": "No Participant Authentication",
            "abstract": "Invitation claim certificate is the only credential - no central user database for participants"
          },
          {
            "id": "tls-everywhere",
            "name": "Mutual TLS Everywhere",
            "abstract": "All inter-router and control plane communication uses mutual TLS - no unencrypted traffic"
          }
        ]
      },
      {
        "id": "manual-cert-tasks",
        "title": "Manual Certificate Tasks (VMS Eliminates)",
        "items": [
          {
            "id": "manual-ca-setup",
            "name": "Set Up Certificate Authority",
            "abstract": "Manually configure CA infrastructure and install CA software - complex PKI setup",
            "color": "#FFFFFF"
          },
          {
            "id": "generate-certs-manually",
            "name": "Generate Site Certificates",
            "abstract": "Create CSRs, submit to CA, receive signed certificates for each site - per-site manual process",
            "color": "#FFFFFF"
          },
          {
            "id": "distribute-certs-manually",
            "name": "Distribute Certificates Securely",
            "abstract": "Deliver certificates to each site via out-of-band secure channel - operational overhead",
            "color": "#FFFFFF"
          },
          {
            "id": "monitor-cert-expiration",
            "name": "Monitor Certificate Expiration",
            "abstract": "Track certificate expiration dates and create alerting - manual monitoring and tracking",
            "color": "#FFFFFF"
          },
          {
            "id": "rotate-certs-manually",
            "name": "Rotate Expiring Certificates",
            "abstract": "Generate new certificates before expiration and coordinate deployment across all sites - complex coordination",
            "color": "#FFFFFF"
          },
          {
            "id": "revoke-and-redistribute",
            "name": "Revoke and Redistribute",
            "abstract": "Manually revoke compromised certificates, update CRLs, and redistribute to all sites - slow incident response",
            "color": "#FFFFFF"
          }
        ]
      }
    ]
  },
  {
    "id": "vms-architecture",
    "title": "VMS Control & Data Plane Architecture",
    "abstract": "Management plane components orchestrate backbone and VAN topology centrally. Site controllers run at each backbone and member site. Data plane uses Skupper router network for application-layer message routing.",
    "categories": [
      {
        "id": "architecture-outcomes",
        "title": "Architecture Outcomes",
        "items": [
          {
            "id": "logically-centralized-control",
            "name": "Logically Centralized Control",
            "abstract": "Single management plane for all backbones and VANs - can be physically distributed for HA",
            "deps": ["management-controller", "postgresql"]
          },
          {
            "id": "in-band-management",
            "name": "In-band Management",
            "abstract": "Site controllers communicate with management controller via data plane - no separate management network required",
            "deps": ["site-controller", "data-plane-communication"]
          },
          {
            "id": "platform-flexibility",
            "name": "Platform Flexibility",
            "abstract": "Management plane on Kubernetes, backbone and member sites on any platform - not limited to Kubernetes",
            "deps": ["site-controller", "skupper-router"]
          },
          {
            "id": "decoupled-data-plane",
            "name": "Decoupled Data Plane",
            "abstract": "Narrow coupling to Skupper router allows future data plane options - architecture flexibility",
            "deps": ["skupper-router"]
          }
        ]
      },
      {
        "id": "management-plane",
        "title": "Management Plane (Centralized)",
        "items": [
          {
            "id": "management-controller",
            "name": "Management Controller",
            "abstract": "Orchestrates backbones, VANs, invitations, sites, and certificates - provides REST API for console and tooling",
            "stage": 1
          },
          {
            "id": "postgresql",
            "name": "PostgreSQL Database",
            "abstract": "Central persistent store for topology, state, and configuration - relational database for audit and history",
            "stage": 1,
            "deps": ["management-controller"]
          },
          {
            "id": "cert-manager",
            "name": "cert-manager",
            "abstract": "Kubernetes certificate controller manages CA hierarchy and certificate lifecycle - VMS management plane component",
            "stage": 1,
            "deps": ["management-controller"]
          },
          {
            "id": "keycloak",
            "name": "Keycloak",
            "abstract": "Identity and access management authenticates service admins and VAN users - no participant authentication",
            "stage": 1,
            "deps": ["management-controller"]
          },
          {
            "id": "vms-console",
            "name": "VMS Console",
            "abstract": "Web UI for managing backbones, VANs, invitations, and members - administrative interface",
            "deps": ["management-controller"]
          },
          {
            "id": "vms-api",
            "name": "VMS REST API",
            "abstract": "Management controller REST API consumed by console, CLI, and external tools - programmable interface",
            "deps": ["management-controller"]
          }
        ]
      },
      {
        "id": "site-controller",
        "title": "Site Controller (Distributed)",
        "items": [
          {
            "id": "site-controller",
            "name": "Site Controller",
            "abstract": "Runs at backbone and member sites communicating with management controller in-band via data plane",
            "stage": 2
          },
          {
            "id": "site-orchestration",
            "name": "Site Orchestration",
            "abstract": "Site controller deploys data plane, registers with management plane, and applies configuration - local automation",
            "deps": ["site-controller"]
          },
          {
            "id": "site-heartbeat",
            "name": "Site Heartbeat",
            "abstract": "Site controller reports status to management controller - central visibility of site health",
            "deps": ["site-controller"]
          },
          {
            "id": "local-access-point-deployment",
            "name": "Local Access Point Deployment",
            "abstract": "Site controller receives access point config from management controller - participant approves or auto-deploys",
            "deps": ["site-controller"]
          },
          {
            "id": "claim-redemption-handler",
            "name": "Claim Redemption Handler",
            "abstract": "Site controller contacts management controller to redeem invitation claim - exchanges claim cert for member cert",
            "deps": ["site-controller"]
          },
          {
            "id": "site-local-api",
            "name": "Site Local API",
            "abstract": "Site controller provides local API for participants to view and manage access points - participant interface",
            "deps": ["site-controller"]
          }
        ]
      },
      {
        "id": "data-plane",
        "title": "Data Plane (Skupper Routers)",
        "items": [
          {
            "id": "skupper-router",
            "name": "Skupper Router Network",
            "abstract": "Application-layer message routing provides abstract, flexible data plane independent of IP topology",
            "stage": 3
          },
          {
            "id": "inter-router-links",
            "name": "Inter-router Links",
            "abstract": "Mutual TLS connections between routers with cost-weighted paths through backbone",
            "deps": ["skupper-router"]
          },
          {
            "id": "data-plane-communication",
            "name": "Data Plane Communication",
            "abstract": "Site controllers use data plane to reach management controller - in-band management traffic",
            "deps": ["skupper-router"]
          },
          {
            "id": "multi-tenant-data-plane",
            "name": "Multi-tenant Data Plane",
            "abstract": "Backbone routers carry traffic for multiple VANs simultaneously - certificate-based addressing provides isolation",
            "deps": ["skupper-router"]
          },
          {
            "id": "service-connectors",
            "name": "Service Connectors",
            "abstract": "Access points that connect to local services - expose services to the VAN",
            "deps": ["skupper-router"]
          },
          {
            "id": "service-listeners",
            "name": "Service Listeners",
            "abstract": "Access points that listen for service traffic - consume services from the VAN",
            "deps": ["skupper-router"]
          }
        ]
      },
      {
        "id": "communication-patterns",
        "title": "Communication Patterns",
        "items": [
          {
            "id": "out-of-band-bootstrap",
            "name": "Out-of-band Bootstrap",
            "abstract": "Initial site and invitation YAMLs delivered via any channel - email, docs, repository, chat",
            "deps": ["bootstrap-yaml", "invitation-yaml"]
          },
          {
            "id": "in-band-registration",
            "name": "In-band Registration",
            "abstract": "Sites register with management plane via data plane after bootstrap - no out-of-band coordination",
            "deps": ["data-plane-communication"]
          },
          {
            "id": "config-push",
            "name": "Configuration Push",
            "abstract": "Management controller pushes access point and topology changes to site controllers - reactive deployment",
            "deps": ["management-controller", "site-controller"]
          },
          {
            "id": "ingress-upload",
            "name": "Ingress Upload",
            "abstract": "Backbone sites report actual ingress addresses to management controller - adapts to cluster networking",
            "deps": ["site-controller"]
          }
        ]
      },
      {
        "id": "deployment-artifacts",
        "title": "Deployment Artifacts",
        "items": [
          {
            "id": "helmfile-deployment",
            "name": "Helmfile Deployment",
            "abstract": "Management plane deployed via Helmfile with PostgreSQL, cert-manager, and management-controller chart"
          },
          {
            "id": "bootstrap-yaml",
            "name": "Backbone Bootstrap YAML",
            "abstract": "Three-step bootstrap: initial deployment, ingress upload, final config - generated by management controller"
          },
          {
            "id": "invitation-yaml",
            "name": "Invitation YAML",
            "abstract": "Self-contained deployment for VAN participants with certificate, metadata, and site controller config"
          }
        ]
      },
      {
        "id": "platform-support",
        "title": "Platform Support",
        "items": [
          {
            "id": "kubernetes-management",
            "name": "Kubernetes Management Plane",
            "abstract": "Management controller, database, and cert-manager run on Kubernetes - OpenShift routes required for management controller API"
          },
          {
            "id": "multi-platform-sites",
            "name": "Multi-platform Sites",
            "abstract": "Backbone and member sites can run on Kubernetes or other platforms - not limited to Kubernetes",
            "deps": ["site-controller"]
          },
          {
            "id": "dmz-deployment",
            "name": "DMZ Deployment",
            "abstract": "Backbone routers can be deployed in DMZ to bridge restricted networks - supports cross-boundary VANs"
          }
        ]
      }
    ]
  }
]
```
