*English · [Deutsch](README.de.md)*

# Dataclasses instead of boilerplate-heavy classes

**Learning goal:** After this, you model Order and OrderItem as dataclasses with StrEnum status and methods that check rules.

**Task:** Turn OrderItem into a frozen dataclass and Order into a dataclass with status rules for place, advance, and cancel.

## Steps

1. Turn `OrderItem` into a `@dataclass(frozen=True, slots=True)` and delete `__init__`, `__eq__` and `__repr__`.
2. Check in `__post_init__` that `quantity` is at least 1, and add the property `total_cents`.
3. Turn `Order` into a dataclass with `field(default_factory=list)` and write `place`, `advance` and `cancel` following the rules in `docs/beispiel-domaene.md`.

The tests in `start/` are skipped at first. Remove the line `pytestmark = pytest.mark.skip(...)` as soon as you start the exercise.

## Check

```bash
cd start
uv run pytest
uv run mypy --strict .
```

One possible solution is in [`solution/`](solution/). From the root folder, `uv run python scripts/check.py 06` checks the starting point and the solution of this exercise.
