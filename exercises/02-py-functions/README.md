*English · [Deutsch](README.de.md)*

# Clear function signatures instead of flag parameters

**Learning goal:** After this, you will write functions with defaults and keyword-only arguments, and avoid shared default lists.

**Task:** Make the discount in order_total a keyword-only argument, fix the shared default list in add_item, and write make_discount as a closure.

## Steps

1. Make `discount_percent` in `order_total` a keyword-only argument and sum the line items.
2. Fix `add_item`: `None` as default, the list passed in stays unchanged.
3. Write `make_discount` as a closure.

The tests in `start/` are skipped at first. Remove the line `pytestmark = pytest.mark.skip(...)` as soon as you start the exercise.

## Check

```bash
cd start
uv run pytest
uv run mypy --strict .
```

One possible solution is in [`solution/`](solution/). From the root folder, `uv run python scripts/check.py 02` checks the starting point and the solution of this exercise.
