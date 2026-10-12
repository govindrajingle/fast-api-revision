from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

# Test home api


def test_home():
    response = client.get("/")
    # check status code first then response data
    assert response.status_code == 200
    assert response.json() == {"message": "hello, govind"}


def test_add():
    response = client.get("/add?a=10&b=3")
    assert response.status_code == 200
    assert response.json() == {"result": 13}
