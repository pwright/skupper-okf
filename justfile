set shell := ["bash", "-eu", "-o", "pipefail", "-c"]

blockscape_base_url := "https://github.com/pwright/skupper-okf/blob/main/"

# List available commands
_default:
    just --list

# Create directories and fetch skupper-docs into human/
init:
    ./scripts/init-layout.sh
    ./scripts/sync-human-skupper-docs.sh

# Create directories only
layout:
    ./scripts/init-layout.sh

# Refresh human/ from skupper-docs main
sync-human:
    ./scripts/sync-human-skupper-docs.sh

# Dry-run the sync script
sync-human-dry-run:
    ./scripts/sync-human-skupper-docs.sh --dry-run

# Build an offline test fixture and validate behavior without network
test:
    ./tests/smoke-test.sh

# Print the expected tree for the MVP
show-expected-layout:
    cat tests/golden/expected-layout.txt

# Print current top-level tree without requiring tree(1)
tree:
    find . -maxdepth 3 -type d -print | sort

# Print the base URL used for Blockscape external links
blockscape-base-url:
    @echo {{blockscape_base_url}}
