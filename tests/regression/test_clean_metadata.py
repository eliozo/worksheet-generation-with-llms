"""Regression tests for the 'clean-metadata' subcommand."""

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from scripts.markdown_proc.clean_metadata import clean_metadata

CONTENT = """\
# <lo-sample/> LV.TST.2020.5.1

Problem one.

<small>

* domain:NT
* _domain: NT
* questionType:Prove
* _questionType:FindAll
* topic:Parity
* topic:Divisibility
* _topic: Divisibility, Parity
* _hasReasoningMethod: Invariant

</small>

## Atrisinājums-1

Solution, mentioning * _domain:NT outside the metadata block.

# <lo-sample/> LV.TST.2020.5.2

No metadata here.

# <lo-sample/> LV.TST.2020.5.3

<small>

* domain:
* _domain:Alg
* subdomain:DOM_Polygons
* _subdomain:

</small>
"""


def test_clean_metadata(tmp_path, capsys):
    problem_dir = tmp_path / 'LV.TST' / 'lv-tst-2020'
    problem_dir.mkdir(parents=True)
    content = problem_dir / 'content_lv.md'
    content.write_text(CONTENT, encoding='utf-8')
    other = problem_dir / 'content_lv2.md'  # not a content_xx.md file
    other.write_text(CONTENT, encoding='utf-8')

    result = clean_metadata(str(tmp_path))

    lines = capsys.readouterr().out.splitlines()
    assert result == (1, 2, 1)
    assert lines == [
        f"{content}: LV.TST.2020.5.1: REMOVED '* _domain: NT' (same as '* domain:NT')",
        f"{content}: LV.TST.2020.5.1: MISMATCH '* questionType:Prove' vs '* _questionType:FindAll'",
        f"{content}: LV.TST.2020.5.1: REMOVED '* _topic: Divisibility, Parity' "
        f"(same as '* topic:Parity | * topic:Divisibility')",
    ]
    expected = CONTENT.replace('* _domain: NT\n', '').replace('* _topic: Divisibility, Parity\n', '')
    assert content.read_text(encoding='utf-8') == expected
    assert other.read_text(encoding='utf-8') == CONTENT

    # Running again finds only the mismatch and changes nothing
    assert clean_metadata(str(tmp_path)) == (0, 0, 1)
    assert content.read_text(encoding='utf-8') == expected
