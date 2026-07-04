---
type: Workflow
title: Skupper example applications
id: skupper-workflow-examples
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source_repos:
  - https://github.com/skupperproject/skupper-example-hello-world.git
  - https://github.com/skupperproject/skupper-example-grpc.git
source_branch: main
source_commits:
  skupper-example-hello-world: 4f190d39c213064d5da1269ddef1847a4ad75481
  skupper-example-grpc: a40e5c41b2b119616c8a715d3bff55a64e30eb1a
source_paths:
  - human/skupper-example-hello-world/README.md
  - human/skupper-example-grpc/README.md
scenario_links:
  hello_world: https://pwright.github.io/webernetes/?scenario=skupper-plain
  grpc: https://pwright.github.io/webernetes/?scenario=skupper-grpc
tags:
  - skupper
  - examples
  - webernetes
  - kubernetes
related:
  - skupper-concept-listener
  - skupper-concept-connector
timestamp: 2026-07-03T18:10:09Z
---

# Skupper example applications

The Skupper example repositories show how an application network connects services across Kubernetes clusters. The Hello World example is the minimal HTTP path; the gRPC example is a larger multi-service application that uses Skupper resources to connect gRPC services across sites.

## Example scenarios

| Example | What it shows | Interactive scenario |
| --- | --- | --- |
| Hello World | A frontend service in one cluster calls a backend service in another cluster without exposing the backend to the public internet. | [skupper-plain](https://pwright.github.io/webernetes/?scenario=skupper-plain) |
| gRPC / Online Boutique | A multi-service gRPC application is split across multiple Kubernetes clusters and connected through a Skupper application network. | [skupper-grpc](https://pwright.github.io/webernetes/?scenario=skupper-grpc) |

## Hello World

The Hello World example is the smallest useful Skupper application pattern. It has a frontend service and a backend service. The backend exposes an HTTP endpoint, and the frontend calls that backend to fetch greetings.

Skupper's role is to let the frontend and backend run in different clusters while preserving service connectivity. The backend can stay private; the frontend reaches it through the application network.

Source: `human/skupper-example-hello-world/README.md`

Interactive view: <https://pwright.github.io/webernetes/?scenario=skupper-plain>

## gRPC / Online Boutique

The gRPC example uses the Online Boutique microservices demo. It deploys a subset of the application's gRPC-based microservices across multiple Kubernetes clusters, creates Skupper sites, links the sites, and then accesses the Boutique Shop application through the connected network.

This example is useful when the reader needs to understand Skupper beyond a two-service demo. It shows service connectivity as part of a larger distributed application rather than as a single frontend-to-backend call.

Source: `human/skupper-example-grpc/README.md`

Interactive view: <https://pwright.github.io/webernetes/?scenario=skupper-grpc>

## How to use these examples

For step-by-step tutorials and installation guides, see:
- [Skupper overview](../input/overview/index.md)
- [Installation guide](../input/install/index.md)
- [Getting started with Kubernetes CLI](../input/kube-cli/index.md)

Use Hello World first when validating the basic Skupper flow:

```text
frontend -> listener -> Skupper application network -> connector -> backend
```

Use the gRPC example when validating a richer multi-site application:

```text
user -> frontend/API entry point -> Skupper application network -> gRPC services across sites
```

Both examples are source snapshots under `human/`, so treat them as read-only inputs. Generate or promote OKF notes from them into `generated/` or `reviewed/` rather than editing the snapshots directly.
