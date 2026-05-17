"""
aggregate_reasoning_methods.py

Walk two problem-base directories (LV.AMO and LV.NOL), parse every
content_lv.md file, and build per-domain count tables for the
_hasReasoningMethod metadata label.

Outputs (written to scripts/metadata_stats/):
  reasoningMethods_Alg.csv   reasoningMethods_Alg.png
  reasoningMethods_Comb.csv  reasoningMethods_Comb.png
  reasoningMethods_Geom.csv  reasoningMethods_Geom.png
  reasoningMethods_NT.csv    reasoningMethods_NT.png
"""

import os
import sys
import csv
from collections import defaultdict
from pathlib import Path

import matplotlib
matplotlib.use("Agg")  # non-interactive backend
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# Locate the scripts/ directory relative to this file so that
# problem_markdown_parser can always be imported regardless of cwd.
# ---------------------------------------------------------------------------
SCRIPTS_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS_DIR))

from problem_markdown_parser import ProblemMarkdownParser  # noqa: E402

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------
PARENT_DIRS = [
    "/Users/kapsitis/workspace-public/math/problembase/LV.AMO",
    "/Users/kapsitis/workspace-public/math/problembase/LV.NOL",
]

DOMAINS = ["Alg", "Comb", "Geom", "NT"]

OUT_DIR = SCRIPTS_DIR / "metadata_stats"
OUT_DIR.mkdir(parents=True, exist_ok=True)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def collect_content_files(parent_dirs):
    """Yield absolute paths of every content_lv.md found under parent_dirs."""
    for parent in parent_dirs:
        p = Path(parent)
        if not p.is_dir():
            print(f"WARNING: directory not found – {parent}", file=sys.stderr)
            continue
        for md_file in sorted(p.rglob("content_lv.md")):
            yield md_file


def get_domain(meta_dict):
    """Return the first/main domain string from a problem's meta_dict, or None."""
    raw = meta_dict.get("domain") or meta_dict.get("_domain")
    if not raw:
        return None
    first = raw[0].strip() if isinstance(raw, list) else str(raw).strip()
    # Normalise common variations
    return first if first else None


# ---------------------------------------------------------------------------
# Main aggregation
# ---------------------------------------------------------------------------

def aggregate():
    # counts[domain][label] = int
    counts = {d: defaultdict(int) for d in DOMAINS}
    files_parsed = 0
    problems_counted = 0
    skipped_no_domain = 0
    skipped_no_method = 0

    for md_path in collect_content_files(PARENT_DIRS):
        try:
            problems = ProblemMarkdownParser.parse_file(str(md_path))
        except Exception as exc:
            print(f"ERROR parsing {md_path}: {exc}", file=sys.stderr)
            continue
        files_parsed += 1

        for prob in problems:
            domain = get_domain(prob.meta_dict)
            if domain not in DOMAINS:
                skipped_no_domain += 1
                continue

            methods = prob.meta_dict.get("_hasReasoningMethod", [])
            if not methods:
                skipped_no_method += 1
                continue

            for method in methods:
                label = method.strip()
                # Skip some very common labels. 
                if label in ['EquivalentTransformationsOfEquationsAndInequalities', 
                             'ConstructiveExampleForExistence', 
                             'ContradictionForImpossibility']:
                    continue
                if label:
                    counts[domain][label] += 1
            problems_counted += 1

    print(f"Files parsed  : {files_parsed}")
    print(f"Problems counted : {problems_counted}")
    print(f"Skipped (no domain)  : {skipped_no_domain}")
    print(f"Skipped (no method)  : {skipped_no_method}")

    return counts


# ---------------------------------------------------------------------------
# Output: CSV
# ---------------------------------------------------------------------------

def write_csv(domain, label_counts):
    out_path = OUT_DIR / f"reasoningMethods_{domain}.csv"
    sorted_items = sorted(label_counts.items(), key=lambda x: (-x[1], x[0]))
    with open(out_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Label", "Count"])
        for label, count in sorted_items:
            writer.writerow([label, count])
    print(f"Wrote {out_path}")


# ---------------------------------------------------------------------------
# Output: PNG bar chart (horizontal bars)
# ---------------------------------------------------------------------------

def write_chart(domain, label_counts):
    if not label_counts:
        print(f"No data for domain={domain}, skipping chart.")
        return

    sorted_items = sorted(label_counts.items(), key=lambda x: x[1])  # ascending so top = most
    labels = [item[0] for item in sorted_items]
    counts = [item[1] for item in sorted_items]

    fig_height = max(4, len(labels) * 0.35 + 1.5)
    fig, ax = plt.subplots(figsize=(10, fig_height))

    bars = ax.barh(labels, counts, color="steelblue", height=0.6)

    # Grid lines at multiples of 5
    max_count = max(counts) if counts else 10
    step = 5
    ax.set_xticks(range(0, max_count + step + 1, step))
    ax.xaxis.grid(True, linestyle="--", linewidth=0.6, alpha=0.7)
    ax.set_axisbelow(True)

    # Label value at the front of each bar (right side)
    for bar, val in zip(bars, counts):
        ax.text(
            bar.get_width() + 0.15,
            bar.get_y() + bar.get_height() / 2,
            str(val),
            va="center",
            ha="left",
            fontsize=7,
        )

    ax.set_xlabel("Number of problems", fontsize=9)
    ax.set_ylabel("")
    ax.set_title(f"Reasoning Methods – domain: {domain}", fontsize=11)
    ax.tick_params(axis="y", labelsize=7)
    ax.tick_params(axis="x", labelsize=8)

    plt.tight_layout()
    out_path = OUT_DIR / f"reasoningMethods_{domain}.png"
    fig.savefig(str(out_path), dpi=120)
    plt.close(fig)
    print(f"Wrote {out_path}")


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    counts = aggregate()
    for domain in DOMAINS:
        write_csv(domain, counts[domain])
        write_chart(domain, counts[domain])
