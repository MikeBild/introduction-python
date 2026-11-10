*English · [Deutsch](README.de.md)*

# Check behavior with pytest, not details

**Learning goal:** After this, you will write pytest tests with assert, fixtures, parametrize, pytest.raises, and tmp_path for code with fixed time.

**Task:** Write tests for place_order with the fixtures from conftest.py, a parametrized test for three error cases, and a receipt test with tmp_path.

## Steps

1. Read `shop.py` and the fixtures in `conftest.py`. The code is finished, you only write tests. It calculates money in whole cents as `int`; only `format_cents` turns that into “1.234,56 €”.
2. Add the checks for total, ID and timestamp in `test_shop.py`.
3. Write a test with `@pytest.mark.parametrize` for three error cases and `pytest.raises`.
4. Check the receipt completely with `tmp_path`.

The tests in `start/` are skipped at first. Remove the line `pytestmark = pytest.mark.skip(...)` as soon as you start the exercise.

## Check

```bash
cd start
uv run pytest
uv run mypy --strict .
```

One possible solution is in [`solution/`](solution/). From the root folder, `uv run python scripts/check.py 10` checks the starting point and the solution of this exercise.
