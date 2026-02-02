import sys
import os
import re
import pytest
from unittest.mock import MagicMock, patch

# Ensure strict path setup so we can import 'scripts'
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from scripts.metadata_utils_new import MetadataUtils, MetadataProperties

# -----------------------------------------------------------------------------
# Helper function copied from eliozo_client.py for testing purposes
# -----------------------------------------------------------------------------
def add_generated_metadata_property(md_text, prop_name, generated_value):
    small_block_re = re.compile(r'(<small>)(.*?)(</small>)', re.DOTALL)
    match = small_block_re.search(md_text)
    
    # The property specific tag to check if it exists
    check_tag = f"_{prop_name}:"

    if match:
        before_tag = match.group(1)
        middle_block = match.group(2)
        after_tag = match.group(3)

        if check_tag in middle_block:
            return md_text

        existing_content = middle_block.strip()
        
        lines_to_add = []
        if isinstance(generated_value, dict):
            # Handle dictionary, specifically for subdomain
            val_main = generated_value.get(prop_name, [])
            if isinstance(val_main, list):
                val_str = ", ".join(val_main)
            else:
                val_str = str(val_main)
            
            lines_to_add.append(f"* {check_tag} {val_str}")
            
            # Check for alternative
            alt_key = f"{prop_name}_alternative"
            alt_val = generated_value.get(alt_key)
            if alt_val:
                lines_to_add.append(f"* _{alt_key}: {alt_val}")
        else:
            lines_to_add.append(f"* {check_tag} {generated_value}")
        
        new_str = "\n".join(lines_to_add)

        if existing_content:
            new_content = existing_content + "\n" + new_str
        else:
            new_content = new_str

        updated_block = f"{before_tag}\n\n{new_content}\n\n{after_tag}"

        return (
            md_text[:match.start()] +
            updated_block +
            md_text[match.end():]
        )
    else:
        return md_text

# -----------------------------------------------------------------------------
# Tests
# -----------------------------------------------------------------------------

@patch('scripts.metadata_utils_new.OpenaiUtils')
def test_classify_and_insert_alternative_subdomain(MockOpenaiUtils):
    # Setup Mock
    mock_instance = MockOpenaiUtils.return_value
    mock_instance.json_request.return_value = {
        "subdomain": ["DOM_Best_Guess"],
        "subdomain_alternative": "Domain_XYZ"
    }

    # Initialize Utils
    utils = MetadataUtils(openai_api_key="fake-key")
    
    # Call process
    problem_text = "Some problem text"
    result = utils.classify_problem(problem_text, "", MetadataProperties.SUBDOMAIN)

    # 1. Verify Dictionary Return
    assert isinstance(result, dict)
    assert result["subdomain"] == ["DOM_Best_Guess"]
    assert result["subdomain_alternative"] == "Domain_XYZ"

    # 2. Verify Markdown Insertion
    dummy_md = """# Title

Problem content...

<small>
* _prior: 123
</small>
"""
    updated_md = add_generated_metadata_property(dummy_md, "subdomain", result)

    print(f"DEBUG: Updated Markdown:\n{updated_md}")

    # Check if lines exist
    assert "* _subdomain: DOM_Best_Guess" in updated_md
    assert "* _subdomain_alternative: Domain_XYZ" in updated_md
    
    # Verify formatting (ensure multiple items are joined if we had multiple)
    # Let's test mixed case quickly with manual dict
    mixed_result = {
        "subdomain": ["DOM_A", "DOM_B"],
        "subdomain_alternative": "DOM_C"
    }
    updated_mixed = add_generated_metadata_property(dummy_md, "subdomain", mixed_result)
    assert "* _subdomain: DOM_A, DOM_B" in updated_mixed
    assert "* _subdomain_alternative: DOM_C" in updated_mixed
