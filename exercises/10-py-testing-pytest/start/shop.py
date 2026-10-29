"""Der Code, den du testest. Er ist fertig – schreib die Tests in test_shop.py."""

from collections.abc import Callable
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path


class OrderError(Exception):
    pass


class UnknownProduct(OrderError):
    pass


class InsufficientStock(OrderError):
    pass


@dataclass(frozen=True, slots=True)
class Product:
    id: str
    name: str
    price_cents: int
    stock: int


@dataclass(frozen=True, slots=True)
class PlacedOrder:
    id: str
    customer_id: str
    items: tuple[tuple[str, int], ...]
    total_cents: int
    created_at: datetime


def place_order(
    customer_id: str,
    items: dict[str, int],
    catalog: dict[str, Product],
    *,
    now: Callable[[], datetime],
    next_id: Callable[[], str],
) -> PlacedOrder:
    """Zeit und IDs kommen als Funktionen herein: so bleibt der Test deterministisch."""
    if not items:
        raise OrderError("an order needs at least one item")
    total = 0
    for product_id, quantity in items.items():
        if product_id not in catalog:
            raise UnknownProduct(product_id)
        product = catalog[product_id]
        if quantity > product.stock:
            raise InsufficientStock(f"{product_id}: {quantity} > {product.stock}")
        total += quantity * product.price_cents
    return PlacedOrder(next_id(), customer_id, tuple(items.items()), total, now())


def format_cents(cents: int) -> str:
    """Geld bleibt bis zur Ausgabe in ganzen Cent: 123456 → "1.234,56 €"."""
    sign = "-" if cents < 0 else ""
    euros, rest = divmod(abs(cents), 100)
    return f"{sign}{euros:_}".replace("_", ".") + f",{rest:02d} €"


def write_receipt(order: PlacedOrder, directory: Path) -> Path:
    path = directory / f"receipt-{order.id}.txt"
    lines = [f"Bestellung {order.id} vom {order.created_at:%d.%m.%Y}"]
    lines += [f"{quantity} × {product_id}" for product_id, quantity in order.items]
    lines.append(f"Summe: {format_cents(order.total_cents)}")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return path
