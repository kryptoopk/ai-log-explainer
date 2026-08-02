from fastapi.testclient import TestClient # It lets us send fake HTTP requests without opening the browser.
from app.main import app

client = TestClient(app)

def test_health_check() -> None:
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status:" "healthy"} 