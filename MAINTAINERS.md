# Maintainers Guide

## Code style

This repository uses:

- **black** for formatting
- **ruff** for linting (and autofixes where safe)

### Install (dev)

```bash
python -m pip install -r requirements-dev.txt
```

### Format

```bash
black .
```

### Lint (and auto-fix)

```bash
ruff check . --fix
```

### CI-friendly (check only)

```bash
ruff check .
black . --check
```

## Refreshing / locking dependencies

- Runtime deps are tracked in `requirements.txt` (currently using a compatible range).
- Dev tooling is tracked in `requirements-dev.txt` (compatible ranges).

To refresh to newer stable versions:
1. Update the version ranges in `requirements*.txt` as desired.
2. Reinstall into a clean environment (recommended):

```bash
python -m venv .venv
. .venv/bin/activate
python -m pip install -U pip
python -m pip install -r requirements.txt -r requirements-dev.txt
```

If you want fully locked, reproducible pins for deployments, generate a lock file using
your preferred workflow (e.g., `pip-tools` / `uv pip compile`) and commit the resulting
lock output according to team conventions.
