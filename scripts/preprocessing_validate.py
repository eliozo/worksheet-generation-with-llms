"""
preprocessing_validate.py

Usage:
    python preprocessing_validate.py <parent_dir> <property>

Visits each direct subdirectory of <parent_dir>, parses content_lv.md using
ProblemMarkdownParser, and checks that every problem has a non-null metadata
<property>.  When property == 'domain', also validates that the value is one of
['Alg', 'Comb', 'Geom', 'NT'].
"""

import os
import sys

# Allow importing from the same scripts/ directory
sys.path.insert(0, os.path.dirname(__file__))

from problem_markdown_parser import ProblemMarkdownParser

VALID_DOMAINS = {'Alg', 'Comb', 'Geom', 'NT'}


def validate_subdir(subdir_path: str, prop: str) -> None:
    md_path = os.path.join(subdir_path, 'content_lv.md')
    if not os.path.isfile(md_path):
        print(f"WARNING: content_lv.md not found in '{subdir_path}'")
        return

    problems = ProblemMarkdownParser.parse_file(md_path)
    for problem in problems:
        values = problem.meta_dict.get(prop)

        # Missing or empty property
        if not values or all(v.strip() == '' for v in values):
            print(f"WARNING: problem '{problem.title}' is missing property '{prop}'")
            continue

        # Domain-specific value check
        if prop == 'domain':
            for v in values:
                stripped = v.strip()
                if stripped not in VALID_DOMAINS:
                    print(
                        f"WARNING: problem '{problem.title}' has invalid domain value "
                        f"'{stripped}' (expected one of {sorted(VALID_DOMAINS)})"
                    )


def main() -> None:
    if len(sys.argv) != 3:
        print(f"Usage: python {os.path.basename(__file__)} <parent_dir> <property>")
        sys.exit(1)

    parent_dir = sys.argv[1]
    prop = sys.argv[2]

    if not os.path.isdir(parent_dir):
        print(f"ERROR: '{parent_dir}' is not a directory or does not exist.")
        sys.exit(1)

    subdirs = sorted(
        entry.path
        for entry in os.scandir(parent_dir)
        if entry.is_dir()
    )

    for subdir in subdirs:
        validate_subdir(subdir, prop)


if __name__ == '__main__':
    main()
