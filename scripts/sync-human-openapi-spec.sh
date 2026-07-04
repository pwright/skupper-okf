#!/usr/bin/env bash
set -Eeuo pipefail

source_url="https://raw.githubusercontent.com/skupperproject/skupper/main/cmd/network-observer/spec/openapi.yaml"
dest="human/skupper-openapi-spec"
sources_dir="sources"
source_name="skupper-openapi-spec"
source_title="Skupper Network Observer OpenAPI Specification"
dry_run="false"

log() {
  printf 'sync-human-openapi: %s\n' "$*" >&2
}

die() {
  printf 'sync-human-openapi: ERROR: %s\n' "$*" >&2
  exit 1
}

usage() {
  cat <<'DOC'
Usage:
  sync-human-openapi-spec.sh [options]

Fetch the Skupper Network Observer OpenAPI specification and populate the local
human/skupper-openapi-spec/ directory with the latest version.

Options:
  --url URL          Raw file URL, default: https://raw.githubusercontent.com/skupperproject/skupper/main/cmd/network-observer/spec/openapi.yaml
  --dest DIR         Destination directory, default: human/skupper-openapi-spec
  --sources-dir DIR  Provenance directory, default: sources
  --dry-run          Show what would happen without modifying files
  -h, --help         Show help

Stdout:
  Prints 'success' on successful fetch.

Stderr:
  Progress and diagnostic messages.
DOC
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --url)
      source_url="${2:-}"
      shift 2
      ;;
    --dest)
      dest="${2:-}"
      shift 2
      ;;
    --sources-dir)
      sources_dir="${2:-}"
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

[[ -n "$source_url" ]] || die "--url must not be empty"
[[ -n "$dest" ]] || die "--dest must not be empty"
[[ -n "$sources_dir" ]] || die "--sources-dir must not be empty"

case "$dest" in
  /|.|..|human|"" )
    die "refusing unsafe destination: $dest"
    ;;
esac

command -v curl >/dev/null 2>&1 || die "curl is required"

log "source URL: $source_url"
log "destination: $dest"

if [[ "$dry_run" == "true" ]]; then
  log "dry run enabled; no files changed"
  printf 'dry-run\n'
  exit 0
fi

retrieved_at="$(date -u +"%Y-%m-%dT%H:%M:%SZ")"

mkdir -p "$dest" "$sources_dir"

log "fetching OpenAPI spec"
curl -fsSL "$source_url" -o "$dest/openapi.yaml" || die "failed to fetch from $source_url"

log "generating markdown from OpenAPI spec"
if command -v npx >/dev/null 2>&1; then
  npx --yes openapi-to-md "$dest/openapi.yaml" "$dest/api-reference.md" || log "warning: openapi-to-md failed, continuing anyway"

  # Copy the generated API reference to sources/ for publication
  if [[ -f "$dest/api-reference.md" ]]; then
    cp "$dest/api-reference.md" "$sources_dir/skupper-openapi-spec-api-reference.md"
    log "copied api-reference.md to $sources_dir/"
  fi
else
  log "warning: npx not found, skipping markdown generation"
fi

cat > "$dest/_source.md" <<DOC
---
type: SourceSnapshot
title: $source_title
source_url: $source_url
retrieved_at: $retrieved_at
status: human-source-snapshot
---

# $source_title

This directory contains the Skupper Network Observer OpenAPI specification.

Do not edit this directory directly. Refresh it with:

\`\`\`bash
./scripts/sync-human-openapi-spec.sh
\`\`\`
DOC

cat > "$sources_dir/$source_name.md" <<DOC
---
type: SourceFile
title: $source_title
id: source-$source_name
url: $source_url
retrieved_at: $retrieved_at
local_snapshot: ../$dest
---

# $source_title

This source entry records the OpenAPI spec used to populate \`$dest/\`.

- URL: \`$source_url\`
- Retrieved: \`$retrieved_at\`
- Local snapshot: \`../$dest/openapi.yaml\`

## Description

The Skupper network observer exposes a read-only HTTP API. This API is used
by the network console frontend to display information about a skupper network.
DOC

log "wrote $dest/openapi.yaml"
log "wrote $dest/_source.md"
log "wrote $sources_dir/$source_name.md"
printf 'success\n'
