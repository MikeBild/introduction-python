from collections.abc import Callable
from datetime import UTC, datetime

import pytest

from shop import PlacedOrder, Product, place_order

type Place = Callable[[dict[str, int]], PlacedOrder]

FIXED_NOW = datetime(2026, 10, 1, 9, 30, tzinfo=UTC)


@pytest.fixture
def catalog() -> dict[str, Product]:
    """Jeder Test bekommt einen frischen Katalog."""
    return {
        "p-hammer": Product("p-hammer", "Hammer", 1299, 5),
        "p-saege": Product("p-saege", "Säge", 2499, 1),
    }


@pytest.fixture
def place(catalog: dict[str, Product]) -> Place:
    """place_order mit fester Zeit und fester ID: jeder Lauf liefert dasselbe Ergebnis."""

    def run(items: dict[str, int]) -> PlacedOrder:
        return place_order("c-ada", items, catalog, now=lambda: FIXED_NOW, next_id=lambda: "o-1")

    return run
