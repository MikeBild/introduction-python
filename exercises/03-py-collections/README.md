*English · [Deutsch](README.de.md)*

# Which collection fits your data?

**Learning goal:** After this, you choose list, tuple, dict, set, or Counter for products and orders based on access.

**Task:** Build an index of products by ID, find low-stock products, collect customer IDs without duplicates, and count quantities per product with Counter.

## Steps

1. Build a dict from product ID to product with `index_by_id`.
2. Return the names of products low on stock in alphabetical order with `low_stock`.
3. Collect every customer ID exactly once with `customer_ids`.
4. Count the ordered quantities with `quantities_by_product` and `Counter`.
5. Return a `frozendict` with `price_list` (built in since Python 3.15).

The tests in `start/` are skipped at first. Remove the line `pytestmark = pytest.mark.skip(...)` as soon as you start the exercise.

## Check

```bash
cd start
uv run pytest
uv run mypy --strict .
```

One possible solution is in [`solution/`](solution/). From the root folder, `uv run python scripts/check.py 03` checks the starting point and the solution of this exercise.
