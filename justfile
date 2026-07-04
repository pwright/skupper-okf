set shell := ["bash", "-eu", "-o", "pipefail", "-c"]

blockscape_base_url := "https://pwright.github.io/skupper-okf/"
blockscape_raw_base_url := "https://raw.githubusercontent.com/pwright/skupper-okf/refs/heads/main/"
blockscape_app_base_url := "https://pwright.github.io/blockscape/"

# List available commands
_default:
    just --list

# Create directories and fetch configured human source snapshots
init:
    ./scripts/init-layout.sh
    ./scripts/sync-human-skupper-docs.sh
    ./scripts/sync-human-skupper-example-hello-world.sh
    ./scripts/sync-human-skupper-example-grpc.sh
    ./scripts/sync-human-skupper.sh
    ./scripts/generate-api-docs.sh
    ./scripts/sync-human-skupper-console.sh
    ./scripts/extract-console-api-calls.sh
    ./scripts/sync-human-skupper-router.sh
    ./scripts/copy-router-markdown.sh

# Create directories only
layout:
    ./scripts/init-layout.sh

# Refresh all configured human source snapshots
sync-human:
    ./scripts/sync-human-skupper-docs.sh
    ./scripts/sync-human-skupper-example-hello-world.sh
    ./scripts/sync-human-skupper-example-grpc.sh
    ./scripts/sync-human-skupper.sh
    ./scripts/generate-api-docs.sh
    ./scripts/sync-human-skupper-console.sh
    ./scripts/extract-console-api-calls.sh
    ./scripts/sync-human-skupper-router.sh
    ./scripts/copy-router-markdown.sh

# Dry-run all human source sync scripts
sync-human-dry-run:
    ./scripts/sync-human-skupper-docs.sh --dry-run
    ./scripts/sync-human-skupper-example-hello-world.sh --dry-run
    ./scripts/sync-human-skupper-example-grpc.sh --dry-run
    ./scripts/sync-human-skupper.sh --dry-run
    ./scripts/generate-api-docs.sh --dry-run
    ./scripts/sync-human-skupper-console.sh --dry-run
    ./scripts/extract-console-api-calls.sh --dry-run
    ./scripts/sync-human-skupper-router.sh --dry-run
    ./scripts/copy-router-markdown.sh --dry-run

# Refresh human/skupper-docs/ from skupper-docs main
sync-human-skupper-docs:
    ./scripts/sync-human-skupper-docs.sh

# Refresh human/skupper-example-hello-world/ from skupper-example-hello-world main
sync-human-example-hello-world:
    ./scripts/sync-human-skupper-example-hello-world.sh

# Refresh human/skupper-example-grpc/ from skupper-example-grpc main
sync-human-example-grpc:
    ./scripts/sync-human-skupper-example-grpc.sh

# Refresh human/skupper/ (full repo clone) for API and CRD doc generation
sync-human-skupper:
    ./scripts/sync-human-skupper.sh

# Generate API and CRD documentation from human/skupper/ to sources/
generate-api-docs:
    ./scripts/generate-api-docs.sh

# Refresh human/skupper-console/ (full repo clone) for console API extraction
sync-human-skupper-console:
    ./scripts/sync-human-skupper-console.sh

# Extract and document API calls from human/skupper-console/ to sources/console.md
extract-console-api-calls:
    ./scripts/extract-console-api-calls.sh

# Refresh human/skupper-router/ (full repo clone) for markdown extraction
sync-human-skupper-router:
    ./scripts/sync-human-skupper-router.sh

# Copy markdown files from human/skupper-router/ to sources/
copy-router-markdown:
    ./scripts/copy-router-markdown.sh

# Build an offline test fixture and validate behavior without network
test:
    ./tests/smoke-test.sh

# Print unique tags from Markdown front matter
tags *paths:
    @./scripts/extract-frontmatter-tags.py {{paths}}

# Wrap Blockscape maps as generated Markdown pages
maps:
    ./tools/update-generated-maps.py --input maps --output generated/maps --source-base-url {{blockscape_raw_base_url}} --blockscape-base-url {{blockscape_app_base_url}}

# Stage publishable OKF content into Quartz
quartz-stage: maps
    python3 tools/stage-quartz-content.py --input generated --input reviewed --input sources --output quartz/content --link-map linkmap.yaml

# Build the Quartz static site
quartz-build: quartz-stage
    cd quartz && node quartz/bootstrap-cli.mjs build

# Serve the Quartz site locally
quartz-serve: quartz-stage
    cd quartz && node quartz/bootstrap-cli.mjs build --serve

# Remove Quartz staged content and build output
quartz-clean:
    rm -rf quartz/content
    mkdir -p quartz/content
    touch quartz/content/.gitkeep
    rm -rf quartz/public

# Print the expected tree for the MVP
show-expected-layout:
    cat tests/golden/expected-layout.txt

# Print current top-level tree without requiring tree(1)
tree:
    find . -maxdepth 3 -type d -print | sort

# Print the base URL used for Blockscape external links
blockscape-base-url:
    @echo {{blockscape_base_url}}
