from __future__ import annotations

import pytest

from python_template.settings import Settings


def test_default_settings() -> None:
    s = Settings(_env_file=None)  # type: ignore[call-arg]
    assert s.app_name == "python-template"
    assert s.debug is False


def test_settings_override(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("APP_NAME", "test-app")
    monkeypatch.setenv("DEBUG", "true")
    s = Settings(_env_file=None)  # type: ignore[call-arg]
    assert s.app_name == "test-app"
    assert s.debug is True
