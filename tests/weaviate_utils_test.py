import json
import random
import pytest
import os

# Place .env file in "tests" directory
# the parent directory to "scripts" must be in PYTHONPATH
from dotenv import load_dotenv
from scripts.weaviate_utils import WeaviateUtils


@pytest.fixture
def utils():
    load_dotenv()
    weaviate_url = os.getenv('WEAVIATE_URL', 'NA')
    weaviate_api_key = os.getenv('WEAVIATE_API_KEY', 'NA') 
    openai_api_key = os.getenv('OPENAI_API_KEY', 'NA')
    fuseki_url = os.getenv('FUSEKI_URL', 'NA')
    return WeaviateUtils(weaviate_url, weaviate_api_key, openai_api_key)
    # return EliozoClient(weaviate_url, weaviate_api_key, openai_api_key, fuseki_url)

def test_ingest_data(utils):
    utils.set_skipping_mode(True)
    utils.ingest_to_weaviate('../../qualification-project/migration-script/resources/LV-AMO-2004-content.ttl')
    utils.close_client()

def test_search_synchronous(utils): 
    utils.set_skipping_mode(True)
    results = utils.near_search("Problem", "rūķīši", 10)
    for prob in results: 
        print(f"**********prob*********** = {prob}")
    assert len(results) == 10


