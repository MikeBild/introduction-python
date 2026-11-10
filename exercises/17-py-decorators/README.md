*English · [Deutsch](README.de.md)*

# Decorators add behavior without changing code

**Learning goal:** After this, you write typed decorators with arguments for timing and retry, and use functools.cache deliberately.

**Task:** Fix timed with functools.wraps and try/finally, write retry for ConnectionError, and cache shipping_cents with functools.cache.

## Steps

1. Add `@functools.wraps(func)` and `try`/`finally` to `timed`.
2. Write `retry` following the same pattern. Exceptions other than those in `on` propagate immediately.
3. Cache `shipping_cents` with `@functools.cache` and delete the `type: ignore` comments in the test.

The tests in `start/` are skipped at first. Remove the line `pytestmark = pytest.mark.skip(...)` as soon as you start the exercise.

## Check

```bash
cd start
uv run pytest
uv run mypy --strict .
```

One possible solution is in [`solution/`](solution/). From the root folder, `uv run python scripts/check.py 17` checks the starting point and the solution of this exercise.
