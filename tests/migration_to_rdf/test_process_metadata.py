import sys
import os
import pytest
import rdflib
from rdflib import Graph, URIRef, Literal, RDF

# Adjust path to import scripts
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

# Mock 'markdown' module before import as it is missing in venv and not needed for this test
from unittest.mock import MagicMock
sys.modules["markdown"] = MagicMock()

from scripts.markdown_proc.mdchunk_reader import process_metadata, extract_metadata, eliozo_ns

@pytest.fixture
def mock_graph():
    g = Graph()
    g.bind("eliozo", rdflib.Namespace(eliozo_ns))
    return g

@pytest.fixture
def problem_node():
    return URIRef(eliozo_ns + "TEST.PROBLEM.1")

def test_process_metadata_regular(mock_graph, problem_node):
    """Test processing of regular properties"""
    meta_dict = {
        "grade": ["10"],
        "topic": ["Algebra"],
        "subdomain": ["Polynomials"]
    }
    
    process_metadata(mock_graph, problem_node, meta_dict)
    
    # Check regular literal
    assert (problem_node, URIRef(eliozo_ns + "grade"), Literal("10")) in mock_graph
    # Check topic (ObjectProperty)
    assert (problem_node, URIRef(eliozo_ns + "topic"), URIRef(eliozo_ns + "Algebra")) in mock_graph
    # Check subdomain
    assert (problem_node, URIRef(eliozo_ns + "subdomain"), URIRef(eliozo_ns + "Polynomials")) in mock_graph

def test_process_metadata_generated_subdomain_conflict(mock_graph, problem_node, capsys):
    """Test Case 1: Both exist but differ (Warning expected, _subdomain ignored)"""
    meta_dict = {
        "subdomain": ["ManualValue"],
        "_subdomain": ["GeneratedValue"]
    }
    
    process_metadata(mock_graph, problem_node, meta_dict)
    
    # Should contain ManualValue
    assert (problem_node, URIRef(eliozo_ns + "subdomain"), URIRef(eliozo_ns + "ManualValue")) in mock_graph
    # Should NOT contain GeneratedValue
    assert (problem_node, URIRef(eliozo_ns + "subdomain"), URIRef(eliozo_ns + "GeneratedValue")) not in mock_graph
    
    # Check warning
    captured = capsys.readouterr()
    assert "WARNING" in captured.out
    assert "Subdomain mismatch" in captured.out

def test_process_metadata_generated_subdomain_promotion(mock_graph, problem_node):
    """Test Case 2: Only generated exists (Promoted to subdomain)"""
    meta_dict = {
        "_subdomain": ["GeneratedValue"]
    }
    
    process_metadata(mock_graph, problem_node, meta_dict)
    
    # Should contain GeneratedValue as proper subdomain
    assert (problem_node, URIRef(eliozo_ns + "subdomain"), URIRef(eliozo_ns + "GeneratedValue")) in mock_graph

def test_process_metadata_generated_subdomain_match(mock_graph, problem_node, capsys):
    """Test Case 1b: Both exist and match (No warning, _subdomain ignored)"""
    meta_dict = {
        "subdomain": ["SameValue"],
        "_subdomain": ["SameValue"]
    }
    
    process_metadata(mock_graph, problem_node, meta_dict)
    
    # Should contain SameValue
    assert (problem_node, URIRef(eliozo_ns + "subdomain"), URIRef(eliozo_ns + "SameValue")) in mock_graph
    
    # Check NO warning
    captured = capsys.readouterr()
    assert "WARNING" not in captured.out

def test_extract_metadata_parsing():
    """Verify our assumption on how metadata is parsed from markdown string"""
    md_text = """
Some text
<small>
* grade: 10
* _subdomain: GenSub
</small>
"""
    meta = extract_metadata(md_text)
    assert meta["grade"] == ["10"]
    assert meta["_subdomain"] == ["GenSub"]

