*English · [Deutsch](README.de.md)*

# A project with uv instead of manual pip and venv

**Learning goal:** After this, you can create a package with uv in the src layout, split code into modules, and start it as its own command.

**Task:** Split cli.py into the money and orders modules, add the command werkstatt to pyproject.toml, and run it with uv run werkstatt 2x1299.

## Steps

1. Change into `start/` and run `uv sync`. This exercise is its own uv project with its own `.venv`.
2. Split `src/werkstatt/cli.py` into the modules `money.py` and `orders.py` and import them absolutely (`from werkstatt.money import format_cents`).
3. Adjust `src/werkstatt/__init__.py` so that it exports the functions from the new modules.
4. Register the command `werkstatt = "werkstatt.cli:main"` under `[project.scripts]`, run `uv sync`, and start `uv run werkstatt 2x1299 1x2499`.

The tests in `start/` are skipped at first. Remove the line `pytestmark = pytest.mark.skip(...)` as soon as you start the exercise.

## Check

```bash
cd start
uv sync
uv run pytest
uv run mypy --strict src tests
```

One possible solution is in [`solution/`](solution/). From the root folder, `uv run python scripts/check.py 05` checks the starting point and the solution of this exercise.
