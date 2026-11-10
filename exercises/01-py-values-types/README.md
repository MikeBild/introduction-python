*English · [Deutsch](README.de.md)*

# Names point to values, values have types

**Learning goal:** After this, you calculate money amounts exactly in whole cents and safely distinguish 0, None, and empty values.

**Task:** Write to_cents, which converts “12,34” exactly to 1234 cents, format_cents for output, and is_free, which distinguishes 0 and None.

## Steps

1. Open `start/money.py`.
2. Write `to_cents`: strip whitespace, replace the comma with a dot, split into euros and cents with `partition`. Invalid input raises `ValueError`.
3. Write `format_cents` with `divmod` and an f-string. The output follows DIN 5008: 123456 cents become “1.234,56 €”.
4. Write `is_free` so that `0` is free and `None` is not.

The tests in `start/` are skipped at first. Remove the line `pytestmark = pytest.mark.skip(...)` as soon as you start the exercise.

## Check

```bash
cd start
uv run pytest
uv run mypy --strict .
```

One possible solution is in [`solution/`](solution/). From the root folder, `uv run python scripts/check.py 01` checks the starting point and the solution of this exercise.
