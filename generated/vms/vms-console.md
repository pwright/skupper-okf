---
type: VmsLandscapePage
title: "VMS Console"
id: vms-console
status: generated
owner: agent
generated_by: generate-vms-landscape-pages.py
reviewed: false
confidence: stub
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/vms/vms-console
tags:
  - vms
  - vms-landscape
timestamp: 2026-08-26T16:01:08Z
---
# VMS Console

Web UI for managing backbones, VANs, invitations, and members - administrative interface

## Appears in

- [VMS Control & Data Plane Architecture](./vms-overview.md) / Management Plane (Centralized)

## Topics

### Dependencies

- [Management Controller](./management-controller.md)


## VMS Console

A React web application built with IBM Carbon Design System for managing VMS backbones, VANs, and certificates.

### Features

- **Carbon Design System** - Professional UI components with IBM's design language
- **Hierarchical Navigation** - Organized menu structure with expandable sections
- **Responsive Layout** - Mobile-friendly design using Carbon's grid system
- **Custom Theming** - Configurable Carbon theme (currently g100 dark theme)
- **React Router** - Clean URL structure with nested routes

### Navigation Structure

- **Dashboard** - Main overview page
- **Backbones** - Backbone configurations, sites, deployment
- **VANs** - Virtual application networks
- **TLS** - TLS certificate management

### Architecture

The console is served by the management controller:

**Production Mode** (`NODE_ENV=production`):
- Serves prebuilt static files from `components/console/dist`
- Requires running `pnpm --filter vms-console build` after changes

**Development Mode** (default):
- Runs Vite dev server inside management controller process
- Hot module replacement (HMR) and live reload
- API routes served by same Express app

### Technology Stack

- **react** & **react-dom** - Core React libraries
- **react-router-dom** - Client-side routing
- **@carbon/react** - Carbon Design System React components
- **@carbon/icons-react** - Carbon icon library
- **sass** - CSS preprocessor for Carbon styles
- **vite** - Dev server and production bundling
- **ViteExpress** - Serves UI and API from same process

### Running the Console

From repository root:

```shell
pnpm install
cd components/management-controller
node index.js
```

The console is accessible at `http://localhost:8085` (default port).

## Source

Based on `human/vms/components/console/README.md`
