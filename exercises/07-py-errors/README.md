*English · [Deutsch](README.de.md)*

# Which exception do you catch, and which do you not?

**Learning goal:** Afterward, you will build your own exception hierarchy for domain errors and catch only what you can handle meaningfully.

**Task:** Throw UnknownProduct and InsufficientStock in place_order, preserve the cause in parse_quantity with raise from, and translate errors into status codes.

## Steps

1. Give `UnknownProduct` and `InsufficientStock` a readable message.
2. Raise `InvalidQuantity(text) from error` in `parse_quantity` for invalid text.
3. Raise `UnknownProduct` (with `from None`) and `InsufficientStock` in `place_order`.
4. Translate errors into status codes in `handle_place_order`. Catch only `OrderError` and its subclasses.

The tests in `start/` are skipped at first. Remove the line `pytestmark = pytest.mark.skip(...)` as soon as you start the exercise.

## Check

```bash
cd start
uv run pytest
uv run mypy --strict .
```

One possible solution is in [`solution/`](solution/). From the root folder, `uv run python scripts/check.py 07` checks the starting point and the solution of this exercise.
