import sys
import os
import pytest

# Adjust path to import scripts
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from scripts.problem_markdown_parser import Problem, ProblemMarkdownParser


# ---------------------------------------------------------------------------
#  Sample markdown snippets used across tests
# ---------------------------------------------------------------------------

SINGLE_PROBLEM_MD = """\
# <lo-sample/> LV.AMO.2023.5.1

Skaitļus no $1$ līdz $9$ ieraksti trijstūros.

![](LV.AMO.2023.5.1.png)

<small>

* topic:ArithmeticOperations
* concepts:difference,distance,triangle
* seeAlso:LV.AMO.2023.6.1
* questionType:FindExample
* domain:Comb

</small>


## Atrisinājums

Sk., piemēram, 2. att.

![](LV.AMO.2023.5.1A.png)
"""

TWO_PROBLEMS_MD = """\
# <lo-sample/> LV.AMO.2023.5.1

Problem one text.

<small>

* topic:ArithmeticOperations
* questionType:FindExample
* domain:Comb

</small>

## Atrisinājums

Solution one.


# <lo-sample/> LV.AMO.2023.5.2

Problem two text.

<small>

* concepts:decimal-notation
* questionType:ProveDisprove,ProveDisprove
* domain:NT

</small>

## Atrisinājums

Solution two.
"""

PROBLEM_WITH_TWO_SOLUTIONS_MD = """\
# <lo-sample/> LV.AMO.2023.5.5

Problem text.

<small>

* topic:PigeonholePrinciple
* questionType:FindOptimal
* domain:Comb

</small>


## Atrisinājums

First solution.

## Atrisinājums

Second solution.
"""

PROBLEM_ENGLISH_MD = """\
# <lo-sample/> WW.TST.2023.1

Find all integers $n$.

<small>

* topic:Divisibility
* questionType:FindAll
* domain:NT

</small>

## Solution

We show that $n = 1$.
"""

PROBLEM_NO_SOLUTION_MD = """\
# <lo-sample/> LV.AMO.2023.7.3

Some problem without a solution section.

<small>

* questionType:Prove
* domain:Geom

</small>
"""


SAMPLE_FILE_PATH = os.path.join(
    os.path.dirname(__file__),
    '..', '..', '..', 'math', 'problembase', 'LV.AMO', 'lv-amo-2023', 'content_lv.md'
)
SAMPLE_FILE_PATH = os.path.normpath(SAMPLE_FILE_PATH)


# ===================================================================
#  Tests for extract_sections
# ===================================================================

class TestExtractSections:
    def test_single_problem(self):
        sections = ProblemMarkdownParser.extract_sections(SINGLE_PROBLEM_MD)
        assert len(sections) == 1
        title, body = sections[0]
        assert title == "LV.AMO.2023.5.1"
        assert "Skaitļus" in body

    def test_two_problems(self):
        sections = ProblemMarkdownParser.extract_sections(TWO_PROBLEMS_MD)
        assert len(sections) == 2
        assert sections[0][0] == "LV.AMO.2023.5.1"
        assert sections[1][0] == "LV.AMO.2023.5.2"

    def test_body_does_not_include_heading(self):
        sections = ProblemMarkdownParser.extract_sections(SINGLE_PROBLEM_MD)
        _, body = sections[0]
        assert not body.startswith("# <lo-sample/>")


# ===================================================================
#  Tests for normalize_text
# ===================================================================

class TestNormalizeText:
    def test_strips_small_block(self):
        sections = ProblemMarkdownParser.extract_sections(SINGLE_PROBLEM_MD)
        body = sections[0][1]
        result = ProblemMarkdownParser.normalize_text(body)
        assert "<small>" not in result
        assert "Atrisinājums" not in result
        assert "Skaitļus" in result

    def test_no_small_block_strips_solution(self):
        text = "Some problem.\n\n## Atrisinājums\n\nSolution."
        result = ProblemMarkdownParser.normalize_text(text)
        assert result == "Some problem."


# ===================================================================
#  Tests for extract_solution
# ===================================================================

class TestExtractSolution:
    def test_latvian_solution(self):
        sections = ProblemMarkdownParser.extract_sections(SINGLE_PROBLEM_MD)
        body = sections[0][1]
        solution = ProblemMarkdownParser.extract_solution(body)
        assert solution.startswith("## Atrisinājums")
        assert "piemēram" in solution

    def test_english_solution(self):
        sections = ProblemMarkdownParser.extract_sections(PROBLEM_ENGLISH_MD)
        body = sections[0][1]
        solution = ProblemMarkdownParser.extract_solution(body)
        assert solution.startswith("## Solution")
        assert "n = 1" in solution

    def test_no_solution(self):
        sections = ProblemMarkdownParser.extract_sections(PROBLEM_NO_SOLUTION_MD)
        body = sections[0][1]
        solution = ProblemMarkdownParser.extract_solution(body)
        # Falls back to content after </small>
        assert "Atrisinājums" not in solution


# ===================================================================
#  Tests for get_solutions (splitting multiple solutions)
# ===================================================================

class TestGetSolutions:
    def test_two_solutions(self):
        sections = ProblemMarkdownParser.extract_sections(PROBLEM_WITH_TWO_SOLUTIONS_MD)
        body = sections[0][1]
        solution_text = ProblemMarkdownParser.extract_solution(body)
        solutions = ProblemMarkdownParser.get_solutions(solution_text)
        assert len(solutions) == 2
        assert "First solution" in solutions[0]
        assert "Second solution" in solutions[1]

    def test_single_solution(self):
        sections = ProblemMarkdownParser.extract_sections(SINGLE_PROBLEM_MD)
        body = sections[0][1]
        solution_text = ProblemMarkdownParser.extract_solution(body)
        solutions = ProblemMarkdownParser.get_solutions(solution_text)
        assert len(solutions) == 1

    def test_empty_input(self):
        assert ProblemMarkdownParser.get_solutions("") == []


# ===================================================================
#  Tests for extract_metadata
# ===================================================================

class TestExtractMetadata:
    def test_basic_metadata(self):
        sections = ProblemMarkdownParser.extract_sections(SINGLE_PROBLEM_MD)
        body = sections[0][1]
        meta = ProblemMarkdownParser.extract_metadata(body)
        assert meta["topic"] == ["ArithmeticOperations"]
        assert "difference" in meta["concepts"]
        assert "distance" in meta["concepts"]
        assert "triangle" in meta["concepts"]
        assert meta["questionType"] == ["FindExample"]
        assert meta["domain"] == ["Comb"]

    def test_multi_value_metadata(self):
        sections = ProblemMarkdownParser.extract_sections(TWO_PROBLEMS_MD)
        body = sections[1][1]
        meta = ProblemMarkdownParser.extract_metadata(body)
        assert meta["questionType"] == ["ProveDisprove", "ProveDisprove"]

    def test_no_metadata(self):
        meta = ProblemMarkdownParser.extract_metadata("Just plain text, no <small> block.")
        assert meta == {}


# ===================================================================
#  Tests for extract_grade
# ===================================================================

class TestExtractGrade:
    def test_grade_5(self):
        assert ProblemMarkdownParser.extract_grade("LV.AMO.2023.5.1") == 5

    def test_grade_12(self):
        assert ProblemMarkdownParser.extract_grade("LV.AMO.2023.12.3") == 12

    def test_grade_with_underscore(self):
        assert ProblemMarkdownParser.extract_grade("LV.AMO.2023.10_11.3") == 10

    def test_no_grade(self):
        assert ProblemMarkdownParser.extract_grade("SomeTitle") == 0


# ===================================================================
#  Tests for extract_images
# ===================================================================

class TestExtractImages:
    def test_images(self):
        text = "![](LV.AMO.2023.5.1.png)\nSome text\n![alt](pic.png){ width=200px }"
        images = ProblemMarkdownParser.extract_images(text)
        assert len(images) == 2
        assert images[0] == ("LV.AMO.2023.5.1.png", "")
        assert images[1][0] == "pic.png"
        assert images[1][1] == "200px"


# ===================================================================
#  Tests for add_generated_property
# ===================================================================

class TestAddGeneratedProperty:
    def test_add_string_property(self):
        sections = ProblemMarkdownParser.extract_sections(SINGLE_PROBLEM_MD)
        body = sections[0][1]
        result = ProblemMarkdownParser.add_generated_property(body, "questionType", "FindExample")
        assert "* _questionType: FindExample" in result

    def test_skip_existing_property(self):
        sections = ProblemMarkdownParser.extract_sections(SINGLE_PROBLEM_MD)
        body = sections[0][1]
        # First add
        result = ProblemMarkdownParser.add_generated_property(body, "questionType", "FindExample")
        # Second add should be a no-op
        result2 = ProblemMarkdownParser.add_generated_property(result, "questionType", "Prove")
        assert result2 == result

    def test_add_dict_property(self):
        sections = ProblemMarkdownParser.extract_sections(SINGLE_PROBLEM_MD)
        body = sections[0][1]
        result = ProblemMarkdownParser.add_generated_property(
            body, "hasSolutionConcept",
            {"solutionConcepts": ["pigeonhole", "extremal"], "readingDifficulty": "medium"}
        )
        assert "_hasSolutionConcept: pigeonhole, extremal" in result
        assert "_readingDifficulty: medium" in result

    def test_no_small_block(self):
        text = "Just text without small block."
        result = ProblemMarkdownParser.add_generated_property(text, "foo", "bar")
        assert result == text


# ===================================================================
#  Tests for parse_text (full Problem objects)
# ===================================================================

class TestParseText:
    def test_single_problem(self):
        problems = ProblemMarkdownParser.parse_text(SINGLE_PROBLEM_MD)
        assert len(problems) == 1
        p = problems[0]
        assert isinstance(p, Problem)
        assert p.title == "LV.AMO.2023.5.1"
        assert p.grade == 5
        assert "Skaitļus" in p.problem_text
        assert "Atrisinājums" in p.solution_text
        assert p.meta_dict["domain"] == ["Comb"]

    def test_two_problems(self):
        problems = ProblemMarkdownParser.parse_text(TWO_PROBLEMS_MD)
        assert len(problems) == 2
        assert problems[0].title == "LV.AMO.2023.5.1"
        assert problems[1].title == "LV.AMO.2023.5.2"
        assert problems[0].grade == 5
        assert problems[1].grade == 5

    def test_problem_fields_populated(self):
        problems = ProblemMarkdownParser.parse_text(TWO_PROBLEMS_MD)
        p = problems[0]
        assert p.problem_text != ""
        assert p.solution_text != ""
        assert len(p.meta_dict) > 0
        assert "<small>" not in p.problem_text


# ===================================================================
#  Tests against real file: LV.AMO.2023 content_lv.md
# ===================================================================

@pytest.mark.skipif(
    not os.path.exists(SAMPLE_FILE_PATH),
    reason=f"Sample file not found: {SAMPLE_FILE_PATH}"
)
class TestRealFile:
    @pytest.fixture(scope="class")
    def problems(self):
        return ProblemMarkdownParser.parse_file(SAMPLE_FILE_PATH)

    def test_problem_count(self, problems):
        """LV.AMO.2023 has 40 problems (grades 5-12, 5 problems each)."""
        assert len(problems) == 40

    def test_first_problem_title(self, problems):
        assert problems[0].title == "LV.AMO.2023.5.1"

    def test_last_problem_title(self, problems):
        assert problems[-1].title == "LV.AMO.2023.12.5"

    def test_grade_extraction(self, problems):
        # First 5 problems should be grade 5
        for p in problems[:5]:
            assert p.grade == 5, f"{p.title} should be grade 5"
        # Last 5 problems should be grade 12
        for p in problems[-5:]:
            assert p.grade == 12, f"{p.title} should be grade 12"

    def test_all_have_metadata(self, problems):
        for p in problems:
            assert len(p.meta_dict) > 0, f"{p.title} should have metadata"

    def test_all_have_domain(self, problems):
        valid_domains = {"Alg", "Comb", "Geom", "NT"}
        for p in problems:
            if "domain" in p.meta_dict:
                for d in p.meta_dict["domain"]:
                    assert d in valid_domains, f"{p.title}: unexpected domain '{d}'"

    def test_all_have_problem_text(self, problems):
        for p in problems:
            assert len(p.problem_text) > 10, f"{p.title} should have problem text"

    def test_all_have_solution(self, problems):
        for p in problems:
            assert len(p.solution_text) > 0, f"{p.title} should have a solution"

    def test_problem_text_no_metadata(self, problems):
        for p in problems:
            assert "<small>" not in p.problem_text, f"{p.title}: problem_text should not contain <small>"
            assert "Atrisinājums" not in p.problem_text, f"{p.title}: problem_text should not contain solution"

    def test_metadata_keys(self, problems):
        """Spot-check known metadata for problem LV.AMO.2023.5.1."""
        p = problems[0]
        assert p.meta_dict["topic"] == ["ArithmeticOperations"]
        assert p.meta_dict["questionType"] == ["FindExample"]
        assert p.meta_dict["domain"] == ["Comb"]
