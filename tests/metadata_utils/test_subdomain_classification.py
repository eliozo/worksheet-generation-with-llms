import os
import sys
import pytest
from dotenv import load_dotenv

# Add scripts directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from scripts.metadata_utils_new import MetadataUtils, MetadataProperties

@pytest.fixture
def metadata_utils():
    # Load environment variables from scripts/.env
    scripts_env = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../scripts/.env'))
    load_dotenv(scripts_env)
    
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        pytest.skip("OPENAI_API_KEY not found in scripts/.env")
    
    return MetadataUtils(api_key)

def test_classify_subdomain_equations(metadata_utils):
    problem_text = "Atrisināt vienādojumu $x^2 + 5x + 6 = 0$."
    
    # We expect something related to Equations
    subdomain = metadata_utils.classify_problem(problem_text, "", MetadataProperties.SUBDOMAIN)
    
    print(f"Equations problem classifications: {subdomain}")
    assert subdomain != "NA"
    assert "DOM_" in subdomain # Subdomains usually start with DOM_
    # Verify it is one of the loaded subdomains (just checking format primarily, but could check specific if stable)
    # The actual return from LLM might be just the ID "DOM_Equations" or "DOM_QuadraticEquations" etc.
    # The prompt asks for JSON {subdomain: ...} and classify_problem returns the value.

def test_classify_subdomain_geometry(metadata_utils):
    problem_text = "Dots trijstūris ABC. Pierādīt, ka leņķu summa ir 180 grādi."
    
    subdomain = metadata_utils.classify_problem(problem_text, "", MetadataProperties.SUBDOMAIN)
    
    print(f"Geometry problem classifications: {subdomain}")
    assert subdomain != "NA"
    assert "DOM_" in subdomain

def test_classify_subdomain_inequalities(metadata_utils):
    problem_text = "Pierādīt, ka visiem pozitīviem skaitļiem a, b izpildās nevienādība a + b >= 2*sqrt(ab)."
    
    subdomain = metadata_utils.classify_problem(problem_text, "", MetadataProperties.SUBDOMAIN)
    
    print(f"Inequalities problem classifications: {subdomain}")
    assert subdomain == "DOM_Inequalities" or "Inequalities" in subdomain 
