"""Die Bestellung als Dataclass mit Regeln für Status und Positionen."""

from dataclasses import dataclass, field
from enum import StrEnum


class Status(StrEnum):
    DRAFT = "draft"
    PLACED = "placed"
    PAID = "paid"
    SHIPPED = "shipped"
    CANCELLED = "cancelled"


@dataclass(frozen=True, slots=True)
class OrderItem:
    product_id: str
    quantity: int
    price_cents: int

    def __post_init__(self) -> None:
        if self.quantity < 1:
            raise ValueError("quantity must be at least 1")

    @property
    def total_cents(self) -> int:
        return self.quantity * self.price_cents


NEXT_STATUS = {Status.PLACED: Status.PAID, Status.PAID: Status.SHIPPED}


@dataclass(slots=True)
class Order:
    id: str
    customer_id: str
    items: list[OrderItem] = field(default_factory=list)
    status: Status = Status.DRAFT

    @property
    def total_cents(self) -> int:
        return sum(item.total_cents for item in self.items)

    def add_item(self, item: OrderItem) -> None:
        if self.status is not Status.DRAFT:
            raise ValueError(f"cannot change items of a {self.status} order")
        self.items.append(item)

    def place(self) -> None:
        if self.status is not Status.DRAFT:
            raise ValueError(f"cannot place a {self.status} order")
        if not self.items:
            raise ValueError("an order needs at least one item")
        self.status = Status.PLACED

    def advance(self) -> None:
        """placed → paid → shipped"""
        if self.status not in NEXT_STATUS:
            raise ValueError(f"cannot advance a {self.status} order")
        self.status = NEXT_STATUS[self.status]

    def cancel(self) -> None:
        if self.status not in (Status.DRAFT, Status.PLACED):
            raise ValueError(f"cannot cancel a {self.status} order")
        self.status = Status.CANCELLED
