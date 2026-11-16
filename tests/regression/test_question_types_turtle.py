"""Regression tests for question types, problem parts and response formats in the md -> ttl conversion."""

import os
import sys

import rdflib

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from scripts.markdown_proc.mdchunk_reader import markdown_md_to_turtle

E = rdflib.Namespace('http://www.dudajevagatve.lv/eliozo#')

CONTENT = """\
# <lo-sample/> LV.TST.2020.7.1

Vai var ...?

**(A)** ja $n=2$;
**(B)** ja $n=3$?

<small>

* questionType:A: QTY_DecideExistence
* questionType:B:
* _questionType:A: QTY_DecideUniversal
* _questionType:B: QTY_DecideExistence
* _questionTypeSource: questionTypes2-v2/prompt-v1
* _questionTypeModel: test-model
* domain:Comb

</small>

# <lo-sample/> LV.TST.2020.7.2

Atrodi visus $x$.

<small>

* questionType:QTY_FindAll
* responseFormat:RSP_AnswerNumeric

</small>

# <lo-sample/> LV.TST.2020.7.3

Cik ...?

<small>

* questionType:
* _questionType: QTY_FindValue,QTY_ConstructExample
* _questionTypeSource: questionTypes2-v2/prompt-v1
* _questionTypeModel: test-model

</small>
"""


def literals(g, node, prop):
    return sorted(str(o) for o in g.objects(node, E[prop]))


def test_question_types_parts_and_response_formats(tmp_path):
    md = tmp_path / 'content_lv.md'
    md.write_text(CONTENT, encoding='utf-8')
    ttl = tmp_path / 'content_lv.ttl'
    markdown_md_to_turtle(str(md), str(ttl), 'lv', True)
    g = rdflib.Graph().parse(str(ttl))

    # Sub-parts: named ProblemPart resources with label, number and their own question type
    p1 = E['LV.TST.2020.7.1']
    part_a, part_b = E['PART.LV.TST.2020.7.1.A'], E['PART.LV.TST.2020.7.1.B']
    assert set(g.objects(p1, E.problemPart)) == {part_a, part_b}
    assert (part_a, rdflib.RDF.type, E.ProblemPart) in g
    assert literals(g, part_a, 'partLabel') == ['A'] and literals(g, part_b, 'partNumber') == ['2']
    assert literals(g, part_a, 'questionType') == ['QTY_DecideExistence']        # human value wins
    assert literals(g, part_b, 'questionType') == ['QTY_DecideExistence']        # empty: LLM value promoted
    assert literals(g, part_a, '_questionType') == ['QTY_DecideUniversal']       # LLM value kept
    assert literals(g, part_a, '_questionTypeModel') == ['test-model']
    assert literals(g, part_b, '_questionTypeSource') == ['questionTypes2-v2/prompt-v1']
    # The problem has the question types of its parts as well
    assert literals(g, p1, 'questionType') == ['QTY_DecideExistence']
    assert literals(g, p1, '_questionType') == ['QTY_DecideExistence', 'QTY_DecideUniversal']
    assert literals(g, p1, 'responseFormat') == ['RSP_SolutionFull']             # default
    assert literals(g, p1, 'domain') == ['Comb']

    # No sub-parts: the question type is on the problem, as before
    p2 = E['LV.TST.2020.7.2']
    assert list(g.objects(p2, E.problemPart)) == []
    assert literals(g, p2, 'questionType') == ['QTY_FindAll']
    assert literals(g, p2, 'responseFormat') == ['RSP_AnswerNumeric']
    assert literals(g, p2, '_questionType') == [] and literals(g, p2, '_questionTypeModel') == []

    # Implicit sub-parts (several types, no markers): all promoted to the problem
    p3 = E['LV.TST.2020.7.3']
    assert literals(g, p3, 'questionType') == ['QTY_ConstructExample', 'QTY_FindValue']
    assert literals(g, p3, '_questionTypeModel') == ['test-model']

    # One query finds problems with and without sub-parts
    found = {str(r[0]) for r in g.query(
        'PREFIX eliozo: <http://www.dudajevagatve.lv/eliozo#> '
        'SELECT ?id WHERE { ?p eliozo:problemID ?id ; eliozo:questionType ?t . '
        'FILTER (?t IN ("QTY_DecideExistence", "QTY_FindAll")) }')}
    assert found == {'LV.TST.2020.7.1', 'LV.TST.2020.7.2'}
