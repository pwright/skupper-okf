---
type: GeneratedDocs
title: Skupper API - network-observer
id: skupper-api-network-observer
source_file: ../human/skupper/cmd/network-observer/spec/openapi.yaml
generated_at: 2026-07-04T10:01:08Z
generator: openapi-to-md
---

# Skupper Network Observer HTTP API.

> Version 0.0.1

The Skupper network observer exposes a read only HTTP API. This API is used by the network console frontend to display information about a skupper network.


## Path Table

| Method | Path | Description |
| --- | --- | --- |
| GET | [/api/v2alpha1/sites](#getapiv2alpha1sites) |  |
| GET | [/api/v2alpha1/sites/{id}](#getapiv2alpha1sitesid) |  |
| GET | [/api/v2alpha1/processes](#getapiv2alpha1processes) |  |
| GET | [/api/v2alpha1/processes/{id}](#getapiv2alpha1processesid) |  |
| GET | [/api/v2alpha1/routers](#getapiv2alpha1routers) |  |
| GET | [/api/v2alpha1/routers/{id}](#getapiv2alpha1routersid) |  |
| GET | [/api/v2alpha1/listeners](#getapiv2alpha1listeners) |  |
| GET | [/api/v2alpha1/listeners/{id}](#getapiv2alpha1listenersid) |  |
| GET | [/api/v2alpha1/connectors](#getapiv2alpha1connectors) |  |
| GET | [/api/v2alpha1/connectors/{id}](#getapiv2alpha1connectorsid) |  |
| GET | [/api/v2alpha1/services](#getapiv2alpha1services) |  |
| GET | [/api/v2alpha1/services/{id}](#getapiv2alpha1servicesid) |  |
| GET | [/api/v2alpha1/components](#getapiv2alpha1components) |  |
| GET | [/api/v2alpha1/components/{id}](#getapiv2alpha1componentsid) |  |
| GET | [/api/v2alpha1/sitepairs](#getapiv2alpha1sitepairs) |  |
| GET | [/api/v2alpha1/sitepairs/{id}](#getapiv2alpha1sitepairsid) |  |
| GET | [/api/v2alpha1/componentpairs](#getapiv2alpha1componentpairs) |  |
| GET | [/api/v2alpha1/componentpairs/{id}](#getapiv2alpha1componentpairsid) |  |
| GET | [/api/v2alpha1/processpairs](#getapiv2alpha1processpairs) |  |
| GET | [/api/v2alpha1/processpairs/{id}](#getapiv2alpha1processpairsid) |  |
| GET | [/api/v2alpha1/routerlinks](#getapiv2alpha1routerlinks) |  |
| GET | [/api/v2alpha1/routerlinks/{id}](#getapiv2alpha1routerlinksid) |  |
| GET | [/api/v2alpha1/routeraccess](#getapiv2alpha1routeraccess) |  |
| GET | [/api/v2alpha1/routeraccess/{id}](#getapiv2alpha1routeraccessid) |  |
| GET | [/api/v2alpha1/hosts](#getapiv2alpha1hosts) |  |
| GET | [/api/v2alpha1/hosts/{id}](#getapiv2alpha1hostsid) |  |
| GET | [/api/v2alpha1/connections](#getapiv2alpha1connections) |  |
| GET | [/api/v2alpha1/applicationflows](#getapiv2alpha1applicationflows) |  |
| GET | [/api/v2alpha1/sites/{id}/processes](#getapiv2alpha1sitesidprocesses) |  |
| GET | [/api/v2alpha1/sites/{id}/routers](#getapiv2alpha1sitesidrouters) |  |
| GET | [/api/v2alpha1/sites/{id}/hosts](#getapiv2alpha1sitesidhosts) |  |
| GET | [/api/v2alpha1/services/{id}/processes](#getapiv2alpha1servicesidprocesses) |  |
| GET | [/api/v2alpha1/services/{id}/processpairs](#getapiv2alpha1servicesidprocesspairs) |  |
| GET | [/api/v2alpha1/services/{id}/connections](#getapiv2alpha1servicesidconnections) |  |

## Reference Table

| Name | Path | Description |
| --- | --- | --- |
| pathID | [#/components/parameters/pathID](#componentsparameterspathid) |  |
| notSupported | [#/components/responses/notSupported](#componentsresponsesnotsupported) | response from unsupported endpoint |
| errorNotFound | [#/components/responses/errorNotFound](#componentsresponseserrornotfound) | resource not found |
| errorBadRequest | [#/components/responses/errorBadRequest](#componentsresponseserrorbadrequest) | bad request |
| getSites | [#/components/responses/getSites](#componentsresponsesgetsites) | response with a list of sites |
| getRouters | [#/components/responses/getRouters](#componentsresponsesgetrouters) | response with a list of routers |
| getProcesses | [#/components/responses/getProcesses](#componentsresponsesgetprocesses) | response with a list of processes |
| getListeners | [#/components/responses/getListeners](#componentsresponsesgetlisteners) | response with a list of listeners |
| getConnectors | [#/components/responses/getConnectors](#componentsresponsesgetconnectors) | response with a list of connectors |
| getServices | [#/components/responses/getServices](#componentsresponsesgetservices) | response with a list of services |
| getComponents | [#/components/responses/getComponents](#componentsresponsesgetcomponents) | response with a list of components |
| getFlowAggregates | [#/components/responses/getFlowAggregates](#componentsresponsesgetflowaggregates) | response with a list of flow aggregates |
| getRouterLinks | [#/components/responses/getRouterLinks](#componentsresponsesgetrouterlinks) | response with a list of router links |
| getRouterAccess | [#/components/responses/getRouterAccess](#componentsresponsesgetrouteraccess) | response with a list of router access |
| getConnections | [#/components/responses/getConnections](#componentsresponsesgetconnections) | response with a list of connections |
| getApplicationFlows | [#/components/responses/getApplicationFlows](#componentsresponsesgetapplicationflows) | response with a list of application flows |
| getSiteByID | [#/components/responses/getSiteByID](#componentsresponsesgetsitebyid) | response with a single site |
| getProcessByID | [#/components/responses/getProcessByID](#componentsresponsesgetprocessbyid) | response with a single process |
| getRouterByID | [#/components/responses/getRouterByID](#componentsresponsesgetrouterbyid) | response with a single router |
| getListenerByID | [#/components/responses/getListenerByID](#componentsresponsesgetlistenerbyid) | response with a single listener |
| getConnectorByID | [#/components/responses/getConnectorByID](#componentsresponsesgetconnectorbyid) | response with a single connector |
| getServiceByID | [#/components/responses/getServiceByID](#componentsresponsesgetservicebyid) | response with a single service |
| getComponentByID | [#/components/responses/getComponentByID](#componentsresponsesgetcomponentbyid) | response with a single component |
| getFlowAggregateByID | [#/components/responses/getFlowAggregateByID](#componentsresponsesgetflowaggregatebyid) | response with a single flow aggregate |
| getRouterLinkByID | [#/components/responses/getRouterLinkByID](#componentsresponsesgetrouterlinkbyid) | response with a single router link |
| getRouterAccessByID | [#/components/responses/getRouterAccessByID](#componentsresponsesgetrouteraccessbyid) | response with a single router link |
| collectionResponse | [#/components/schemas/collectionResponse](#componentsschemascollectionresponse) |  |
| ErrorResponse | [#/components/schemas/ErrorResponse](#componentsschemaserrorresponse) |  |
| SiteResponse | [#/components/schemas/SiteResponse](#componentsschemassiteresponse) |  |
| SiteListResponse | [#/components/schemas/SiteListResponse](#componentsschemassitelistresponse) |  |
| ProcessResponse | [#/components/schemas/ProcessResponse](#componentsschemasprocessresponse) |  |
| ProcessListResponse | [#/components/schemas/ProcessListResponse](#componentsschemasprocesslistresponse) |  |
| ListenerResponse | [#/components/schemas/ListenerResponse](#componentsschemaslistenerresponse) |  |
| ListenerListResponse | [#/components/schemas/ListenerListResponse](#componentsschemaslistenerlistresponse) |  |
| ConnectorResponse | [#/components/schemas/ConnectorResponse](#componentsschemasconnectorresponse) |  |
| ConnectorListResponse | [#/components/schemas/ConnectorListResponse](#componentsschemasconnectorlistresponse) |  |
| RouterListResponse | [#/components/schemas/RouterListResponse](#componentsschemasrouterlistresponse) |  |
| RouterResponse | [#/components/schemas/RouterResponse](#componentsschemasrouterresponse) |  |
| ServiceListResponse | [#/components/schemas/ServiceListResponse](#componentsschemasservicelistresponse) |  |
| ServiceResponse | [#/components/schemas/ServiceResponse](#componentsschemasserviceresponse) |  |
| ComponentListResponse | [#/components/schemas/ComponentListResponse](#componentsschemascomponentlistresponse) |  |
| ComponentResponse | [#/components/schemas/ComponentResponse](#componentsschemascomponentresponse) |  |
| FlowAggregateListResponse | [#/components/schemas/FlowAggregateListResponse](#componentsschemasflowaggregatelistresponse) |  |
| FlowAggregateResponse | [#/components/schemas/FlowAggregateResponse](#componentsschemasflowaggregateresponse) |  |
| RouterLinkListResponse | [#/components/schemas/RouterLinkListResponse](#componentsschemasrouterlinklistresponse) |  |
| RouterLinkResponse | [#/components/schemas/RouterLinkResponse](#componentsschemasrouterlinkresponse) |  |
| RouterAccessListResponse | [#/components/schemas/RouterAccessListResponse](#componentsschemasrouteraccesslistresponse) |  |
| RouterAccessResponse | [#/components/schemas/RouterAccessResponse](#componentsschemasrouteraccessresponse) |  |
| ConnectionListResponse | [#/components/schemas/ConnectionListResponse](#componentsschemasconnectionlistresponse) |  |
| ConnectionResponse | [#/components/schemas/ConnectionResponse](#componentsschemasconnectionresponse) |  |
| ApplicationFlowResponse | [#/components/schemas/ApplicationFlowResponse](#componentsschemasapplicationflowresponse) |  |
| baseRecord | [#/components/schemas/baseRecord](#componentsschemasbaserecord) |  |
| sitePlatformType | [#/components/schemas/sitePlatformType](#componentsschemassiteplatformtype) | The platform used for the site. |
| processBindingType | [#/components/schemas/processBindingType](#componentsschemasprocessbindingtype) | Indicates whether a process is exposed or not in a skupper network |
| serviceIdentifierType | [#/components/schemas/serviceIdentifierType](#componentsschemasserviceidentifiertype) | a special string for identifying services uses the form `name@identity@protocol` |
| linkRoleType | [#/components/schemas/linkRoleType](#componentsschemaslinkroletype) | The class of skupper link |
| proxyProtocolType | [#/components/schemas/proxyProtocolType](#componentsschemasproxyprotocoltype) | The proxy protocol used when the link connection is established. |
| SiteRecord | [#/components/schemas/SiteRecord](#componentsschemassiterecord) |  |
| ProcessRecord | [#/components/schemas/ProcessRecord](#componentsschemasprocessrecord) |  |
| RouterRecord | [#/components/schemas/RouterRecord](#componentsschemasrouterrecord) |  |
| ListenerRecord | [#/components/schemas/ListenerRecord](#componentsschemaslistenerrecord) |  |
| ConnectorRecord | [#/components/schemas/ConnectorRecord](#componentsschemasconnectorrecord) |  |
| ServiceRecord | [#/components/schemas/ServiceRecord](#componentsschemasservicerecord) |  |
| ComponentRecord | [#/components/schemas/ComponentRecord](#componentsschemascomponentrecord) |  |
| flowAggregatePairType | [#/components/schemas/flowAggregatePairType](#componentsschemasflowaggregatepairtype) |  |
| FlowAggregateRecord | [#/components/schemas/FlowAggregateRecord](#componentsschemasflowaggregaterecord) |  |
| operStatusType | [#/components/schemas/operStatusType](#componentsschemasoperstatustype) |  |
| RouterLinkRecord | [#/components/schemas/RouterLinkRecord](#componentsschemasrouterlinkrecord) |  |
| RouterAccessRecord | [#/components/schemas/RouterAccessRecord](#componentsschemasrouteraccessrecord) |  |
| ConnectionRecord | [#/components/schemas/ConnectionRecord](#componentsschemasconnectionrecord) |  |
| ApplicationFlowRecord | [#/components/schemas/ApplicationFlowRecord](#componentsschemasapplicationflowrecord) |  |

## Path Details

***

### [GET]/api/v2alpha1/sites

- Operation id  
sites

#### Responses

- 200 undefined

- 400 undefined

***

### [GET]/api/v2alpha1/sites/{id}

- Operation id  
siteById

#### Responses

- 200 undefined

- 404 undefined

***

### [GET]/api/v2alpha1/processes

- Operation id  
processes

#### Responses

- 200 undefined

- 400 undefined

***

### [GET]/api/v2alpha1/processes/{id}

- Operation id  
processById

#### Responses

- 200 undefined

- 404 undefined

***

### [GET]/api/v2alpha1/routers

- Operation id  
routers

#### Responses

- 200 undefined

- 400 undefined

***

### [GET]/api/v2alpha1/routers/{id}

- Operation id  
routerByID

#### Responses

- 200 undefined

- 404 undefined

***

### [GET]/api/v2alpha1/listeners

- Operation id  
listeners

#### Responses

- 200 undefined

- 400 undefined

***

### [GET]/api/v2alpha1/listeners/{id}

- Operation id  
listenerByID

#### Responses

- 200 undefined

- 404 undefined

***

### [GET]/api/v2alpha1/connectors

- Operation id  
connectors

#### Responses

- 200 undefined

- 400 undefined

***

### [GET]/api/v2alpha1/connectors/{id}

- Operation id  
connectorByID

#### Responses

- 200 undefined

- 404 undefined

***

### [GET]/api/v2alpha1/services

- Operation id  
services

#### Responses

- 200 undefined

- 400 undefined

***

### [GET]/api/v2alpha1/services/{id}

- Operation id  
serviceByID

#### Responses

- 200 undefined

- 404 undefined

***

### [GET]/api/v2alpha1/components

- Operation id  
components

#### Responses

- 200 undefined

- 400 undefined

***

### [GET]/api/v2alpha1/components/{id}

- Operation id  
componentByID

#### Responses

- 200 undefined

- 404 undefined

***

### [GET]/api/v2alpha1/sitepairs

- Operation id  
sitepairs

#### Responses

- 200 undefined

- 400 undefined

***

### [GET]/api/v2alpha1/sitepairs/{id}

- Operation id  
sitepairByID

#### Responses

- 200 undefined

- 404 undefined

***

### [GET]/api/v2alpha1/componentpairs

- Operation id  
componentpairs

#### Responses

- 200 undefined

- 400 undefined

***

### [GET]/api/v2alpha1/componentpairs/{id}

- Operation id  
componentpairByID

#### Responses

- 200 undefined

- 404 undefined

***

### [GET]/api/v2alpha1/processpairs

- Operation id  
processpairs

#### Responses

- 200 undefined

- 400 undefined

***

### [GET]/api/v2alpha1/processpairs/{id}

- Operation id  
processpairByID

#### Responses

- 200 undefined

- 404 undefined

***

### [GET]/api/v2alpha1/routerlinks

- Operation id  
routerlinks

#### Responses

- 200 undefined

- 400 undefined

***

### [GET]/api/v2alpha1/routerlinks/{id}

- Operation id  
routerlinkByID

#### Responses

- 200 undefined

- 404 undefined

***

### [GET]/api/v2alpha1/routeraccess

- Operation id  
routeraccess

#### Responses

- 200 undefined

- 400 undefined

***

### [GET]/api/v2alpha1/routeraccess/{id}

- Operation id  
routeraccessByID

#### Responses

- 200 undefined

- 404 undefined

***

### [GET]/api/v2alpha1/hosts

- Operation id  
hosts

#### Responses

- 410 undefined

***

### [GET]/api/v2alpha1/hosts/{id}

- Operation id  
hostsByID

#### Responses

- 200 undefined

- 404 undefined

***

### [GET]/api/v2alpha1/connections

- Operation id  
connections

#### Responses

- 200 undefined

***

### [GET]/api/v2alpha1/applicationflows

- Operation id  
applicationflows

#### Responses

- 200 undefined

***

### [GET]/api/v2alpha1/sites/{id}/processes

- Operation id  
processesBySite

#### Responses

- 200 undefined

- 404 undefined

***

### [GET]/api/v2alpha1/sites/{id}/routers

- Operation id  
routersBySite

#### Responses

- 200 undefined

- 404 undefined

***

### [GET]/api/v2alpha1/sites/{id}/hosts

- Operation id  
hostsBySite

#### Responses

- 410 undefined

***

### [GET]/api/v2alpha1/services/{id}/processes

- Operation id  
processesByService

#### Responses

- 200 undefined

- 400 undefined

***

### [GET]/api/v2alpha1/services/{id}/processpairs

- Operation id  
processPairsByService

#### Responses

- 200 undefined

- 404 undefined

***

### [GET]/api/v2alpha1/services/{id}/connections

- Operation id  
connectionsByService

#### Responses

- 200 undefined

- 404 undefined

## References

### #/components/parameters/pathID

```typescript
id: string
```

### #/components/responses/notSupported

- application/json

```typescript
{
  message: string
  code: string
}
```

### #/components/responses/errorNotFound

- application/json

```typescript
{
  message: string
  code: string
}
```

### #/components/responses/errorBadRequest

- application/json

```typescript
{
  message: string
  code: string
}
```

### #/components/responses/getSites

- application/json

```typescript
undefined?: #/components/schemas/collectionResponse & {
   results?: #/components/schemas/baseRecord & {
      // Possible values are 'AWS', 'IBM', 'Azure' ecc. Can be any string or 'unknown'
      provider: string
      // The platform used for the site.
      platform: enum[kubernetes, podman, docker, linux, unknown]
      name: string
      namespace: string
      // The current skupper version installed. Can be any string or 'unknown'
      version: string
      routerCount: integer
    }[]
 }
```

### #/components/responses/getRouters

- application/json

```typescript
undefined?: #/components/schemas/collectionResponse & {
   results?: #/components/schemas/baseRecord & {
      siteId: string
      name: string
      mode: string
      namespace?: string
      imageName: string
      imageVersion: string
      hostName: string
      buildVersion: string
    }[]
 }
```

### #/components/responses/getProcesses

- application/json

```typescript
undefined?: #/components/schemas/collectionResponse & {
   results?: #/components/schemas/baseRecord & {
      name: string
      // Id of the site associated to the process.
      siteId: string
      siteName: string
      // Id of the component associated to the process.
      componentId: string
      componentName: string
      // The IP address of the pod within the Kubernetes cluster
      hostName: string
      // The IP address of the node where the pod is running
      sourceHost: string
      imageName: string
      // Internal processes are processes related to Skupper. Remote processes are processes indirectly connected, such as a proxy
      role: enum[internal, external, remote]
      // Indicates whether a process is exposed or not in a skupper network
      binding: enum[bound, unbound]
      // a special string for identifying services uses the form `name@identity@protocol`
      services?: string[]
    }[]
 }
```

### #/components/responses/getListeners

- application/json

```typescript
undefined?: #/components/schemas/collectionResponse & {
   results?: #/components/schemas/baseRecord & {
      routerId: string
      name: string
      destHost: string
      destPort: string
      protocol: string
      routingKey: string
      serviceId?: string
      siteId: string
      siteName: string
    }[]
 }
```

### #/components/responses/getConnectors

- application/json

```typescript
undefined?: #/components/schemas/collectionResponse & {
   results?: #/components/schemas/baseRecord & {
      routerId: string
      name: string
      destHost: string
      destPort: string
      protocol: string
      routingKey: string
      serviceId?: string
      processId: string
      target: string
      siteId: string
      siteName: string
    }[]
 }
```

### #/components/responses/getServices

- application/json

```typescript
undefined?: #/components/schemas/collectionResponse & {
   results?: #/components/schemas/baseRecord & {
      name: string
      protocol: string
      observedApplicationProtocols?: string[]
      listenerCount: integer
      connectorCount: integer
      // true when there are both listeners and connectors configured
      isBound: boolean
      // true when there is at least one listener for this routingKey
      hasListener: boolean
    }[]
 }
```

### #/components/responses/getComponents

- application/json

```typescript
undefined?: #/components/schemas/collectionResponse & {
   results?: #/components/schemas/baseRecord & {
      name: string
      role: string
      processCount: integer
    }[]
 }
```

### #/components/responses/getFlowAggregates

- application/json

```typescript
undefined?: #/components/schemas/collectionResponse & {
   results?: #/components/schemas/baseRecord & {
      pairType: enum[SITE, PROCESS, PROCESS_GROUP]
      recordCount: integer
      sourceId: string
      destinationId: string
      sourceName: string
      destinationName: string
      sourceSiteId?: string
      destinationSiteId?: string
      sourceSiteName?: string
      destinationSiteName?: string
      protocol: string
    }[]
 }
```

### #/components/responses/getRouterLinks

- application/json

```typescript
undefined?: #/components/schemas/collectionResponse & {
   results?: #/components/schemas/baseRecord & {
      routerId: string
      routerName: string
      name: string
      // When connected, cost will be set to the link cost attribute
      cost: integer
      // The class of skupper link
      role: enum[inter-router, edge, unknown]
      status: enum[up, down]
      octetCount: integer
      octetReverseCount: integer
      // When connected, the identity of the destitation (peer) router access.
      routerAccessId: string
      // When connected, the identity of the destitation (peer) router.
      destinationRouterId: string
      // When connected, the name of the destitation (peer) router.
      destinationRouterName: string
      sourceSiteId: string
      sourceSiteName: string
      // When connected, the identity of the destitation (peer) site.
      destinationSiteId: string
      // When connected, the name of the destitation (peer) site.
      destinationSiteName: string
      proxyProtocol?: #/components/schemas/proxyProtocolType
    }[]
 }
```

### #/components/responses/getRouterAccess

- application/json

```typescript
undefined?: #/components/schemas/collectionResponse & {
   results?: #/components/schemas/baseRecord & {
      routerId: string
      name: string
      linkCount: integer
      role: string
    }[]
 }
```

### #/components/responses/getConnections

- application/json

```typescript
undefined?: #/components/schemas/collectionResponse & {
   results?: #/components/schemas/baseRecord & {
      duration: integer
      processPairId: string
      componentPairId: string
      sitePairId: string
      sourceSiteId: string
      sourceSiteName: string
      destSiteId: string
      destSiteName: string
      sourceProcessId: string
      sourceProcessName: string
      destProcessId: string
      destProcessName: string
      routingKey: string
      protocol: string
      listenerId: string
      connectorId: string
      sourceHost: string
      sourcePort: string
      destHost: string
      destPort: string
      proxyHost: string
      proxyPort: string
      octetCount: integer
      octetReverseCount: integer
      latency: integer
      latencyReverse: integer
      listenerError: string
      connectorError: string
      traceRouters?: string[]
      traceSites?: string[]
    }[]
 }
```

### #/components/responses/getApplicationFlows

- application/json

```typescript
undefined?: #/components/schemas/collectionResponse & {
   results?: #/components/schemas/baseRecord & {
      connectionId: string
      duration: integer
      sourceSiteId: string
      sourceSiteName: string
      destSiteId: string
      destSiteName: string
      sourceProcessId: string
      sourceProcessName: string
      destProcessId: string
      destProcessName: string
      routingKey: string
      protocol: string
      method: string
      status: string
      octetCount: integer
      octetReverseCount: integer
      traceRouters?: string[]
      traceSites?: string[]
    }[]
 }
```

### #/components/responses/getSiteByID

- application/json

```typescript
{
  results: #/components/schemas/baseRecord & {
     // Possible values are 'AWS', 'IBM', 'Azure' ecc. Can be any string or 'unknown'
     provider: string
     // The platform used for the site.
     platform: enum[kubernetes, podman, docker, linux, unknown]
     name: string
     namespace: string
     // The current skupper version installed. Can be any string or 'unknown'
     version: string
     routerCount: integer
   }
}
```

### #/components/responses/getProcessByID

- application/json

```typescript
{
  results: #/components/schemas/baseRecord & {
     name: string
     // Id of the site associated to the process.
     siteId: string
     siteName: string
     // Id of the component associated to the process.
     componentId: string
     componentName: string
     // The IP address of the pod within the Kubernetes cluster
     hostName: string
     // The IP address of the node where the pod is running
     sourceHost: string
     imageName: string
     // Internal processes are processes related to Skupper. Remote processes are processes indirectly connected, such as a proxy
     role: enum[internal, external, remote]
     // Indicates whether a process is exposed or not in a skupper network
     binding: enum[bound, unbound]
     // a special string for identifying services uses the form `name@identity@protocol`
     services?: string[]
   }
}
```

### #/components/responses/getRouterByID

- application/json

```typescript
{
  results: #/components/schemas/baseRecord & {
     siteId: string
     name: string
     mode: string
     namespace?: string
     imageName: string
     imageVersion: string
     hostName: string
     buildVersion: string
   }
}
```

### #/components/responses/getListenerByID

- application/json

```typescript
{
  results: #/components/schemas/baseRecord & {
     routerId: string
     name: string
     destHost: string
     destPort: string
     protocol: string
     routingKey: string
     serviceId?: string
     siteId: string
     siteName: string
   }
}
```

### #/components/responses/getConnectorByID

- application/json

```typescript
{
  results: #/components/schemas/baseRecord & {
     routerId: string
     name: string
     destHost: string
     destPort: string
     protocol: string
     routingKey: string
     serviceId?: string
     processId: string
     target: string
     siteId: string
     siteName: string
   }
}
```

### #/components/responses/getServiceByID

- application/json

```typescript
{
  results: #/components/schemas/baseRecord & {
     name: string
     protocol: string
     observedApplicationProtocols?: string[]
     listenerCount: integer
     connectorCount: integer
     // true when there are both listeners and connectors configured
     isBound: boolean
     // true when there is at least one listener for this routingKey
     hasListener: boolean
   }
}
```

### #/components/responses/getComponentByID

- application/json

```typescript
{
  results: #/components/schemas/baseRecord & {
     name: string
     role: string
     processCount: integer
   }
}
```

### #/components/responses/getFlowAggregateByID

- application/json

```typescript
{
  results: #/components/schemas/baseRecord & {
     pairType: enum[SITE, PROCESS, PROCESS_GROUP]
     recordCount: integer
     sourceId: string
     destinationId: string
     sourceName: string
     destinationName: string
     sourceSiteId?: string
     destinationSiteId?: string
     sourceSiteName?: string
     destinationSiteName?: string
     protocol: string
   }
}
```

### #/components/responses/getRouterLinkByID

- application/json

```typescript
{
  results: #/components/schemas/baseRecord & {
     routerId: string
     routerName: string
     name: string
     // When connected, cost will be set to the link cost attribute
     cost: integer
     // The class of skupper link
     role: enum[inter-router, edge, unknown]
     status: enum[up, down]
     octetCount: integer
     octetReverseCount: integer
     // When connected, the identity of the destitation (peer) router access.
     routerAccessId: string
     // When connected, the identity of the destitation (peer) router.
     destinationRouterId: string
     // When connected, the name of the destitation (peer) router.
     destinationRouterName: string
     sourceSiteId: string
     sourceSiteName: string
     // When connected, the identity of the destitation (peer) site.
     destinationSiteId: string
     // When connected, the name of the destitation (peer) site.
     destinationSiteName: string
     proxyProtocol?: #/components/schemas/proxyProtocolType
   }
}
```

### #/components/responses/getRouterAccessByID

- application/json

```typescript
{
  results: #/components/schemas/baseRecord & {
     routerId: string
     name: string
     linkCount: integer
     role: string
   }
}
```

### #/components/schemas/collectionResponse

```typescript
{
  // number of results in response
  count: integer
  // number of results matching filtering and time range constraints before any limit or offset is applied.
  timeRangeCount: integer
}
```

### #/components/schemas/ErrorResponse

```typescript
{
  message: string
  code: string
}
```

### #/components/schemas/SiteResponse

```typescript
{
  results: #/components/schemas/baseRecord & {
     // Possible values are 'AWS', 'IBM', 'Azure' ecc. Can be any string or 'unknown'
     provider: string
     // The platform used for the site.
     platform: enum[kubernetes, podman, docker, linux, unknown]
     name: string
     namespace: string
     // The current skupper version installed. Can be any string or 'unknown'
     version: string
     routerCount: integer
   }
}
```

### #/components/schemas/SiteListResponse

```typescript
undefined?: #/components/schemas/collectionResponse & {
   results?: #/components/schemas/baseRecord & {
      // Possible values are 'AWS', 'IBM', 'Azure' ecc. Can be any string or 'unknown'
      provider: string
      // The platform used for the site.
      platform: enum[kubernetes, podman, docker, linux, unknown]
      name: string
      namespace: string
      // The current skupper version installed. Can be any string or 'unknown'
      version: string
      routerCount: integer
    }[]
 }
```

### #/components/schemas/ProcessResponse

```typescript
{
  results: #/components/schemas/baseRecord & {
     name: string
     // Id of the site associated to the process.
     siteId: string
     siteName: string
     // Id of the component associated to the process.
     componentId: string
     componentName: string
     // The IP address of the pod within the Kubernetes cluster
     hostName: string
     // The IP address of the node where the pod is running
     sourceHost: string
     imageName: string
     // Internal processes are processes related to Skupper. Remote processes are processes indirectly connected, such as a proxy
     role: enum[internal, external, remote]
     // Indicates whether a process is exposed or not in a skupper network
     binding: enum[bound, unbound]
     // a special string for identifying services uses the form `name@identity@protocol`
     services?: string[]
   }
}
```

### #/components/schemas/ProcessListResponse

```typescript
undefined?: #/components/schemas/collectionResponse & {
   results?: #/components/schemas/baseRecord & {
      name: string
      // Id of the site associated to the process.
      siteId: string
      siteName: string
      // Id of the component associated to the process.
      componentId: string
      componentName: string
      // The IP address of the pod within the Kubernetes cluster
      hostName: string
      // The IP address of the node where the pod is running
      sourceHost: string
      imageName: string
      // Internal processes are processes related to Skupper. Remote processes are processes indirectly connected, such as a proxy
      role: enum[internal, external, remote]
      // Indicates whether a process is exposed or not in a skupper network
      binding: enum[bound, unbound]
      // a special string for identifying services uses the form `name@identity@protocol`
      services?: string[]
    }[]
 }
```

### #/components/schemas/ListenerResponse

```typescript
{
  results: #/components/schemas/baseRecord & {
     routerId: string
     name: string
     destHost: string
     destPort: string
     protocol: string
     routingKey: string
     serviceId?: string
     siteId: string
     siteName: string
   }
}
```

### #/components/schemas/ListenerListResponse

```typescript
undefined?: #/components/schemas/collectionResponse & {
   results?: #/components/schemas/baseRecord & {
      routerId: string
      name: string
      destHost: string
      destPort: string
      protocol: string
      routingKey: string
      serviceId?: string
      siteId: string
      siteName: string
    }[]
 }
```

### #/components/schemas/ConnectorResponse

```typescript
{
  results: #/components/schemas/baseRecord & {
     routerId: string
     name: string
     destHost: string
     destPort: string
     protocol: string
     routingKey: string
     serviceId?: string
     processId: string
     target: string
     siteId: string
     siteName: string
   }
}
```

### #/components/schemas/ConnectorListResponse

```typescript
undefined?: #/components/schemas/collectionResponse & {
   results?: #/components/schemas/baseRecord & {
      routerId: string
      name: string
      destHost: string
      destPort: string
      protocol: string
      routingKey: string
      serviceId?: string
      processId: string
      target: string
      siteId: string
      siteName: string
    }[]
 }
```

### #/components/schemas/RouterListResponse

```typescript
undefined?: #/components/schemas/collectionResponse & {
   results?: #/components/schemas/baseRecord & {
      siteId: string
      name: string
      mode: string
      namespace?: string
      imageName: string
      imageVersion: string
      hostName: string
      buildVersion: string
    }[]
 }
```

### #/components/schemas/RouterResponse

```typescript
{
  results: #/components/schemas/baseRecord & {
     siteId: string
     name: string
     mode: string
     namespace?: string
     imageName: string
     imageVersion: string
     hostName: string
     buildVersion: string
   }
}
```

### #/components/schemas/ServiceListResponse

```typescript
undefined?: #/components/schemas/collectionResponse & {
   results?: #/components/schemas/baseRecord & {
      name: string
      protocol: string
      observedApplicationProtocols?: string[]
      listenerCount: integer
      connectorCount: integer
      // true when there are both listeners and connectors configured
      isBound: boolean
      // true when there is at least one listener for this routingKey
      hasListener: boolean
    }[]
 }
```

### #/components/schemas/ServiceResponse

```typescript
{
  results: #/components/schemas/baseRecord & {
     name: string
     protocol: string
     observedApplicationProtocols?: string[]
     listenerCount: integer
     connectorCount: integer
     // true when there are both listeners and connectors configured
     isBound: boolean
     // true when there is at least one listener for this routingKey
     hasListener: boolean
   }
}
```

### #/components/schemas/ComponentListResponse

```typescript
undefined?: #/components/schemas/collectionResponse & {
   results?: #/components/schemas/baseRecord & {
      name: string
      role: string
      processCount: integer
    }[]
 }
```

### #/components/schemas/ComponentResponse

```typescript
{
  results: #/components/schemas/baseRecord & {
     name: string
     role: string
     processCount: integer
   }
}
```

### #/components/schemas/FlowAggregateListResponse

```typescript
undefined?: #/components/schemas/collectionResponse & {
   results?: #/components/schemas/baseRecord & {
      pairType: enum[SITE, PROCESS, PROCESS_GROUP]
      recordCount: integer
      sourceId: string
      destinationId: string
      sourceName: string
      destinationName: string
      sourceSiteId?: string
      destinationSiteId?: string
      sourceSiteName?: string
      destinationSiteName?: string
      protocol: string
    }[]
 }
```

### #/components/schemas/FlowAggregateResponse

```typescript
{
  results: #/components/schemas/baseRecord & {
     pairType: enum[SITE, PROCESS, PROCESS_GROUP]
     recordCount: integer
     sourceId: string
     destinationId: string
     sourceName: string
     destinationName: string
     sourceSiteId?: string
     destinationSiteId?: string
     sourceSiteName?: string
     destinationSiteName?: string
     protocol: string
   }
}
```

### #/components/schemas/RouterLinkListResponse

```typescript
undefined?: #/components/schemas/collectionResponse & {
   results?: #/components/schemas/baseRecord & {
      routerId: string
      routerName: string
      name: string
      // When connected, cost will be set to the link cost attribute
      cost: integer
      // The class of skupper link
      role: enum[inter-router, edge, unknown]
      status: enum[up, down]
      octetCount: integer
      octetReverseCount: integer
      // When connected, the identity of the destitation (peer) router access.
      routerAccessId: string
      // When connected, the identity of the destitation (peer) router.
      destinationRouterId: string
      // When connected, the name of the destitation (peer) router.
      destinationRouterName: string
      sourceSiteId: string
      sourceSiteName: string
      // When connected, the identity of the destitation (peer) site.
      destinationSiteId: string
      // When connected, the name of the destitation (peer) site.
      destinationSiteName: string
      proxyProtocol?: #/components/schemas/proxyProtocolType
    }[]
 }
```

### #/components/schemas/RouterLinkResponse

```typescript
{
  results: #/components/schemas/baseRecord & {
     routerId: string
     routerName: string
     name: string
     // When connected, cost will be set to the link cost attribute
     cost: integer
     // The class of skupper link
     role: enum[inter-router, edge, unknown]
     status: enum[up, down]
     octetCount: integer
     octetReverseCount: integer
     // When connected, the identity of the destitation (peer) router access.
     routerAccessId: string
     // When connected, the identity of the destitation (peer) router.
     destinationRouterId: string
     // When connected, the name of the destitation (peer) router.
     destinationRouterName: string
     sourceSiteId: string
     sourceSiteName: string
     // When connected, the identity of the destitation (peer) site.
     destinationSiteId: string
     // When connected, the name of the destitation (peer) site.
     destinationSiteName: string
     proxyProtocol?: #/components/schemas/proxyProtocolType
   }
}
```

### #/components/schemas/RouterAccessListResponse

```typescript
undefined?: #/components/schemas/collectionResponse & {
   results?: #/components/schemas/baseRecord & {
      routerId: string
      name: string
      linkCount: integer
      role: string
    }[]
 }
```

### #/components/schemas/RouterAccessResponse

```typescript
{
  results: #/components/schemas/baseRecord & {
     routerId: string
     name: string
     linkCount: integer
     role: string
   }
}
```

### #/components/schemas/ConnectionListResponse

```typescript
undefined?: #/components/schemas/collectionResponse & {
   results?: #/components/schemas/baseRecord & {
      duration: integer
      processPairId: string
      componentPairId: string
      sitePairId: string
      sourceSiteId: string
      sourceSiteName: string
      destSiteId: string
      destSiteName: string
      sourceProcessId: string
      sourceProcessName: string
      destProcessId: string
      destProcessName: string
      routingKey: string
      protocol: string
      listenerId: string
      connectorId: string
      sourceHost: string
      sourcePort: string
      destHost: string
      destPort: string
      proxyHost: string
      proxyPort: string
      octetCount: integer
      octetReverseCount: integer
      latency: integer
      latencyReverse: integer
      listenerError: string
      connectorError: string
      traceRouters?: string[]
      traceSites?: string[]
    }[]
 }
```

### #/components/schemas/ConnectionResponse

```typescript
{
  results: #/components/schemas/baseRecord & {
     duration: integer
     processPairId: string
     componentPairId: string
     sitePairId: string
     sourceSiteId: string
     sourceSiteName: string
     destSiteId: string
     destSiteName: string
     sourceProcessId: string
     sourceProcessName: string
     destProcessId: string
     destProcessName: string
     routingKey: string
     protocol: string
     listenerId: string
     connectorId: string
     sourceHost: string
     sourcePort: string
     destHost: string
     destPort: string
     proxyHost: string
     proxyPort: string
     octetCount: integer
     octetReverseCount: integer
     latency: integer
     latencyReverse: integer
     listenerError: string
     connectorError: string
     traceRouters?: string[]
     traceSites?: string[]
   }
}
```

### #/components/schemas/ApplicationFlowResponse

```typescript
undefined?: #/components/schemas/collectionResponse & {
   results?: #/components/schemas/baseRecord & {
      connectionId: string
      duration: integer
      sourceSiteId: string
      sourceSiteName: string
      destSiteId: string
      destSiteName: string
      sourceProcessId: string
      sourceProcessName: string
      destProcessId: string
      destProcessName: string
      routingKey: string
      protocol: string
      method: string
      status: string
      octetCount: integer
      octetReverseCount: integer
      traceRouters?: string[]
      traceSites?: string[]
    }[]
 }
```

### #/components/schemas/baseRecord

```typescript
{
  // The unique identifier for the record.
  identity: string
  // The creation time in microseconds of the record in Unix timestamp format. The value 0 means that the record is not terminated
  startTime: integer
  // The end time in microseconds of the record in Unix timestamp format.
  endTime: integer
}
```

### #/components/schemas/sitePlatformType

```typescript
// The platform used for the site.
enum[kubernetes, podman, docker, linux, unknown]
```

### #/components/schemas/processBindingType

```typescript
// Indicates whether a process is exposed or not in a skupper network
enum[bound, unbound]
```

### #/components/schemas/serviceIdentifierType

```typescript
// a special string for identifying services uses the form `name@identity@protocol`
string
```

### #/components/schemas/linkRoleType

```typescript
// The class of skupper link
enum[inter-router, edge, unknown]
```

### #/components/schemas/proxyProtocolType

```typescript
// The proxy protocol used when the link connection is established.
enum[NONE, HTTP]
```

### #/components/schemas/SiteRecord

```typescript
undefined?: #/components/schemas/baseRecord & {
   // Possible values are 'AWS', 'IBM', 'Azure' ecc. Can be any string or 'unknown'
   provider: string
   // The platform used for the site.
   platform: enum[kubernetes, podman, docker, linux, unknown]
   name: string
   namespace: string
   // The current skupper version installed. Can be any string or 'unknown'
   version: string
   routerCount: integer
 }
```

### #/components/schemas/ProcessRecord

```typescript
undefined?: #/components/schemas/baseRecord & {
   name: string
   // Id of the site associated to the process.
   siteId: string
   siteName: string
   // Id of the component associated to the process.
   componentId: string
   componentName: string
   // The IP address of the pod within the Kubernetes cluster
   hostName: string
   // The IP address of the node where the pod is running
   sourceHost: string
   imageName: string
   // Internal processes are processes related to Skupper. Remote processes are processes indirectly connected, such as a proxy
   role: enum[internal, external, remote]
   // Indicates whether a process is exposed or not in a skupper network
   binding: enum[bound, unbound]
   // a special string for identifying services uses the form `name@identity@protocol`
   services?: string[]
 }
```

### #/components/schemas/RouterRecord

```typescript
undefined?: #/components/schemas/baseRecord & {
   siteId: string
   name: string
   mode: string
   namespace?: string
   imageName: string
   imageVersion: string
   hostName: string
   buildVersion: string
 }
```

### #/components/schemas/ListenerRecord

```typescript
undefined?: #/components/schemas/baseRecord & {
   routerId: string
   name: string
   destHost: string
   destPort: string
   protocol: string
   routingKey: string
   serviceId?: string
   siteId: string
   siteName: string
 }
```

### #/components/schemas/ConnectorRecord

```typescript
undefined?: #/components/schemas/baseRecord & {
   routerId: string
   name: string
   destHost: string
   destPort: string
   protocol: string
   routingKey: string
   serviceId?: string
   processId: string
   target: string
   siteId: string
   siteName: string
 }
```

### #/components/schemas/ServiceRecord

```typescript
undefined?: #/components/schemas/baseRecord & {
   name: string
   protocol: string
   observedApplicationProtocols?: string[]
   listenerCount: integer
   connectorCount: integer
   // true when there are both listeners and connectors configured
   isBound: boolean
   // true when there is at least one listener for this routingKey
   hasListener: boolean
 }
```

### #/components/schemas/ComponentRecord

```typescript
undefined?: #/components/schemas/baseRecord & {
   name: string
   role: string
   processCount: integer
 }
```

### #/components/schemas/flowAggregatePairType

```typescript
enum[SITE, PROCESS, PROCESS_GROUP]
```

### #/components/schemas/FlowAggregateRecord

```typescript
undefined?: #/components/schemas/baseRecord & {
   pairType: enum[SITE, PROCESS, PROCESS_GROUP]
   recordCount: integer
   sourceId: string
   destinationId: string
   sourceName: string
   destinationName: string
   sourceSiteId?: string
   destinationSiteId?: string
   sourceSiteName?: string
   destinationSiteName?: string
   protocol: string
 }
```

### #/components/schemas/operStatusType

```typescript
enum[up, down]
```

### #/components/schemas/RouterLinkRecord

```typescript
undefined?: #/components/schemas/baseRecord & {
   routerId: string
   routerName: string
   name: string
   // When connected, cost will be set to the link cost attribute
   cost: integer
   // The class of skupper link
   role: enum[inter-router, edge, unknown]
   status: enum[up, down]
   octetCount: integer
   octetReverseCount: integer
   // When connected, the identity of the destitation (peer) router access.
   routerAccessId: string
   // When connected, the identity of the destitation (peer) router.
   destinationRouterId: string
   // When connected, the name of the destitation (peer) router.
   destinationRouterName: string
   sourceSiteId: string
   sourceSiteName: string
   // When connected, the identity of the destitation (peer) site.
   destinationSiteId: string
   // When connected, the name of the destitation (peer) site.
   destinationSiteName: string
   proxyProtocol?: #/components/schemas/proxyProtocolType
 }
```

### #/components/schemas/RouterAccessRecord

```typescript
undefined?: #/components/schemas/baseRecord & {
   routerId: string
   name: string
   linkCount: integer
   role: string
 }
```

### #/components/schemas/ConnectionRecord

```typescript
undefined?: #/components/schemas/baseRecord & {
   duration: integer
   processPairId: string
   componentPairId: string
   sitePairId: string
   sourceSiteId: string
   sourceSiteName: string
   destSiteId: string
   destSiteName: string
   sourceProcessId: string
   sourceProcessName: string
   destProcessId: string
   destProcessName: string
   routingKey: string
   protocol: string
   listenerId: string
   connectorId: string
   sourceHost: string
   sourcePort: string
   destHost: string
   destPort: string
   proxyHost: string
   proxyPort: string
   octetCount: integer
   octetReverseCount: integer
   latency: integer
   latencyReverse: integer
   listenerError: string
   connectorError: string
   traceRouters?: string[]
   traceSites?: string[]
 }
```

### #/components/schemas/ApplicationFlowRecord

```typescript
undefined?: #/components/schemas/baseRecord & {
   connectionId: string
   duration: integer
   sourceSiteId: string
   sourceSiteName: string
   destSiteId: string
   destSiteName: string
   sourceProcessId: string
   sourceProcessName: string
   destProcessId: string
   destProcessName: string
   routingKey: string
   protocol: string
   method: string
   status: string
   octetCount: integer
   octetReverseCount: integer
   traceRouters?: string[]
   traceSites?: string[]
 }
```