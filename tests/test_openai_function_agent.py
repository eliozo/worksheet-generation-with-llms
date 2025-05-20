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

def client():
    load_dotenv()
    weaviate_url = os.getenv('WEAVIATE_URL', 'NA')
    weaviate_api_key = os.getenv('WEAVIATE_API_KEY', 'NA') 
    openai_api_key = os.getenv('OPENAI_API_KEY', 'NA')
    fuseki_url = os.getenv('FUSEKI_URL', 'NA')
    fuseki_user = os.getenv('FUSEKI_USER', 'NA')
    fuseki_password = os.getenv('FUSEKI_PASSWORD', 'NA')
    with open('get-problems/task.json', 'r', encoding='utf-8') as f:
        task_data = json.load(f)
    return OpenaiFunctionAgent(openai_api_key, fuseki_url, fuseki_user, fuseki_password, weaviate_url, weaviate_api_key, task_data)

def test_list_subtopics(client):
    result = client.list_subtopics('Alg')
    assert len(result) >= 10
    result[0]['label'] == "AlgebraicTransformations"

def test_find_topics(client):
    result = client.find_topics()
    assert len(result) > 0

def test_query_fuseki(client):
    result = client.query_fuseki('ArithmeticIdentities')
    assert len(result) >= 1
    assert result[0]['problemid'] == 'LV.AMO.2023.5.1'
    print("AAAAAAAA")
    print(result[0])
    assert len(result[0]['solution']) > 20

