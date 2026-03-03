# Python Template (FastAPI + Pydantic v2 + uv)

This template is a modern baseline for agent-facing Python services:
- `uv` for dependency and environment management
- FastAPI app factory + lifespan startup/shutdown hooks
- Pydantic v2 + `pydantic-settings` for typed configuration
- `ruff`, `ty`, and `pytest` wired for strict CI checks

## Quick Start

```bash
uv sync --all-groups
uv run python-template
```

Default server URL:
- `http://127.0.0.1:8000/api/v1/health`

## Project Layout

```text
src/python_template/
  app.py                # FastAPI app factory + lifespan
  main.py               # Console entrypoint (runs uvicorn)
  settings.py           # Typed app config (BaseSettings)
  api/
    router.py           # API router registry
    routes/health.py    # Health endpoint + response schema
scripts/
  example_uv_script.py  # PEP 723 + uv shebang script template
```

## Environment Variables

Copy `.env.example` to `.env` and adjust as needed:

```dotenv
APP_NAME=python-template
APP_ENV=local
DEBUG=false
API_V1_PREFIX=/api/v1
HOST=127.0.0.1
PORT=8000
LOG_LEVEL=INFO
```

## Developer Commands

```bash
# lint + format check
uv run ruff check .
uv run ruff format --check .

# type-check
uv run ty check

# test
uv run pytest
```

## uv Script Shebang Pattern

For standalone scripts, prefer the uv shebang pattern over `#!/usr/bin/env python3`:

```python
#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.13"
# dependencies = []
# ///
```

A ready-to-copy example is in `scripts/example_uv_script.py`.
