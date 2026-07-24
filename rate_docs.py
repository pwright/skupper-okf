#!/usr/bin/env python3
"""
Add documentation quality ratings to Skupper docs landscape.
Reads generated docs to determine ratings based on actual content indicators.

Usage:
    python3 rate_docs.py              # Rate all items + aggregate
    python3 rate_docs.py --aggregate  # Only update aggregates (preserve existing ratings)
"""

import json
import re
import sys
from pathlib import Path
from typing import Dict, Optional

# Base paths
BASE_DIR = Path(__file__).parent
LANDSCAPE_FILE = BASE_DIR / "maps" / "skupper-docs-landscape.bs"
DOCS_DIR = BASE_DIR / "generated" / "skupper-docs-landscape"

# Rating statistics
stats = {
    "total_items": 0,
    "rated_items": 0,
    "no_rating": 0,
    "missing_files": [],
    "errors": []
}


def extract_frontmatter(content: str) -> Dict[str, str]:
    """Extract YAML frontmatter from markdown file."""
    match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    if not match:
        return {}

    frontmatter = {}
    for line in match.group(1).split('\n'):
        if ':' in line:
            key, value = line.split(':', 1)
            frontmatter[key.strip()] = value.strip()

    return frontmatter


def count_human_links(content: str) -> int:
    """Count links to human/ directory (indicates real written docs)."""
    return len(re.findall(r'\bhuman/', content))


def count_external_links(content: str) -> int:
    """Count external website links."""
    # Look for ## Website Links section
    links_match = re.search(r'^## Website Links\s*\n(.*?)(?=\n##|\Z)', content, re.MULTILINE | re.DOTALL)
    if not links_match:
        return 0

    links_section = links_match.group(1)
    link_lines = [line for line in links_section.split('\n') if line.strip().startswith(('- ', '* '))]
    return len(link_lines)


def count_sources(content: str) -> int:
    """Count source references in the markdown file."""
    sources_match = re.search(r'^## Sources\s*\n(.*?)(?=\n##|\Z)', content, re.MULTILINE | re.DOTALL)
    if not sources_match:
        return 0

    sources_section = sources_match.group(1)
    source_lines = [line for line in sources_section.split('\n') if line.strip().startswith(('- ', '* '))]
    return len(source_lines)


def has_specific_draft_notes(content: str) -> bool:
    """Check if draft notes are specific (not just generic TODO)."""
    notes_match = re.search(r'^## Draft Notes\s*\n(.*?)(?=\n##|\Z)', content, re.MULTILINE | re.DOTALL)
    if not notes_match:
        return False

    notes = notes_match.group(1).strip()
    # Check for specific indicators
    specific_indicators = [
        'skupper',  # Mentions specific commands/tools
        'procedure',  # Mentions procedures
        'example',  # Mentions examples
        'verification',  # Mentions verification steps
        'validation',  # Mentions validation
        'prerequisite',  # Mentions prerequisites
        'command',  # Mentions specific commands
        'configuration',  # Mentions configuration
    ]

    notes_lower = notes.lower()
    return any(indicator in notes_lower for indicator in specific_indicators)


def determine_rating(source_path: Path) -> Optional[str]:
    """Determine rating for a documentation file. Returns score string in format (h.e.s.c) or None for stubs."""
    if not source_path.exists():
        stats["missing_files"].append(str(source_path))
        return None

    try:
        content = source_path.read_text()
        frontmatter = extract_frontmatter(content)
        confidence = frontmatter.get('confidence', 'unknown')

        # Stubs get no rating
        if confidence == 'stub':
            return None

        # For drafts and reviewed, analyze content indicators
        human_links = count_human_links(content)
        external_links = count_external_links(content)
        source_count = count_sources(content)

        # Confidence score: 10 if reviewed, 0 otherwise
        confidence_score = 10 if confidence == 'reviewed' else 0

        # Return in (h,e,s,c) format
        return f"({human_links},{external_links},{source_count},{confidence_score})"

    except Exception as e:
        stats["errors"].append(f"{source_path}: {str(e)}")
        return None


def add_rating_to_name(name: str, rating: Optional[str]) -> str:
    """Add or remove rating from name field."""
    # Remove existing rating if present (both old format and new format)
    name_clean = re.sub(r'\s*\(\d+\)$', '', name.strip())
    name_clean = re.sub(r'\s*\(\d+,\d+,\d+,\d+\)$', '', name_clean)

    # Add new rating if provided
    if rating is not None:
        return f"{name_clean} {rating}"
    else:
        return name_clean


def process_item(item: Dict, base_path: Path) -> None:
    """Process a single item and add rating to its name."""
    if 'source' not in item:
        # No source file, skip (category header)
        return

    stats["total_items"] += 1

    # Get source file path
    source_rel = item['source']
    source_path = base_path / source_rel

    # Determine rating
    rating = determine_rating(source_path)

    # Update name
    item['name'] = add_rating_to_name(item['name'], rating)

    # Update stats
    if rating is None:
        stats["no_rating"] += 1
    else:
        stats["rated_items"] += 1


def process_map(map_obj: Dict, base_path: Path) -> None:
    """Process a map object and all its categories/items."""
    if 'categories' in map_obj:
        for category in map_obj['categories']:
            if 'items' in category:
                for item in category['items']:
                    process_item(item, base_path)


def calculate_map_aggregate(map_obj: Dict) -> Optional[str]:
    """Calculate aggregate rating for all items in a map. Returns average in (h,e,s,c) format."""
    h_scores = []
    e_scores = []
    s_scores = []
    c_scores = []

    if 'categories' in map_obj:
        for category in map_obj['categories']:
            if 'items' in category:
                for item in category['items']:
                    # Extract rating from name if present
                    name = item.get('name', '')
                    match = re.search(r'\((\d+),(\d+),(\d+),(\d+)\)$', name)
                    if match:
                        h_scores.append(int(match.group(1)))
                        e_scores.append(int(match.group(2)))
                        s_scores.append(int(match.group(3)))
                        c_scores.append(int(match.group(4)))

    if not h_scores:
        return None

    # Calculate averages and round to integers
    avg_h = round(sum(h_scores) / len(h_scores))
    avg_e = round(sum(e_scores) / len(e_scores))
    avg_s = round(sum(s_scores) / len(s_scores))
    avg_c = round(sum(c_scores) / len(c_scores))

    return f"({avg_h},{avg_e},{avg_s},{avg_c})"


def aggregate_nav_ratings(landscape: list) -> None:
    """Aggregate ratings from detailed maps to nav-only items in parent maps."""
    # Build a lookup of map_id -> map_obj
    maps_by_id = {m['id']: m for m in landscape}

    print("\nAggregating ratings for navigation items...")

    # Process each map
    for map_obj in landscape:
        if 'categories' not in map_obj:
            continue

        for category in map_obj['categories']:
            if 'items' not in category:
                continue

            for item in category['items']:
                # Check if this item has no rating (nav only) but has a corresponding map
                name = item.get('name', '')
                item_id = item.get('id', '')

                # Skip if already has a rating
                if re.search(r'\(\d+,\d+,\d+,\d+\)$', name):
                    continue

                # Check if there's a detailed map for this item
                if item_id in maps_by_id:
                    detailed_map = maps_by_id[item_id]
                    avg_rating = calculate_map_aggregate(detailed_map)

                    if avg_rating is not None:
                        item['name'] = f"{name} {avg_rating}"
                        print(f"  {name} -> {avg_rating}")


def main():
    """Main function to process the landscape file."""
    # Check for --aggregate flag
    aggregate_only = '--aggregate' in sys.argv or '--agg' in sys.argv

    print("Reading landscape file...")
    with open(LANDSCAPE_FILE) as f:
        landscape = json.load(f)

    if aggregate_only:
        print("Aggregate-only mode: preserving existing ratings, updating aggregates only\n")
    else:
        print(f"Processing {len(landscape)} maps...")
        for map_obj in landscape:
            process_map(map_obj, BASE_DIR)

    # Aggregate ratings for nav items
    aggregate_nav_ratings(landscape)

    print("\nWriting updated landscape file...")
    with open(LANDSCAPE_FILE, 'w') as f:
        json.dump(landscape, f, indent=2)

    if not aggregate_only:
        print("\n" + "="*60)
        print("RATING SUMMARY")
        print("="*60)
        print(f"Total items processed: {stats['total_items']}")
        print(f"Items with ratings: {stats['rated_items']}")
        print(f"Items with no rating (stubs): {stats['no_rating']}")

        if stats['missing_files']:
            print(f"\nMissing files ({len(stats['missing_files'])}):")
            for f in stats['missing_files'][:10]:
                print(f"  - {f}")
            if len(stats['missing_files']) > 10:
                print(f"  ... and {len(stats['missing_files']) - 10} more")

        if stats['errors']:
            print(f"\nErrors ({len(stats['errors'])}):")
            for e in stats['errors'][:10]:
                print(f"  - {e}")
            if len(stats['errors']) > 10:
                print(f"  ... and {len(stats['errors']) - 10} more")

    print("\nDone!")


if __name__ == '__main__':
    main()
