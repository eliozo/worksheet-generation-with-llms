import json
import random
import pytest
import os
import re

# Place .env file in "tests" directory
# the parent directory to "scripts" must be in PYTHONPATH
from dotenv import load_dotenv
from scripts.eliozo_client import EliozoClient
from scripts.openai_function_agent import OpenaiFunctionAgent


@pytest.fixture
# def client():
#     load_dotenv()
#     weaviate_url = os.getenv('WEAVIATE_URL', 'NA')
#     weaviate_api_key = os.getenv('WEAVIATE_API_KEY', 'NA') 
#     openai_api_key = os.getenv('OPENAI_API_KEY', 'NA')
#     fuseki_url = os.getenv('FUSEKI_URL', 'NA')
#     fuseki_user = os.getenv('FUSEKI_USER', 'NA')
#     fuseki_password = os.getenv('FUSEKI_PASSWORD', 'NA')
#     return EliozoClient(weaviate_url, weaviate_api_key, openai_api_key, fuseki_url, fuseki_user, fuseki_password)
def client():
    load_dotenv()
    weaviate_url = os.getenv('WEAVIATE_URL', 'NA')
    weaviate_api_key = os.getenv('WEAVIATE_API_KEY', 'NA') 
    openai_api_key = os.getenv('OPENAI_API_KEY', 'NA')
    fuseki_url = os.getenv('FUSEKI_URL', 'NA')
    fuseki_user = os.getenv('FUSEKI_USER', 'NA')
    fuseki_password = os.getenv('FUSEKI_PASSWORD', 'NA')
    return OpenaiFunctionAgent(openai_api_key, fuseki_url, fuseki_user, fuseki_password, weaviate_url, weaviate_api_key)


# def test_add_metadata(client):
#     client.add_metadata('test.md', 'questionType', 'OpenAI', 'test_with_qtypes.md')
#     with open('test_with_qtypes.md', 'r', encoding='utf-8') as file:
#         content = file.read()
#     question_types = re.findall(r'_questionType:\s*(\w+)', content)
#     assert question_types == ['ProveDisprove', 'FindAll']
#     # client.set_reference(f'test_result.json')
#     # (retvalue, data) = client.add_metadata('input_file', 'questionType', 'OpenAI')
#     # assert retvalue == 0
#     # client.store(data)

def test_find_topics(client):
    result = client.find_topics('Dirihlē princips')
    assert len(result) > 0

def test_query_fuseki(client):
    result = client.query_fuseki('ArithmeticIdentities')
    assert len(result) >= 1
    assert result[0]['problemid'] == 'LV.AMO.2023.5.1'