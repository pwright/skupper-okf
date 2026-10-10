# Generated documentation report

Documents: **146**  
Headings: **729**  
Links: **138**  
Code blocks: **467**

Each document entry lists headings, links, and code block languages extracted by `mq`.

## `human/skupper-docs/CHANGES-SUMMARY.md`

Headings (28):
- # Changes Summary: Configurable Link Prefix for MkDocs Integration
- ## Problem Solved
- ## Solution Implemented
- ## Files Changed
- ### 1.
- ### 2.
- ### 3.
- ## Usage
- ### For MkDocs (default)
- ### For Transom/Jekyll
- ### For Custom Path
- ### For Root-Level Deployment
- ## Generated Link Examples
- ### With Default (/refdog)
- ### With Empty Prefix
- ### With Custom Prefix (/reference)
- ## Verification
- ## New/Updated Files
- ### Scripts
- ### Documentation
- ## Benefits
- ## Testing
- ## Migration for Existing Users
- ### Old Workflow (with sed)
- ### New Workflow (clean)
- ## Backward Compatibility
- ## Next Steps
- ## Questions?

Links (0):
- None

Code blocks (14):
- `python`
- `bash`
- `bash`
- `bash`
- `bash`
- `html`
- `html`
- `html`
- `bash`
- `bash`
- `bash`
- `bash`
- `bash`
- `bash`

## `human/skupper-docs/DEBUG-LINKS.md`

Headings (8):
- # Debug: Why Links Lose /docs Prefix
- ## Current Situation
- ## Possible Causes
- ### 1. MkDocs  Processing
- ### 2. Base URL Tag
- ### 3. Site URL Configuration
- ## Quick Fix: Use Relative Links
- ## Next Steps

Links (0):
- None

Code blocks (3):
- `yaml`
- `html`
- `html`

## `human/skupper-docs/LINK-RESOLUTION.md`

Headings (29):
- # Link Resolution Guide
- ## How Refdog Links Work
- ### Your Current Structure
- ## Finding the Right Prefix
- ### Test 1: Check MkDocs Structure
- ### Test 2: Check Generated Links
- ### Test 3: Verify in Browser
- ## Common Scenarios
- ### Scenario 1: Refdog at /refdog/
- ### Scenario 2: Refdog at Root
- ### Scenario 3: Custom Path
- ## How MkDocs Resolves Links
- ## Testing Link Resolution
- ### Quick Test
- ### Full Test with MkDocs
- ## Debugging 404s
- ### Check 1: Verify File Exists
- ### Check 2: Check Browser Network Tab
- ### Check 3: Try Different Prefix
- ## Setting Default Prefix
- ### Option 1: Environment Variable
- ### Option 2: Edit Script
- ### Option 3: Wrapper Script
- ## Link Types in Refdog Output
- ### 1. Between Commands
- ### 2. Between Resources
- ### 3. Commands ↔ Resources
- ### 4. To External Links
- ## Summary

Links (0):
- None

Code blocks (24):
- `unspecified`
- `bash`
- `bash`
- `unspecified`
- `unspecified`
- `bash`
- `unspecified`
- `unspecified`
- `bash`
- `unspecified`
- `unspecified`
- `bash`
- `bash`
- `bash`
- `bash`
- `bash`
- `bash`
- `bash`
- `bash`
- `bash`
- `html`
- `html`
- `html`
- `html`

## `human/skupper-docs/MKDOCS-INTEGRATION.md`

Headings (14):
- # MkDocs Integration Fix: Refdog Template Syntax
- ## Problem
- ## Solutions
- ### Option 1: Configure Macros to Ignore Reference Docs (Recommended)
- ### Option 2: Fix Refdog Generator to Output MkDocs-Compatible Syntax
- #### In :
- ### Option 3: Post-Process Refdog Output for MkDocs
- ### Option 4: Make Refdog Output Configurable
- #### In :
- ## Recommended Approach
- ### Short Term: Option 1 (Exclude from Macros)
- ### Better Short Term: Option 3 (Post-Process)
- ### Long Term: Option 4 (Configurable Output)
- ## Immediate Action

Links (0):
- None

Code blocks (9):
- `yaml`
- `python`
- `bash`
- `bash`
- `bash`
- `python`
- `bash`
- `yaml`
- `bash`

## `human/skupper-docs/PLAN.md`

Headings (51):
- # Integration Plan: Refdog Reference Documentation → Skupper Website
- ## Executive Summary
- ### Recommended Approach: Option 2 - MkDocs Integration via Symlinks + Post-Processing
- ## Current Architecture
- ### Refdog (docs-vale/refdog/)
- ### Website MkDocs (website-mkdocs/)
- ## Integration Options
- ### Option 1: Copy on Build ❌ (Not Recommended)
- ### Option 2: Symlink Integration ✅ (Recommended)
- ### Option 3: Git Submodule ⚠️ (Overkill)
- ### Option 4: Monorepo ⚠️ (Major Change)
- ## Recommended Implementation: Option 2 (Symlinks)
- ### Phase 1: Commands Integration (1 hour)
- #### Step 1.1: Create Reference Directory Structure
- #### Step 1.2: Create Symlinks
- #### Step 1.3: Update MkDocs Configuration
- #### Step 1.4: Test Local Build
- #### Step 1.5: Regeneration Workflow
- ### Phase 2: Resources Integration (1 hour)
- #### Step 2.1: Create Resources Symlink
- #### Step 2.2: Update MkDocs Navigation
- #### Step 2.3: Test and Verify
- ### Phase 3: Polish and Navigation (1 hour)
- #### Step 3.1: Create Reference Landing Page
- #### Step 3.2: Add Cross-Links
- #### Step 3.3: Add Search Integration
- #### Step 3.4: Update Home Page
- ## Build Integration
- ### Development Workflow
- ### CI/CD Integration
- ### Netlify Integration
- ## MkDocs Compatibility
- ### Markdown Compatibility
- ### Theme Compatibility
- ### Plugin Recommendations
- ## Migration Strategy
- ### Incremental Rollout
- ### Validation Checklist
- ## Alternative: Separate Reference Site
- ## HTML Export Alternative
- ### Option: Generate HTML, Copy to MkDocs Static
- ## Recommended Timeline
- ### Phase 1: Commands (Week 1)
- ### Phase 2: Resources (Week 2+)
- ### Phase 3: Enhancement (Week 3)
- ## Success Criteria
- ### Must Have
- ### Nice to Have
- ## Rollback Plan
- ## Questions to Answer
- ## Next Steps

Links (0):
- None

Code blocks (33):
- `unspecified`
- `unspecified`
- `bash`
- `bash`
- `unspecified`
- `bash`
- `bash`
- `bash`
- `yaml`
- `bash`
- `bash`
- `bash`
- `yaml`
- `bash`
- `markdown`
- `markdown`
- `markdown`
- `bash`
- `markdown`
- `bash`
- `yaml`
- `toml`
- `yaml`
- `yaml`
- `yaml`
- `bash`
- `bash`
- `bash`
- `bash`
- `markdown`
- `bash`
- `yaml`
- `bash`

## `human/skupper-docs/QUICK-FIX.md`

Headings (12):
- # Quick Fix: Link Resolution
- ## Problem
- ## Solution
- ## How to Find the Correct Prefix
- ### Method 1: Check Your URL Structure
- ### Method 2: Check mkdocs.yml
- ### Method 3: Test and Verify
- ## Common Prefixes
- ## Default Updated
- ## Verification
- ## Testing Checklist
- ## If Links Still 404

Links (0):
- None

Code blocks (9):
- `bash`
- `unspecified`
- `yaml`
- `unspecified`
- `unspecified`
- `bash`
- `html`
- `html`
- `unspecified`

## `human/skupper-docs/README.md`

Headings (4):
- # Refdog: Skupper Reference Doc Generation
- ## Start here
- ## Short version
- ## Additional reference

Links (3):
- [refdog/README.md](./refdog/README.md)
- [refdog/resources.md](./refdog/resources.md)
- [refdog/crd-generation-proposal.md](./refdog/crd-generation-proposal.md)

Code blocks (1):
- `bash`

## `human/skupper-docs/REFDOG-NAVIGATION.md`

Headings (21):
- # Refdog Navigation Options for MkDocs
- ## Problem
- ## Solutions
- ### Option 1: Awesome Pages Plugin ✅ (Recommended)
- #### 
- #### 
- #### 
- ### Option 2: Literate Nav Plugin
- ### Option 3: Section Plugin with Auto-discovery
- ### Option 4: Generate Navigation Programmatically
- ### Option 5: Minimal Manual Nav (Simple)
- ## Recommended: Awesome Pages Plugin
- ### Implementation Steps
- #### 1. Install Plugin
- #### 2. Update mkdocs.yml
- #### 3. Create Navigation Files in Refdog
- #### 4. Update Main Nav
- #### 5. Generate .pages Files Automatically
- ## Integration with Build Process
- ## Quick Start: Minimal Approach
- ## Recommendation

Links (0):
- None

Code blocks (27):
- `bash`
- `yaml`
- `yaml`
- `yaml`
- `yaml`
- `yaml`
- `bash`
- `yaml`
- `markdown`
- `yaml`
- `bash`
- `yaml`
- `python`
- `bash`
- `yaml`
- `bash`
- `yaml`
- `yaml`
- `yaml`
- `yaml`
- `yaml`
- `yaml`
- `yaml`
- `bash`
- `bash`
- `bash`
- `yaml`

## `human/skupper-docs/_source.md`

Headings (1):
- # Skupper documentation source snapshot

Links (0):
- None

Code blocks (1):
- `bash`

## `human/skupper-docs/external/transom/README.md`

Headings (6):
- # Transom
- ## Overview
- ## Installation
- ## Using the transom command
- ## Templates
- ## Setting up Transom for a website repo

Links (1):
- [](https://github.com/ssorj/transom/actions?query=workflow%3Amain)

Code blocks (12):
- `unspecified`
- `sh`
- `sh`
- `sh`
- `python`
- `html`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`

## `human/skupper-docs/external/transom/external/mistune/BACKERS.md`

Headings (3):
- # Sponsors and Backers
- ## Sponsors
- ## Awesome Backers

Links (1):
- [Support Me via GitHub Sponsors](https://github.com/sponsors/lepture)

Code blocks (0):
- None

## `human/skupper-docs/external/transom/external/mistune/README.md`

Headings (8):
- # Mistune v3
- ## Paid plugins
- ## Sponsors
- ## Install
- ## Overview
- ## Security Reporting
- ## Benchmarks
- ## License

Links (4):
- [one time tier (Mistune enhance)](https://github.com/sponsors/lepture/sponsorships?tier_id=220664)
- [Support Me via GitHub Sponsors](https://github.com/sponsors/lepture)
- [me@lepture.com](mailto:me@lepture.com)
- [Tidelift security contact](https://tidelift.com/security)

Code blocks (4):
- `unspecified`
- `python`
- `unspecified`
- `unspecified`

## `human/skupper-docs/external/transom/external/mistune/tests/fixtures/include/hello.md`

Headings (0):
- None

Links (0):
- None

Code blocks (0):
- None

## `human/skupper-docs/external/transom/external/mistune/tests/fixtures/include/text.md`

Headings (1):
- # Include

Links (0):
- None

Code blocks (0):
- None

## `human/skupper-docs/external/transom/external/plano/README.md`

Headings (9):
- # Plano
- ## Installation
- ## A self-contained command with subcommands
- ## A self-contained test command
- ## Programmatic test definition
- ## Things to know
- ## Dependencies
- ## Setting up Plano as an embedded dependency
- ## Extending an existing command

Links (1):
- [](https://github.com/ssorj/plano/actions?query=workflow%3Amain)

Code blocks (14):
- `unspecified`
- `unspecified`
- `python`
- `shell`
- `python`
- `shell`
- `python`
- `unspecified`
- `console`
- `shell`
- `shell`
- `shell`
- `python`
- `python`

## `human/skupper-docs/external/transom/profiles/website/input/index.md`

Headings (1):
- # Hello!

Links (0):
- None

Code blocks (0):
- None

## `human/skupper-docs/external/transom/test-site/config/swatch.md`

Headings (0):
- None

Links (1):
- [swatch](http://example.net)

Code blocks (0):
- None

## `human/skupper-docs/external/transom/test-site/input/adir/bdir/test.md`

Headings (1):
- # Test

Links (0):
- None

Code blocks (0):
- None

## `human/skupper-docs/external/transom/test-site/input/test-1.md`

Headings (1):
- # Test 1

Links (0):
- None

Code blocks (0):
- None

## `human/skupper-docs/external/transom/test-site/input/test-2.md`

Headings (1):
- # Test 2

Links (0):
- None

Code blocks (0):
- None

## `human/skupper-docs/input/console/configuration.md`

Headings (42):
- # Network Observer Configuration Reference
- ## External access
- ### Ingress
- ### Route (OpenShift)
- ## Authentication
- ### Basic Authentication
- ### OpenShift OAuth
- ## TLS Certificates
- ## Router Connection
- ## Network Observer Tuning
- ## Prometheus Configuration
- ### Configuration File
- ### Command-Line Flags
- ### Extra Volumes and Mounts
- ## Data Persistence
- ### Persistence Options
- ## Container Resources
- ### Network Observer Container
- ### Prometheus Container
- ### Proxy Container
- ## Container Images
- ### Network Observer Image
- ### Prometheus Image
- ### NGINX Proxy Image
- ### OpenShift OAuth Proxy Image
- ## Labels and Annotations
- ## Service
- ## Security
- ### Pod Security Context
- ### Container Security Contexts
- ## Advanced Options
- ### Name Overrides
- ### Skip Management Labels
- ## Metrics Endpoint
- ### Metrics Service
- ### Scraping Metrics
- ## Validation and Troubleshooting
- ### Verify Services
- ### Test Metrics Endpoint
- ### Check Observer Logs
- ### Verify Prometheus Configuration
- ### PersistentVolumeClaim Issues

Links (0):
- None

Code blocks (19):
- `yaml`
- `yaml`
- `yaml`
- `yaml`
- `unspecified`
- `unspecified`
- `unspecified`
- `yaml`
- `yaml`
- `yaml`
- `yaml`
- `bash`
- `text`
- `bash`
- `text`
- `bash`
- `text`
- `bash`
- `bash`

## `human/skupper-docs/input/console/index.md`

Headings (8):
- # Using the Skupper network console
- ## Getting started with Skupper network console
- ## Advanced Configuration
- ### Configuration Examples
- ### Validation and Troubleshooting
- ### Upgrade and Rollback
- ### Uninstallation
- ## Exploring the Network console

Links (2):
- [API documentation](/api/)
- [Network Observer Configuration](configuration.md)

Code blocks (21):
- `unspecified`
- `unspecified`
- `unspecified`
- `bash`
- `yaml`
- `bash`
- `yaml`
- `yaml`
- `yaml`
- `yaml`
- `yaml`
- `yaml`
- `bash`
- `bash`
- `bash`
- `bash`
- `bash`
- `bash`
- `bash`
- `bash`
- `bash`

## `human/skupper-docs/input/index.md`

Headings (5):
- # Skupper documentation
- ## Get started with the CLI
- ## Create application networks declaratively
- ## Explore conceptual deep dives
- ## Reference material

Links (16):
- [Getting started](https://skupper.io/start/index.html)
- [Kubernetes YAML overview](kube-yaml/index.html)
- [Configure sites with Kubernetes YAML](kube-yaml/site-configuration.html)
- [Link sites with Kubernetes YAML](kube-yaml/site-linking.html)
- [Expose services with Kubernetes YAML](kube-yaml/service-exposure.html)
- [System YAML overview](system-yaml/index.html)
- [Configure sites with system YAML](system-yaml/site-configuration.html)
- [Link sites with system YAML](system-yaml/site-linking.html)
- [Expose services with system YAML](system-yaml/service-exposure.html)
- [Reference home](refdog/index.html)
- [Skupper concepts](refdog/concepts/index.html)
- [Operational topics](refdog/topics/index.html)
- [CLI reference](refdog/commands/index.html)
- [Resource reference](refdog/resources/index.html)
- [Console guide](console/index.html)
- [Troubleshooting](troubleshooting/index.html)

Code blocks (0):
- None

## `human/skupper-docs/input/install/index.md`

Headings (7):
- # Installing the Skupper controller
- ## Installing the Skupper controller using YAML
- ## Installing the Skupper controller using the Skupper Helm charts
- ## Installing the Skupper CLI
- ## Upgrading sites
- ### Upgrading local sites
- ### Upgrading the Skupper controller

Links (3):
- [install the CLI](#installing-cli)
- [https://helm.sh/docs/intro/install/](https://helm.sh/docs/intro/install/)
- [Releases](https://github.com/skupperproject/skupper/releases)

Code blocks (9):
- `bash`
- `bash`
- `unspecified`
- `bash`
- `bash`
- `bash`
- `unspecified`
- `unspecified`
- `unspecified`

## `human/skupper-docs/input/kube-cli/index.md`

Headings (1):
- # Overview of Skupper CLI on Kubernetes

Links (0):
- None

Code blocks (0):
- None

## `human/skupper-docs/input/kube-cli/service-exposure.md`

Headings (3):
- # Exposing services on the application network using the CLI
- ## Creating a connector using the CLI
- ## Creating a listener using the CLI

Links (0):
- None

Code blocks (5):
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`

## `human/skupper-docs/input/kube-cli/site-configuration.md`

Headings (5):
- # Creating a site on Kubernetes using the Skupper CLI
- ## Checking the Skupper CLI
- ## Creating a simple site using the CLI on Kubernetes
- ## Creating a high availability site using the CLI on Kubernetes
- ## Deleting a site using the CLI on Kubernetes

Links (3):
- [Installing Skupper](https://skupper.io/releases/index.html)
- [Pod Quality of Service Classes](https://kubernetes.io/docs/concepts/workloads/pods/pod-qos/)
- [Setting site resources](../kube-yaml/site-configuration.html#kube-site-resources-yaml)

Code blocks (9):
- `unspecified`
- `unspecified`
- `bash`
- `bash`
- `bash`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`

## `human/skupper-docs/input/kube-cli/site-linking.md`

Headings (6):
- # Linking sites on Kubernetes using the Skupper CLI
- ## Linking sites using a token
- ## Linking sites using a  resource
- ## Linking sites through an HTTP proxy
- ## Using custom certificates
- ## Specifying link cost

Links (0):
- None

Code blocks (20):
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`

## `human/skupper-docs/input/kube-yaml/custom-certs.md`

Headings (3):
- # Linking sites using custom certificates
- ## Linking sites using a custom , and custom certificates
- ## Linking sites using  resources and custom certificates

Links (0):
- None

Code blocks (12):
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`

## `human/skupper-docs/input/kube-yaml/custom-labels.md`

Headings (11):
- # Propagating custom labels and annotations using YAML
- ## Creating a label template using YAML
- ## Controlling label template scope
- ## Filtering label templates by resource type
- ## Excluding specific keys from propagation
- ## Using multiple label templates
- ## Managing label template lifecycle
- ## Label template reference
- ### Affected resources
- ### ConfigMap data fields
- ### Complete example

Links (2):
- [Kubernetes label selector syntax](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#label-selectors)
- [Kubernetes label selector syntax](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#label-selectors)

Code blocks (10):
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`
- `yaml`

## `human/skupper-docs/input/kube-yaml/index.md`

Headings (1):
- # Overview of using YAML on Kubernetes

Links (0):
- None

Code blocks (0):
- None

## `human/skupper-docs/input/kube-yaml/service-exposure.md`

Headings (5):
- # Exposing services on the application network using YAML
- ## Creating a connector using YAML
- ## Creating a listener using YAML
- ## Creating a multi-key listener using YAML
- ## Creating a connector for a different namespace using YAML

Links (1):
- [Creating a connector using YAML](#kube-creating-connector-yaml)

Code blocks (11):
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`

## `human/skupper-docs/input/kube-yaml/site-configuration.md`

Headings (4):
- # Creating a site on Kubernetes using YAML
- ## Creating a simple site on Kubernetes using YAML
- ## Creating a high availability site using YAML
- ## Setting site resources

Links (3):
- [Pod Quality of Service Classes](https://kubernetes.io/docs/concepts/workloads/pods/pod-qos/)
- [Setting site resources](#kube-site-resources-yaml)
- [Setting site resources](#kube-site-resources-yaml)

Code blocks (10):
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`

## `human/skupper-docs/input/kube-yaml/site-linking.md`

Headings (4):
- # Linking sites on Kubernetes using YAML
- ## Linking sites using  and  resources
- ## Specifying link cost using YAML
- ## Using custom certificates

Links (0):
- None

Code blocks (12):
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`
- `yaml`
- `bash`
- `unspecified`
- `unspecified`
- `bash`
- `bash`

## `human/skupper-docs/input/overview/connectivity.md`

Headings (1):
- # Skupper connectivity

Links (0):
- None

Code blocks (0):
- None

## `human/skupper-docs/input/overview/index.md`

Headings (4):
- # Skupper overview
- ## Application Networks
- ## Skupper routers
- ## Skupper

Links (0):
- None

Code blocks (0):
- None

## `human/skupper-docs/input/overview/load-balancing.md`

Headings (3):
- # Skupper load balancing and failover
- ## Preferred approach: Multi-key listeners
- ## Alternative: Link cost

Links (0):
- None

Code blocks (0):
- None

## `human/skupper-docs/input/overview/migrating.md`

Headings (4):
- # Migrating from Skupper v1
- ## Creating sites
- ## Linking sites
- ## Exposing services

Links (0):
- None

Code blocks (7):
- `v1`
- `v2`
- `v1`
- `v2`
- `v1`
- `v2`
- `v2`

## `human/skupper-docs/input/overview/resources.md`

Headings (7):
- # Skupper resources on Kubernetes
- ## Custom resource definitions
- ## Service accounts, roles and role bindings
- ## Deployments
- ## ConfigMaps
- ## Secrets
- ## Services

Links (0):
- None

Code blocks (0):
- None

## `human/skupper-docs/input/overview/routing.md`

Headings (1):
- # Skupper routing

Links (0):
- None

Code blocks (0):
- None

## `human/skupper-docs/input/overview/security.md`

Headings (1):
- # Skupper security

Links (0):
- None

Code blocks (0):
- None

## `human/skupper-docs/input/refdog/commands/connector/create.md`

Headings (4):
- # Connector create command
- ## Examples
- ## Primary options
- ## Global options

Links (0):
- None

Code blocks (2):
- `shell`
- `console`

## `human/skupper-docs/input/refdog/commands/connector/delete.md`

Headings (4):
- # Connector delete command
- ## Examples
- ## Primary options
- ## Global options

Links (0):
- None

Code blocks (2):
- `shell`
- `console`

## `human/skupper-docs/input/refdog/commands/connector/generate.md`

Headings (4):
- # Connector generate command
- ## Examples
- ## Primary options
- ## Global options

Links (0):
- None

Code blocks (2):
- `shell`
- `console`

## `human/skupper-docs/input/refdog/commands/connector/index.md`

Headings (2):
- # Connector command
- ## Subcommands

Links (0):
- None

Code blocks (1):
- `shell`

## `human/skupper-docs/input/refdog/commands/connector/status.md`

Headings (4):
- # Connector status command
- ## Examples
- ## Primary options
- ## Global options

Links (0):
- None

Code blocks (2):
- `shell`
- `console`

## `human/skupper-docs/input/refdog/commands/connector/update.md`

Headings (4):
- # Connector update command
- ## Examples
- ## Primary options
- ## Global options

Links (0):
- None

Code blocks (2):
- `shell`
- `console`

## `human/skupper-docs/input/refdog/commands/debug/check.md`

Headings (3):
- # Debug check command
- ## Primary options
- ## Global options

Links (0):
- None

Code blocks (1):
- `shell`

## `human/skupper-docs/input/refdog/commands/debug/dump.md`

Headings (4):
- # Debug dump command
- ## Examples
- ## Primary options
- ## Global options

Links (0):
- None

Code blocks (2):
- `shell`
- `console`

## `human/skupper-docs/input/refdog/commands/debug/index.md`

Headings (2):
- # Debug command
- ## Subcommands

Links (0):
- None

Code blocks (1):
- `shell`

## `human/skupper-docs/input/refdog/commands/index.md`

Headings (13):
- # Skupper CLI commands
- ## Command index
- ## Overview
- #### Capabilities
- #### Usage
- #### Context
- #### Blocking
- #### Errors
- #### Resource commands
- #### Token commands
- #### System commands
- #### Debug commands
- #### Version command

Links (0):
- None

Code blocks (6):
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`

## `human/skupper-docs/input/refdog/commands/link/delete.md`

Headings (4):
- # Link delete command
- ## Examples
- ## Primary options
- ## Global options

Links (0):
- None

Code blocks (2):
- `shell`
- `console`

## `human/skupper-docs/input/refdog/commands/link/generate.md`

Headings (4):
- # Link generate command
- ## Examples
- ## Primary options
- ## Global options

Links (0):
- None

Code blocks (2):
- `shell`
- `console`

## `human/skupper-docs/input/refdog/commands/link/index.md`

Headings (2):
- # Link command
- ## Subcommands

Links (0):
- None

Code blocks (1):
- `shell`

## `human/skupper-docs/input/refdog/commands/link/status.md`

Headings (4):
- # Link status command
- ## Examples
- ## Primary options
- ## Global options

Links (0):
- None

Code blocks (2):
- `shell`
- `console`

## `human/skupper-docs/input/refdog/commands/link/update.md`

Headings (4):
- # Link update command
- ## Examples
- ## Primary options
- ## Global options

Links (0):
- None

Code blocks (2):
- `shell`
- `console`

## `human/skupper-docs/input/refdog/commands/listener/create.md`

Headings (4):
- # Listener create command
- ## Examples
- ## Primary options
- ## Global options

Links (0):
- None

Code blocks (2):
- `shell`
- `console`

## `human/skupper-docs/input/refdog/commands/listener/delete.md`

Headings (4):
- # Listener delete command
- ## Examples
- ## Primary options
- ## Global options

Links (0):
- None

Code blocks (2):
- `shell`
- `console`

## `human/skupper-docs/input/refdog/commands/listener/generate.md`

Headings (4):
- # Listener generate command
- ## Examples
- ## Primary options
- ## Global options

Links (0):
- None

Code blocks (2):
- `shell`
- `console`

## `human/skupper-docs/input/refdog/commands/listener/index.md`

Headings (2):
- # Listener command
- ## Subcommands

Links (0):
- None

Code blocks (1):
- `shell`

## `human/skupper-docs/input/refdog/commands/listener/status.md`

Headings (4):
- # Listener status command
- ## Examples
- ## Primary options
- ## Global options

Links (0):
- None

Code blocks (2):
- `shell`
- `console`

## `human/skupper-docs/input/refdog/commands/listener/update.md`

Headings (4):
- # Listener update command
- ## Examples
- ## Primary options
- ## Global options

Links (0):
- None

Code blocks (2):
- `shell`
- `console`

## `human/skupper-docs/input/refdog/commands/site/create.md`

Headings (5):
- # Site create command
- ## Examples
- ## Primary options
- ## Global options
- ## Errors

Links (0):
- None

Code blocks (2):
- `shell`
- `console`

## `human/skupper-docs/input/refdog/commands/site/delete.md`

Headings (5):
- # Site delete command
- ## Examples
- ## Primary options
- ## Global options
- ## Errors

Links (0):
- None

Code blocks (2):
- `shell`
- `console`

## `human/skupper-docs/input/refdog/commands/site/generate.md`

Headings (4):
- # Site generate command
- ## Examples
- ## Primary options
- ## Global options

Links (0):
- None

Code blocks (2):
- `shell`
- `console`

## `human/skupper-docs/input/refdog/commands/site/index.md`

Headings (2):
- # Site command
- ## Subcommands

Links (0):
- None

Code blocks (1):
- `shell`

## `human/skupper-docs/input/refdog/commands/site/reload.md`

Headings (2):
- # Site reload command
- ## Usage

Links (0):
- None

Code blocks (1):
- `shell`

## `human/skupper-docs/input/refdog/commands/site/start.md`

Headings (2):
- # Site start command
- ## Usage

Links (0):
- None

Code blocks (1):
- `shell`

## `human/skupper-docs/input/refdog/commands/site/status.md`

Headings (4):
- # Site status command
- ## Examples
- ## Primary options
- ## Global options

Links (0):
- None

Code blocks (2):
- `shell`
- `console`

## `human/skupper-docs/input/refdog/commands/site/stop.md`

Headings (2):
- # Site stop command
- ## Usage

Links (0):
- None

Code blocks (1):
- `shell`

## `human/skupper-docs/input/refdog/commands/site/update.md`

Headings (5):
- # Site update command
- ## Examples
- ## Primary options
- ## Global options
- ## Errors

Links (0):
- None

Code blocks (2):
- `shell`
- `console`

## `human/skupper-docs/input/refdog/commands/system/apply.md`

Headings (3):
- # System apply command
- ## Primary options
- ## Global options

Links (0):
- None

Code blocks (1):
- `shell`

## `human/skupper-docs/input/refdog/commands/system/delete.md`

Headings (3):
- # System delete command
- ## Primary options
- ## Global options

Links (0):
- None

Code blocks (1):
- `shell`

## `human/skupper-docs/input/refdog/commands/system/generate-bundle.md`

Headings (3):
- # System generate-bundle command
- ## Primary options
- ## Global options

Links (0):
- None

Code blocks (1):
- `shell`

## `human/skupper-docs/input/refdog/commands/system/index.md`

Headings (2):
- # System command
- ## Subcommands

Links (0):
- None

Code blocks (1):
- `shell`

## `human/skupper-docs/input/refdog/commands/system/install.md`

Headings (3):
- # System install command
- ## Primary options
- ## Global options

Links (0):
- None

Code blocks (1):
- `shell`

## `human/skupper-docs/input/refdog/commands/system/reload.md`

Headings (3):
- # System reload command
- ## Primary options
- ## Global options

Links (0):
- None

Code blocks (1):
- `shell`

## `human/skupper-docs/input/refdog/commands/system/start.md`

Headings (3):
- # System start command
- ## Primary options
- ## Global options

Links (0):
- None

Code blocks (1):
- `shell`

## `human/skupper-docs/input/refdog/commands/system/stop.md`

Headings (3):
- # System stop command
- ## Primary options
- ## Global options

Links (0):
- None

Code blocks (1):
- `shell`

## `human/skupper-docs/input/refdog/commands/system/uninstall.md`

Headings (3):
- # System uninstall command
- ## Primary options
- ## Global options

Links (0):
- None

Code blocks (1):
- `shell`

## `human/skupper-docs/input/refdog/commands/token/index.md`

Headings (2):
- # Token command
- ## Subcommands

Links (0):
- None

Code blocks (1):
- `shell`

## `human/skupper-docs/input/refdog/commands/token/issue.md`

Headings (5):
- # Token issue command
- ## Examples
- ## Primary options
- ## Global options
- ## Errors

Links (0):
- None

Code blocks (2):
- `shell`
- `console`

## `human/skupper-docs/input/refdog/commands/token/redeem.md`

Headings (4):
- # Token redeem command
- ## Examples
- ## Primary options
- ## Global options

Links (0):
- None

Code blocks (2):
- `shell`
- `console`

## `human/skupper-docs/input/refdog/commands/version.md`

Headings (4):
- # Version command
- ## Examples
- ## Primary options
- ## Global options

Links (0):
- None

Code blocks (2):
- `shell`
- `console`

## `human/skupper-docs/input/refdog/concepts/access-token.md`

Headings (1):
- # Access token concept

Links (1):
- [link](link.html)

Code blocks (0):
- None

## `human/skupper-docs/input/refdog/concepts/application.md`

Headings (1):
- # Application concept

Links (2):
- [components](component.html)
- [network](network.html)

Code blocks (0):
- None

## `human/skupper-docs/input/refdog/concepts/component.md`

Headings (1):
- # Component concept

Links (2):
- [application](application.html)
- [workloads](workload.html)

Code blocks (0):
- None

## `human/skupper-docs/input/refdog/concepts/connector.md`

Headings (1):
- # Connector concept

Links (4):
- [workload](workload.html)
- [listeners](listener.html)
- [sites](site.html)
- [routing keys](routing-key.html)

Code blocks (0):
- None

## `human/skupper-docs/input/refdog/concepts/index.md`

Headings (7):
- # Skupper concepts
- ## Concept index
- ## Overview
- #### Sites
- #### Networks
- #### Services
- #### Applications

Links (11):
- [site](site.html)
- [platform](platform.html)
- [workloads](workload.html)
- [links](link.html)
- [network](network.html)
- [access tokens](access-token.html)
- [listeners](listener.html)
- [connectors](connector.html)
- [routing key](routing-key.html)
- [application](application.html)
- [components](component.html)

Code blocks (0):
- None

## `human/skupper-docs/input/refdog/concepts/link.md`

Headings (1):
- # Link concept

Links (3):
- [sites](site.html)
- [network](network.html)
- [access tokens](access-token.html)

Code blocks (0):
- None

## `human/skupper-docs/input/refdog/concepts/listener.md`

Headings (1):
- # Listener concept

Links (3):
- [connectors](connector.html)
- [sites](site.html)
- [routing keys](routing-key.html)

Code blocks (0):
- None

## `human/skupper-docs/input/refdog/concepts/multi-key-listener.md`

Headings (6):
- # Multi-key-listener concept
- ## Strategies
- ### Priority strategy
- ### Weighted strategy
- ## Use cases
- ## Multi-key listeners and link cost

Links (4):
- [connectors](connector.html)
- [sites](site.html)
- [routing keys](routing-key.html)
- [listener](listener.html)

Code blocks (0):
- None

## `human/skupper-docs/input/refdog/concepts/network.md`

Headings (1):
- # Network concept

Links (2):
- [sites](site.html)
- [links](link.html)

Code blocks (0):
- None

## `human/skupper-docs/input/refdog/concepts/platform.md`

Headings (1):
- # Platform concept

Links (2):
- [workloads](workload.html)
- [sites](site.html)

Code blocks (0):
- None

## `human/skupper-docs/input/refdog/concepts/routing-key.md`

Headings (1):
- # Routing key concept

Links (2):
- [listeners](listener.html)
- [connectors](connector.html)

Code blocks (0):
- None

## `human/skupper-docs/input/refdog/concepts/site.md`

Headings (1):
- # Site concept

Links (4):
- [network](network.html)
- [workloads](workload.html)
- [links](link.html)
- [platforms](platform.html)

Code blocks (0):
- None

## `human/skupper-docs/input/refdog/concepts/workload.md`

Headings (1):
- # Workload concept

Links (5):
- [platform](platform.html)
- [site](site.html)
- [network](network.html)
- [connectors](connector.html)
- [connectors](connector.html)

Code blocks (0):
- None

## `human/skupper-docs/input/refdog/index.md`

Headings (1):
- # Refdog

Links (3):
- [Skupper concepts](concepts/index.html)
- [API reference](resources/index.html)
- [CLI reference](commands/index.html)

Code blocks (0):
- None

## `human/skupper-docs/input/refdog/resources/access-grant.md`

Headings (4):
- # AccessGrant resource
- ## Metadata properties
- ## Spec properties
- ## Status properties

Links (0):
- None

Code blocks (0):
- None

## `human/skupper-docs/input/refdog/resources/access-token.md`

Headings (4):
- # AccessToken resource
- ## Metadata properties
- ## Spec properties
- ## Status properties

Links (0):
- None

Code blocks (0):
- None

## `human/skupper-docs/input/refdog/resources/attached-connector-binding.md`

Headings (4):
- # AttachedConnectorBinding resource
- ## Metadata properties
- ## Spec properties
- ## Status properties

Links (0):
- None

Code blocks (0):
- None

## `human/skupper-docs/input/refdog/resources/attached-connector.md`

Headings (4):
- # AttachedConnector resource
- ## Metadata properties
- ## Spec properties
- ## Status properties

Links (0):
- None

Code blocks (0):
- None

## `human/skupper-docs/input/refdog/resources/connector.md`

Headings (5):
- # Connector resource
- ## Examples
- ## Metadata properties
- ## Spec properties
- ## Status properties

Links (2):
- [listeners](listener.html)
- [sites](site.html)

Code blocks (1):
- `yaml`

## `human/skupper-docs/input/refdog/resources/index.md`

Headings (9):
- # Skupper API resources
- ## Resource index
- ## Overview
- #### Capabilities
- #### Controller
- #### Operations
- #### Primary resources
- #### Site linking resources
- #### Service exposure resources

Links (12):
- [Site](site.html)
- [Link](link.html)
- [Listener](listener.html)
- [Connector](connector.html)
- [Link](link.html)
- [AccessGrant](access-grant.html)
- [AccessToken](access-token.html)
- [RouterAccess](router-access.html)
- [Listener](listener.html)
- [Connector](connector.html)
- [AttachedConnector](attached-connector.html)
- [AttachedConnectorBinding](attached-connector-binding.html)

Code blocks (0):
- None

## `human/skupper-docs/input/refdog/resources/link.md`

Headings (4):
- # Link resource
- ## Metadata properties
- ## Spec properties
- ## Status properties

Links (1):
- [sites](site.html)

Code blocks (0):
- None

## `human/skupper-docs/input/refdog/resources/listener.md`

Headings (5):
- # Listener resource
- ## Examples
- ## Metadata properties
- ## Spec properties
- ## Status properties

Links (2):
- [connectors](connector.html)
- [sites](site.html)

Code blocks (1):
- `yaml`

## `human/skupper-docs/input/refdog/resources/multi-key-listener.md`

Headings (5):
- # MultiKeyListener resource
- ## Examples
- ## Metadata properties
- ## Spec properties
- ## Status properties

Links (3):
- [sites](site.html)
- [connectors](connector.html)
- [listener](listener.html)

Code blocks (2):
- `yaml`
- `yaml`

## `human/skupper-docs/input/refdog/resources/router-access.md`

Headings (4):
- # RouterAccess resource
- ## Metadata properties
- ## Spec properties
- ## Status properties

Links (0):
- None

Code blocks (0):
- None

## `human/skupper-docs/input/refdog/resources/site.md`

Headings (5):
- # Site resource
- ## Examples
- ## Metadata properties
- ## Spec properties
- ## Status properties

Links (1):
- [links](link.html)

Code blocks (2):
- `yaml`
- `yaml`

## `human/skupper-docs/input/refdog/topics/application-tls.md`

Headings (1):
- # Application TLS

Links (0):
- None

Code blocks (0):
- None

## `human/skupper-docs/input/refdog/topics/attached-connectors.md`

Headings (1):
- # Attached connectors

Links (0):
- None

Code blocks (0):
- None

## `human/skupper-docs/input/refdog/topics/components.md`

Headings (1):
- # Components

Links (0):
- None

Code blocks (0):
- None

## `human/skupper-docs/input/refdog/topics/controller-configuration.md`

Headings (1):
- # Controller configuration

Links (0):
- None

Code blocks (0):
- None

## `human/skupper-docs/input/refdog/topics/debug-dumps.md`

Headings (1):
- # Debug dumps

Links (0):
- None

Code blocks (1):
- `unspecified`

## `human/skupper-docs/input/refdog/topics/high-availability.md`

Headings (1):
- # High availability

Links (0):
- None

Code blocks (0):
- None

## `human/skupper-docs/input/refdog/topics/index.md`

Headings (1):
- # Topics

Links (0):
- None

Code blocks (0):
- None

## `human/skupper-docs/input/refdog/topics/individual-pod-services.md`

Headings (1):
- # Individual pod services

Links (0):
- None

Code blocks (0):
- None

## `human/skupper-docs/input/refdog/topics/large-networks.md`

Headings (1):
- # Large networks

Links (0):
- None

Code blocks (0):
- None

## `human/skupper-docs/input/refdog/topics/load-balancing.md`

Headings (1):
- # Load balancing

Links (0):
- None

Code blocks (0):
- None

## `human/skupper-docs/input/refdog/topics/resource-settings.md`

Headings (1):
- # Resource settings

Links (0):
- None

Code blocks (0):
- None

## `human/skupper-docs/input/refdog/topics/resource-status.md`

Headings (1):
- # Resource status

Links (0):
- None

Code blocks (0):
- None

## `human/skupper-docs/input/refdog/topics/router-tls.md`

Headings (1):
- # Router TLS

Links (0):
- None

Code blocks (0):
- None

## `human/skupper-docs/input/refdog/topics/service-exposure.md`

Headings (1):
- # Service exposure

Links (0):
- None

Code blocks (0):
- None

## `human/skupper-docs/input/refdog/topics/site-configuration.md`

Headings (1):
- # Site configuration

Links (0):
- None

Code blocks (0):
- None

## `human/skupper-docs/input/refdog/topics/site-linking.md`

Headings (2):
- # Site linking
- ## Using kubectl to generate an access token from an access grant

Links (0):
- None

Code blocks (1):
- `sh`

## `human/skupper-docs/input/refdog/topics/skupper-overview.md`

Headings (1):
- # Skupper overview

Links (0):
- None

Code blocks (0):
- None

## `human/skupper-docs/input/refdog/topics/system-namespaces.md`

Headings (1):
- # System namespaces

Links (0):
- None

Code blocks (0):
- None

## `human/skupper-docs/input/refdog/topics/system-tls-credentials.md`

Headings (1):
- # System TLS credentials

Links (0):
- None

Code blocks (0):
- None

## `human/skupper-docs/input/system-cli/index.md`

Headings (1):
- # Overview of Skupper CLI on local systems

Links (0):
- None

Code blocks (0):
- None

## `human/skupper-docs/input/system-cli/service-exposure.md`

Headings (3):
- # Exposing services on the application network using the CLI
- ## Creating a connector using the CLI
- ## Creating a listener using the CLI

Links (0):
- None

Code blocks (4):
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`

## `human/skupper-docs/input/system-cli/site-configuration.md`

Headings (5):
- # Creating a site on a local system using the Skupper CLI
- ## Checking the Skupper CLI and environment
- ## Creating a simple site using the CLI on local systems
- ## Deleting a site using the CLI on local systems
- ## Creating a site bundle using the CLI on local systems

Links (1):
- [Installing Skupper](https://skupper.io/releases/index.html)

Code blocks (12):
- `unspecified`
- `unspecified`
- `bash`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`

## `human/skupper-docs/input/system-cli/site-linking.md`

Headings (3):
- # Linking sites on local systems using the Skupper CLI
- ## Linking to Kubernetes sites using a token
- ## Linking sites using a  resource

Links (0):
- None

Code blocks (10):
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`

## `human/skupper-docs/input/system-yaml/index.md`

Headings (1):
- # Overview of using YAML on local systems

Links (0):
- None

Code blocks (0):
- None

## `human/skupper-docs/input/system-yaml/service-exposure.md`

Headings (4):
- # Exposing services on the application network using YAML
- ## Creating a connector using YAML
- ## Creating a listener using YAML
- ## Creating a multi-key listener using YAML

Links (1):
- [Creating a connector using YAML](#system-creating-connector-yaml)

Code blocks (6):
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`

## `human/skupper-docs/input/system-yaml/site-configuration.md`

Headings (2):
- # Creating a site on local systems using YAML
- ## Creating a simple site on local systems using YAML

Links (0):
- None

Code blocks (3):
- `unspecified`
- `unspecified`
- `unspecified`

## `human/skupper-docs/input/system-yaml/site-linking.md`

Headings (2):
- # Linking sites on local systems using YAML
- ## Linking sites using a  resource

Links (0):
- None

Code blocks (4):
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`

## `human/skupper-docs/input/troubleshooting/index.md`

Headings (5):
- # Troubleshooting an application network
- ## Checking sites
- ## Checking links
- ## Creating a Skupper debug tar file
- ## Troubleshooting the Dynamic System Controller

Links (0):
- None

Code blocks (9):
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`

## `human/skupper-docs/refdog/README.md`

Headings (15):
- # Refdog
- ## What this directory is for
- ## Pipeline
- ## What actually generates markdown
- ## Current source of truth
- ### Commands
- ### Resources
- ## Normal user workflow
- ## Build commands
- ### Rebuild only refdog markdown
- ### Rebuild MkDocs docs
- ### Rebuild the website variant
- ## What the user should edit
- ## Current caveat
- ## Optional background docs

Links (0):
- None

Code blocks (10):
- `bash`
- `unspecified`
- `unspecified`
- `bash`
- `bash`
- `bash`
- `bash`
- `bash`
- `bash`
- `bash`

## `human/skupper-docs/refdog/config/commands/overview.md`

Headings (11):
- ## Overview
- #### Capabilities
- #### Usage
- #### Context
- #### Blocking
- #### Errors
- #### Resource commands
- #### Token commands
- #### System commands
- #### Debug commands
- #### Version command

Links (0):
- None

Code blocks (6):
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`

## `human/skupper-docs/refdog/config/concepts/overview.md`

Headings (5):
- ## Overview
- #### Sites
- #### Networks
- #### Services
- #### Applications

Links (11):
- [site](site.html)
- [platform](platform.html)
- [workloads](workload.html)
- [links](link.html)
- [network](network.html)
- [access tokens](access-token.html)
- [listeners](listener.html)
- [connectors](connector.html)
- [routing key](routing-key.html)
- [application](application.html)
- [components](component.html)

Code blocks (0):
- None

## `human/skupper-docs/refdog/config/resources/overview.md`

Headings (7):
- ## Overview
- #### Capabilities
- #### Controller
- #### Operations
- #### Primary resources
- #### Site linking resources
- #### Service exposure resources

Links (12):
- [Site](site.html)
- [Link](link.html)
- [Listener](listener.html)
- [Connector](connector.html)
- [Link](link.html)
- [AccessGrant](access-grant.html)
- [AccessToken](access-token.html)
- [RouterAccess](router-access.html)
- [Listener](listener.html)
- [Connector](connector.html)
- [AttachedConnector](attached-connector.html)
- [AttachedConnectorBinding](attached-connector-binding.html)

Code blocks (0):
- None

## `human/skupper-docs/refdog/crd-generation-proposal.md`

Headings (28):
- # Proposal: Generate Documentation Directly from CRDs
- ## Executive Summary
- ## Current Architecture
- ### What We Have Now
- ## Proposed Architecture
- ### Option 1: Pure CRD Generation (Recommended)
- ### Option 2: Hybrid Approach
- ## What CRDs Already Provide
- ### ✅ Available in CRDs
- ### ❌ Missing from CRDs (Need to Add)
- ## Implementation Approaches
- ### Approach A: Use CRD Annotations (Kubernetes-Native)
- ### Approach B: Separate Metadata Files (Recommended)
- ### Approach C: Examples in Separate Directory
- ## Recommended Implementation Plan
- ### Phase 1: Enhance CRD Descriptions (If Needed)
- ### Phase 2: Create Minimal Metadata Files
- ### Phase 3: Modify Generation Code
- ### Phase 4: Migration
- ### Phase 5: Update Workflow
- ## Migration Script
- ## Benefits of This Approach
- ## Risks and Mitigations
- ### Risk 1: CRD Descriptions Not Documentation-Quality
- ### Risk 2: Loss of Documentation Control
- ### Risk 3: Breaking Existing Workflow
- ## Estimated Effort
- ## Recommendation

Links (0):
- None

Code blocks (12):
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`
- `yaml`
- `yaml`
- `unspecified`
- `yaml`
- `python`
- `python`

## `human/skupper-docs/refdog/resources.md`

Headings (36):
- # Custom Resource (CR) Management Processes
- ## Overview
- ## Architecture
- ### Source Files
- #### 1. YAML Configuration Files ()
- #### 2. Shared Properties ()
- #### 3. Overview Documentation ()
- #### 4. CRD Files ()
- ### Generated Files
- #### Generated Markdown ()
- ## YAML Configuration Structure
- ### Property Groups
- ### Property Attributes
- ## Processes
- ### 1. Updating CRDs from Skupper Repository
- ### 2. Generating Documentation from YAML
- ### 3. Validation and Consistency Checking
- ### 4. Syncing CRD Descriptions to YAML Configs
- ### 5. Adding a New Resource
- ### 6. Updating an Existing Resource
- ### 7. Updating Shared Properties
- ### 8. Full Documentation Build and Test
- ## File Relationships
- ## Code Components
- ### Python Modules
- #### 
- #### 
- #### 
- ### Plano Commands
- ## Best Practices
- ### Documentation Maintenance
- ### Workflow
- ## Troubleshooting
- ### Common Issues
- ## Future Enhancements
- ## References

Links (3):
- [https://github.com/skupperproject/skupper](https://github.com/skupperproject/skupper)
- [https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/)
- [https://kubernetes.io/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definitions/#validation](https://kubernetes.io/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definitions/#validation)

Code blocks (13):
- `yaml`
- `unspecified`
- `unspecified`
- `yaml`
- `yaml`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`
- `unspecified`

## `human/skupper-docs/refdog/todo.md`

Headings (8):
- # Refdog TODO
- ## Outstanding work
- ### MkDocs source warnings
- ### Refdog link model
- ### Topic pages
- ### Tree handoff
- ### Docs cleanup
- ## Suggested next steps

Links (0):
- None

Code blocks (0):
- None

## `human/skupper-docs/style.md`

Headings (10):
- # Skupper Documentation Style Guide
- ## Numbered Lists and Code Blocks
- ### Indentation Requirements
- ### Formatting Shell Commands
- ### Formatting Command Output
- ### Multiple Command/Output Pairs
- ### Commands Without Output
- ### YAML and Configuration Files
- ### Reference Documentation (refdog directory only)
- ### Key Differences: Procedural vs Reference

Links (0):
- None

Code blocks (0):
- None

## `human/skupper-docs/test-relative-links.md`

Headings (4):
- # Alternative: Use Relative Links
- ## Try Relative Links Instead
- ## Quick Test
- ## Or Try Without Prefix At All

Links (0):
- None

Code blocks (3):
- `html`
- `html`
- `bash`
