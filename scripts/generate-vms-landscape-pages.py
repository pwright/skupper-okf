#!/usr/bin/env python3
"""Generate markdown pages for VMS landscape items."""

import json
import os
from datetime import datetime, timezone
from pathlib import Path

def load_vms_maps(maps_file):
    """Load VMS Blockscape maps."""
    with open(maps_file, 'r') as f:
        return json.load(f)

def is_manual_task(item):
    """Check if item is a manual task (white color)."""
    return item.get('color') == '#FFFFFF'

def find_parent_map_and_category(item_id, maps):
    """Find which map and category contains this item."""
    for map_obj in maps:
        for category in map_obj.get('categories', []):
            for item in category.get('items', []):
                if item.get('id') == item_id:
                    return map_obj.get('title'), category.get('title')
    return None, None

def generate_topics_section(item, maps):
    """Generate Topics section based on dependencies."""
    deps = item.get('deps', [])
    if not deps:
        return "## Topics\n\n- This item has no documented dependencies.\n"

    # Group deps by type if possible, or just list them
    topics = "## Topics\n\n### Dependencies\n\n"
    for dep_id in deps:
        # Find the dep item to get its name
        dep_name = None
        for map_obj in maps:
            for category in map_obj.get('categories', []):
                for dep_item in category.get('items', []):
                    if dep_item.get('id') == dep_id:
                        dep_name = dep_item.get('name')
                        break
                if dep_name:
                    break
            if dep_name:
                break

        if dep_name:
            topics += f"- [{dep_name}](./{dep_id}.md)\n"
        else:
            topics += f"- {dep_id}\n"

    return topics

def generate_markdown(item, parent_map, parent_category, maps, output_dir):
    """Generate markdown file for an item."""
    item_id = item.get('id')
    title = item.get('name')
    abstract = item.get('abstract', 'No description available.')

    timestamp = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')

    # Build frontmatter
    frontmatter = f"""---
type: VmsLandscapePage
title: "{title}"
id: {item_id}
status: generated
owner: agent
generated_by: generate-vms-landscape-pages.py
reviewed: false
confidence: stub
source: blockscape-json
external: https://pwright.github.io/skupper-okf/generated/vms/{item_id}
tags:
  - vms
  - vms-landscape
timestamp: {timestamp}
---
"""

    # Build content
    content = f"""# {title}

{abstract}

## Appears in

- [{parent_map}](./vms-overview.md) / {parent_category}

{generate_topics_section(item, maps)}

## Notes

- TODO: Expand with detailed documentation content from VMS source materials.
"""

    # Write file
    output_file = output_dir / f"{item_id}.md"
    with open(output_file, 'w') as f:
        f.write(frontmatter + content)

    return output_file

def main():
    """Main entry point."""
    script_dir = Path(__file__).parent
    repo_root = script_dir.parent
    maps_file = repo_root / 'maps' / 'vms.bs'
    output_dir = repo_root / 'generated' / 'vms'

    # Create output directory
    output_dir.mkdir(parents=True, exist_ok=True)

    # Load maps
    maps = load_vms_maps(maps_file)

    # Generate markdown for each non-manual item
    generated_count = 0
    skipped_count = 0

    for map_obj in maps:
        for category in map_obj.get('categories', []):
            for item in category.get('items', []):
                if 'id' not in item or 'name' not in item:
                    continue

                if is_manual_task(item):
                    skipped_count += 1
                    continue

                parent_map, parent_category = find_parent_map_and_category(
                    item['id'], maps
                )

                if parent_map and parent_category:
                    output_file = generate_markdown(
                        item, parent_map, parent_category, maps, output_dir
                    )
                    generated_count += 1
                    print(f"Generated: {output_file.name}")

    print(f"\nSummary:")
    print(f"  Generated: {generated_count} markdown files")
    print(f"  Skipped (manual tasks): {skipped_count} items")
    print(f"  Output: {output_dir}")

if __name__ == '__main__':
    main()
