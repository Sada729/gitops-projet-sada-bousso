from app import app

def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"Sada Bousso" in response.data

def test_healthz():
    client = app.test_client()
    response = client.get("/healthz")
    assert response.status_code == 200
