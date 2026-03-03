from __future__ import annotations

import pytest

from python_template.settings import Settings


def test_default_settings() -> None:
    s = Settings(_env_file=None)  # type: ignore[call-arg]
    assert s.app_name == "python-template"
    assert s.app_env == "local"
    assert s.debug is False
    assert s.api_v1_prefix == "/api/v1"
    assert s.port == 8000


def test_settings_override(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("APP_NAME", "test-app")
    monkeypatch.setenv("APP_ENV", "dev")
    monkeypatch.setenv("API_V1_PREFIX", "/api")
    monkeypatch.setenv("DEBUG", "true")
    monkeypatch.setenv("PORT", "9000")
    s = Settings(_env_file=None)  # type: ignore[call-arg]
    assert s.app_name == "test-app"
    assert s.app_env == "dev"
    assert s.api_v1_prefix == "/api"
    assert s.debug is True
    assert s.port == 9000
