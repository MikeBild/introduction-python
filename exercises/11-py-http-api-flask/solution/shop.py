"""Fachlogik des Werkstatt-Shops, unabhängig von Flask."""

from dataclasses import dataclass, field
from datetime import UTC, datetime
from itertools import count


class OrderError(Exception):
    pass


class UnknownProduct(OrderError):
    pass


class InsufficientStock(OrderError):
    pass


class ValidationError(Exception):
    def __init__(self, issues: list[str]) -> None:
        super().__init__("; ".join(issues))
        self.issues = issues


@dataclass(slots=True)
class Product:
    id: str
    name: str
    price_cents: int
    stock: int


@dataclass(frozen=True, slots=True)
class OrderItem:
    product_id: str
    quantity: int
    price_cents: int


@dataclass(frozen=True, slots=True)
class Order:
    id: str
    customer_id: str
    items: tuple[OrderItem, ...]
    status: str
    created_at: datetime

    @property
    def total_cents(self) -> int:
        return sum(item.quantity * item.price_cents for item in self.items)


def parse_place_order(payload: object) -> tuple[str, list[tuple[str, int]]]:
    """Prüft den Body von POST /orders: {customerId, items: [{productId, quantity}]}, nichts sonst."""
    if not isinstance(payload, dict):
        raise ValidationError(["body must be a JSON object"])
    issues = [f"unexpected field: {key}" for key in payload if key not in {"customerId", "items"}]
    customer_id = payload.get("customerId")
    if not isinstance(customer_id, str) or not customer_id:
        issues.append("customerId must be a non-empty string")
    raw_items = payload.get("items")
    items: list[tuple[str, int]] = []
    if not isinstance(raw_items, list) or not raw_items:
        issues.append("items must be a non-empty list")
    else:
        for index, item in enumerate(raw_items):
            product_id = item.get("productId") if isinstance(item, dict) else None
            quantity = item.get("quantity") if isinstance(item, dict) else None
            if not isinstance(product_id, str) or not product_id:
                issues.append(f"items[{index}].productId must be a non-empty string")
            elif type(quantity) is not int or quantity < 1:
                issues.append(f"items[{index}].quantity must be an integer >= 1")
            else:
                items.append((product_id, quantity))
    if issues:
        raise ValidationError(issues)
    assert isinstance(customer_id, str)
    return customer_id, items


@dataclass
class Store:
    products: dict[str, Product]
    orders: dict[str, Order] = field(default_factory=dict)
    _ids: count[int] = field(default_factory=lambda: count(1001))

    @classmethod
    def with_demo_data(cls) -> "Store":
        return cls(
            {
                "p-hammer": Product("p-hammer", "Hammer", 1299, 12),
                "p-saege": Product("p-saege", "Säge", 2499, 4),
            }
        )

    def place_order(self, customer_id: str, items: list[tuple[str, int]]) -> Order:
        for product_id, quantity in items:
            product = self.products.get(product_id)
            if product is None:
                raise UnknownProduct(f"unknown product: {product_id}")
            if quantity > product.stock:
                raise InsufficientStock(f"only {product.stock} of {product_id} in stock")
        order_items = []
        for product_id, quantity in items:
            product = self.products[product_id]
            product.stock -= quantity
            order_items.append(OrderItem(product_id, quantity, product.price_cents))
        order = Order(f"o-{next(self._ids)}", customer_id, tuple(order_items), "placed", datetime.now(UTC))
        self.orders[order.id] = order
        return order


def product_to_json(product: Product) -> dict[str, object]:
    return {"id": product.id, "name": product.name, "priceCents": product.price_cents, "stock": product.stock}


def order_to_json(order: Order) -> dict[str, object]:
    return {
        "id": order.id,
        "customerId": order.customer_id,
        "status": order.status,
        "createdAt": order.created_at.isoformat(),
        "totalCents": order.total_cents,
        "items": [
            {"productId": item.product_id, "quantity": item.quantity, "priceCents": item.price_cents}
            for item in order.items
        ],
    }
