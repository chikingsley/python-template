# python-template

## Package Management

This project uses **uv** exclusively. Never use pip, pip-tools, poetry, or conda.

### Dependencies

```bash
uv add <package>              # Add runtime dependency
uv add --dev <package>        # Add dev dependency
uv remove <package>           # Remove dependency
uv sync                       # Sync all dependencies from lockfile
uv lock --upgrade-package X   # Upgrade specific package
```

### Running Code

```bash
uv run python_template        # Run the CLI entry point
uv run <script.py>            # Run a script
uv run python                 # REPL
```

**Never use** `uv run python -m <tool>`. Use `uv run <tool>` directly — uv resolves tools from the project venv automatically.

If `uv run <tool>` fails with "Failed to spawn", fix stale venv shebangs:
```bash
rm -rf .venv && uv sync
```

## Development Commands

```bash
uv run ruff check .           # Lint
uv run ruff check --fix .     # Lint + auto-fix
uv run ruff format .          # Format
uv run ty check               # Type check (strict)
uv run pytest                 # Run tests
uv run pytest -v              # Verbose tests
uv run pytest -x              # Stop on first failure
```

## Build System

- **Build backend**: hatchling
- **Source layout**: `src/python_template/`
- **Tests**: `tests/`

## Linting & Formatting (Ruff)

Ruff is configured with a strict rule set in `pyproject.toml`. Key points:

- **Line length**: 88
- **Target**: Python 3.13
- All code must use `from __future__ import annotations`
- No `print()` in production code (use `logging` instead, or `# noqa: T201` for CLI entry points)
- Imports sorted with isort conventions
- Test files have relaxed rules (asserts, magic values, unused args for fixtures, etc.)
- Use `# noqa: RULE` to suppress specific rules with the exact rule code (e.g. `T201`, not `T20`)

## Type Checking (ty)

ty runs in strict mode — all default warnings are promoted to errors. Code must be fully typed:

- All function signatures need type annotations
- Use `from __future__ import annotations` in every file
- `py.typed` marker is present for PEP 561 compliance
- Type-only imports go in `if TYPE_CHECKING:` blocks

## Settings (Pydantic Settings)

Application config lives in `src/python_template/settings.py` using `pydantic-settings`:

- Settings are loaded from environment variables and `.env` file
- `.env` is gitignored; `.env.example` is the template
- Access settings via `from python_template.settings import settings`
- Add new settings as typed fields on the `Settings` class
- Use `model_config = SettingsConfigDict(...)` for config (not class-level `Config`)

## Testing (pytest)

- Tests live in `tests/`
- Coverage required: 80% minimum
- pytest runs with `--strict-markers`, `--strict-config`, and `filterwarnings = ["error"]`
- Coverage is automatic via `--cov=python_template`
