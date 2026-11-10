*English · [Deutsch](README.de.md)*

# mypy checks type hints, not Python

**Learning goal:** After this, you annotate a module with NewType, Literal, TypedDict, and X | None so mypy --strict checks it without errors.

**Task:** Annotate pricing.py with NewType IDs, Literal, and TypedDict until uv run mypy --strict is clean, and fix the bug mypy finds.

## Steps

1. Run `uv run mypy --strict pricing.py` in `start/` and read the messages.
2. Define `OrderId`, `CustomerId` and `ProductId` as `NewType`, the status as `Literal`, `OrderItem` and `Order` as `TypedDict`.
3. Annotate all functions. `find_order` returns `Order | None`.
4. Fix the error in `invoice_total` that mypy now reports and adapt the tests to the NewTypes.

The tests in `start/` are skipped at first. Remove the line `pytestmark = pytest.mark.skip(...)` as soon as you start the exercise.

## Check

```bash
cd start
uv run pytest
uv run mypy --strict .
```

One possible solution is in [`solution/`](solution/). From the root folder, `uv run python scripts/check.py 09` checks the starting point and the solution of this exercise.
