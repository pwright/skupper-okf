---
title: "Skupper Docs Landscape"
type: BlockscapeMap
status: generated
source_path: maps/skupper-docs-landscape.bs
tags:
  - skupper
  - blockscape
---

# Skupper Docs Landscape

Edit: [Blockscape](https://pwright.github.io/blockscape/?load=https://raw.githubusercontent.com/pwright/skupper-okf/refs/heads/main/maps/skupper-docs-landscape.bs)

```bs full
[
  {
    "id": "skupper-docs-series",
    "title": "Skupper Documentation Landscape",
    "abstract": "An overview of the Skupper documentation journey, from understanding application networks and evaluating new capabilities through planning, installation, extension, operations, development, integration, platform guidance, and reference resources. Each item corresponds to a dedicated map whose model id matches the item id.",
    "status": "generated",
    "reviewed": false,
    "source_paths": [
      "generated/skupper-docs-landscape/skupper-docs-series.md"
    ],
    "categories": [
      {
        "id": "orient",
        "title": "Orient",
        "items": [
          {
            "id": "skupper-whats-new",
            "name": "What's New",
            "deps": [
              "discover-skupper",
              "skupper-reference"
            ],
            "source": "generated/skupper-docs-landscape/skupper-whats-new.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/skupper-whats-new"
          },
          {
            "id": "discover-skupper",
            "name": "Discover Skupper",
            "deps": [
              "plan-skupper"
            ],
            "source": "generated/skupper-docs-landscape/discover-skupper.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/discover-skupper"
          },
          {
            "id": "skupper-previews",
            "name": "Technology Previews",
            "deps": [
              "discover-skupper",
              "skupper-reference"
            ],
            "source": "generated/skupper-docs-landscape/skupper-previews.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/skupper-previews"
          },
          {
            "id": "get-started",
            "name": "Get Started",
            "deps": [
              "install-skupper",
              "configure-skupper"
            ],
            "source": "generated/skupper-docs-landscape/get-started.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/get-started"
          }
        ]
      },
      {
        "id": "adopt",
        "title": "Adopt",
        "items": [
          {
            "id": "plan-skupper",
            "name": "Plan",
            "deps": [
              "discover-skupper",
              "secure-skupper"
            ],
            "source": "generated/skupper-docs-landscape/plan-skupper.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/plan-skupper"
          },
          {
            "id": "install-skupper",
            "name": "Install",
            "deps": [
              "plan-skupper",
              "platform-guides"
            ],
            "source": "generated/skupper-docs-landscape/install-skupper.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/install-skupper"
          },
          {
            "id": "extend-skupper",
            "name": "Extend",
            "deps": [
              "configure-skupper",
              "secure-skupper"
            ],
            "source": "generated/skupper-docs-landscape/extend-skupper.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/extend-skupper"
          },
          {
            "id": "upgrade-skupper",
            "name": "Upgrade",
            "deps": [
              "administer-skupper",
              "skupper-reference"
            ],
            "source": "generated/skupper-docs-landscape/upgrade-skupper.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/upgrade-skupper"
          },
          {
            "id": "migrate-skupper",
            "name": "Migrate",
            "deps": [
              "plan-skupper",
              "upgrade-skupper"
            ],
            "source": "generated/skupper-docs-landscape/migrate-skupper.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/migrate-skupper"
          }
        ]
      },
      {
        "id": "operate",
        "title": "Operate",
        "items": [
          {
            "id": "administer-skupper",
            "name": "Administer",
            "deps": [
              "configure-skupper",
              "observe-skupper"
            ],
            "source": "generated/skupper-docs-landscape/administer-skupper.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/administer-skupper"
          },
          {
            "id": "configure-skupper",
            "name": "Configure",
            "deps": [
              "install-skupper",
              "skupper-reference"
            ],
            "source": "generated/skupper-docs-landscape/configure-skupper.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/configure-skupper"
          },
          {
            "id": "secure-skupper",
            "name": "Secure",
            "deps": [
              "configure-skupper",
              "skupper-reference"
            ],
            "source": "generated/skupper-docs-landscape/secure-skupper.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/secure-skupper"
          },
          {
            "id": "observe-skupper",
            "name": "Observe",
            "deps": [
              "administer-skupper",
              "skupper-reference"
            ],
            "source": "generated/skupper-docs-landscape/observe-skupper.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/observe-skupper"
          },
          {
            "id": "optimize-skupper",
            "name": "Optimize",
            "deps": [
              "observe-skupper",
              "administer-skupper"
            ],
            "source": "generated/skupper-docs-landscape/optimize-skupper.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/optimize-skupper"
          },
          {
            "id": "troubleshoot-skupper",
            "name": "Troubleshoot",
            "deps": [
              "observe-skupper",
              "skupper-reference"
            ],
            "source": "generated/skupper-docs-landscape/troubleshoot-skupper.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/troubleshoot-skupper"
          }
        ]
      },
      {
        "id": "build",
        "title": "Build and Integrate",
        "items": [
          {
            "id": "develop-skupper",
            "name": "Develop",
            "deps": [
              "skupper-reference",
              "configure-skupper"
            ],
            "source": "generated/skupper-docs-landscape/develop-skupper.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/develop-skupper"
          },
          {
            "id": "integrate-skupper",
            "name": "Integrate",
            "deps": [
              "develop-skupper",
              "secure-skupper"
            ],
            "source": "generated/skupper-docs-landscape/integrate-skupper.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/integrate-skupper"
          },
          {
            "id": "platform-guides",
            "name": "Platforms and Managed Environments",
            "deps": [
              "install-skupper",
              "integrate-skupper"
            ],
            "source": "generated/skupper-docs-landscape/platform-guides.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/platform-guides"
          }
        ]
      },
      {
        "id": "resources",
        "title": "Resources",
        "items": [
          {
            "id": "skupper-reference",
            "name": "Reference",
            "deps": [],
            "source": "generated/skupper-docs-landscape/skupper-reference.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/skupper-reference"
          },
          {
            "id": "skupper-pdf-library",
            "name": "Downloadable Guides",
            "deps": [
              "skupper-reference"
            ],
            "source": "generated/skupper-docs-landscape/skupper-pdf-library.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/skupper-pdf-library"
          }
        ]
      }
    ],
    "source_base_url": "https://pwright.github.io/skupper-okf/"
  },
  {
    "id": "skupper-whats-new",
    "title": "What's New in Skupper",
    "abstract": "Track user-visible improvements, compatibility changes, preview capabilities, and operational impacts so teams can decide what to adopt and how to prepare.",
    "status": "generated",
    "reviewed": false,
    "source_paths": [
      "generated/skupper-docs-landscape/skupper-whats-new.md"
    ],
    "categories": [
      {
        "id": "highlights",
        "title": "Release Highlights",
        "items": [
          {
            "id": "new-capabilities",
            "name": "New Capabilities",
            "source": "generated/skupper-docs-landscape/new-capabilities.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/new-capabilities",
            "deps": [
              "release-notes",
              "compatibility-matrix"
            ]
          },
          {
            "id": "behavior-changes",
            "name": "Behavior Changes",
            "source": "generated/skupper-docs-landscape/behavior-changes.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/behavior-changes",
            "deps": [
              "release-notes",
              "upgrade-notes"
            ]
          }
        ]
      },
      {
        "id": "adoption",
        "title": "Adoption Impact",
        "items": [
          {
            "id": "upgrade-decisions",
            "name": "Upgrade Decisions",
            "source": "generated/skupper-docs-landscape/upgrade-decisions.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/upgrade-decisions",
            "deps": [
              "behavior-changes",
              "deprecations"
            ]
          },
          {
            "id": "preview-evaluation",
            "name": "Preview Evaluation",
            "source": "generated/skupper-docs-landscape/preview-evaluation.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/preview-evaluation",
            "deps": [
              "preview-status",
              "known-limitations"
            ]
          }
        ]
      },
      {
        "id": "sources",
        "title": "Authoritative Sources",
        "items": [
          {
            "id": "release-notes",
            "name": "Release Notes",
            "source": "generated/skupper-docs-landscape/release-notes.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/release-notes",
            "deps": []
          },
          {
            "id": "upgrade-notes",
            "name": "Upgrade Notes",
            "source": "generated/skupper-docs-landscape/upgrade-notes.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/upgrade-notes",
            "deps": [
              "release-notes"
            ]
          },
          {
            "id": "deprecations",
            "name": "Deprecations",
            "source": "generated/skupper-docs-landscape/deprecations.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/deprecations",
            "deps": [
              "release-notes"
            ]
          },
          {
            "id": "preview-status",
            "name": "Preview Status",
            "source": "generated/skupper-docs-landscape/preview-status.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/preview-status",
            "deps": [
              "release-notes"
            ]
          },
          {
            "id": "known-limitations",
            "name": "Known Limitations",
            "source": "generated/skupper-docs-landscape/known-limitations.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/known-limitations",
            "deps": [
              "release-notes"
            ]
          },
          {
            "id": "compatibility-matrix",
            "name": "Compatibility Matrix",
            "source": "generated/skupper-docs-landscape/compatibility-matrix.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/compatibility-matrix",
            "deps": []
          }
        ]
      }
    ],
    "source_base_url": "https://pwright.github.io/skupper-okf/"
  },
  {
    "id": "discover-skupper",
    "title": "Discover Skupper",
    "abstract": "Explain how Skupper creates secure application networks across Kubernetes clusters, virtual machines, and cloud boundaries, and how that capability improves application connectivity without exposing services publicly.",
    "status": "generated",
    "reviewed": false,
    "source_paths": [
      "generated/skupper-docs-landscape/discover-skupper.md"
    ],
    "categories": [
      {
        "id": "value",
        "title": "User Value",
        "items": [
          {
            "id": "multi-site-connectivity",
            "name": "Connect Applications Across Sites",
            "source": "generated/skupper-docs-landscape/multi-site-connectivity.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/multi-site-connectivity",
            "deps": [
              "application-network",
              "service-exposure"
            ]
          },
          {
            "id": "private-connectivity",
            "name": "Keep Services Private",
            "source": "generated/skupper-docs-landscape/private-connectivity.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/private-connectivity",
            "deps": [
              "secure-links",
              "identity-model"
            ]
          }
        ]
      },
      {
        "id": "concepts",
        "title": "Core Concepts",
        "items": [
          {
            "id": "application-network",
            "name": "Application Network",
            "source": "generated/skupper-docs-landscape/application-network.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/application-network",
            "deps": [
              "sites",
              "links"
            ]
          },
          {
            "id": "service-exposure",
            "name": "Service Exposure",
            "source": "generated/skupper-docs-landscape/service-exposure.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/service-exposure",
            "deps": [
              "sites",
              "routing"
            ]
          },
          {
            "id": "secure-links",
            "name": "Secure Links",
            "source": "generated/skupper-docs-landscape/secure-links.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/secure-links",
            "deps": [
              "links",
              "identity-model"
            ]
          }
        ]
      },
      {
        "id": "foundations",
        "title": "Foundations",
        "items": [
          {
            "id": "sites",
            "name": "Sites",
            "source": "generated/skupper-docs-landscape/sites.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/sites",
            "deps": []
          },
          {
            "id": "links",
            "name": "Site Links",
            "source": "generated/skupper-docs-landscape/links.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/links",
            "deps": [
              "sites"
            ]
          },
          {
            "id": "routing",
            "name": "Service Routing",
            "source": "generated/skupper-docs-landscape/routing.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/routing",
            "deps": [
              "sites"
            ]
          },
          {
            "id": "identity-model",
            "name": "Certificates and Identity",
            "source": "generated/skupper-docs-landscape/identity-model.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/identity-model",
            "deps": []
          }
        ]
      }
    ],
    "source_base_url": "https://pwright.github.io/skupper-okf/"
  },
  {
    "id": "skupper-previews",
    "title": "Skupper Technology Previews",
    "abstract": "Help users assess experimental or early-access Skupper capabilities, understand their limits, and validate them safely before production use.",
    "status": "generated",
    "reviewed": false,
    "source_paths": [
      "generated/skupper-docs-landscape/skupper-previews.md"
    ],
    "categories": [
      {
        "id": "evaluate",
        "title": "Evaluate Preview Value",
        "items": [
          {
            "id": "preview-use-cases",
            "name": "Candidate Use Cases",
            "source": "generated/skupper-docs-landscape/preview-use-cases.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/preview-use-cases",
            "deps": [
              "preview-catalog",
              "support-boundaries"
            ]
          },
          {
            "id": "preview-fit",
            "name": "Preview Fit Assessment",
            "source": "generated/skupper-docs-landscape/preview-fit.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/preview-fit",
            "deps": [
              "preview-use-cases",
              "compatibility-checks"
            ]
          }
        ]
      },
      {
        "id": "validate",
        "title": "Validate Safely",
        "items": [
          {
            "id": "sandbox-trial",
            "name": "Sandbox Trial",
            "source": "generated/skupper-docs-landscape/sandbox-trial.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/sandbox-trial",
            "deps": [
              "preview-installation",
              "test-plan"
            ]
          },
          {
            "id": "feedback-loop",
            "name": "Feedback and Issue Reporting",
            "source": "generated/skupper-docs-landscape/feedback-loop.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/feedback-loop",
            "deps": [
              "sandbox-trial",
              "known-issues"
            ]
          }
        ]
      },
      {
        "id": "controls",
        "title": "Preview Controls",
        "items": [
          {
            "id": "preview-catalog",
            "name": "Preview Catalog",
            "source": "generated/skupper-docs-landscape/preview-catalog.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/preview-catalog",
            "deps": []
          },
          {
            "id": "support-boundaries",
            "name": "Support Boundaries",
            "source": "generated/skupper-docs-landscape/support-boundaries.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/support-boundaries",
            "deps": []
          },
          {
            "id": "compatibility-checks",
            "name": "Compatibility Checks",
            "source": "generated/skupper-docs-landscape/compatibility-checks.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/compatibility-checks",
            "deps": [
              "preview-catalog"
            ]
          },
          {
            "id": "preview-installation",
            "name": "Preview Installation",
            "source": "generated/skupper-docs-landscape/preview-installation.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/preview-installation",
            "deps": [
              "compatibility-checks"
            ]
          },
          {
            "id": "test-plan",
            "name": "Validation Test Plan",
            "source": "generated/skupper-docs-landscape/test-plan.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/test-plan",
            "deps": []
          },
          {
            "id": "known-issues",
            "name": "Known Issues",
            "source": "generated/skupper-docs-landscape/known-issues.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/known-issues",
            "deps": [
              "preview-catalog"
            ]
          }
        ]
      }
    ],
    "source_base_url": "https://pwright.github.io/skupper-okf/"
  },
  {
    "id": "get-started",
    "title": "Get Started with Skupper",
    "abstract": "Guide a new user from prerequisites to a working multi-site application network, including site creation, linking, service exposure, and validation.",
    "status": "generated",
    "reviewed": false,
    "source_paths": [
      "generated/skupper-docs-landscape/get-started.md"
    ],
    "categories": [
      {
        "id": "outcome",
        "title": "First Working Network",
        "items": [
          {
            "id": "first-connected-service",
            "name": "Connected Service Across Sites",
            "source": "generated/skupper-docs-landscape/first-connected-service.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/first-connected-service",
            "deps": [
              "first-sites",
              "first-link",
              "first-exposure"
            ]
          },
          {
            "id": "first-validation",
            "name": "Connectivity Validation",
            "source": "generated/skupper-docs-landscape/first-validation.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/first-validation",
            "deps": [
              "first-connected-service",
              "basic-observation"
            ]
          }
        ]
      },
      {
        "id": "workflow",
        "title": "Starter Workflow",
        "items": [
          {
            "id": "first-sites",
            "name": "Create Two Sites",
            "source": "generated/skupper-docs-landscape/first-sites.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/first-sites",
            "deps": [
              "starter-prerequisites",
              "cli-install"
            ]
          },
          {
            "id": "first-link",
            "name": "Link the Sites",
            "source": "generated/skupper-docs-landscape/first-link.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/first-link",
            "deps": [
              "first-sites",
              "link-credentials"
            ]
          },
          {
            "id": "first-exposure",
            "name": "Expose a Service",
            "source": "generated/skupper-docs-landscape/first-exposure.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/first-exposure",
            "deps": [
              "first-sites",
              "service-selection"
            ]
          },
          {
            "id": "basic-observation",
            "name": "Check Network Status",
            "source": "generated/skupper-docs-landscape/basic-observation.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/basic-observation",
            "deps": [
              "first-sites",
              "first-link"
            ]
          }
        ]
      },
      {
        "id": "setup",
        "title": "Starter Setup",
        "items": [
          {
            "id": "starter-prerequisites",
            "name": "Cluster or Host Prerequisites",
            "source": "generated/skupper-docs-landscape/starter-prerequisites.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/starter-prerequisites",
            "deps": []
          },
          {
            "id": "cli-install",
            "name": "Install the Skupper CLI",
            "source": "generated/skupper-docs-landscape/cli-install.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/cli-install",
            "deps": [
              "starter-prerequisites"
            ]
          },
          {
            "id": "link-credentials",
            "name": "Generate Link Credentials",
            "source": "generated/skupper-docs-landscape/link-credentials.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/link-credentials",
            "deps": []
          },
          {
            "id": "service-selection",
            "name": "Choose a Test Service",
            "source": "generated/skupper-docs-landscape/service-selection.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/service-selection",
            "deps": []
          }
        ]
      }
    ],
    "source_base_url": "https://pwright.github.io/skupper-okf/"
  },
  {
    "id": "plan-skupper",
    "title": "Plan a Skupper Deployment",
    "abstract": "Translate application connectivity goals into a site topology, security model, capacity plan, ownership model, and rollout sequence.",
    "status": "generated",
    "reviewed": false,
    "source_paths": [
      "generated/skupper-docs-landscape/plan-skupper.md"
    ],
    "categories": [
      {
        "id": "design",
        "title": "Deployment Design",
        "items": [
          {
            "id": "target-topology",
            "name": "Target Application Network Topology",
            "source": "generated/skupper-docs-landscape/target-topology.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/target-topology",
            "deps": [
              "site-inventory",
              "traffic-flows"
            ]
          },
          {
            "id": "rollout-plan",
            "name": "Rollout Plan",
            "source": "generated/skupper-docs-landscape/rollout-plan.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/rollout-plan",
            "deps": [
              "target-topology",
              "ownership-model",
              "risk-assessment"
            ]
          }
        ]
      },
      {
        "id": "requirements",
        "title": "Requirements and Constraints",
        "items": [
          {
            "id": "traffic-flows",
            "name": "Traffic Flow Requirements",
            "source": "generated/skupper-docs-landscape/traffic-flows.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/traffic-flows",
            "deps": [
              "application-inventory"
            ]
          },
          {
            "id": "security-requirements",
            "name": "Security Requirements",
            "source": "generated/skupper-docs-landscape/security-requirements.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/security-requirements",
            "deps": [
              "trust-boundaries",
              "identity-policy"
            ]
          },
          {
            "id": "capacity-plan",
            "name": "Capacity Plan",
            "source": "generated/skupper-docs-landscape/capacity-plan.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/capacity-plan",
            "deps": [
              "traffic-flows",
              "availability-targets"
            ]
          }
        ]
      },
      {
        "id": "inputs",
        "title": "Planning Inputs",
        "items": [
          {
            "id": "application-inventory",
            "name": "Application and Service Inventory",
            "source": "generated/skupper-docs-landscape/application-inventory.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/application-inventory",
            "deps": []
          },
          {
            "id": "site-inventory",
            "name": "Cluster and Host Inventory",
            "source": "generated/skupper-docs-landscape/site-inventory.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/site-inventory",
            "deps": []
          },
          {
            "id": "trust-boundaries",
            "name": "Trust Boundaries",
            "source": "generated/skupper-docs-landscape/trust-boundaries.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/trust-boundaries",
            "deps": []
          },
          {
            "id": "identity-policy",
            "name": "Identity and Certificate Policy",
            "source": "generated/skupper-docs-landscape/identity-policy.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/identity-policy",
            "deps": []
          },
          {
            "id": "availability-targets",
            "name": "Availability Targets",
            "source": "generated/skupper-docs-landscape/availability-targets.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/availability-targets",
            "deps": []
          },
          {
            "id": "ownership-model",
            "name": "Operational Ownership",
            "source": "generated/skupper-docs-landscape/ownership-model.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/ownership-model",
            "deps": []
          },
          {
            "id": "risk-assessment",
            "name": "Rollout Risk Assessment",
            "source": "generated/skupper-docs-landscape/risk-assessment.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/risk-assessment",
            "deps": []
          }
        ]
      }
    ],
    "source_base_url": "https://pwright.github.io/skupper-okf/"
  },
  {
    "id": "install-skupper",
    "title": "Install Skupper",
    "abstract": "Cover installation paths for supported environments, from prerequisites and tooling through site initialization and post-install validation.",
    "status": "generated",
    "reviewed": false,
    "source_paths": [
      "generated/skupper-docs-landscape/install-skupper.md"
    ],
    "categories": [
      {
        "id": "outcome",
        "title": "Installed Environment",
        "items": [
          {
            "id": "installed-site",
            "name": "Operational Skupper Site",
            "source": "generated/skupper-docs-landscape/installed-site.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/installed-site",
            "deps": [
              "installation-method",
              "site-initialization"
            ]
          },
          {
            "id": "validated-install",
            "name": "Validated Installation",
            "source": "generated/skupper-docs-landscape/validated-install.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/validated-install",
            "deps": [
              "installed-site",
              "health-checks"
            ]
          }
        ]
      },
      {
        "id": "methods",
        "title": "Installation Methods",
        "items": [
          {
            "id": "cli-installation",
            "name": "CLI Installation",
            "source": "generated/skupper-docs-landscape/cli-installation.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/cli-installation",
            "deps": [
              "platform-prerequisites",
              "cli-package"
            ]
          },
          {
            "id": "operator-installation",
            "name": "Operator Installation",
            "source": "generated/skupper-docs-landscape/operator-installation.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/operator-installation",
            "deps": [
              "platform-prerequisites",
              "operator-package"
            ]
          },
          {
            "id": "host-installation",
            "name": "Host Installation",
            "source": "generated/skupper-docs-landscape/host-installation.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/host-installation",
            "deps": [
              "host-prerequisites",
              "host-package"
            ]
          },
          {
            "id": "installation-method",
            "name": "Select Installation Method",
            "source": "generated/skupper-docs-landscape/installation-method.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/installation-method",
            "deps": [
              "cli-installation",
              "operator-installation",
              "host-installation"
            ]
          }
        ]
      },
      {
        "id": "foundation",
        "title": "Prerequisites and Validation",
        "items": [
          {
            "id": "platform-prerequisites",
            "name": "Kubernetes Platform Prerequisites",
            "source": "generated/skupper-docs-landscape/platform-prerequisites.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/platform-prerequisites",
            "deps": []
          },
          {
            "id": "host-prerequisites",
            "name": "Linux Host Prerequisites",
            "source": "generated/skupper-docs-landscape/host-prerequisites.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/host-prerequisites",
            "deps": []
          },
          {
            "id": "cli-package",
            "name": "CLI Package",
            "source": "generated/skupper-docs-landscape/cli-package.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/cli-package",
            "deps": [
              "platform-prerequisites"
            ]
          },
          {
            "id": "operator-package",
            "name": "Operator Package",
            "source": "generated/skupper-docs-landscape/operator-package.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/operator-package",
            "deps": [
              "platform-prerequisites"
            ]
          },
          {
            "id": "host-package",
            "name": "Host Package",
            "source": "generated/skupper-docs-landscape/host-package.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/host-package",
            "deps": [
              "host-prerequisites"
            ]
          },
          {
            "id": "site-initialization",
            "name": "Site Initialization",
            "source": "generated/skupper-docs-landscape/site-initialization.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/site-initialization",
            "deps": [
              "installation-method"
            ]
          },
          {
            "id": "health-checks",
            "name": "Post-install Health Checks",
            "source": "generated/skupper-docs-landscape/health-checks.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/health-checks",
            "deps": [
              "site-initialization"
            ]
          }
        ]
      }
    ],
    "source_base_url": "https://pwright.github.io/skupper-okf/"
  },
  {
    "id": "extend-skupper",
    "title": "Extend a Skupper Application Network",
    "abstract": "Add new sites, connect additional environments, and expose more services while preserving identity, routing, and operational consistency.",
    "status": "generated",
    "reviewed": false,
    "source_paths": [
      "generated/skupper-docs-landscape/extend-skupper.md"
    ],
    "categories": [
      {
        "id": "outcomes",
        "title": "Expansion Outcomes",
        "items": [
          {
            "id": "new-site-connected",
            "name": "New Site Connected",
            "source": "generated/skupper-docs-landscape/new-site-connected.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/new-site-connected",
            "deps": [
              "site-onboarding",
              "link-establishment"
            ]
          },
          {
            "id": "new-service-reachable",
            "name": "New Service Reachable",
            "source": "generated/skupper-docs-landscape/new-service-reachable.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/new-service-reachable",
            "deps": [
              "new-site-connected",
              "service-onboarding"
            ]
          }
        ]
      },
      {
        "id": "workflow",
        "title": "Expansion Workflow",
        "items": [
          {
            "id": "site-onboarding",
            "name": "Onboard a Site",
            "source": "generated/skupper-docs-landscape/site-onboarding.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/site-onboarding",
            "deps": [
              "site-template",
              "site-identity"
            ]
          },
          {
            "id": "link-establishment",
            "name": "Establish a Link",
            "source": "generated/skupper-docs-landscape/link-establishment.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/link-establishment",
            "deps": [
              "link-token",
              "network-policy"
            ]
          },
          {
            "id": "service-onboarding",
            "name": "Onboard a Service",
            "source": "generated/skupper-docs-landscape/service-onboarding.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/service-onboarding",
            "deps": [
              "service-definition",
              "routing-policy"
            ]
          }
        ]
      },
      {
        "id": "controls",
        "title": "Expansion Controls",
        "items": [
          {
            "id": "site-template",
            "name": "Site Configuration Template",
            "source": "generated/skupper-docs-landscape/site-template.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/site-template",
            "deps": []
          },
          {
            "id": "site-identity",
            "name": "Site Identity",
            "source": "generated/skupper-docs-landscape/site-identity.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/site-identity",
            "deps": []
          },
          {
            "id": "link-token",
            "name": "Link Credential or Token",
            "source": "generated/skupper-docs-landscape/link-token.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/link-token",
            "deps": [
              "site-identity"
            ]
          },
          {
            "id": "network-policy",
            "name": "Network Policy",
            "source": "generated/skupper-docs-landscape/network-policy.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/network-policy",
            "deps": []
          },
          {
            "id": "service-definition",
            "name": "Service Definition",
            "source": "generated/skupper-docs-landscape/service-definition.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/service-definition",
            "deps": []
          },
          {
            "id": "routing-policy",
            "name": "Routing Policy",
            "source": "generated/skupper-docs-landscape/routing-policy.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/routing-policy",
            "deps": [
              "service-definition"
            ]
          }
        ]
      }
    ],
    "source_base_url": "https://pwright.github.io/skupper-okf/"
  },
  {
    "id": "upgrade-skupper",
    "title": "Upgrade Skupper",
    "abstract": "Plan and execute Skupper upgrades with compatibility checks, staged rollout, state protection, validation, and rollback readiness.",
    "status": "generated",
    "reviewed": false,
    "source_paths": [
      "generated/skupper-docs-landscape/upgrade-skupper.md"
    ],
    "categories": [
      {
        "id": "outcome",
        "title": "Upgrade Outcome",
        "items": [
          {
            "id": "upgraded-network",
            "name": "Upgraded Application Network",
            "source": "generated/skupper-docs-landscape/upgraded-network.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/upgraded-network",
            "deps": [
              "upgrade-sequence",
              "component-upgrades"
            ]
          },
          {
            "id": "upgrade-validation",
            "name": "Upgrade Validation",
            "source": "generated/skupper-docs-landscape/upgrade-validation.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/upgrade-validation",
            "deps": [
              "upgraded-network",
              "post-upgrade-tests"
            ]
          }
        ]
      },
      {
        "id": "execution",
        "title": "Upgrade Execution",
        "items": [
          {
            "id": "upgrade-sequence",
            "name": "Site Upgrade Sequence",
            "source": "generated/skupper-docs-landscape/upgrade-sequence.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/upgrade-sequence",
            "deps": [
              "compatibility-review",
              "maintenance-plan"
            ]
          },
          {
            "id": "component-upgrades",
            "name": "CLI, Operator, and Router Upgrades",
            "source": "generated/skupper-docs-landscape/component-upgrades.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/component-upgrades",
            "deps": [
              "upgrade-sequence",
              "backup-state"
            ]
          },
          {
            "id": "rollback-plan",
            "name": "Rollback Plan",
            "source": "generated/skupper-docs-landscape/rollback-plan.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/rollback-plan",
            "deps": [
              "backup-state",
              "version-compatibility"
            ]
          }
        ]
      },
      {
        "id": "readiness",
        "title": "Upgrade Readiness",
        "items": [
          {
            "id": "compatibility-review",
            "name": "Compatibility Review",
            "source": "generated/skupper-docs-landscape/compatibility-review.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/compatibility-review",
            "deps": [
              "version-compatibility",
              "release-differences"
            ]
          },
          {
            "id": "maintenance-plan",
            "name": "Maintenance and Communication Plan",
            "source": "generated/skupper-docs-landscape/maintenance-plan.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/maintenance-plan",
            "deps": []
          },
          {
            "id": "backup-state",
            "name": "Configuration and State Backup",
            "source": "generated/skupper-docs-landscape/backup-state.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/backup-state",
            "deps": []
          },
          {
            "id": "post-upgrade-tests",
            "name": "Post-upgrade Test Suite",
            "source": "generated/skupper-docs-landscape/post-upgrade-tests.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/post-upgrade-tests",
            "deps": []
          },
          {
            "id": "version-compatibility",
            "name": "Version Compatibility",
            "source": "generated/skupper-docs-landscape/version-compatibility.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/version-compatibility",
            "deps": []
          },
          {
            "id": "release-differences",
            "name": "Release Differences",
            "source": "generated/skupper-docs-landscape/release-differences.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/release-differences",
            "deps": []
          }
        ]
      }
    ],
    "source_base_url": "https://pwright.github.io/skupper-okf/"
  },
  {
    "id": "migrate-skupper",
    "title": "Migrate to or Between Skupper Deployments",
    "abstract": "Move application-network connectivity between environments, deployment models, or major versions while preserving service reachability and minimizing disruption.",
    "status": "generated",
    "reviewed": false,
    "source_paths": [
      "generated/skupper-docs-landscape/migrate-skupper.md"
    ],
    "categories": [
      {
        "id": "outcome",
        "title": "Migration Outcome",
        "items": [
          {
            "id": "migrated-connectivity",
            "name": "Migrated Application Connectivity",
            "source": "generated/skupper-docs-landscape/migrated-connectivity.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/migrated-connectivity",
            "deps": [
              "migration-wave",
              "cutover"
            ]
          },
          {
            "id": "migration-acceptance",
            "name": "Migration Acceptance",
            "source": "generated/skupper-docs-landscape/migration-acceptance.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/migration-acceptance",
            "deps": [
              "migrated-connectivity",
              "acceptance-tests"
            ]
          }
        ]
      },
      {
        "id": "execution",
        "title": "Migration Execution",
        "items": [
          {
            "id": "migration-wave",
            "name": "Migration Waves",
            "source": "generated/skupper-docs-landscape/migration-wave.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/migration-wave",
            "deps": [
              "source-assessment",
              "target-design"
            ]
          },
          {
            "id": "parallel-run",
            "name": "Parallel Run",
            "source": "generated/skupper-docs-landscape/parallel-run.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/parallel-run",
            "deps": [
              "migration-wave",
              "dual-connectivity"
            ]
          },
          {
            "id": "cutover",
            "name": "Traffic Cutover",
            "source": "generated/skupper-docs-landscape/cutover.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/cutover",
            "deps": [
              "parallel-run",
              "rollback-path"
            ]
          }
        ]
      },
      {
        "id": "readiness",
        "title": "Migration Readiness",
        "items": [
          {
            "id": "source-assessment",
            "name": "Source Deployment Assessment",
            "source": "generated/skupper-docs-landscape/source-assessment.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/source-assessment",
            "deps": []
          },
          {
            "id": "target-design",
            "name": "Target Deployment Design",
            "source": "generated/skupper-docs-landscape/target-design.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/target-design",
            "deps": []
          },
          {
            "id": "dual-connectivity",
            "name": "Dual Connectivity Plan",
            "source": "generated/skupper-docs-landscape/dual-connectivity.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/dual-connectivity",
            "deps": [
              "source-assessment",
              "target-design"
            ]
          },
          {
            "id": "rollback-path",
            "name": "Rollback Path",
            "source": "generated/skupper-docs-landscape/rollback-path.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/rollback-path",
            "deps": []
          },
          {
            "id": "acceptance-tests",
            "name": "Acceptance Tests",
            "source": "generated/skupper-docs-landscape/acceptance-tests.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/acceptance-tests",
            "deps": []
          }
        ]
      }
    ],
    "source_base_url": "https://pwright.github.io/skupper-okf/"
  },
  {
    "id": "administer-skupper",
    "title": "Administer Skupper",
    "abstract": "Operate sites, links, services, credentials, and lifecycle tasks consistently across an application network.",
    "status": "generated",
    "reviewed": false,
    "source_paths": [
      "generated/skupper-docs-landscape/administer-skupper.md"
    ],
    "categories": [
      {
        "id": "operations",
        "title": "Operational Outcomes",
        "items": [
          {
            "id": "healthy-network",
            "name": "Healthy Application Network",
            "source": "generated/skupper-docs-landscape/healthy-network.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/healthy-network",
            "deps": [
              "site-operations",
              "link-operations",
              "service-operations"
            ]
          },
          {
            "id": "controlled-change",
            "name": "Controlled Administrative Change",
            "source": "generated/skupper-docs-landscape/controlled-change.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/controlled-change",
            "deps": [
              "change-workflow",
              "access-controls"
            ]
          }
        ]
      },
      {
        "id": "workflows",
        "title": "Administrative Workflows",
        "items": [
          {
            "id": "site-operations",
            "name": "Site Operations",
            "source": "generated/skupper-docs-landscape/site-operations.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/site-operations",
            "deps": [
              "site-status",
              "site-configuration"
            ]
          },
          {
            "id": "link-operations",
            "name": "Link Operations",
            "source": "generated/skupper-docs-landscape/link-operations.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/link-operations",
            "deps": [
              "link-status",
              "link-credentials"
            ]
          },
          {
            "id": "service-operations",
            "name": "Service Operations",
            "source": "generated/skupper-docs-landscape/service-operations.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/service-operations",
            "deps": [
              "service-status",
              "service-configuration"
            ]
          },
          {
            "id": "change-workflow",
            "name": "Change Workflow",
            "source": "generated/skupper-docs-landscape/change-workflow.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/change-workflow",
            "deps": [
              "configuration-backup",
              "audit-records"
            ]
          }
        ]
      },
      {
        "id": "state",
        "title": "Operational State",
        "items": [
          {
            "id": "site-status",
            "name": "Site Status",
            "source": "generated/skupper-docs-landscape/site-status.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/site-status",
            "deps": []
          },
          {
            "id": "site-configuration",
            "name": "Site Configuration",
            "source": "generated/skupper-docs-landscape/site-configuration.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/site-configuration",
            "deps": []
          },
          {
            "id": "link-status",
            "name": "Link Status",
            "source": "generated/skupper-docs-landscape/link-status.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/link-status",
            "deps": []
          },
          {
            "id": "link-credentials",
            "name": "Link Credentials",
            "source": "generated/skupper-docs-landscape/link-credentials.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/link-credentials",
            "deps": []
          },
          {
            "id": "service-status",
            "name": "Service Status",
            "source": "generated/skupper-docs-landscape/service-status.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/service-status",
            "deps": []
          },
          {
            "id": "service-configuration",
            "name": "Service Configuration",
            "source": "generated/skupper-docs-landscape/service-configuration.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/service-configuration",
            "deps": []
          }
        ]
      },
      {
        "id": "governance",
        "title": "Governance Controls",
        "items": [
          {
            "id": "configuration-backup",
            "name": "Configuration Backup",
            "source": "generated/skupper-docs-landscape/configuration-backup.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/configuration-backup",
            "deps": []
          },
          {
            "id": "access-controls",
            "name": "Administrative Access Controls",
            "source": "generated/skupper-docs-landscape/access-controls.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/access-controls",
            "deps": []
          },
          {
            "id": "audit-records",
            "name": "Audit Records",
            "source": "generated/skupper-docs-landscape/audit-records.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/audit-records",
            "deps": []
          }
        ]
      }
    ],
    "source_base_url": "https://pwright.github.io/skupper-okf/"
  },
  {
    "id": "configure-skupper",
    "title": "Configure Skupper",
    "abstract": "Define sites, links, listeners, connectors, services, policies, and runtime behavior so the application network matches intended traffic flows.",
    "status": "generated",
    "reviewed": false,
    "source_paths": [
      "generated/skupper-docs-landscape/configure-skupper.md"
    ],
    "categories": [
      {
        "id": "outcomes",
        "title": "Configured Behavior",
        "items": [
          {
            "id": "service-connectivity",
            "name": "Configured Service Connectivity",
            "source": "generated/skupper-docs-landscape/service-connectivity.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/service-connectivity",
            "deps": [
              "listener-config",
              "connector-config",
              "service-routing"
            ]
          },
          {
            "id": "site-behavior",
            "name": "Configured Site Behavior",
            "source": "generated/skupper-docs-landscape/site-behavior.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/site-behavior",
            "deps": [
              "site-config",
              "runtime-settings"
            ]
          }
        ]
      },
      {
        "id": "resources",
        "title": "Configuration Resources",
        "items": [
          {
            "id": "site-config",
            "name": "Site Configuration",
            "source": "generated/skupper-docs-landscape/site-config.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/site-config",
            "deps": [
              "site-identity-config",
              "namespace-scope"
            ]
          },
          {
            "id": "listener-config",
            "name": "Listener Configuration",
            "source": "generated/skupper-docs-landscape/listener-config.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/listener-config",
            "deps": [
              "service-address"
            ]
          },
          {
            "id": "connector-config",
            "name": "Connector Configuration",
            "source": "generated/skupper-docs-landscape/connector-config.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/connector-config",
            "deps": [
              "backend-endpoint"
            ]
          },
          {
            "id": "service-routing",
            "name": "Service Routing Configuration",
            "source": "generated/skupper-docs-landscape/service-routing.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/service-routing",
            "deps": [
              "service-address",
              "routing-mode"
            ]
          },
          {
            "id": "runtime-settings",
            "name": "Runtime Settings",
            "source": "generated/skupper-docs-landscape/runtime-settings.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/runtime-settings",
            "deps": [
              "resource-limits",
              "logging-settings"
            ]
          }
        ]
      },
      {
        "id": "inputs",
        "title": "Configuration Inputs",
        "items": [
          {
            "id": "site-identity-config",
            "name": "Site Identity Settings",
            "source": "generated/skupper-docs-landscape/site-identity-config.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/site-identity-config",
            "deps": []
          },
          {
            "id": "namespace-scope",
            "name": "Namespace Scope",
            "source": "generated/skupper-docs-landscape/namespace-scope.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/namespace-scope",
            "deps": []
          },
          {
            "id": "service-address",
            "name": "Service Address",
            "source": "generated/skupper-docs-landscape/service-address.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/service-address",
            "deps": []
          },
          {
            "id": "backend-endpoint",
            "name": "Backend Endpoint",
            "source": "generated/skupper-docs-landscape/backend-endpoint.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/backend-endpoint",
            "deps": []
          },
          {
            "id": "routing-mode",
            "name": "Routing Mode",
            "source": "generated/skupper-docs-landscape/routing-mode.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/routing-mode",
            "deps": []
          },
          {
            "id": "resource-limits",
            "name": "Resource Limits",
            "source": "generated/skupper-docs-landscape/resource-limits.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/resource-limits",
            "deps": []
          },
          {
            "id": "logging-settings",
            "name": "Logging Settings",
            "source": "generated/skupper-docs-landscape/logging-settings.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/logging-settings",
            "deps": []
          }
        ]
      }
    ],
    "source_base_url": "https://pwright.github.io/skupper-okf/"
  },
  {
    "id": "secure-skupper",
    "title": "Secure Skupper",
    "abstract": "Protect the application network with authenticated links, certificate lifecycle management, least-privilege access, workload isolation, and auditable policy.",
    "status": "generated",
    "reviewed": false,
    "source_paths": [
      "generated/skupper-docs-landscape/secure-skupper.md"
    ],
    "categories": [
      {
        "id": "outcomes",
        "title": "Security Outcomes",
        "items": [
          {
            "id": "trusted-connectivity",
            "name": "Trusted Site Connectivity",
            "source": "generated/skupper-docs-landscape/trusted-connectivity.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/trusted-connectivity",
            "deps": [
              "mutual-authentication",
              "certificate-lifecycle"
            ]
          },
          {
            "id": "least-privilege-network",
            "name": "Least-Privilege Application Network",
            "source": "generated/skupper-docs-landscape/least-privilege-network.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/least-privilege-network",
            "deps": [
              "access-policy",
              "network-isolation"
            ]
          }
        ]
      },
      {
        "id": "controls",
        "title": "Security Controls",
        "items": [
          {
            "id": "mutual-authentication",
            "name": "Mutual Authentication",
            "source": "generated/skupper-docs-landscape/mutual-authentication.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/mutual-authentication",
            "deps": [
              "site-certificates",
              "trust-bundle"
            ]
          },
          {
            "id": "access-policy",
            "name": "Access Policy",
            "source": "generated/skupper-docs-landscape/access-policy.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/access-policy",
            "deps": [
              "rbac",
              "service-policy"
            ]
          },
          {
            "id": "network-isolation",
            "name": "Network Isolation",
            "source": "generated/skupper-docs-landscape/network-isolation.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/network-isolation",
            "deps": [
              "namespace-controls",
              "firewall-rules"
            ]
          },
          {
            "id": "certificate-lifecycle",
            "name": "Certificate Lifecycle",
            "source": "generated/skupper-docs-landscape/certificate-lifecycle.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/certificate-lifecycle",
            "deps": [
              "issuance",
              "rotation"
            ]
          }
        ]
      },
      {
        "id": "identity",
        "title": "Identity Foundations",
        "items": [
          {
            "id": "site-certificates",
            "name": "Site Certificates",
            "source": "generated/skupper-docs-landscape/site-certificates.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/site-certificates",
            "deps": []
          },
          {
            "id": "trust-bundle",
            "name": "Trust Bundle",
            "source": "generated/skupper-docs-landscape/trust-bundle.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/trust-bundle",
            "deps": []
          },
          {
            "id": "rbac",
            "name": "Role-Based Access Control",
            "source": "generated/skupper-docs-landscape/rbac.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/rbac",
            "deps": []
          },
          {
            "id": "service-policy",
            "name": "Service Exposure Policy",
            "source": "generated/skupper-docs-landscape/service-policy.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/service-policy",
            "deps": []
          }
        ]
      },
      {
        "id": "isolation",
        "title": "Isolation Foundations",
        "items": [
          {
            "id": "namespace-controls",
            "name": "Namespace Controls",
            "source": "generated/skupper-docs-landscape/namespace-controls.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/namespace-controls",
            "deps": []
          },
          {
            "id": "firewall-rules",
            "name": "Firewall Rules",
            "source": "generated/skupper-docs-landscape/firewall-rules.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/firewall-rules",
            "deps": []
          },
          {
            "id": "issuance",
            "name": "Certificate Issuance",
            "source": "generated/skupper-docs-landscape/issuance.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/issuance",
            "deps": []
          },
          {
            "id": "rotation",
            "name": "Certificate Rotation",
            "source": "generated/skupper-docs-landscape/rotation.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/rotation",
            "deps": [
              "issuance"
            ]
          }
        ]
      }
    ],
    "source_base_url": "https://pwright.github.io/skupper-okf/"
  },
  {
    "id": "observe-skupper",
    "title": "Observe Skupper",
    "abstract": "Make application-network health, topology, traffic, and faults visible through status views, metrics, logs, events, and traces.",
    "status": "generated",
    "reviewed": false,
    "source_paths": [
      "generated/skupper-docs-landscape/observe-skupper.md"
    ],
    "categories": [
      {
        "id": "outcomes",
        "title": "Operational Visibility",
        "items": [
          {
            "id": "network-health-view",
            "name": "Network Health View",
            "source": "generated/skupper-docs-landscape/network-health-view.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/network-health-view",
            "deps": [
              "site-metrics",
              "link-metrics",
              "service-metrics"
            ]
          },
          {
            "id": "traffic-insight",
            "name": "Traffic Insight",
            "source": "generated/skupper-docs-landscape/traffic-insight.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/traffic-insight",
            "deps": [
              "flow-metrics",
              "trace-correlation"
            ]
          }
        ]
      },
      {
        "id": "signals",
        "title": "Observability Signals",
        "items": [
          {
            "id": "site-metrics",
            "name": "Site Metrics",
            "source": "generated/skupper-docs-landscape/site-metrics.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/site-metrics",
            "deps": [
              "metrics-export"
            ]
          },
          {
            "id": "link-metrics",
            "name": "Link Metrics",
            "source": "generated/skupper-docs-landscape/link-metrics.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/link-metrics",
            "deps": [
              "metrics-export"
            ]
          },
          {
            "id": "service-metrics",
            "name": "Service Metrics",
            "source": "generated/skupper-docs-landscape/service-metrics.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/service-metrics",
            "deps": [
              "metrics-export"
            ]
          },
          {
            "id": "flow-metrics",
            "name": "Flow Metrics",
            "source": "generated/skupper-docs-landscape/flow-metrics.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/flow-metrics",
            "deps": [
              "metrics-export"
            ]
          },
          {
            "id": "event-stream",
            "name": "Events",
            "source": "generated/skupper-docs-landscape/event-stream.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/event-stream",
            "deps": [
              "event-collection"
            ]
          },
          {
            "id": "runtime-logs",
            "name": "Runtime Logs",
            "source": "generated/skupper-docs-landscape/runtime-logs.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/runtime-logs",
            "deps": [
              "log-collection"
            ]
          },
          {
            "id": "trace-correlation",
            "name": "Trace Correlation",
            "source": "generated/skupper-docs-landscape/trace-correlation.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/trace-correlation",
            "deps": [
              "trace-context"
            ]
          }
        ]
      },
      {
        "id": "backends",
        "title": "Collection and Presentation",
        "items": [
          {
            "id": "metrics-export",
            "name": "Metrics Export",
            "source": "generated/skupper-docs-landscape/metrics-export.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/metrics-export",
            "deps": []
          },
          {
            "id": "event-collection",
            "name": "Event Collection",
            "source": "generated/skupper-docs-landscape/event-collection.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/event-collection",
            "deps": []
          },
          {
            "id": "log-collection",
            "name": "Log Collection",
            "source": "generated/skupper-docs-landscape/log-collection.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/log-collection",
            "deps": []
          },
          {
            "id": "trace-context",
            "name": "Trace Context",
            "source": "generated/skupper-docs-landscape/trace-context.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/trace-context",
            "deps": []
          },
          {
            "id": "network-console",
            "name": "Network Console",
            "source": "generated/skupper-docs-landscape/network-console.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/network-console",
            "deps": [
              "metrics-export",
              "event-collection"
            ]
          },
          {
            "id": "dashboards",
            "name": "Dashboards and Alerts",
            "source": "generated/skupper-docs-landscape/dashboards.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/dashboards",
            "deps": [
              "metrics-export",
              "log-collection"
            ]
          }
        ]
      }
    ],
    "source_base_url": "https://pwright.github.io/skupper-okf/"
  },
  {
    "id": "optimize-skupper",
    "title": "Optimize Skupper",
    "abstract": "Improve latency, throughput, reliability, and resource efficiency by tuning topology, routing, capacity, and runtime settings based on observed behavior.",
    "status": "generated",
    "reviewed": false,
    "source_paths": [
      "generated/skupper-docs-landscape/optimize-skupper.md"
    ],
    "categories": [
      {
        "id": "outcomes",
        "title": "Optimization Outcomes",
        "items": [
          {
            "id": "performance-targets",
            "name": "Met Performance Targets",
            "source": "generated/skupper-docs-landscape/performance-targets.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/performance-targets",
            "deps": [
              "routing-tuning",
              "capacity-tuning"
            ]
          },
          {
            "id": "efficient-operation",
            "name": "Efficient Resource Use",
            "source": "generated/skupper-docs-landscape/efficient-operation.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/efficient-operation",
            "deps": [
              "resource-tuning",
              "traffic-shaping"
            ]
          }
        ]
      },
      {
        "id": "tuning",
        "title": "Optimization Levers",
        "items": [
          {
            "id": "routing-tuning",
            "name": "Routing Tuning",
            "source": "generated/skupper-docs-landscape/routing-tuning.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/routing-tuning",
            "deps": [
              "topology-analysis",
              "path-selection"
            ]
          },
          {
            "id": "capacity-tuning",
            "name": "Capacity Tuning",
            "source": "generated/skupper-docs-landscape/capacity-tuning.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/capacity-tuning",
            "deps": [
              "traffic-baseline",
              "headroom-model"
            ]
          },
          {
            "id": "resource-tuning",
            "name": "Runtime Resource Tuning",
            "source": "generated/skupper-docs-landscape/resource-tuning.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/resource-tuning",
            "deps": [
              "resource-profile",
              "load-tests"
            ]
          },
          {
            "id": "traffic-shaping",
            "name": "Traffic Shaping",
            "source": "generated/skupper-docs-landscape/traffic-shaping.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/traffic-shaping",
            "deps": [
              "service-priorities",
              "rate-controls"
            ]
          }
        ]
      },
      {
        "id": "analysis",
        "title": "Analysis Inputs",
        "items": [
          {
            "id": "topology-analysis",
            "name": "Topology Analysis",
            "source": "generated/skupper-docs-landscape/topology-analysis.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/topology-analysis",
            "deps": []
          },
          {
            "id": "path-selection",
            "name": "Path Selection Data",
            "source": "generated/skupper-docs-landscape/path-selection.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/path-selection",
            "deps": []
          },
          {
            "id": "traffic-baseline",
            "name": "Traffic Baseline",
            "source": "generated/skupper-docs-landscape/traffic-baseline.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/traffic-baseline",
            "deps": []
          },
          {
            "id": "headroom-model",
            "name": "Capacity Headroom Model",
            "source": "generated/skupper-docs-landscape/headroom-model.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/headroom-model",
            "deps": []
          }
        ]
      },
      {
        "id": "validation",
        "title": "Validation Inputs",
        "items": [
          {
            "id": "resource-profile",
            "name": "CPU and Memory Profile",
            "source": "generated/skupper-docs-landscape/resource-profile.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/resource-profile",
            "deps": []
          },
          {
            "id": "load-tests",
            "name": "Load Tests",
            "source": "generated/skupper-docs-landscape/load-tests.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/load-tests",
            "deps": []
          },
          {
            "id": "service-priorities",
            "name": "Service Priorities",
            "source": "generated/skupper-docs-landscape/service-priorities.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/service-priorities",
            "deps": []
          },
          {
            "id": "rate-controls",
            "name": "Rate Controls",
            "source": "generated/skupper-docs-landscape/rate-controls.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/rate-controls",
            "deps": []
          }
        ]
      }
    ],
    "source_base_url": "https://pwright.github.io/skupper-okf/"
  },
  {
    "id": "troubleshoot-skupper",
    "title": "Troubleshoot Skupper",
    "abstract": "Diagnose connectivity, routing, identity, configuration, and performance problems using a layered workflow from symptoms to evidence, root cause, and recovery.",
    "status": "generated",
    "reviewed": false,
    "source_paths": [
      "generated/skupper-docs-landscape/troubleshoot-skupper.md"
    ],
    "categories": [
      {
        "id": "outcomes",
        "title": "Troubleshooting Outcomes",
        "items": [
          {
            "id": "restored-connectivity",
            "name": "Restored Connectivity",
            "source": "generated/skupper-docs-landscape/restored-connectivity.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/restored-connectivity",
            "deps": [
              "fault-isolation",
              "remediation"
            ]
          },
          {
            "id": "prevented-recurrence",
            "name": "Prevented Recurrence",
            "source": "generated/skupper-docs-landscape/prevented-recurrence.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/prevented-recurrence",
            "deps": [
              "root-cause-record",
              "corrective-actions"
            ]
          }
        ]
      },
      {
        "id": "workflow",
        "title": "Diagnostic Workflow",
        "items": [
          {
            "id": "fault-isolation",
            "name": "Fault Isolation",
            "source": "generated/skupper-docs-landscape/fault-isolation.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/fault-isolation",
            "deps": [
              "symptom-capture",
              "layered-checks"
            ]
          },
          {
            "id": "root-cause-record",
            "name": "Root Cause Record",
            "source": "generated/skupper-docs-landscape/root-cause-record.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/root-cause-record",
            "deps": [
              "fault-isolation",
              "evidence-bundle"
            ]
          },
          {
            "id": "remediation",
            "name": "Remediation",
            "source": "generated/skupper-docs-landscape/remediation.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/remediation",
            "deps": [
              "root-cause-record",
              "recovery-procedure"
            ]
          },
          {
            "id": "corrective-actions",
            "name": "Corrective Actions",
            "source": "generated/skupper-docs-landscape/corrective-actions.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/corrective-actions",
            "deps": [
              "root-cause-record",
              "monitoring-improvements"
            ]
          }
        ]
      },
      {
        "id": "evidence",
        "title": "Diagnostic Evidence",
        "items": [
          {
            "id": "symptom-capture",
            "name": "Symptom Capture",
            "source": "generated/skupper-docs-landscape/symptom-capture.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/symptom-capture",
            "deps": []
          },
          {
            "id": "layered-checks",
            "name": "Site, Link, Route, and Service Checks",
            "source": "generated/skupper-docs-landscape/layered-checks.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/layered-checks",
            "deps": []
          },
          {
            "id": "evidence-bundle",
            "name": "Logs, Events, Metrics, and Configuration",
            "source": "generated/skupper-docs-landscape/evidence-bundle.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/evidence-bundle",
            "deps": []
          },
          {
            "id": "recovery-procedure",
            "name": "Recovery Procedure",
            "source": "generated/skupper-docs-landscape/recovery-procedure.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/recovery-procedure",
            "deps": []
          },
          {
            "id": "monitoring-improvements",
            "name": "Monitoring Improvements",
            "source": "generated/skupper-docs-landscape/monitoring-improvements.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/monitoring-improvements",
            "deps": []
          }
        ]
      }
    ],
    "source_base_url": "https://pwright.github.io/skupper-okf/"
  },
  {
    "id": "develop-skupper",
    "title": "Develop with Skupper",
    "abstract": "Support application developers and platform engineers who automate Skupper, embed connectivity into delivery workflows, or build against its command-line and declarative interfaces.",
    "status": "generated",
    "reviewed": false,
    "source_paths": [
      "generated/skupper-docs-landscape/develop-skupper.md"
    ],
    "categories": [
      {
        "id": "outcomes",
        "title": "Developer Outcomes",
        "items": [
          {
            "id": "automated-connectivity",
            "name": "Automated Application Connectivity",
            "source": "generated/skupper-docs-landscape/automated-connectivity.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/automated-connectivity",
            "deps": [
              "declarative-resources",
              "pipeline-integration"
            ]
          },
          {
            "id": "repeatable-environments",
            "name": "Repeatable Skupper Environments",
            "source": "generated/skupper-docs-landscape/repeatable-environments.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/repeatable-environments",
            "deps": [
              "configuration-as-code",
              "test-harness"
            ]
          }
        ]
      },
      {
        "id": "interfaces",
        "title": "Development Interfaces",
        "items": [
          {
            "id": "declarative-resources",
            "name": "Declarative Resources",
            "source": "generated/skupper-docs-landscape/declarative-resources.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/declarative-resources",
            "deps": [
              "resource-schema",
              "examples"
            ]
          },
          {
            "id": "cli-automation",
            "name": "CLI Automation",
            "source": "generated/skupper-docs-landscape/cli-automation.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/cli-automation",
            "deps": [
              "cli-contract",
              "error-handling"
            ]
          },
          {
            "id": "pipeline-integration",
            "name": "CI/CD Integration",
            "source": "generated/skupper-docs-landscape/pipeline-integration.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/pipeline-integration",
            "deps": [
              "cli-automation",
              "secrets-injection"
            ]
          },
          {
            "id": "configuration-as-code",
            "name": "Configuration as Code",
            "source": "generated/skupper-docs-landscape/configuration-as-code.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/configuration-as-code",
            "deps": [
              "declarative-resources",
              "version-control"
            ]
          }
        ]
      },
      {
        "id": "foundations",
        "title": "Developer Foundations",
        "items": [
          {
            "id": "resource-schema",
            "name": "Resource Schemas",
            "source": "generated/skupper-docs-landscape/resource-schema.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/resource-schema",
            "deps": []
          },
          {
            "id": "examples",
            "name": "Reference Examples",
            "source": "generated/skupper-docs-landscape/examples.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/examples",
            "deps": []
          },
          {
            "id": "cli-contract",
            "name": "CLI Command Contract",
            "source": "generated/skupper-docs-landscape/cli-contract.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/cli-contract",
            "deps": []
          },
          {
            "id": "error-handling",
            "name": "Exit Codes and Error Handling",
            "source": "generated/skupper-docs-landscape/error-handling.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/error-handling",
            "deps": []
          },
          {
            "id": "secrets-injection",
            "name": "Secrets Injection",
            "source": "generated/skupper-docs-landscape/secrets-injection.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/secrets-injection",
            "deps": []
          },
          {
            "id": "version-control",
            "name": "Version Control",
            "source": "generated/skupper-docs-landscape/version-control.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/version-control",
            "deps": []
          },
          {
            "id": "test-harness",
            "name": "Integration Test Harness",
            "source": "generated/skupper-docs-landscape/test-harness.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/test-harness",
            "deps": [
              "examples"
            ]
          }
        ]
      }
    ],
    "source_base_url": "https://pwright.github.io/skupper-okf/"
  },
  {
    "id": "integrate-skupper",
    "title": "Integrate Skupper",
    "abstract": "Connect Skupper with Kubernetes platforms, virtual machines, service frameworks, CI/CD systems, observability stacks, security tooling, and enterprise network controls.",
    "status": "generated",
    "reviewed": false,
    "source_paths": [
      "generated/skupper-docs-landscape/integrate-skupper.md"
    ],
    "categories": [
      {
        "id": "outcomes",
        "title": "Integration Outcomes",
        "items": [
          {
            "id": "platform-connectivity",
            "name": "Platform-to-Platform Connectivity",
            "source": "generated/skupper-docs-landscape/platform-connectivity.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/platform-connectivity",
            "deps": [
              "kubernetes-integration",
              "host-integration"
            ]
          },
          {
            "id": "operational-integration",
            "name": "Operational Toolchain Integration",
            "source": "generated/skupper-docs-landscape/operational-integration.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/operational-integration",
            "deps": [
              "observability-integration",
              "security-integration",
              "delivery-integration"
            ]
          }
        ]
      },
      {
        "id": "patterns",
        "title": "Integration Patterns",
        "items": [
          {
            "id": "kubernetes-integration",
            "name": "Kubernetes Integration",
            "source": "generated/skupper-docs-landscape/kubernetes-integration.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/kubernetes-integration",
            "deps": [
              "service-discovery",
              "resource-automation"
            ]
          },
          {
            "id": "host-integration",
            "name": "Linux Host Integration",
            "source": "generated/skupper-docs-landscape/host-integration.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/host-integration",
            "deps": [
              "host-service-binding",
              "host-identity"
            ]
          },
          {
            "id": "observability-integration",
            "name": "Observability Integration",
            "source": "generated/skupper-docs-landscape/observability-integration.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/observability-integration",
            "deps": [
              "metrics-interface",
              "logging-interface"
            ]
          },
          {
            "id": "security-integration",
            "name": "Security Tooling Integration",
            "source": "generated/skupper-docs-landscape/security-integration.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/security-integration",
            "deps": [
              "certificate-interface",
              "policy-interface"
            ]
          },
          {
            "id": "delivery-integration",
            "name": "CI/CD Integration",
            "source": "generated/skupper-docs-landscape/delivery-integration.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/delivery-integration",
            "deps": [
              "automation-interface",
              "secrets-interface"
            ]
          }
        ]
      },
      {
        "id": "platform-interfaces",
        "title": "Platform Interfaces",
        "items": [
          {
            "id": "service-discovery",
            "name": "Service Discovery Interface",
            "source": "generated/skupper-docs-landscape/service-discovery.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/service-discovery",
            "deps": []
          },
          {
            "id": "resource-automation",
            "name": "Resource Automation Interface",
            "source": "generated/skupper-docs-landscape/resource-automation.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/resource-automation",
            "deps": []
          },
          {
            "id": "host-service-binding",
            "name": "Host Service Binding",
            "source": "generated/skupper-docs-landscape/host-service-binding.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/host-service-binding",
            "deps": []
          },
          {
            "id": "host-identity",
            "name": "Host Identity",
            "source": "generated/skupper-docs-landscape/host-identity.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/host-identity",
            "deps": []
          }
        ]
      },
      {
        "id": "operations-interfaces",
        "title": "Operations Interfaces",
        "items": [
          {
            "id": "metrics-interface",
            "name": "Metrics Interface",
            "source": "generated/skupper-docs-landscape/metrics-interface.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/metrics-interface",
            "deps": []
          },
          {
            "id": "logging-interface",
            "name": "Logging Interface",
            "source": "generated/skupper-docs-landscape/logging-interface.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/logging-interface",
            "deps": []
          },
          {
            "id": "certificate-interface",
            "name": "Certificate Interface",
            "source": "generated/skupper-docs-landscape/certificate-interface.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/certificate-interface",
            "deps": []
          },
          {
            "id": "policy-interface",
            "name": "Policy Interface",
            "source": "generated/skupper-docs-landscape/policy-interface.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/policy-interface",
            "deps": []
          },
          {
            "id": "automation-interface",
            "name": "Automation Interface",
            "source": "generated/skupper-docs-landscape/automation-interface.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/automation-interface",
            "deps": []
          },
          {
            "id": "secrets-interface",
            "name": "Secrets Interface",
            "source": "generated/skupper-docs-landscape/secrets-interface.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/secrets-interface",
            "deps": []
          }
        ]
      }
    ],
    "source_base_url": "https://pwright.github.io/skupper-okf/"
  },
  {
    "id": "platform-guides",
    "title": "Skupper Platform and Managed-Environment Guides",
    "abstract": "Adapt Skupper deployment and operations to Kubernetes distributions, managed cloud platforms, virtual machines, and mixed environments with platform-specific prerequisites and controls.",
    "status": "generated",
    "reviewed": false,
    "source_paths": [
      "generated/skupper-docs-landscape/platform-guides.md"
    ],
    "categories": [
      {
        "id": "outcomes",
        "title": "Platform Outcomes",
        "items": [
          {
            "id": "supported-deployment",
            "name": "Supported Platform Deployment",
            "source": "generated/skupper-docs-landscape/supported-deployment.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/supported-deployment",
            "deps": [
              "platform-profile",
              "installation-pattern"
            ]
          },
          {
            "id": "hybrid-environment",
            "name": "Hybrid Environment Connectivity",
            "source": "generated/skupper-docs-landscape/hybrid-environment.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/hybrid-environment",
            "deps": [
              "cluster-pattern",
              "host-pattern",
              "network-controls"
            ]
          }
        ]
      },
      {
        "id": "patterns",
        "title": "Platform Patterns",
        "items": [
          {
            "id": "cluster-pattern",
            "name": "Kubernetes Cluster Pattern",
            "source": "generated/skupper-docs-landscape/cluster-pattern.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/cluster-pattern",
            "deps": [
              "platform-profile",
              "operator-or-cli"
            ]
          },
          {
            "id": "managed-platform-pattern",
            "name": "Managed Kubernetes Pattern",
            "source": "generated/skupper-docs-landscape/managed-platform-pattern.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/managed-platform-pattern",
            "deps": [
              "platform-profile",
              "cloud-network-rules"
            ]
          },
          {
            "id": "host-pattern",
            "name": "Linux Host Pattern",
            "source": "generated/skupper-docs-landscape/host-pattern.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/host-pattern",
            "deps": [
              "host-profile",
              "system-service"
            ]
          },
          {
            "id": "mixed-platform-pattern",
            "name": "Mixed Platform Pattern",
            "source": "generated/skupper-docs-landscape/mixed-platform-pattern.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/mixed-platform-pattern",
            "deps": [
              "cluster-pattern",
              "host-pattern"
            ]
          }
        ]
      },
      {
        "id": "inputs",
        "title": "Platform Inputs",
        "items": [
          {
            "id": "platform-profile",
            "name": "Platform Compatibility Profile",
            "source": "generated/skupper-docs-landscape/platform-profile.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/platform-profile",
            "deps": []
          },
          {
            "id": "host-profile",
            "name": "Host Compatibility Profile",
            "source": "generated/skupper-docs-landscape/host-profile.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/host-profile",
            "deps": []
          },
          {
            "id": "installation-pattern",
            "name": "Installation Pattern",
            "source": "generated/skupper-docs-landscape/installation-pattern.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/installation-pattern",
            "deps": [
              "platform-profile"
            ]
          },
          {
            "id": "operator-or-cli",
            "name": "Operator or CLI Choice",
            "source": "generated/skupper-docs-landscape/operator-or-cli.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/operator-or-cli",
            "deps": []
          },
          {
            "id": "cloud-network-rules",
            "name": "Cloud Network Rules",
            "source": "generated/skupper-docs-landscape/cloud-network-rules.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/cloud-network-rules",
            "deps": []
          },
          {
            "id": "system-service",
            "name": "System Service Configuration",
            "source": "generated/skupper-docs-landscape/system-service.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/system-service",
            "deps": [
              "host-profile"
            ]
          },
          {
            "id": "network-controls",
            "name": "Firewall and Egress Controls",
            "source": "generated/skupper-docs-landscape/network-controls.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/network-controls",
            "deps": []
          }
        ]
      }
    ],
    "source_base_url": "https://pwright.github.io/skupper-okf/"
  },
  {
    "id": "skupper-reference",
    "title": "Skupper Reference",
    "abstract": "Provide precise command, resource, field, status, compatibility, and terminology details for users who need authoritative implementation information.",
    "status": "generated",
    "reviewed": false,
    "source_paths": [
      "generated/skupper-docs-landscape/skupper-reference.md"
    ],
    "categories": [
      {
        "id": "interfaces",
        "title": "Interface Reference",
        "items": [
          {
            "id": "cli-reference",
            "name": "CLI Reference",
            "source": "generated/skupper-docs-landscape/cli-reference.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/cli-reference",
            "deps": [
              "command-syntax",
              "exit-status"
            ]
          },
          {
            "id": "resource-reference",
            "name": "Resource Reference",
            "source": "generated/skupper-docs-landscape/resource-reference.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/resource-reference",
            "deps": [
              "resource-fields",
              "resource-status"
            ]
          }
        ]
      },
      {
        "id": "runtime",
        "title": "Runtime Reference",
        "items": [
          {
            "id": "configuration-reference",
            "name": "Configuration Reference",
            "source": "generated/skupper-docs-landscape/configuration-reference.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/configuration-reference",
            "deps": [
              "defaults",
              "constraints"
            ]
          },
          {
            "id": "status-reference",
            "name": "Status and Condition Reference",
            "source": "generated/skupper-docs-landscape/status-reference.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/status-reference",
            "deps": [
              "resource-status",
              "event-codes"
            ]
          },
          {
            "id": "compatibility-reference",
            "name": "Compatibility Reference",
            "source": "generated/skupper-docs-landscape/compatibility-reference.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/compatibility-reference",
            "deps": [
              "version-matrix",
              "platform-matrix"
            ]
          }
        ]
      },
      {
        "id": "syntax",
        "title": "Syntax and Schema",
        "items": [
          {
            "id": "command-syntax",
            "name": "Command Syntax",
            "source": "generated/skupper-docs-landscape/command-syntax.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/command-syntax",
            "deps": []
          },
          {
            "id": "exit-status",
            "name": "Exit Status and Errors",
            "source": "generated/skupper-docs-landscape/exit-status.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/exit-status",
            "deps": []
          },
          {
            "id": "resource-fields",
            "name": "Resource Fields",
            "source": "generated/skupper-docs-landscape/resource-fields.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/resource-fields",
            "deps": []
          },
          {
            "id": "resource-status",
            "name": "Resource Status",
            "source": "generated/skupper-docs-landscape/resource-status.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/resource-status",
            "deps": []
          }
        ]
      },
      {
        "id": "semantics",
        "title": "Defaults and Diagnostics",
        "items": [
          {
            "id": "defaults",
            "name": "Default Values",
            "source": "generated/skupper-docs-landscape/defaults.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/defaults",
            "deps": []
          },
          {
            "id": "constraints",
            "name": "Validation Constraints",
            "source": "generated/skupper-docs-landscape/constraints.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/constraints",
            "deps": []
          },
          {
            "id": "event-codes",
            "name": "Event and Diagnostic Codes",
            "source": "generated/skupper-docs-landscape/event-codes.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/event-codes",
            "deps": []
          }
        ]
      },
      {
        "id": "matrices",
        "title": "Matrices and Terms",
        "items": [
          {
            "id": "version-matrix",
            "name": "Version Matrix",
            "source": "generated/skupper-docs-landscape/version-matrix.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/version-matrix",
            "deps": []
          },
          {
            "id": "platform-matrix",
            "name": "Platform Matrix",
            "source": "generated/skupper-docs-landscape/platform-matrix.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/platform-matrix",
            "deps": []
          },
          {
            "id": "glossary",
            "name": "Glossary",
            "source": "generated/skupper-docs-landscape/glossary.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/glossary",
            "deps": []
          }
        ]
      }
    ],
    "source_base_url": "https://pwright.github.io/skupper-okf/"
  },
  {
    "id": "skupper-pdf-library",
    "title": "Skupper Downloadable Guides",
    "abstract": "Package the most useful Skupper learning, deployment, operations, security, and reference material into stable downloadable guides for offline use and controlled distribution.",
    "status": "generated",
    "reviewed": false,
    "source_paths": [
      "generated/skupper-docs-landscape/skupper-pdf-library.md"
    ],
    "categories": [
      {
        "id": "guides",
        "title": "Downloadable Guides",
        "items": [
          {
            "id": "getting-started-guide",
            "name": "Getting Started Guide",
            "source": "generated/skupper-docs-landscape/getting-started-guide.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/getting-started-guide",
            "deps": [
              "guide-source",
              "release-version"
            ]
          },
          {
            "id": "operations-guide",
            "name": "Operations Guide",
            "source": "generated/skupper-docs-landscape/operations-guide.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/operations-guide",
            "deps": [
              "guide-source",
              "release-version"
            ]
          },
          {
            "id": "security-guide",
            "name": "Security Guide",
            "source": "generated/skupper-docs-landscape/security-guide.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/security-guide",
            "deps": [
              "guide-source",
              "release-version"
            ]
          },
          {
            "id": "reference-guide",
            "name": "Reference Guide",
            "source": "generated/skupper-docs-landscape/reference-guide.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/reference-guide",
            "deps": [
              "reference-source",
              "release-version"
            ]
          }
        ]
      },
      {
        "id": "publishing",
        "title": "Publishing Workflow",
        "items": [
          {
            "id": "pdf-build",
            "name": "PDF Build",
            "source": "generated/skupper-docs-landscape/pdf-build.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/pdf-build",
            "deps": [
              "guide-source",
              "reference-source"
            ]
          },
          {
            "id": "quality-review",
            "name": "PDF Quality Review",
            "source": "generated/skupper-docs-landscape/quality-review.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/quality-review",
            "deps": [
              "pdf-build",
              "link-check"
            ]
          },
          {
            "id": "release-publish",
            "name": "Release Publication",
            "source": "generated/skupper-docs-landscape/release-publish.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/release-publish",
            "deps": [
              "quality-review",
              "release-version"
            ]
          }
        ]
      },
      {
        "id": "sources",
        "title": "Source and Versioning",
        "items": [
          {
            "id": "guide-source",
            "name": "Guide Source Content",
            "source": "generated/skupper-docs-landscape/guide-source.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/guide-source",
            "deps": []
          },
          {
            "id": "reference-source",
            "name": "Reference Source Content",
            "source": "generated/skupper-docs-landscape/reference-source.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/reference-source",
            "deps": []
          },
          {
            "id": "release-version",
            "name": "Release Version Metadata",
            "source": "generated/skupper-docs-landscape/release-version.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/release-version",
            "deps": []
          },
          {
            "id": "link-check",
            "name": "Link and Cross-reference Check",
            "source": "generated/skupper-docs-landscape/link-check.md",
            "external": "https://pwright.github.io/skupper-okf/generated/skupper-docs-landscape/link-check",
            "deps": []
          }
        ]
      }
    ],
    "source_base_url": "https://pwright.github.io/skupper-okf/"
  }
]
```
