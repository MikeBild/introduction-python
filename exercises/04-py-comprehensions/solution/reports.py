"""Auswertungen über Bestellungen mit Comprehensions statt Schleifen mit append."""

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
    """Gesamtsumme = Σ quantity × priceCents, als Generator Expression in sum()."""
    return sum(item["quantity"] * item["priceCents"] for item in order["items"])


def totals_by_order(orders: list[Order]) -> dict[str, int]:
    """Dict Comprehension: Bestell-ID → Gesamtsumme."""
    return {order["id"]: order_total(order) for order in orders}


def open_order_ids(orders: list[Order]) -> list[str]:
    """List Comprehension mit Filter: nur placed und paid."""
    return [order["id"] for order in orders if order["status"] in {"placed", "paid"}]


def products_sold(orders: list[Order]) -> set[str]:
    """Set Comprehension über alle Positionen nicht stornierter Bestellungen."""
    return {
        item["productId"]
        for order in orders
        if order["status"] != "cancelled"
        for item in order["items"]
    }


def all_items(orders: list[Order]) -> list[OrderItem]:
    """Seit Python 3.15 entpackt * direkt in der Comprehension (PEP 798)."""
    return [*order["items"] for order in orders]


def top_orders(orders: list[Order], n: int = 3) -> list[tuple[str, int]]:
    """Die n größten Bestellungen als (ID, Summe), absteigend."""
    totals = totals_by_order(orders)
    return sorted(totals.items(), key=lambda entry: entry[1], reverse=True)[:n]
