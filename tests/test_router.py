from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_root_endpoint_returns_welcome_message():
    response = client.get("/")

    assert response.status_code == 200
    assert "Visit /docs" in response.json()["message"]


def test_generate_endpoint_returns_success_when_services_succeed(monkeypatch):
    monkeypatch.setattr(
        "router.router.analyze_repo",
        lambda provider, repo_url, token, branch: (
            "analysis.csv",
            [{"file_name": "a.py"}],
        ),
    )
    monkeypatch.setattr(
        "router.router.create_sphinx_setup",
        lambda provider, repo_url, token, branch, analysis_file: True,
    )

    response = client.post(
        "/generate",
        json={
            "provider": "github",
            "repo_url": "example/project",
            "token": "secret",
            "branch": "main",
        },
    )

    assert response.status_code == 200
    assert response.json()["status"] == "success"


def test_generate_endpoint_returns_not_found_when_analysis_is_empty(monkeypatch):
    """"""Tests the /generate endpoint for a 404 response when analysis is empty.\n\n    Args:\n        monkeypatch: A pytest fixture to modify the behavior of the analyze_repo function.\n\n    Returns:\n        None: Asserts that the response status code is 404.\n""""""
    monkeypatch.setattr(
        "router.router.analyze_repo",
        lambda provider, repo_url, token, branch: ("analysis.csv", []),
    )

    response = client.post(
        "/generate",
        json={
            "provider": "github",
            "repo_url": "example/project",
            "token": "secret",
            "branch": "main",
        },
    )

    assert response.status_code == 404
