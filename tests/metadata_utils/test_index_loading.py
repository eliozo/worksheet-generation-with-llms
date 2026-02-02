import sys
import os
import pytest
from unittest.mock import MagicMock

# Ensure strict path setup so we can import 'scripts'
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from scripts.metadata_utils_new import MetadataUtils, MetadataProperties

@pytest.fixture
def metadata_utils():
    return MetadataUtils(openai_api_key="fake-key")

def test_load_subdomains_structure(metadata_utils):
    """
    Check if subdomains are loaded as a list of dictionaries with correct fields.
    """
    subdomains = metadata_utils.subdomains
    assert isinstance(subdomains, list)
    assert len(subdomains) > 0
    
    # Check structure of the first item
    first_item = subdomains[0]
    assert isinstance(first_item, dict)
    assert "label" in first_item
    assert "desc" in first_item
    assert "branch" in first_item
    assert "formatted" in first_item

def test_load_subdomains_content(metadata_utils):
    """
    Check specific entries to ensure 'branch' is mapped correctly from L1.
    Mappings expected:
    L1=1 -> Algebra
    L1=2 -> Combinatorics
    L1=3 -> Geometry
    L1=4 -> NumberTheory
    """
    subdomains = metadata_utils.subdomains

    # Helper to find item by label
    def find_by_label(lbl):
        return next((item for item in subdomains if item['label'] == lbl), None)

    # 1. Test Algebra (L1=1)
    # Using 'DOM_Inequalities' which has L1=1 in CSV
    ineq = find_by_label("DOM_Inequalities")
    assert ineq is not None
    assert ineq['branch'] == "Algebra"
    # Check simplified substring to avoid case/inflection issues
    assert "nevienādīb" in ineq['desc'].lower() or "inequalities" in ineq['desc'].lower()

    # 2. Test Combinatorics (L1=2)
    # Using 'DOM_CombinatorialGames' which has L1=2
    comb_game = find_by_label("DOM_CombinatorialGames")
    assert comb_game is not None
    assert comb_game['branch'] == "Combinatorics"

    # 3. Test Geometry (L1=3)
    # Using 'DOM_Triangles' which has L1=3
    tri = find_by_label("DOM_Triangles")
    assert tri is not None
    assert tri['branch'] == "Geometry"

    # 4. Test NumberTheory (L1=4)
    # Using 'DOM_Primes' or similar. 
    # CSV has 'DOM_PrimeFactors' with L1=4
    primes = find_by_label("DOM_PrimeFactors")
    assert primes is not None
    assert primes['branch'] == "NumberTheory"

    # 5. Check formatted string
    # Verify it looks like "Label [Branch: BranchName] (Desc)"
    assert ineq['formatted'].startswith("DOM_Inequalities [Branch: Algebra] (")
    assert ineq['formatted'].endswith(")")
