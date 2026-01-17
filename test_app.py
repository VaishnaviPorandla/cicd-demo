import pytest
from app import app

def test_home_route():
    # Create a test client to simulate a browser
    client = app.test_client()
    
    # Make a GET request to the homepage
    response = client.get('/')
    
    # Check if the website works (Status 200 means OK)
    assert response.status_code == 200
    
    # Check if the text matches
    assert b"Hello! I was deployed automatically" in response.data