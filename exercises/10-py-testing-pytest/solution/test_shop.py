from collections.abc import Callable
from datetime import UTC, datetime
from pathlib import Path

import pytest

from shop import (
    InsufficientStock,
    OrderError,
    PlacedOrder,
    UnknownProduct,
    format_cents,
    write_receipt,
)

type Place = Callable[[dict[str, int]], PlacedOrder]
FIXED_NOW = datetime(2026, 10, 1, 9, 30, tzinfo=UTC)


def test_place_order_sums_all_items(place: Place) -> None:
    order = place({"p-hammer": 2, "p-saege": 1})
    assert order.total_cents == 2 * 1299 + 2499
    assert order.id == "o-1"
    assert order.created_at == FIXED_NOW


@pytest.mark.parametrize(
    ("items", "error"),
    [
        ({}, OrderError),
        ({"p-bohrer": 1}, UnknownProduct),
        ({"p-saege": 2}, InsufficientStock),
    ],
    ids=["empty", "unknown-product", "insufficient-stock"],
)
def test_place_order_rejects_invalid_orders(
    place: Place, items: dict[str, int], error: type[OrderError]
) -> None:
    with pytest.raises(error):
        place(items)


def test_insufficient_stock_names_the_product(place: Place) -> None:
    with pytest.raises(InsufficientStock, match="p-saege"):
        place({"p-saege": 2})


def test_write_receipt_creates_a_readable_file(place: Place, tmp_path: Path) -> None:
    path = write_receipt(place({"p-hammer": 2}), tmp_path)
    assert path.read_text(encoding="utf-8") == (
        "Bestellung o-1 vom 01.10.2026\n2 × p-hammer\nSumme: 25,98 €\n"
    )


@pytest.mark.parametrize(
    ("cents", "text"),
    [(0, "0,00 €"), (2598, "25,98 €"), (123456, "1.234,56 €"), (-250, "-2,50 €")],
)
def test_format_cents_uses_whole_cents(cents: int, text: str) -> None:
    assert format_cents(cents) == text
