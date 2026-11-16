from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_hello():
    print("Não deve lançar a q1")
    response = client.get("/hello")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, World!"}


def test_healthy():
    response = client.get("/healthy")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}
