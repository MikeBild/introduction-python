*English · [Deutsch](README.de.md)*

# Wait with asyncio without blocking

**Learning goal:** After this, you query several services at once with asyncio, limit duration and concurrency, and handle TaskGroup errors.

**Task:** In stock_for, query the stock for all products at once with TaskGroup and asyncio.timeout, and limit concurrency in stock_limited with Semaphore.

## Steps

1. Write `stock_for` with `asyncio.timeout` and `asyncio.TaskGroup`.
2. Write `stock_limited` with `asyncio.Semaphore`.
3. The tests call `asyncio.run`; you do not need an extra package.

The tests in `start/` are skipped at first. Remove the line `pytestmark = pytest.mark.skip(...)` as soon as you start the exercise.

## Check

```bash
cd start
uv run pytest
uv run mypy --strict .
```

One possible solution is in [`solution/`](solution/). From the root folder, `uv run python scripts/check.py 14` checks the starting point and the solution of this exercise.
