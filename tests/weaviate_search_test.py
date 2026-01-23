import pytest
import os
import sys

# Add the parent directory to sys.path so we can import scripts
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from dotenv import load_dotenv
from scripts.weaviate_utils import WeaviateUtils

@pytest.fixture
def utils():
    # Try loading .env from current directory or tests directory
    load_dotenv()
    load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '.env'))

    weaviate_url = os.getenv('WEAVIATE_URL', 'NA')
    weaviate_api_key = os.getenv('WEAVIATE_API_KEY', 'NA')
    openai_api_key = os.getenv('OPENAI_API_KEY', 'NA')
    
    if weaviate_url == 'NA' or weaviate_api_key == 'NA':
        pytest.fail(
            "Missing Weaviate credentials! Please create a .env file in the project root or 'tests/' directory.\n"
            "It must contain:\n"
            "WEAVIATE_URL=...\n"
            "WEAVIATE_API_KEY=...\n"
            "OPENAI_API_KEY=..."
        )

    print(f"\n[Fixture] Connecting to Weaviate at {weaviate_url}...")
    try:
        utils_obj = WeaviateUtils(weaviate_url, weaviate_api_key, openai_api_key)
    except Exception as e:
        pytest.fail(f"Failed to initialize Weaviate client: {e}")

    yield utils_obj
    
    if utils_obj.client and utils_obj.client.is_connected():
         utils_obj.client.close() 

def test_get_problems_returns_ten_results(utils):
    """
    Test that searching for a specific problem returns exactly 10 results.
    Assumes data is already ingested.
    """
    query = """
    Mihailo izvēlējās 3 dažādus pozitīvus skaitļus $a,b,c$.
    Viņš uz tāfeles uzrakstīja sekojošus 6 skaitļus: $a+b$, $b+c$, $c+a$, $ab$, $bc$, $ca$. Kāds ir mazākais iespējamais atšķirīgu skaitļu skaits, ko var šādi uzrakstīt uz tāfeles?
    """
    
    print(f"\n--- Test: Search for 'Mihailo' problem (limit=10) ---")
    
    # helper wrapper returns (code, data)
    code, data = utils.get_problems(query, 10)
    
    assert code == 0, f"Expected return code 0, got {code}"
    
    problems = data.get('problems', [])
    assert len(problems) == 10, f"Expected 10 problems, got {len(problems)}"
    
    print(f'\nProblem 0: {problems[0]}')
    

    print("\nReturned Problem IDs:")
    for prob in problems:
        pid = prob.get('problemID', 'UNKNOWN_ID')
        print(f" - {pid}")

if __name__ == "__main__":
    sys.exit(pytest.main(["-s", __file__]))
