"""
Helper for the 'merge-directories' subcommand.

Compares content_lv.md and content_lv2.md in a directory.  If the two files
contain identical problems (same title, problem text, and solution) and
content_lv2.md only adds metadata properties that are in the allowed set,
the directory is *merged*: content_lv.md is replaced by content_lv2.md and
the extra file is removed.  Otherwise the directory is *skipped*.
"""

import os
import shutil
from scripts.problem_markdown_parser import ProblemMarkdownParser

FILE_A = "content_lv.md"
FILE_B = "content_lv2.md"


def _problems_are_mergeable(lv_problems, lv2_problems, allowed_props):
    """Return True iff lv2 differs from lv only by having extra allowed properties."""
    if len(lv_problems) != len(lv2_problems):
        return False
    for p1, p2 in zip(lv_problems, lv2_problems):
        if p1.title != p2.title:
            return False
        if p1.problem_text != p2.problem_text:
            return False
        if p1.solution_text != p2.solution_text:
            return False
        # Every key in lv must be present in lv2 with the same values
        for key, vals in p1.meta_dict.items():
            if key not in p2.meta_dict:
                return False
            if sorted(vals) != sorted(p2.meta_dict[key]):
                return False
        # Any extra keys in lv2 must be in the allowed set
        for key in p2.meta_dict:
            if key not in p1.meta_dict and key not in allowed_props:
                return False
    return True


def try_merge_directory(dirpath, allowed_props):
    """Compare content_lv.md and content_lv2.md in *dirpath*.

    If they are mergeable (content_lv2.md adds only allowed properties),
    replace content_lv.md with content_lv2.md and delete content_lv2.md.

    Returns 'merged' or 'skipped'.
    """
    path_a = os.path.join(dirpath, FILE_A)
    path_b = os.path.join(dirpath, FILE_B)
    if not os.path.isfile(path_a) or not os.path.isfile(path_b):
        return 'skipped'

    lv_problems = ProblemMarkdownParser.parse_file(path_a)
    lv2_problems = ProblemMarkdownParser.parse_file(path_b)

    if _problems_are_mergeable(lv_problems, lv2_problems, set(allowed_props)):
        shutil.copy2(path_b, path_a)
        os.remove(path_b)
        return 'merged'
    return 'skipped'


def resolve_directories(directory_arg):
    """Expand the directory argument into a list of concrete directory paths.

    Accepts either a plain directory path or a glob of the form ``dirname/*``
    (which expands to all immediate subdirectories of *dirname*).
    """
    if directory_arg.endswith('/*'):
        base = directory_arg[:-2]
        if not os.path.isdir(base):
            return []
        return sorted(
            os.path.join(base, entry)
            for entry in os.listdir(base)
            if os.path.isdir(os.path.join(base, entry))
        )
    return [directory_arg]
