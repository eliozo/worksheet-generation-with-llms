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

questionType may be given per sub-part ("* questionType:A: QTY_FindAll",
"* _questionType:A: QTY_FindAll"); then each sub-part is compared separately,
and different sub-parts on the two sides are a mismatch. An LLM value that is a
subtype of the human one (QTY_DecideExistence for QTY_Decide, per
questionTypes2.csv) is consistent: not a mismatch, but kept, as it is more precise.
"""

import csv
import os
import re

CONTENT_FILE_RE = re.compile(r'^content_[a-z]{2}\.md$')
PROBLEM_TITLE_RE = re.compile(r'^#\s+<lo-sample\s*/>\s*(\S+)')
PROPERTY_RE = re.compile(r'^\s*\*\s*(_?)([A-Za-z][\w-]*)\s*:(.*)$')

# Properties that may be given per sub-part: "questionType:A: value"
RUBRIC_PROPERTIES = {'questionType'}
RUBRIC_VALUE_RE = re.compile(r'^\s*([A-Za-z0-9]{1,2})\s*:(.*)$')
QUESTION_TYPES_CSV = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'setup', 'resources',
                                  'questionTypes2.csv')
_question_type_parents = None


def _parents():
    """questionType label -> its group label (QTY_FindAll -> QTY_Find), from questionTypes2.csv."""
    global _question_type_parents
    if _question_type_parents is None:
        _question_type_parents = {}
        if os.path.exists(QUESTION_TYPES_CSV):
            with open(QUESTION_TYPES_CSV, encoding='utf-8') as f:
                rows = list(csv.DictReader(f))
            groups = {r['L1']: r['Label'] for r in rows if r['L2'].strip() == '0'}
            _question_type_parents = {r['Label']: groups.get(r['L1']) for r in rows if r['L2'].strip() != '0'}
    return _question_type_parents


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


def _rubric_values(lines):
    """{sub-part: set of values} ('' for lines without a sub-part)."""
    result = {}
    for line in lines:
        value = PROPERTY_RE.match(line).group(3)
        m = RUBRIC_VALUE_RE.match(value)
        rubric, value = (m.group(1), m.group(2)) if m else ('', value)
        result.setdefault(rubric, set()).update(v.strip() for v in value.split(',') if v.strip())
    return result


def _refines(llm_vals, human_vals):
    """Each value on either side equals, or is a subtype of, a value on the other side."""
    parents = _parents()
    match = lambda v, h: v == h or parents.get(v) == h
    return (all(any(match(v, h) for h in human_vals) for v in llm_vals)
            and all(any(match(v, h) for v in llm_vals) for h in human_vals))


def _compare_rubrics(human_lines, llm_lines):
    """'duplicate', 'mismatch' or None (nothing to do) for a per-sub-part property."""
    human, llm = _rubric_values(human_lines), _rubric_values(llm_lines)
    if not any(human.values()) or not any(llm.values()):
        return None
    if set(human) != set(llm):
        return 'mismatch'
    outcomes = set()
    for rubric in human:
        if not human[rubric] or not llm[rubric]:
            outcomes.add('incomplete')
        elif human[rubric] == llm[rubric]:
            outcomes.add('equal')
        elif _refines(llm[rubric], human[rubric]):
            outcomes.add('refined')
        else:
            return 'mismatch'
    return 'duplicate' if outcomes == {'equal'} else None


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
        if prop in RUBRIC_PROPERTIES:
            outcome = _compare_rubrics(human_lines, llm_lines)
            if outcome == 'duplicate':
                # with the value, also its "_<prop>Source" and "_<prop>Model" lines
                to_remove.extend(llm_idx + llm.get(prop + 'Source', []) + llm.get(prop + 'Model', []))
            if outcome:
                report(outcome, prop, human_lines, llm_lines)
            continue
        human_vals, llm_vals = _values(human_lines), _values(llm_lines)
        if not human_vals or not llm_vals:
            continue
        if human_vals == llm_vals:
            to_remove.extend(llm_idx + llm.get(prop + 'Source', []) + llm.get(prop + 'Model', []))
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
