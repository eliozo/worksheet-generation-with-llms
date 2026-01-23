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
    
    print("\n[Fixture] Closing Weaviate client...")
    # Add check if client needs closing or is already closed
    # The utils methods often close the client, so we don't strictly need to do it here 
    # unless we want to ensure cleanup. Since methods close it, doing it here might be redundant
    # but safe if we check.
    if utils_obj.client and utils_obj.client.is_connected():
         utils_obj.client.close() 

def test_drop_collections_make_search_fail(utils):
    """
    Test that after dropping collections, searching throws an exception.
    """
    print("\n--- Test: Drop Collections and Search Failure ---")
    
    # 1. Drop all collections
    utils.drop_collections()
    
    # 2. Try to search "Problem" - expecting Exception
    with pytest.raises(Exception) as excinfo:
        utils.near_search("Problem", "test query", 5)
    
    print(f"Caught expected exception: {excinfo.value}")
    assert "does not exist" in str(excinfo.value)
    # utils.close_client() # handled by fixture

def test_create_schema_makes_search_empty(utils):
    """
    Test that after creating schema, searching returns empty list (no error).
    """
    print("\n--- Test: Create Schema and Search Empty ---")
    
    # 1. Create Schema
    utils.create_schema()
    
    # 2. Search "Problem" - expecting empty list, NO exception
    results = utils.near_search("Problem", "test query", 5)
    print(f"Search results: {results}")
    
    assert isinstance(results, list)
    assert len(results) == 0
    # utils.close_client() # handled by fixture

# def test_get_problems_lifecycle(utils):
#     """
#     Test the get_problems wrapper specifically.
#     """
#     print("\n--- Test: get_problems Lifecycle ---")

#     utils.drop_collections()
#     with pytest.raises(Exception):
#         utils.get_problems("some query", 5)
#     utils.create_schema()

#     code, data = utils.get_problems("some query", 5)
#     assert code == 0
#     assert data['problems'] == []

if __name__ == "__main__":
    sys.exit(pytest.main(["-s", __file__]))


