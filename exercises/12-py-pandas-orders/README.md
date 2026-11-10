*English · [Deutsch](README.de.md)*

# Analyze orders with pandas instead of loops

**Learning goal:** Afterward, you flatten nested orders with pandas and calculate revenue by product, month, and customer with groupby.

**Task:** In analysis.py, calculate revenueCents vectorized, filter canceled orders, and analyze revenue by product, month, and customer with groupby.

## Steps

1. Add the column `revenueCents` in `load_items`, vectorized without a loop.
2. Filter out canceled orders and drafts in `completed` with a boolean mask.
3. Write `revenue_by_product`, `revenue_by_month` and `customer_summary` with `groupby`.

The tests in `start/` are skipped at first. Remove the line `pytestmark = pytest.mark.skip(...)` as soon as you start the exercise.

## Check

```bash
cd start
uv run pytest
uv run mypy --strict .
```

One possible solution is in [`solution/`](solution/). From the root folder, `uv run python scripts/check.py 12` checks the starting point and the solution of this exercise.
