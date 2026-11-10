*English · [Deutsch](README.de.md)*

# Build a package others can install

**Learning goal:** After this, you use uv build to build a typed Wheel with metadata and a command, and check it before publishing.

**Task:** Add version, description, license, and the werkstatt-money command in pyproject.toml, create py.typed, and check the Wheel with the tests.

## Steps

1. Change into `start/` and run `uv sync`. This exercise is its own uv project.
2. Add version `1.0.0`, `description`, `readme`, `license = "MIT"` and the command `werkstatt-money` to `pyproject.toml`.
3. Create the empty file `src/werkstatt_money/py.typed`.
4. Build with `uv build` and try `uvx --from ./dist/werkstatt_money-1.0.0-py3-none-any.whl werkstatt-money 12,34`.

The tests in `start/` are skipped at first. Remove the line `pytestmark = pytest.mark.skip(...)` as soon as you start the exercise.

## Check

```bash
cd start
uv sync
uv run pytest
uv run mypy --strict src tests
```

One possible solution is in [`solution/`](solution/). From the root folder, `uv run python scripts/check.py 15` checks the starting point and the solution of this exercise.
