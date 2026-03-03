from __future__ import annotations

from importlib.metadata import PackageNotFoundError, version
from typing import Annotated, Literal

from fastapi import APIRouter, Depends
from pydantic import BaseModel, ConfigDict

from python_template.settings import Settings, get_settings

router = APIRouter()


def _package_version() -> str:
    try:
        return version("python-template")
    except PackageNotFoundError:
        return "0.1.0"


class HealthResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")

    status: Literal["ok"] = "ok"
    app_name: str
    environment: Literal["local", "dev", "staging", "prod"]
    version: str


@router.get("/health", response_model=HealthResponse)
def health(settings: Annotated[Settings, Depends(get_settings)]) -> HealthResponse:
    return HealthResponse(
        app_name=settings.app_name,
        environment=settings.app_env,
        version=_package_version(),
    )
