"""
aggregate_reasoning_mistakes.py

Walk two problem-base directories (LV.AMO and LV.NOL), parse every
content_lv.md file, and build per-domain count tables for the
_hasReasoningMistake metadata label.

Only the *first* entry in _hasReasoningMistake is counted per problem
(the most important mistake).  Each count is split by _mistakesFit value
("high", "medium", "low").

Outputs (written to scripts/metadata_stats/):
  reasoningMistakes_Alg.csv   reasoningMistakes_Alg.png
  reasoningMistakes_Comb.csv  reasoningMistakes_Comb.png
  reasoningMistakes_Geom.csv  reasoningMistakes_Geom.png
  reasoningMistakes_NT.csv    reasoningMistakes_NT.png
"""

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
FIT_LEVELS = ["high", "medium", "low"]

# Chart colours per fit level
FIT_COLORS = {
    "high":   "#8B0000",   # dark red
    "medium": "#FFA500",   # amber
    "low":    "#90EE90",   # light green
}

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
    return first if first else None


def get_fit(meta_dict):
    """Return the _mistakesFit value normalised to lower-case, or None."""
    raw = meta_dict.get("_mistakesFit")
    if not raw:
        return None
    val = (raw[0] if isinstance(raw, list) else str(raw)).strip().lower()
    return val if val in FIT_LEVELS else None


# ---------------------------------------------------------------------------
# Main aggregation
# ---------------------------------------------------------------------------

def aggregate():
    # counts[domain][label][fit_level] = int
    counts = {d: defaultdict(lambda: defaultdict(int)) for d in DOMAINS}
    files_parsed = 0
    problems_counted = 0
    skipped_no_domain = 0
    skipped_no_mistake = 0

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

            mistakes = prob.meta_dict.get("_hasReasoningMistake", [])
            if not mistakes:
                skipped_no_mistake += 1
                continue

            # Only count the first (most important) mistake
            first_label = mistakes[0].strip() if isinstance(mistakes, list) else str(mistakes).strip()
            if not first_label:
                skipped_no_mistake += 1
                continue

            fit = get_fit(prob.meta_dict) or "low"   # default to "low" if unset
            counts[domain][first_label][fit] += 1
            problems_counted += 1

    print(f"Files parsed        : {files_parsed}")
    print(f"Problems counted    : {problems_counted}")
    print(f"Skipped (no domain) : {skipped_no_domain}")
    print(f"Skipped (no mistake): {skipped_no_mistake}")

    return counts


# ---------------------------------------------------------------------------
# Sorting key: descending high, then medium, then low
# ---------------------------------------------------------------------------

def sort_key_desc(item):
    _label, fit_dict = item
    return (
        -fit_dict.get("high", 0),
        -fit_dict.get("medium", 0),
        -fit_dict.get("low", 0),
    )


# ---------------------------------------------------------------------------
# Output: CSV
# ---------------------------------------------------------------------------

def write_csv(domain, label_fit_counts):
    out_path = OUT_DIR / f"reasoningMistakes_{domain}.csv"
    sorted_items = sorted(label_fit_counts.items(), key=sort_key_desc)
    with open(out_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Label", "HighCount", "MediumCount", "LowCount"])
        for label, fit_dict in sorted_items:
            writer.writerow([
                label,
                fit_dict.get("high", 0),
                fit_dict.get("medium", 0),
                fit_dict.get("low", 0),
            ])
    print(f"Wrote {out_path}")


# ---------------------------------------------------------------------------
# Output: PNG bar chart (stacked horizontal bars)
# ---------------------------------------------------------------------------

def write_chart(domain, label_fit_counts):
    if not label_fit_counts:
        print(f"No data for domain={domain}, skipping chart.")
        return

    # barh draws index 0 at the bottom and the last item at the top.
    # Sorting with reverse=True and sort_key_desc (which uses negatives) gives
    # [lowest, ..., highest] so the highest HighCount bar ends up at the top.
    sorted_items = sorted(label_fit_counts.items(), key=sort_key_desc, reverse=True)

    labels = [item[0] for item in sorted_items]
    high_counts   = [item[1].get("high",   0) for item in sorted_items]
    medium_counts = [item[1].get("medium", 0) for item in sorted_items]
    low_counts    = [item[1].get("low",    0) for item in sorted_items]
    totals        = [h + m + l for h, m, l in zip(high_counts, medium_counts, low_counts)]

    fig_height = max(4, len(labels) * 0.35 + 1.5)
    fig, ax = plt.subplots(figsize=(10, fig_height))

    bars_high   = ax.barh(labels, high_counts,   color=FIT_COLORS["high"],   height=0.6,
                          label="high")
    bars_medium = ax.barh(labels, medium_counts, color=FIT_COLORS["medium"], height=0.6,
                          left=high_counts, label="medium")
    bars_low    = ax.barh(labels, low_counts,    color=FIT_COLORS["low"],    height=0.6,
                          left=[h + m for h, m in zip(high_counts, medium_counts)],
                          label="low")

    # Grid lines at multiples of 5
    max_total = max(totals) if totals else 10
    step = 5
    ax.set_xticks(range(0, max_total + step + 1, step))
    ax.xaxis.grid(True, linestyle="--", linewidth=0.6, alpha=0.7)
    ax.set_axisbelow(True)

    # Total count label to the right of each bar
    for i, total in enumerate(totals):
        ax.text(
            total + 0.15,
            i,
            str(total),
            va="center",
            ha="left",
            fontsize=7,
        )

    ax.set_xlabel("Number of problems", fontsize=9)
    ax.set_ylabel("")
    ax.set_title(f"Reasoning Mistakes – domain: {domain}", fontsize=11)
    ax.tick_params(axis="y", labelsize=7)
    ax.tick_params(axis="x", labelsize=8)
    ax.legend(title="_mistakesFit", fontsize=7, title_fontsize=7,
              loc="lower right")

    plt.tight_layout()
    out_path = OUT_DIR / f"reasoningMistakes_{domain}.png"
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
