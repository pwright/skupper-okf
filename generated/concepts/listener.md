---
type: Concept
title: Listener
id: skupper-concept-listener
status: generated
owner: agent
generated_by: codex
reviewed: false
confidence: draft
source_repo: https://github.com/skupperproject/skupper-docs.git
source_branch: main
source_commit: fdfd4594ade939dd2d756215e5f3afdb54190c44
source_paths:
  - human/input/refdog/concepts/listener.md
  - human/refdog/config/concepts/listener.yaml
  - human/refdog/config/resources/listener.yaml
  - human/input/system-yaml/service-exposure.md
  - human/input/system-cli/service-exposure.md
  - human/refdog/config/commands/listener.yaml
human_context:
  - MultiKeyListener should be treated as a listener type in this wiki model, not as a separate concept family.
  - Multi-key listener behavior may become the default listener behavior in the future.
tags:
  - skupper
  - service-exposure
  - routing-key
  - listener
related:
  - skupper-concept-connector
  - skupper-concept-routing-key
timestamp: 2026-07-03T14:03:38Z
---

# Listener

A Skupper listener is the local endpoint that clients connect to when they want to consume a service exposed from another site. The listener is matched to one or more remote connectors by routing key, and Skupper routers forward matching client connections across the application network.

## Outcome

A working listener gives local clients a host and port for a remote service.

```text
local client -> listener host:port -> Skupper router -> matching routing key -> remote connector -> workload
```

## Key ideas

- A site can have zero or more listeners.
- Each listener has a local connection endpoint, defined by host and port.
- Each listener has a routing key.
- A service is usable when at least one listener and one connector share the same routing key.
- On Kubernetes, a listener is implemented as a Kubernetes Service.
- On Docker, Podman, and Linux, a listener is a listening socket bound to a local network interface.
- A multi-key listener is a listener variant that binds one local endpoint to multiple routing keys.

## Common fields

The Listener resource uses these core fields:

- `spec.routingKey`: the identifier that matches this listener to connector resources, usually in remote sites.
- `spec.host`: the hostname or IP address local clients use for the listener endpoint.
- `spec.port`: the port local clients use for the listener endpoint.

If a service needs multiple ports, create multiple listeners using the same host value and different ports.

## Creation paths

For Kubernetes-style YAML workflows, create a `Listener` resource and apply it through Skupper:

```yaml
apiVersion: skupper.io/v2alpha1
kind: Listener
metadata:
  name: backend
  namespace: west
spec:
  routingKey: backend
  host: east-backend
  port: 8080
```

```bash
skupper system apply -f <filename>
```

For local CLI workflows on Docker, Podman, or Linux platforms, create a listener directly:

```bash
skupper listener create <name> <port> --routing-key <routing-key>
skupper system reload
```

When `--routing-key` and `--host` are not specified, the listener name is used as the default routing key and host.

## Verify

Check listener status:

```bash
skupper listener status
```

Expected shape:

```text
NAME      STATUS  ROUTING-KEY  HOST     PORT  MATCHING-CONNECTOR  MESSAGE
backend   Ready   backend      ...      8080  true                OK
```

The service is not operational until the listener has a matching connector. In resource status, the relevant signals are `hasMatchingConnector` and the conditions `Configured`, `Matched`, and `Ready`.

## Listener variants

A standard listener binds one local endpoint to one routing key. A multi-key listener is still a listener in the wiki model: it binds one local endpoint to multiple routing keys and uses a strategy to decide how traffic is distributed.

Current Skupper source material describes multi-key listeners as a separate resource, `MultiKeyListener`. For this wiki, treat that as an implementation detail or listener subtype rather than a separate concept family. This distinction matters because multi-key behavior may become the default listener behavior in the future.

## Caveats

- A listener does not expose a workload by itself; a connector with the same routing key is required.
- A routing key can match multiple listeners and multiple connectors.
- Multi-key listeners aggregate several routing keys behind one local endpoint.
- On local-system platforms, configuration changes may require `skupper system reload`.
