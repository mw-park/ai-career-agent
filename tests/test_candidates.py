from fastapi.testclient import TestClient
from ai_career_agent.main import app

client = TestClient(app)


def test_create_candidate():
    response = client.post("/candidates", json={
        "name": "Test Candidate",
        "headline": "Senior Solutions Architect",
        "summary": "Enterprise integration experience",
        "skills": ["Python", "AWS"],
        "target_roles": ["Solutions Architect"],
        "preferences": {
            "minimum_salary": 175000,
            "maximum_travel_percent": 10
        }
    })

    assert response.status_code == 201
    assert response.json()["id"] == 1
    assert response.json()["preferences"]["maximum_travel_percent"] == 10

def test_create_candidate_requires_name():
    response = client.post("/candidates", json={
        "headline": "Senior Solutions Architect",
        "summary": "Enterprise integration experience",
        "skills": ["Python", "AWS"],
        "target_roles": ["Solutions Architect"]
    })

    assert response.status_code == 422
