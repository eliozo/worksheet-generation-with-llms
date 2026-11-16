"""Regression tests for preprocess_add_metadata.py (no LLM calls: the classifier is faked)."""

import os
import sys

import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from scripts import preprocess_add_metadata
from scripts.metadata_utils import MetadataProperties, MetadataUtils

CONTENT = """\
Preamble before the first problem stays as it is.

# <lo-sample/> LV.TST.2020.5.1

Pierādīt, ka $n^2+n$ ir pāra skaitlis.

<small>

* questionType:Prove
* domain:NT

</small>

## Atrisinājums-1

Secret solution text.

# <lo-sample/> LV.TST.2020.10.2

Atrast visus $x$, kuriem $x^2=4$.

<small>

* domain:Alg
* _questionType: QTY_FindAll

</small>

# <lo-sample/> LV.TST.2020.11.3

Cik ir pirmskaitļu?

<small>
* domain:NT
</small>

# <lo-sample/> LV.TST.2020.12.4

Kļūdains uzdevums.

<small>

* domain:Comb

</small>
"""


def test_adds_missing_property_from_problem_text_only(tmp_path, monkeypatch, capsys):
    calls = []

    def fake_classify(self, title, problem_text, problem_solution, property, meta_dict=None):
        calls.append((title, problem_text, problem_solution, property, meta_dict))
        if 'Kļūdains' in problem_text:
            return 'NA'  # what a failed request looks like
        return 'QTY_ProveUniversal' if problem_text.startswith('Pierādīt') else 'QTY_FindValue'

    monkeypatch.setattr(MetadataUtils, 'classify_problem', fake_classify)
    monkeypatch.setenv('OPENAI_API_KEY', 'test')
    monkeypatch.setenv('OPENAI_MODEL', 'test-model')
    problem_dir = tmp_path / 'lv-tst-2020'
    problem_dir.mkdir()
    content = problem_dir / 'content_lv.md'
    content.write_text(CONTENT, encoding='utf-8')

    assert preprocess_add_metadata.main([str(tmp_path), 'questionType']) == 1  # one failure

    # The model sees the problem text only: no title, solution or metadata
    assert calls == [
        ('', 'Pierādīt, ka $n^2+n$ ir pāra skaitlis.', '', MetadataProperties.QUESTION_TYPE, None),
        ('', 'Cik ir pirmskaitļu?', '', MetadataProperties.QUESTION_TYPE, None),
        ('', 'Kļūdains uzdevums.', '', MetadataProperties.QUESTION_TYPE, None),
    ]
    judgement = '* _questionTypeSource: questionTypes2-v2/prompt-v1\n* _questionTypeModel: test-model\n'
    expected = (CONTENT
                .replace('* domain:NT\n\n</small>', '* domain:NT\n* _questionType: QTY_ProveUniversal\n'
                         + judgement + '\n</small>')
                .replace('* domain:NT\n</small>', '* domain:NT\n* _questionType: QTY_FindValue\n' + judgement + '</small>'))
    assert content.read_text(encoding='utf-8') == expected
    out = capsys.readouterr().out
    assert 'added: 2, already present: 1, failed: 1' in out

    # A rerun only retries the failed problem
    calls.clear()
    preprocess_add_metadata.main([str(tmp_path), 'questionType'])
    assert [c[1] for c in calls] == ['Kļūdains uzdevums.']


def test_rejects_unsupported_properties(tmp_path, capsys):
    assert preprocess_add_metadata.main([str(tmp_path), 'subdomain']) == 1
    assert ('questionType, domain, hasSolutionStructure, hasSolutionConcept, hasReasoningMethod, '
            'hasReasoningMistake') in capsys.readouterr().out


def test_default_model_comes_from_the_environment(monkeypatch):
    from scripts import openai_utils
    monkeypatch.setattr(openai_utils, 'load_dotenv', lambda path: None)
    monkeypatch.setenv('OPENAI_MODEL', 'some-model')
    assert openai_utils.normalize_openai_provider(None) == 'some-model'
    assert openai_utils.normalize_openai_provider('openai:other-model') == 'other-model'
    monkeypatch.delenv('OPENAI_MODEL')
    with pytest.raises(RuntimeError, match='OPENAI_MODEL'):
        openai_utils.normalize_openai_provider(None)


def test_question_type_prompt_and_answer_check():
    utils = MetadataUtils('test')
    labels = [row['Label'] for row in utils.question_types]
    # The QTY_ leaves of questionTypes2.csv: no group types (L2 = 0), no response formats
    assert labels == ['QTY_FindAll', 'QTY_FindValue', 'QTY_FindOptimal', 'QTY_ConstructExample',
                      'QTY_ConstructProcedure', 'QTY_ProveExistence', 'QTY_ProveUniversal',
                      'QTY_DecideExistence', 'QTY_DecideUniversal', 'QTY_DecideWinner']
    prompt = utils.make_prompt(MetadataProperties.QUESTION_TYPE, 'LV.TST.2020.5.1', 'Uzdevuma teksts.')
    assert prompt.rstrip().endswith('Uzdevums:\n\nUzdevuma teksts.')
    assert 'LV.TST' not in prompt and 'QTY_Prove –' not in prompt and 'RSP_' not in prompt
    check = utils._checked_question_type
    assert check([' QTY_FindAll '], []) == 'QTY_FindAll'
    assert check(['QTY_FindOptimal', 'QTY_ConstructProcedure'], []) == 'QTY_FindOptimal,QTY_ConstructProcedure'
    assert check('QTY_FindAll', []) == 'QTY_FindAll'
    assert check(['FindAll'], []) == 'NA'           # legacy value
    assert check(['QTY_Prove'], []) == 'NA'         # group type, not a leaf
    assert check({'A': ['QTY_FindAll']}, []) == 'NA'


def test_question_type_with_sub_parts():
    utils = MetadataUtils('test')
    text = 'Dots skaitlis $n$. **(A)** Atrodi visus $n$. **(B)** Pierādi, ka $n>1$. **(A)** vēlreiz.'
    prompt = utils.make_prompt(MetadataProperties.QUESTION_TYPE, '', text)
    assert 'Uzdevumam ir apakšpunkti (A), (B).' in prompt
    assert '{"uzdevuma_tips": {"A": ["..."], "B": ["..."]}}' in prompt
    assert 'Uzdevumam nav apakšpunktu' not in prompt
    assert 'Uzdevumam nav apakšpunktu' in utils.make_prompt(MetadataProperties.QUESTION_TYPE, '', 'Bez apakšpunktiem.')

    check = utils._checked_question_type
    assert check({'A': ['QTY_FindAll'], '(B)': ['QTY_ProveUniversal']}, ['A', 'B']) == \
        {'A': 'QTY_FindAll', 'B': 'QTY_ProveUniversal'}
    assert check({'A': ['QTY_FindAll'], 'B': ['QTY_FindOptimal', 'QTY_ConstructProcedure']}, ['A', 'B']) == \
        {'A': 'QTY_FindAll', 'B': 'QTY_FindOptimal,QTY_ConstructProcedure'}
    assert check({'A': ['QTY_FindAll']}, ['A', 'B']) == 'NA'                       # sub-part missing
    assert check({'A': ['QTY_FindAll'], 'B': ['Prove']}, ['A', 'B']) == 'NA'      # invalid value
    assert check(['QTY_FindAll'], ['A', 'B']) == 'NA'                             # not per sub-part


def test_sub_part_answers_become_separate_lines(tmp_path, monkeypatch):
    monkeypatch.setattr(MetadataUtils, 'classify_problem',
                        lambda self, *args, **kwargs: {'A': 'QTY_FindValue', 'B': 'QTY_DecideExistence'})
    monkeypatch.setenv('OPENAI_API_KEY', 'test')
    monkeypatch.setenv('OPENAI_MODEL', 'test-model')
    content = tmp_path / 'lv-tst-2020' / 'content_lv.md'
    content.parent.mkdir()
    content.write_text('# <lo-sample/> LV.TST.2020.7.1\n\n**(A)** Cik ...? **(B)** Vai var ...?\n\n'
                       '<small>\n\n* questionType:A: QTY_FindValue\n* questionType:B: QTY_Decide\n\n</small>\n',
                       encoding='utf-8')
    preprocess_add_metadata.main([str(tmp_path), 'questionType'])
    assert ('* questionType:B: QTY_Decide\n* _questionType:A: QTY_FindValue\n'
            '* _questionType:B: QTY_DecideExistence\n* _questionTypeSource: questionTypes2-v2/prompt-v1\n'
            '* _questionTypeModel: test-model\n\n</small>') in content.read_text(encoding='utf-8')
