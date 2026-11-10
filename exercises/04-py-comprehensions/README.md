*English · [Deutsch](README.de.md)*

# Comprehensions instead of loops with append

**Learning goal:** After this, you write order reports as list, dict, and set comprehensions and generator expressions.

**Task:** In reports.py, replace every loop with append with a comprehension, and sort the largest orders with sorted and key.

## Steps

1. Replace the loops in `order_total` and `totals_by_order` with `sum(...)` and a dict comprehension.
2. Write `open_order_ids`, `products_sold` and `all_items` as comprehensions.
3. Sort in `top_orders` with `sorted`, `key` and `reverse=True`.

The tests in `start/` are skipped at first. Remove the line `pytestmark = pytest.mark.skip(...)` as soon as you start the exercise.

## Check

```bash
cd start
uv run pytest
uv run mypy --strict .
```

One possible solution is in [`solution/`](solution/). From the root folder, `uv run python scripts/check.py 04` checks the starting point and the solution of this exercise.
