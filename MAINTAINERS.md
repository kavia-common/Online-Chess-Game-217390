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
