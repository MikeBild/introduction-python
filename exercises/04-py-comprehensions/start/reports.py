"""Auswertungen über Bestellungen. Ersetze jede Schleife mit append durch eine Comprehension."""

from typing import Literal, TypedDict

type Status = Literal["draft", "placed", "paid", "shipped", "cancelled"]


class OrderItem(TypedDict):
    productId: str
    quantity: int
    priceCents: int


class Order(TypedDict):
    id: str
    customerId: str
    status: Status
    items: list[OrderItem]


def order_total(order: Order) -> int:
    total = 0
    for item in order["items"]:
        total += item["quantity"] * item["priceCents"]
    return total  # TODO: als sum(... for ...) in einer Zeile


def totals_by_order(orders: list[Order]) -> dict[str, int]:
    totals = {}
    for order in orders:
        totals[order["id"]] = order_total(order)
    return totals  # TODO: Dict Comprehension


def open_order_ids(orders: list[Order]) -> list[str]:
    """Nur Bestellungen im Status placed oder paid."""
    # TODO: List Comprehension mit if
    raise NotImplementedError


def products_sold(orders: list[Order]) -> set[str]:
    """Alle Produkt-IDs aus nicht stornierten Bestellungen."""
    # TODO: Set Comprehension mit zwei for-Klauseln
    raise NotImplementedError


def all_items(orders: list[Order]) -> list[OrderItem]:
    """Alle Positionen aller Bestellungen in einer flachen Liste."""
    # TODO: Seit Python 3.15 geht [*order["items"] for order in orders]
    raise NotImplementedError


def top_orders(orders: list[Order], n: int = 3) -> list[tuple[str, int]]:
    """Die n größten Bestellungen als (ID, Summe), absteigend."""
    # TODO: sorted(..., key=..., reverse=True) und Slicing [:n]
    raise NotImplementedError
