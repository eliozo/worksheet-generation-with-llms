import json
import random
import pytest
import os
import re

# Place .env file in "tests" directory
# the parent directory to "scripts" must be in PYTHONPATH
from dotenv import load_dotenv
from scripts.eliozo_client import EliozoClient



@pytest.fixture
def client():
    load_dotenv()
    weaviate_url = os.getenv('WEAVIATE_URL', 'NA')
    weaviate_api_key = os.getenv('WEAVIATE_API_KEY', 'NA') 
    openai_api_key = os.getenv('OPENAI_API_KEY', 'NA')
    fuseki_url = os.getenv('FUSEKI_URL', 'NA')
    fuseki_user = os.getenv('FUSEKI_USER', 'NA')
    fuseki_password = os.getenv('FUSEKI_PASSWORD', 'NA')
    return EliozoClient(weaviate_url, weaviate_api_key, openai_api_key, fuseki_url, fuseki_user, fuseki_password)


def test_add_metadata(client):
    client.add_metadata('test.md', 'questionType', 'OpenAI', 'test_with_qtypes.md')
    with open('test_with_qtypes.md', 'r', encoding='utf-8') as file:
        content = file.read()
    question_types = re.findall(r'_questionType:\s*(\w+)', content)
    assert question_types == ['ProveDisprove', 'FindAll']
    # client.set_reference(f'test_result.json')
    # (retvalue, data) = client.add_metadata('input_file', 'questionType', 'OpenAI')
    # assert retvalue == 0
    # client.store(data)
