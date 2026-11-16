"""Add an LLM-classified "_<property>" to every problem under a directory.

Usage:
    python preprocess_add_metadata.py <base_dir> <property> [--provider MODEL] [--dry-run]

Example:
    python preprocess_add_metadata.py ../../math/problembase/LV.NOL questionType

Visits every content_lv.md in the subdirectories of <base_dir> and, for each
problem whose <small>...</small> block has no "_<property>" yet, adds the line
"* _<property>: <value>" classified by an OpenAI model (the same as running
"eliozo_client.py add-metadata" on each file, editing it in place). The model is
OPENAI_MODEL in scripts/.env unless --provider is given. questionType, domain and
hasSolutionStructure are classified from the problem text alone; the other
properties also use the solution. Problems that already have the property are
left alone, so the script can be rerun after an interruption or failed requests.
"""

import argparse
import os
import sys
from dotenv import load_dotenv

# Ensure the parent directory is in the sys.path
script_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(script_dir, '..'))
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

from scripts.eliozo_client import EliozoClient
from scripts.metadata_utils import ADD_METADATA_PROPERTIES

CONTENT_FILE = "content_lv.md"


def find_content_files(base_dir):
    """All content_lv.md files under base_dir, in sorted order."""
    result = []
    for root, dirs, files in os.walk(base_dir):
        dirs.sort()
        if CONTENT_FILE in files:
            result.append(os.path.join(root, CONTENT_FILE))
    return sorted(result)


def main(argv=None):
    allowed = [p.value for p in ADD_METADATA_PROPERTIES]
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument('base_dir', help='Directory whose subdirectories contain content_lv.md files')
    parser.add_argument('property', help='Property to add: ' + ', '.join(allowed))
    parser.add_argument('--provider', default=None,
                        help='OpenAI model to classify with (default: OPENAI_MODEL in scripts/.env)')
    parser.add_argument('--dry-run', action='store_true',
                        help='Only list the problems that would be classified; no LLM calls, no changes')
    args = parser.parse_args(argv)

    if args.property not in allowed:
        print(f"Unsupported property '{args.property}'. Supported properties: {', '.join(allowed)}")
        return 1
    if not os.path.isdir(args.base_dir):
        print(f"Error: Directory not found: {args.base_dir}")
        return 1

    # Load environment variables (e.g. OPENAI_API_KEY)
    load_dotenv()
    client = EliozoClient(os.getenv("WEAVIATE_URL", "NA"), os.getenv("WEAVIATE_API_KEY", "NA"),
                          os.getenv("OPENAI_API_KEY", "NA"), os.getenv("FUSEKI_URL", "NA"),
                          os.getenv("FUSEKI_USER", "NA"), os.getenv("FUSEKI_PASSWORD", "NA"))
    client.set_command("add-metadata")

    md_files = find_content_files(args.base_dir)
    print(f"Found {len(md_files)} {CONTENT_FILE} files in: {args.base_dir}")

    totals = {}
    for md_file in md_files:
        print(f"\nProcessing {md_file} ...")
        (_, data) = client.add_metadata(md_file, args.property, args.provider, dry_run=args.dry_run)
        for key in ('added', 'existing', 'failed', 'no_metadata_block'):
            totals[key] = totals.get(key, 0) + data[key]

    added = 'would be classified' if args.dry_run else 'added'
    print(f"\nDone: _{args.property} {added}: {totals.get('added', 0)}, "
          f"already present: {totals.get('existing', 0)}, failed: {totals.get('failed', 0)}, "
          f"without <small> block: {totals.get('no_metadata_block', 0)}")
    return 1 if totals.get('failed') else 0


if __name__ == "__main__":
    sys.exit(main())
