from __future__ import annotations

import uvicorn

from python_template.settings import get_settings


def main() -> None:
    settings = get_settings()
    uvicorn.run(
        "python_template.app:create_app",
        factory=True,
        host=settings.host,
        port=settings.port,
        reload=settings.debug,
        log_level=settings.log_level.lower(),
    )
