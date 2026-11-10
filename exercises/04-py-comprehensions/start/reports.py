"""Analyses over orders. Replace every loop with append with a comprehension."""

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
    return total  # TODO: as sum(... for ...) in one line


def totals_by_order(orders: list[Order]) -> dict[str, int]:
    totals = {}
    for order in orders:
        totals[order["id"]] = order_total(order)
    return totals  # TODO: dict comprehension


def open_order_ids(orders: list[Order]) -> list[str]:
    """Only orders in status placed or paid."""
    # TODO: list comprehension with if
    raise NotImplementedError


def products_sold(orders: list[Order]) -> set[str]:
    """All product IDs from orders that are not cancelled."""
    # TODO: set comprehension with two for clauses
    raise NotImplementedError


def all_items(orders: list[Order]) -> list[OrderItem]:
    """All line items of all orders in one flat list."""
    # TODO: Since Python 3.15, [*order["items"] for order in orders] works
    raise NotImplementedError


def top_orders(orders: list[Order], n: int = 3) -> list[tuple[str, int]]:
    """The n largest orders as (ID, total), descending."""
    # TODO: sorted(..., key=..., reverse=True) and slicing [:n]
    raise NotImplementedError
