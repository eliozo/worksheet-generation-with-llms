"""
Helper for the 'clean-metadata' subcommand.

Visits every content_xx.md file under a parent directory.  For each problem
("# <lo-sample/> PROBLEM.ID") it compares the properties in the problem's
<small>...</small> block that occur both human-edited ("* domain: NT") and
LLM-generated ("* _domain: NT"):

* same values      -> the "_" lines are removed from the file (reported);
* different values -> reported as a mismatch, nothing is changed;
* only one of them exists, or one of them is empty -> nothing happens.

Values are compared as sets: a property may span several lines and each line
may hold a comma-separated list, so order and spacing do not matter.
"""

import os
import re

CONTENT_FILE_RE = re.compile(r'^content_[a-z]{2}\.md$')
PROBLEM_TITLE_RE = re.compile(r'^#\s+<lo-sample\s*/>\s*(\S+)')
PROPERTY_RE = re.compile(r'^\s*\*\s*(_?)([A-Za-z][\w-]*)\s*:(.*)$')


def find_content_files(parent_dir):
    """All content_xx.md files under *parent_dir*, in sorted order."""
    result = []
    for dirpath, dirnames, filenames in os.walk(parent_dir):
        dirnames.sort()
        for name in sorted(filenames):
            if CONTENT_FILE_RE.match(name):
                result.append(os.path.join(dirpath, name))
    return result


def _values(lines):
    return {v.strip() for line in lines for v in PROPERTY_RE.match(line).group(3).split(',') if v.strip()}


def _clean_block(lines, start, end, report):
    """Check the property lines lines[start:end] of one <small> block.

    Calls report(kind, prop, human_lines, llm_lines) for each duplicate or
    mismatch; returns the indices of the lines to remove.
    """
    human, llm = {}, {}
    for i in range(start, end):
        m = PROPERTY_RE.match(lines[i])
        if m:
            (llm if m.group(1) else human).setdefault(m.group(2), []).append(i)

    to_remove = []
    for prop, llm_idx in llm.items():
        if prop not in human:
            continue
        human_lines = [lines[i] for i in human[prop]]
        llm_lines = [lines[i] for i in llm_idx]
        human_vals, llm_vals = _values(human_lines), _values(llm_lines)
        if not human_vals or not llm_vals:
            continue
        if human_vals == llm_vals:
            to_remove.extend(llm_idx)
            report('duplicate', prop, human_lines, llm_lines)
        else:
            report('mismatch', prop, human_lines, llm_lines)
    return to_remove


def clean_file(path, write=True):
    """Remove redundant "_" properties from one file; return [(kind, message), ...]
    where kind is 'duplicate' (removed) or 'mismatch'."""
    with open(path, encoding='utf-8', newline='') as f:
        lines = f.read().splitlines(keepends=True)

    messages = []
    to_remove = []
    problem_id = None
    i = 0
    while i < len(lines):
        m = PROBLEM_TITLE_RE.match(lines[i])
        if m:
            problem_id = m.group(1)
            # The problem's metadata: the nearest <small>...</small> before the next problem
            j = i + 1
            while j < len(lines) and not PROBLEM_TITLE_RE.match(lines[j]) and '<small>' not in lines[j]:
                j += 1
            if j < len(lines) and '<small>' in lines[j]:
                k = j + 1
                while k < len(lines) and '</small>' not in lines[k] and not PROBLEM_TITLE_RE.match(lines[k]):
                    k += 1

                def report(kind, prop, human_lines, llm_lines, pid=problem_id):
                    human_txt = ' | '.join(l.strip() for l in human_lines)
                    llm_txt = ' | '.join(l.strip() for l in llm_lines)
                    if kind == 'duplicate':
                        messages.append((kind, f"{path}: {pid}: REMOVED '{llm_txt}' (same as '{human_txt}')"))
                    else:
                        messages.append((kind, f"{path}: {pid}: MISMATCH '{human_txt}' vs '{llm_txt}'"))

                to_remove.extend(_clean_block(lines, j + 1, k, report))
                i = k
        i += 1

    if to_remove and write:
        removed = set(to_remove)
        with open(path, 'w', encoding='utf-8', newline='') as f:
            f.write(''.join(line for n, line in enumerate(lines) if n not in removed))
    return messages


def clean_metadata(parent_dir, write=True):
    """Clean all content_xx.md files under *parent_dir*; print one line per duplicate or mismatch.

    Returns (files_changed, duplicates_removed, mismatches).
    """
    files_changed = duplicates = mismatches = 0
    for path in find_content_files(parent_dir):
        messages = clean_file(path, write)
        for _, msg in messages:
            print(msg)
        file_duplicates = sum(kind == 'duplicate' for kind, _ in messages)
        duplicates += file_duplicates
        mismatches += len(messages) - file_duplicates
        files_changed += file_duplicates > 0
    return files_changed, duplicates, mismatches
