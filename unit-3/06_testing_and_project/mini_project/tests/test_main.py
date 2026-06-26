from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()

def test_predict_positive():
    response = client.post("/predict", json={"text": "I am feeling very happy today"})
    assert response.status_code == 200
    assert response.json()["sentiment"] == "Positive"

def test_predict_negative():
    response = client.post("/predict", json={"text": "This is terrible news"})
    assert response.status_code == 200
    assert response.json()["sentiment"] == "Negative"

def test_predict_neutral():
    response = client.post("/predict", json={"text": "I am eating a sandwich"})
    assert response.status_code == 200
    assert response.json()["sentiment"] == "Neutral"

# Run tests by executing: pytest
