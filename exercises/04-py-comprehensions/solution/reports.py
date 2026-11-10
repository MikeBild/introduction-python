"""Analyses over orders with comprehensions instead of loops with append."""

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
    """Total = Σ quantity × priceCents, as a generator expression in sum()."""
    return sum(item["quantity"] * item["priceCents"] for item in order["items"])


def totals_by_order(orders: list[Order]) -> dict[str, int]:
    """Dict comprehension: order ID → total."""
    return {order["id"]: order_total(order) for order in orders}


def open_order_ids(orders: list[Order]) -> list[str]:
    """List comprehension with a filter: only placed and paid."""
    return [order["id"] for order in orders if order["status"] in {"placed", "paid"}]


def products_sold(orders: list[Order]) -> set[str]:
    """Set comprehension over all line items of orders that are not cancelled."""
    return {
        item["productId"]
        for order in orders
        if order["status"] != "cancelled"
        for item in order["items"]
    }


def all_items(orders: list[Order]) -> list[OrderItem]:
    """Since Python 3.15, * unpacks directly in the comprehension (PEP 798)."""
    return [*order["items"] for order in orders]


def top_orders(orders: list[Order], n: int = 3) -> list[tuple[str, int]]:
    """The n largest orders as (ID, total), descending."""
    totals = totals_by_order(orders)
    return sorted(totals.items(), key=lambda entry: entry[1], reverse=True)[:n]
