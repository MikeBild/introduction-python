*English · [Deutsch](README.de.md)*

# Generators return values only on demand

**Learning goal:** After this, you will process large order files with generators, itertools.batched, and islice in constant memory.

**Task:** Turn read_orders and with_status into generators, add totals and running_total with yield, and split orders into batches with itertools.batched.

## Steps

1. Turn `read_orders` and `with_status` into generators.
2. Write `totals` and `running_total` with `yield`.
3. Use `itertools.batched` in `in_batches` and `itertools.islice` in `first_paid`.

The tests in `start/` are skipped at first. Remove the line `pytestmark = pytest.mark.skip(...)` as soon as you start the exercise.

## Check

```bash
cd start
uv run pytest
uv run mypy --strict .
```

One possible solution is in [`solution/`](solution/). From the root folder, `uv run python scripts/check.py 16` checks the starting point and the solution of this exercise.
