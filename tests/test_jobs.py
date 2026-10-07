from fastapi.testclient import TestClient
from ai_career_agent.main import app

client = TestClient(app)


def test_create_job():
    response = client.post(
        "/jobs",
        json={
            "company": "Acme",
            "title": "Solutions Architect",
            "description": "Design enterprise software solutions.",
        },
    )

    assert response.status_code == 201
    assert response.json()["company"] == "Acme"
    assert response.json()["title"] == "Solutions Architect"
    assert response.json()["id"] == 1


def test_create_job_requires_title():
    response = client.post(
        "/jobs",
        json={
            "company": "Acme",
            "description": "Design enterprise software solutions.",
        },
    )

    assert response.status_code == 422

def test_create_job_invalid_travel_percent():
    response = client.post(
        "/jobs",
        json={
            "company": "Acme",
            "title": "Solutions Architect",
            "description": "Design enterprise software solutions.",
            "travel_percent": "a lot",
        },
    )

    assert response.status_code == 422


