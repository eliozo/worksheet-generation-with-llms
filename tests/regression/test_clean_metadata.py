"""Regression tests for the 'clean-metadata' subcommand."""

import os
import sys

import pytest

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


RUBRICS = """\
# <lo-sample/> LV.TST.2020.7.1

**(A)** Cik ...? **(B)** Vai var ...?

<small>

* questionType:A: QTY_FindValue
* questionType:B: QTY_Decide
* _questionType:A: QTY_FindValue
* _questionType:B: {b}

</small>
"""


@pytest.mark.parametrize('llm_b, removed, output', [
    ('QTY_Decide', True, "REMOVED '* _questionType:A: QTY_FindValue | * _questionType:B: QTY_Decide'"),
    ('QTY_DecideExistence', False, None),   # a subtype of QTY_Decide: consistent, kept
    ('QTY_ProveUniversal', False, "MISMATCH '* questionType:A: QTY_FindValue | * questionType:B: QTY_Decide'"),
])
def test_question_type_per_sub_part(tmp_path, capsys, llm_b, removed, output):
    content = tmp_path / 'content_lv.md'
    text = RUBRICS.format(b=llm_b)
    content.write_text(text, encoding='utf-8')
    clean_metadata(str(tmp_path))
    out = capsys.readouterr().out
    if output:
        assert output in out
    else:
        assert out == ''
    after = content.read_text(encoding='utf-8')
    assert ('_questionType' not in after) if removed else (after == text)


def test_question_type_sub_parts_must_correspond(tmp_path, capsys):
    content = tmp_path / 'content_lv.md'
    content.write_text(RUBRICS.format(b='QTY_Decide').replace('* _questionType:A: QTY_FindValue\n'
                                                               '* _questionType:B: QTY_Decide',
                                                               '* _questionType: QTY_FindValue'),
                       encoding='utf-8')
    assert clean_metadata(str(tmp_path)) == (0, 0, 1)
    assert 'MISMATCH' in capsys.readouterr().out


def test_duplicate_removal_takes_source_and_model_lines_along(tmp_path, capsys):
    content = tmp_path / 'content_lv.md'
    content.write_text('# <lo-sample/> LV.TST.2020.7.2\n\nAtrodi visus $x$.\n\n<small>\n\n'
                       '* questionType:QTY_FindAll\n* _questionType: QTY_FindAll\n'
                       '* _questionTypeSource: questionTypes2-v2/prompt-v1\n* _questionTypeModel: test-model\n'
                       '* domain:Alg\n\n</small>\n', encoding='utf-8')
    assert clean_metadata(str(tmp_path)) == (1, 1, 0)
    assert content.read_text(encoding='utf-8') == ('# <lo-sample/> LV.TST.2020.7.2\n\nAtrodi visus $x$.\n\n'
                                                   '<small>\n\n* questionType:QTY_FindAll\n* domain:Alg\n\n</small>\n')
