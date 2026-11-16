"""Regression tests for the prompts in scripts/metadata_utils.yaml."""

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from scripts.metadata_utils import (ADD_METADATA_PROPERTIES, PLACEHOLDER_RE, MetadataProperties,
                                    MetadataUtils, fill_placeholders, load_prompts)

KNOWN_PLACEHOLDERS = {'problem_text', 'solution_text', 'title', 'domain', 'question_types',
                      'subdomains', 'concepts', 'domain_methods', 'domain_mistakes'}


def test_every_property_has_a_system_message_and_a_prompt():
    prompts = load_prompts()
    for prop in list(ADD_METADATA_PROPERTIES) + [MetadataProperties.SUBDOMAIN]:
        entry = prompts[prop.value]
        assert entry['system'].strip() and entry['prompt'].strip(), prop
        assert '{problem_text}' in entry['prompt'], prop


def test_templates_use_only_known_placeholders():
    for name, entry in load_prompts().items():
        for text in entry.values():
            assert set(PLACEHOLDER_RE.findall(text)) <= KNOWN_PLACEHOLDERS, name


def test_placeholders_are_filled_in_one_pass():
    filled = fill_placeholders('A {problem_text} B {title} {"json": {x}}',
                               {'problem_text': 'text with {title}', 'title': 'T'})
    assert filled == 'A text with {title} B T {"json": {x}}'


def test_rendered_prompt_keeps_braces_and_backslashes():
    utils = MetadataUtils('test')
    prompt = utils.make_prompt(MetadataProperties.HAS_REASONING_METHOD, ' LV.TST.2020.7.1 ',
                               ' Pierādi, ka {x} ir $\\alpha$. ', ' Atrisinājums. ', {'domain': ['NT']})
    assert '```Pierādi, ka {x} ir $\\alpha$.```' in prompt
    assert 'Uzdevums: "LV.TST.2020.7.1"' in prompt and 'nozare ir **NT**' in prompt
    assert '"newMethod": {"label": "RepunitFactorization",' in prompt  # JSON example, single braces
    assert not set(PLACEHOLDER_RE.findall(prompt)) & KNOWN_PLACEHOLDERS  # all filled in
    system = utils.make_sys_instructions(MetadataProperties.DOMAIN)
    assert '{"domain": ["Alg"]}' in system
