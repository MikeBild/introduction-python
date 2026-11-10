*English · [Deutsch](README.de.md)*

# Read and write JSON and CSV safely with pathlib

**Learning goal:** After this, you will read and write products and orders as JSON and CSV with pathlib, with, and explicit encoding.

**Task:** Read the catalog from data/products.json, save orders atomically as <id>.json, and export all line items as CSV.

## Steps

1. Read the file in `load_products` with `path.open(encoding="utf-8")` and `json.load`.
2. In `save_order`, write `<id>.tmp` first, then rename it with `replace`.
3. Read all `*.json` files in sorted order in `load_orders`.
4. Export one row per line item in `export_csv` with `csv.DictWriter` (open the file with `newline=""`).

The tests in `start/` are skipped at first. Remove the line `pytestmark = pytest.mark.skip(...)` as soon as you start the exercise.

## Check

```bash
cd start
uv run pytest
uv run mypy --strict .
```

One possible solution is in [`solution/`](solution/). From the root folder, `uv run python scripts/check.py 08` checks the starting point and the solution of this exercise.
