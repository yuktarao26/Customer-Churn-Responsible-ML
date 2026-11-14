
from fastapi.testclient import TestClient
import app.main as main_module

client = TestClient(main_module.app)


def test_root_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["docs"] == "/docs"


def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200


def test_predict_endpoint(monkeypatch):
    def fake_predict(messages):
        return [{
            "message": messages[0],
            "label": "spam",
            "spam_probability": 0.91,
            "ham_probability": 0.09,
        }]

    monkeypatch.setattr(main_module, "predict_messages", fake_predict)

    response = client.post(
        "/predict",
        json={"messages": ["You won a prize!"]}
    )

    assert response.status_code == 200
    assert response.json()["predictions"][0]["label"] == "spam"


def test_empty_messages():
    response = client.post("/predict", json={"messages": []})
    assert response.status_code == 422
