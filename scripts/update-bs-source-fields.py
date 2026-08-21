#!/usr/bin/env python3
"""
Add source and external fields to Blockscape .bs files
Pattern:
  "source": "generated/{directory}/{item-id}.md",
  "external": "https://pwright.github.io/skupper-okf/generated/{directory}/{item-id}"
"""

import json
import sys

def update_bs_file(filepath, directory):
    """Add source and external fields to all items in a .bs file"""

    with open(filepath, 'r') as f:
        data = json.load(f)

    changes_made = 0

    for map_obj in data.get('maps', []):
        for category in map_obj.get('categories', []):
            for item in category.get('items', []):
                item_id = item.get('id')
                if not item_id:
                    continue

                # Add source field if missing
                if 'source' not in item:
                    item['source'] = f"generated/{directory}/{item_id}.md"
                    changes_made += 1

                # Add external field if missing
                if 'external' not in item:
                    item['external'] = f"https://pwright.github.io/skupper-okf/generated/{directory}/{item_id}"
                    changes_made += 1

    # Write back with pretty formatting (2-space indent)
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write('\n')  # Add trailing newline

    return changes_made

def main():
    print("Updating Blockscape .bs files with source and external fields...")
    print()

    # Update skupper-adoption-bridge.bs
    file1 = "maps/skupper-adoption-bridge.bs"
    changes1 = update_bs_file(file1, "skupper-adoption-bridge")
    print(f"✅ {file1}: {changes1} fields added")

    # Update skupper-value-perspectives.bs
    file2 = "maps/skupper-value-perspectives.bs"
    changes2 = update_bs_file(file2, "skupper-value-perspectives")
    print(f"✅ {file2}: {changes2} fields added")

    print()
    print(f"Total: {changes1 + changes2} fields added")
    print()
    print("Note: Items that already referenced existing docs (e.g., in skupper-docs-landscape)")
    print("      kept their original source paths. Only new items got updated.")

if __name__ == '__main__':
    main()
