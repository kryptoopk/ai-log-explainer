from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_analyze_log_returns_successful_response() -> None:
    response = client.post(
        "/analyze",
        json={
            "log": "Failed password for root from 192.168.1.10",
        },
    )

    assert response.status_code == 200
    assert response.json() == {
        "received_log": "Failed password for root from 192.168.1.10",
        "category": "authentication",
        "severity": "medium",
        "reason": "Failed password detected in log.",
        "recommendation": (
            "Verify credentials and inspect the source IP."
        ),
        "message": "Log analyzed successfully",
    }


def test_analyze_log_rejects_empty_log() -> None:
    response = client.post(
        "/analyze",
        json={
            "log": "",
        },
    )

    assert response.status_code == 422


def test_analyze_log_rejects_whitespace_only_log() -> None:
    response = client.post(
        "/analyze",
        json={
            "log": "   ",
        },
    )

    assert response.status_code == 422