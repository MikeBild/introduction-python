"""Rechnungssummen mit Typ-Hinweisen, die mypy --strict prüft."""

from typing import Literal, NewType, TypedDict

OrderId = NewType("OrderId", str)
CustomerId = NewType("CustomerId", str)
ProductId = NewType("ProductId", str)

type Status = Literal["draft", "placed", "paid", "shipped", "cancelled"]


class OrderItem(TypedDict):
    productId: ProductId
    quantity: int
    priceCents: int


class Order(TypedDict):
    id: OrderId
    customerId: CustomerId
    status: Status
    items: list[OrderItem]


def find_order(orders: list[Order], order_id: OrderId) -> Order | None:
    for order in orders:
        if order["id"] == order_id:
            return order
    return None


def order_total(order: Order) -> int:
    return sum(item["quantity"] * item["priceCents"] for item in order["items"])


def discount_percent(customer_id: CustomerId, vip_customers: set[CustomerId]) -> int:
    return 10 if customer_id in vip_customers else 0


def invoice_total(orders: list[Order], order_id: OrderId, vip_customers: set[CustomerId]) -> int:
    order = find_order(orders, order_id)
    if order is None:
        raise LookupError(f"unknown order: {order_id}")
    total = order_total(order)
    return total - total * discount_percent(order["customerId"], vip_customers) // 100
