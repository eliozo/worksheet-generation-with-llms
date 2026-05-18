"""
collect_problems_by_mistake.py

For each label in MISTAKE_LABELS, collect all problems from LV.AMO and LV.NOL
whose domain matches DOMAIN and whose _hasReasoningMistake list *starts* with
that label.  The collected problems are sorted (descending) by the length of
their _hasReasoningMethod list, then by the length of their _hasSolutionConcept
list.  One markdown file per label is written to DIRECTORY.
"""

import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# Hardcoded parameters
# ---------------------------------------------------------------------------
MISTAKE_LABELS = [
    "WrongDivisibilityRule",
    "NonCoprimeFactorDivisibility",
    "MissingBoundOrExample",
    "PrimeOnePointConfusion",
    "UnstatedNumberSetAssumption"
]

DOMAIN = "NT"

DIRECTORY = "problem_collections/NT"

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
SCRIPTS_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS_DIR))

from problem_markdown_parser import ProblemMarkdownParser  # noqa: E402

PARENT_DIRS = [
    "/Users/kapsitis/workspace-public/math/problembase/LV.AMO",
    "/Users/kapsitis/workspace-public/math/problembase/LV.NOL",
]

OUT_DIR = SCRIPTS_DIR / DIRECTORY
OUT_DIR.mkdir(parents=True, exist_ok=True)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def collect_content_files(parent_dirs):
    """Yield absolute paths of every content_lv.md under parent_dirs."""
    for parent in parent_dirs:
        p = Path(parent)
        if not p.is_dir():
            print(f"WARNING: directory not found – {parent}", file=sys.stderr)
            continue
        for md_file in sorted(p.rglob("content_lv.md")):
            yield md_file


def get_domain(meta_dict):
    raw = meta_dict.get("domain") or meta_dict.get("_domain")
    if not raw:
        return None
    first = raw[0].strip() if isinstance(raw, list) else str(raw).strip()
    return first if first else None


def first_mistake(meta_dict):
    """Return the first _hasReasoningMistake label, or empty string."""
    mistakes = meta_dict.get("_hasReasoningMistake", [])
    if not mistakes:
        return ""
    val = mistakes[0] if isinstance(mistakes, list) else str(mistakes)
    return val.strip()


def sort_key(prob):
    """Descending by #reasoning-methods, then by #solution-concepts."""
    n_methods  = len(prob.meta_dict.get("_hasReasoningMethod",   []))
    n_concepts = len(prob.meta_dict.get("_hasSolutionConcept",   []))
    return (-n_methods, -n_concepts)


def problem_to_markdown(prob):
    """Reconstruct a markdown block with title and problem text only (no metadata, no solution)."""
    return f"# <lo-sample/> {prob.title}\n\n{prob.problem_text}\n"


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    # Bucket: label -> list of Problem
    buckets = {label: [] for label in MISTAKE_LABELS}

    files_parsed = 0
    for md_path in collect_content_files(PARENT_DIRS):
        try:
            problems = ProblemMarkdownParser.parse_file(str(md_path))
        except Exception as exc:
            print(f"ERROR parsing {md_path}: {exc}", file=sys.stderr)
            continue
        files_parsed += 1

        for prob in problems:
            if get_domain(prob.meta_dict) != DOMAIN:
                continue
            fm = first_mistake(prob.meta_dict)
            if fm in buckets:
                buckets[fm].append(prob)

    print(f"Files parsed: {files_parsed}")

    # Sort each bucket and write output
    for label in MISTAKE_LABELS:
        probs = sorted(buckets[label], key=sort_key)
        out_path = OUT_DIR / f"{label}.md"
        with open(out_path, "w", encoding="utf-8") as f:
            for prob in probs:
                f.write(problem_to_markdown(prob))
                f.write("\n")
        print(f"  {label}: {len(probs)} problems -> {out_path}")


if __name__ == "__main__":
    main()
