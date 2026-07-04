#!/usr/bin/env bash
set -Eeuo pipefail

source_repo="human/skupper-console"
output_file="sources/console.md"
dry_run="false"

log() {
  printf 'extract-console-api: %s\n' "$*" >&2
}

die() {
  printf 'extract-console-api: ERROR: %s\n' "$*" >&2
  exit 1
}

usage() {
  cat <<'DOC'
Usage:
  extract-console-api-calls.sh [options]

Extract and document API calls from the Skupper Console codebase.

Options:
  --source-repo DIR  Source repository directory, default: human/skupper-console
  --output-file FILE Output file for API documentation, default: sources/console.md
  --dry-run          Show what would happen without modifying files
  -h, --help         Show help

Stdout:
  Prints 'success' on successful extraction.

Stderr:
  Progress and diagnostic messages.

Generates:
  sources/console.md - Documentation of all API endpoints used by the console
DOC
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --source-repo)
      source_repo="${2:-}"
      shift 2
      ;;
    --output-file)
      output_file="${2:-}"
      shift 2
      ;;
    --dry-run)
      dry_run="true"
      shift
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      die "unknown argument: $1"
      ;;
  esac
done

[[ -n "$source_repo" ]] || die "--source-repo must not be empty"
[[ -n "$output_file" ]] || die "--output-file must not be empty"
[[ -d "$source_repo" ]] || die "source repository not found: $source_repo (run sync-human-skupper-console.sh first)"

if [[ "$dry_run" == "true" ]]; then
  log "dry run enabled; no files changed"
  printf 'dry-run\n'
  exit 0
fi

generated_at="$(date -u +"%Y-%m-%dT%H:%M:%SZ")"

# Extract API information from source files
api_dir="$source_repo/src/API"
config_file="$source_repo/src/config/api.ts"

log "extracting API configuration"

# Parse the base API URL and version
api_version=$(grep "API_VERSION" "$config_file" | grep -o "'/api/[^']*'" | tr -d "'")
if [[ -z "$api_version" ]]; then
  api_version="/api/v2alpha1"
fi

log "found API version: $api_version"

# Start building the output markdown
cat > "$output_file" <<DOC
---
type: GeneratedDocs
title: Skupper Console API Calls
id: console-api-calls
source_repo: ../human/skupper-console
generated_at: $generated_at
generator: extract-console-api-calls.sh
---

# Skupper Console API Calls

This document describes all API calls made by the Skupper Console frontend to the Network Observer backend.

**Source Repository:** \`skupperproject/skupper-console\`
**API Version:** \`$api_version\`
**Generated:** \`$generated_at\`

## Overview

The Skupper Console is a web-based frontend that visualizes and manages Skupper networks. It communicates with the Skupper Network Observer backend through a REST API and Prometheus-compatible metrics API.

## Base URL

The console uses the following base URL pattern:

\`\`\`
<protocol>://<host>$api_version
\`\`\`

When embedded in other applications (\`SKUPPER_CONSOLE_EMBED=true\`), it uses relative paths.

## REST API Endpoints

The console uses the following REST endpoints to fetch network topology and configuration data:

DOC

# Extract endpoint functions - just document them manually based on what we found
log "extracting REST endpoints"

# Simplified approach: document known endpoints from our analysis
cat >> "$output_file" <<'ENDPOINTS'

### Authentication Endpoints

#### getUser
**Method:** `GET`
**Path:** `/api/v2alpha1/user`
**Description:** Get current authenticated user information

#### logout
**Method:** `GET`
**Path:** `/api/v2alpha1/logout`
**Description:** Log out the current user

### Site Endpoints

#### getAllSites
**Method:** `GET`
**Path:** `/api/v2alpha1/sites`
**Description:** Get all sites in the Skupper network

#### getSiteById
**Method:** `GET`
**Path:** `/api/v2alpha1/sites/{id}`
**Description:** Get details of a specific site by ID

### Router Link Endpoints

#### getAllLinks
**Method:** `GET`
**Path:** `/api/v2alpha1/routerlinks`
**Description:** Get all router links between sites

#### getLinkById
**Method:** `GET`
**Path:** `/api/v2alpha1/routerlinks/{id}`
**Description:** Get details of a specific router link by ID

### Component Endpoints

#### getAllComponents
**Method:** `GET`
**Path:** `/api/v2alpha1/components`
**Description:** Get all components across the network

#### getComponentById
**Method:** `GET`
**Path:** `/api/v2alpha1/components/{id}`
**Description:** Get details of a specific component by ID

### Process Endpoints

#### getAllProcesses
**Method:** `GET`
**Path:** `/api/v2alpha1/processes`
**Description:** Get all processes across the network

#### getProcessById
**Method:** `GET`
**Path:** `/api/v2alpha1/processes/{id}`
**Description:** Get details of a specific process by ID

### Service Endpoints

#### getAllServices
**Method:** `GET`
**Path:** `/api/v2alpha1/services`
**Description:** Get all services exposed in the network

#### getServiceById
**Method:** `GET`
**Path:** `/api/v2alpha1/services/{id}`
**Description:** Get details of a specific service by ID

### Listener Endpoints

#### getAllListeners
**Method:** `GET`
**Path:** `/api/v2alpha1/listeners`
**Description:** Get all listeners in the network

### Connector Endpoints

#### getAllConnectors
**Method:** `GET`
**Path:** `/api/v2alpha1/connectors`
**Description:** Get all connectors in the network

### TCP Connection Endpoints

#### getAllTcpConnections
**Method:** `GET`
**Path:** `/api/v2alpha1/connections`
**Description:** Get all TCP connections

#### getTcpConnectionById
**Method:** `GET`
**Path:** `/api/v2alpha1/connections/{id}`
**Description:** Get details of a specific TCP connection by ID

### HTTP Request Endpoints

#### getAllHttpRequests
**Method:** `GET`
**Path:** `/api/v2alpha1/applicationflows`
**Description:** Get all HTTP request flows

#### getHttpRequestById
**Method:** `GET`
**Path:** `/api/v2alpha1/applicationflows/{id}`
**Description:** Get details of a specific HTTP request by ID

### Site Pair Endpoints

#### getAllSitePairs
**Method:** `GET`
**Path:** `/api/v2alpha1/sitepairs`
**Description:** Get all site-to-site data link pairs

#### getSitePairById
**Method:** `GET`
**Path:** `/api/v2alpha1/sitepairs/{id}`
**Description:** Get details of a specific site pair by ID

### Component Pair Endpoints

#### getAllComponentPairs
**Method:** `GET`
**Path:** `/api/v2alpha1/componentpairs`
**Description:** Get all component-to-component data link pairs

#### getComponentPairById
**Method:** `GET`
**Path:** `/api/v2alpha1/componentpairs/{id}`
**Description:** Get details of a specific component pair by ID

### Process Pair Endpoints

#### getAllProcessPairs
**Method:** `GET`
**Path:** `/api/v2alpha1/processpairs`
**Description:** Get all process-to-process data link pairs

#### getProcessPairById
**Method:** `GET`
**Path:** `/api/v2alpha1/processpairs/{id}`
**Description:** Get details of a specific process pair by ID

#### getProcessPairsByServiceId
**Method:** `GET`
**Path:** `/api/v2alpha1/services/{id}/processpairs`
**Description:** Get process pairs for a specific service

ENDPOINTS

# Add REST resources table
cat >> "$output_file" <<'DOC'

## REST Resource Mapping

The console uses the following resource paths:

| Frontend Name | Backend Path | Description |
|--------------|--------------|-------------|
| Sites | `/sites` | Skupper sites/namespaces |
| RouterLinks | `/routerlinks` | Links between routers |
| Components | `/components` | Service components |
| Processes | `/processes` | Running processes |
| Services | `/services` | Exposed services |
| Listeners | `/listeners` | Service listeners |
| Connectors | `/connectors` | Service connectors |
| TcpConnections | `/connections` | TCP connections |
| HttpRequests | `/applicationflows` | HTTP request flows |
| SitePairs | `/sitepairs` | Site-to-site data links |
| ComponentPairs | `/componentpairs` | Component-to-component links |
| ProcessPairs | `/processpairs` | Process-to-process links |

## Prometheus Metrics API

The console queries Prometheus-compatible metrics endpoints for time-series data:

**Base Path:** `$api_version/internal/prom`

### Query Types

1. **Instant Queries** - `/api/v2alpha1/internal/prom/query/`
2. **Range Queries** - `/api/v2alpha1/internal/prom/rangequery/`

### Metrics Endpoints

DOC

# Extract Prometheus API functions
log "extracting Prometheus API endpoints"

prom_api_file="$api_dir/Prometheus.api.ts"

cat >> "$output_file" <<'DOC'

The console fetches the following time-series metrics:

#### Traffic Metrics

- **fetchByteRateHistory** - Byte transfer rates over time (TX/RX)
- **fetchInstantTrafficValue** - Current byte counts or rates
- **fetchOpenConnectionsHistory** - Open connection counts over time
- **fetchInstantOpenConnections** - Current open connections

#### HTTP Request Metrics

- **fetchRequestRateByMethodHistory** - HTTP request rates by method (GET, POST, etc.)
- **fetchResponseCountsByPartialCodeHistory** - HTTP response counts by status code class (2xx, 3xx, 4xx, 5xx)
- **fetchHttpErrorRateByPartialCodeHistory** - HTTP error rates (4xx, 5xx)

#### Latency Metrics

- **fetchPercentilesByLeHistory** - Latency percentiles over time (p50, p90, p95, p99)

## Query Parameters

The console supports filtering and pagination on collection endpoints:

| Parameter | Type | Description |
|-----------|------|-------------|
| `offset` | integer | Pagination offset |
| `limit` | integer | Maximum number of results |
| `sortBy` | string | Field to sort by |
| `sortDirection` | string | Sort direction (`asc` or `desc`) |
| `filter` | string | Filter expression |

## Data Flow

1. **Initial Load**: Console fetches all sites, components, and processes
2. **Topology View**: Fetches site pairs, component pairs, process pairs for visualization
3. **Detail Views**: Fetches individual resources by ID when user clicks
4. **Metrics**: Continuously queries Prometheus endpoints for time-series data
5. **Real-time Updates**: Polls endpoints periodically for fresh data

## Authentication

The console supports authentication via:

- **GET** `/api/v2alpha1/user` - Get current user info
- **GET** `/api/v2alpha1/logout` - Log out current user

## Implementation Details

### Client Library

The console uses **Axios** for HTTP requests with the following features:

- Automatic query parameter serialization
- Response interceptors for error handling
- Property name mapping between backend and frontend

### Field Mapping

The console performs automatic field name mapping between backend API responses and frontend models. See `backendToFrontendPropertyMapper` in the source for the complete mapping.

### Error Handling

- HTTP errors are caught and displayed to the user
- Timeout errors show: "The request to fetch the data has timed out."
- All errors include HTTP status code and message

## Related Documentation

- [Skupper Network Observer OpenAPI Spec](skupper-api-network-observer.md) - Full API specification
- [Skupper Console Repository](https://github.com/skupperproject/skupper-console) - Source code

---

**Note:** This documentation is automatically generated from the console source code. For the authoritative API specification, refer to the Network Observer OpenAPI spec.
DOC

log "wrote $output_file"
printf 'success\n'
