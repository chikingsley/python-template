from __future__ import annotations

import pytest
from fastapi.testclient import TestClient

from python_template.app import create_app


def test_health_endpoint(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("APP_NAME", "agent-template")
    monkeypatch.setenv("APP_ENV", "dev")
    monkeypatch.setenv("API_V1_PREFIX", "/api/v1")

    app = create_app()
    with TestClient(app) as client:
        response = client.get("/api/v1/health")

    assert response.status_code == 200
    payload = response.json()
    assert payload["status"] == "ok"
    assert payload["app_name"] == "agent-template"
    assert payload["environment"] == "dev"
    assert isinstance(payload["version"], str)
