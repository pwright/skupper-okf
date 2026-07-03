set shell := ["bash", "-eu", "-o", "pipefail", "-c"]

blockscape_base_url := "https://github.com/pwright/skupper-okf/blob/main/"

# List available commands
_default:
    just --list

# Create directories and fetch configured human source snapshots
init:
    ./scripts/init-layout.sh
    ./scripts/sync-human-skupper-docs.sh
    ./scripts/sync-human-skupper-example-hello-world.sh

# Create directories only
layout:
    ./scripts/init-layout.sh

# Refresh all configured human source snapshots
sync-human:
    ./scripts/sync-human-skupper-docs.sh
    ./scripts/sync-human-skupper-example-hello-world.sh

# Dry-run all human source sync scripts
sync-human-dry-run:
    ./scripts/sync-human-skupper-docs.sh --dry-run
    ./scripts/sync-human-skupper-example-hello-world.sh --dry-run

# Refresh human/skupper-docs/ from skupper-docs main
sync-human-skupper-docs:
    ./scripts/sync-human-skupper-docs.sh

# Refresh human/skupper-example-hello-world/ from skupper-example-hello-world main
sync-human-example-hello-world:
    ./scripts/sync-human-skupper-example-hello-world.sh

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
