from collections.abc import Callable
from datetime import UTC, datetime
from pathlib import Path

import pytest

from shop import InsufficientStock, OrderError, PlacedOrder, UnknownProduct, write_receipt

type Place = Callable[[dict[str, int]], PlacedOrder]
FIXED_NOW = datetime(2026, 10, 1, 9, 30, tzinfo=UTC)

pytestmark = pytest.mark.skip(reason="Entferne diese Zeile, um die Tests zu aktivieren.")


def test_place_order_sums_all_items(place: Place) -> None:
    order = place({"p-hammer": 2, "p-saege": 1})
    # TODO: Summe, ID und created_at prüfen (FIXED_NOW)
    assert order


# TODO: Ein parametrisierter Test (@pytest.mark.parametrize) für drei Fehlerfälle:
#       leere Bestellung → OrderError, unbekanntes Produkt → UnknownProduct,
#       zu wenig Bestand → InsufficientStock. Nutze pytest.raises.
def test_place_order_rejects_invalid_orders(place: Place) -> None:
    _ = OrderError, UnknownProduct, InsufficientStock, FIXED_NOW
    pytest.fail("TODO")


def test_write_receipt_creates_a_readable_file(place: Place, tmp_path: Path) -> None:
    # TODO: Beleg in tmp_path schreiben und den Inhalt vollständig vergleichen
    _ = write_receipt
    pytest.fail("TODO")
