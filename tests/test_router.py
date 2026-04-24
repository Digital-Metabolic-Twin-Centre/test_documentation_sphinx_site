from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_root_endpoint_returns_welcome_message():
    """
    Tests the root endpoint for a welcome message.

        Args:
            None

        Returns:
            None: Asserts that the response status code is 200 and contains a specific message.

    """
    response = client.get("/")

    assert response.status_code == 200
    assert "Visit /docs" in response.json()["message"]


def test_generate_endpoint_returns_success_when_services_succeed(monkeypatch):
    """
    Tests the /generate endpoint for successful service execution.

    Args:
        monkeypatch: A pytest fixture to modify attributes for testing.

    Returns:
        None: Asserts the response status and content.

    """
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
    """
    Test that the /generate endpoint returns a 404 status when the analysis result is empty.

        Args:
            monkeypatch: A pytest fixture to modify the behavior of the analyze_repo function.

        Returns:
            None: This function asserts the response status code directly.

    """
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
