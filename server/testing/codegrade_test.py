import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from app import app


def test_codegrade_placeholder():
    """Codegrade placeholder test"""
    assert 1 == 1


def test_index_route():
    """Test the index route returns correct response"""
    with app.test_client() as client:
        response = client.get("/")
        assert response.status_code == 200
        assert b"The host for this page is" in response.data
        assert b"The name of this application is" in response.data
        assert b"The path of this application on the user's device is" in response.data
