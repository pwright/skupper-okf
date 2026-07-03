---
type: Concept
title: Connector
id: skupper-concept-connector
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source_repo: https://github.com/skupperproject/skupper-docs.git
source_branch: main
source_commit: fdfd4594ade939dd2d756215e5f3afdb54190c44
source_paths:
  - human/input/refdog/concepts/connector.md
  - human/refdog/config/resources/connector.yaml
  - human/refdog/config/resources/attached-connector.yaml
  - human/refdog/config/resources/attached-connector-binding.yaml
  - human/input/refdog/topics/attached-connectors.md
  - human/input/kube-yaml/service-exposure.md
  - human/input/system-yaml/service-exposure.md
  - human/input/system-cli/service-exposure.md
  - human/refdog/config/commands/connector.yaml
human_context:
  - AttachedConnector should be treated as a connector type in this wiki model, not as a separate concept family.
tags:
  - skupper
  - service-exposure
  - routing-key
  - connector
  - attached-connector
related:
  - skupper-concept-listener
  - skupper-concept-routing-key
timestamp: 2026-07-03T14:45:49Z
---

# Connector

A Skupper connector is the network-side handle for a workload that should be reachable from other sites. The connector selects or addresses the local workload, assigns it a routing key, and lets matching listeners forward client connections to that workload through the Skupper application network.

## Outcome

A working connector makes a local workload consumable from remote listeners that use the same routing key.

```text
remote client -> listener -> matching routing key -> connector -> local workload
```

## Key ideas

- A site can have zero or more connectors.
- Each connector has a workload endpoint and a routing key.
- A service is usable when at least one connector and one listener share the same routing key.
- On Kubernetes, a connector usually selects workload pods with a label selector or workload reference.
- On Docker, Podman, and Linux, a connector usually addresses a local server by host and port.
- An attached connector is a connector variant for Kubernetes workloads in a peer namespace.

## Common fields

The Connector resource uses these core fields:

- `spec.routingKey`: the identifier that matches this connector to listener resources, usually in remote sites.
- `spec.port`: the target server port.
- `spec.selector`: a Kubernetes label selector for target pods.
- `spec.host`: a host name or address for a local server, used on Docker, Podman, Linux, and optionally Kubernetes.

When `--routing-key` is not specified in CLI workflows, the connector name is the default routing key. On Kubernetes, the connector name also defines the default pod selector when `--selector` and `--workload` are not specified.

## Creation paths

For Kubernetes-style YAML workflows, create a `Connector` resource and apply it through Skupper:

```yaml
apiVersion: skupper.io/v2alpha1
kind: Connector
metadata:
  name: backend
  namespace: east
spec:
  routingKey: backend
  selector: app=backend
  port: 8080
```

```bash
skupper system apply -f <filename>
```

For local CLI workflows, create a connector directly:

```bash
skupper connector create <name> <port> --routing-key <routing-key>
skupper system reload
```

On Kubernetes, the CLI can also select a workload explicitly:

```bash
skupper connector create backend 8080 --workload deployment/backend
```

## Connector variants

A standard connector is created in the site namespace and directly describes the workload to expose. An attached connector is still a connector in the wiki model: it exposes a workload from a peer namespace without requiring a separate site or inter-site link for that workload namespace.

Current Skupper source material describes this with two Kubernetes resources:

- `AttachedConnector`: created in the workload namespace. It selects the workload pods, sets the port, and names the site namespace it should attach to.
- `AttachedConnectorBinding`: created in the site namespace. It binds the attached connector to the site and controls the routing key.

The two resources must have matching names. The `AttachedConnector.spec.siteNamespace` and `AttachedConnectorBinding.spec.connectorNamespace` values must correspond. Attached connectors require Skupper to be deployed cluster-wide, and they are created with YAML resources rather than the `skupper connector` CLI.

Example shape:

```text
site namespace: AttachedConnectorBinding -- peer namespace: AttachedConnector -> workload pods
```

## Verify

Check connector status:

```bash
skupper connector status
```

Expected shape:

```text
NAME      STATUS  ROUTING-KEY  SELECTOR     HOST    PORT  LISTENERS
backend   Ready   backend      app=backend  <none>  8080  true
```

For attached connectors, check the binding from the site namespace:

```bash
kubectl get AttachedConnectorBinding
```

Expected shape:

```text
NAME      ROUTING KEY   CONNECTOR NAMESPACE   STATUS   HAS MATCHING LISTENER
backend   backend       attached              Ready    true
```

The service is not operational until the connector has at least one matching listener. In resource status, the relevant signals include `hasMatchingListener`, `selectedPods`, and `Ready`.

## Caveats

- A connector does not create a local client endpoint by itself; a listener with the same routing key is required.
- A routing key can match multiple connectors and multiple listeners.
- Attached connectors split responsibility: the workload namespace controls pod selection, while the site namespace controls the routing key.
- To expose one peer-namespace workload into multiple application networks, create multiple attached connectors and corresponding bindings.
- On local-system platforms, configuration changes may require `skupper system reload`.
