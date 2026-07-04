#!/usr/bin/env bash
set -Eeuo pipefail

source_repo="human/skupper"
output_dir="generated/skupper"
dry_run="false"

log() {
  printf 'generate-api-docs: %s\n' "$*" >&2
}

die() {
  printf 'generate-api-docs: ERROR: %s\n' "$*" >&2
  exit 1
}

usage() {
  cat <<'DOC'
Usage:
  generate-api-docs.sh [options]

Generate documentation from API specs and CRDs in the skupper repository clone.

Options:
  --source-repo DIR  Source repository directory, default: human/skupper
  --output-dir DIR   Output directory for generated docs, default: generated/skupper
  --dry-run          Show what would happen without modifying files
  -h, --help         Show help

Stdout:
  Prints 'success' on successful generation.

Stderr:
  Progress and diagnostic messages.

Requirements:
  - npx (for openapi-to-md)
  - yq (for CRD parsing, optional)

Generates:
  - generated/skupper/skupper-api-*.md (from OpenAPI specs)
  - generated/skupper/skupper-crd-*.md (from CRD YAML files)
DOC
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --source-repo)
      source_repo="${2:-}"
      shift 2
      ;;
    --output-dir)
      output_dir="${2:-}"
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
[[ -n "$output_dir" ]] || die "--output-dir must not be empty"
[[ -d "$source_repo" ]] || die "source repository not found: $source_repo (run sync-human-skupper.sh first)"

if [[ "$dry_run" == "true" ]]; then
  log "dry run enabled; no files changed"
  printf 'dry-run\n'
  exit 0
fi

generated_at="$(date -u +"%Y-%m-%dT%H:%M:%SZ")"
mkdir -p "$output_dir"

generated_count=0

# Generate documentation from OpenAPI specs
log "searching for OpenAPI specs"
while IFS= read -r -d '' spec_file; do
  log "found OpenAPI spec: $spec_file"

  # Derive a sensible name from the path
  # e.g., cmd/network-observer/spec/openapi.yaml -> network-observer
  base_name=$(echo "$spec_file" | sed -E 's|.*/([^/]+)/spec/openapi\.yaml|\1|' | tr '/' '-')
  if [[ "$base_name" == "$spec_file" ]]; then
    # Fallback if pattern doesn't match
    base_name=$(basename "$(dirname "$spec_file")")
  fi

  output_name="skupper-api-${base_name}"

  if command -v npx >/dev/null 2>&1; then
    log "generating markdown for $base_name"

    # Generate markdown from OpenAPI spec
    npx --yes openapi-to-md "$spec_file" "${output_dir}/${output_name}.md.tmp" || {
      log "warning: openapi-to-md failed for $spec_file, skipping"
      continue
    }

    # Add frontmatter
    cat > "${output_dir}/${output_name}.md" <<DOC
---
type: GeneratedDocs
title: Skupper API - ${base_name}
id: ${output_name}
source_file: ../$spec_file
generated_at: $generated_at
generator: openapi-to-md
---

DOC
    cat "${output_dir}/${output_name}.md.tmp" >> "${output_dir}/${output_name}.md"
    rm -f "${output_dir}/${output_name}.md.tmp"

    log "wrote ${output_dir}/${output_name}.md"
    : $((generated_count++))
  else
    log "warning: npx not found, skipping OpenAPI generation"
    break
  fi
done < <(find "$source_repo" -name "openapi.yaml" -print0 || true)

# Generate documentation from CRDs
log "searching for CRDs"
crd_search_paths=(
  "$source_repo/config/crd/bases"
  "$source_repo/config/crd"
  "$source_repo/deploy/crds"
)

for search_path in "${crd_search_paths[@]}"; do
  if [[ ! -d "$search_path" ]]; then
    continue
  fi

  while IFS= read -r crd_file; do
    log "found CRD: $crd_file"

    # Extract CRD name from the file
    # CRDs typically have kind: CustomResourceDefinition
    if ! grep -q "kind: CustomResourceDefinition" "$crd_file" 2>/dev/null; then
      log "skipping non-CRD file: $crd_file"
      continue
    fi

    # Try to extract the resource name (e.g., skuppers.skupper.io)
    crd_name=$(grep "^  name:" "$crd_file" | head -1 | sed 's/.*name: *//' | tr '.' '-')

    if [[ -z "$crd_name" ]]; then
      crd_name=$(basename "$crd_file" .yaml | sed 's/_crd$//')
    fi

    output_name="skupper-crd-${crd_name}"

    # Create a basic markdown representation
    cat > "${output_dir}/${output_name}.md" <<DOC
---
type: GeneratedDocs
title: Skupper CRD - ${crd_name}
id: ${output_name}
source_file: ../$crd_file
generated_at: $generated_at
generator: manual
---

# Skupper CRD: ${crd_name}

Source: \`$crd_file\`

\`\`\`yaml
DOC

    cat "$crd_file" >> "${output_dir}/${output_name}.md"

    cat >> "${output_dir}/${output_name}.md" <<DOC
\`\`\`
DOC

    log "wrote ${output_dir}/${output_name}.md"
    : $((generated_count++))
  done < <(find "$search_path" -maxdepth 1 \( -name "*_crd.yaml" -o -name "*-crd.yaml" \) 2>/dev/null || true)
done

if [[ $generated_count -eq 0 ]]; then
  log "warning: no API specs or CRDs found"
  printf 'no-docs-generated\n'
else
  log "generated $generated_count documentation files"
  printf 'success\n'
fi
