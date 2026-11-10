"""The order as a class. TODO: Turn it into dataclasses with clear rules."""

from enum import StrEnum


class Status(StrEnum):
    DRAFT = "draft"
    PLACED = "placed"
    PAID = "paid"
    SHIPPED = "shipped"
    CANCELLED = "cancelled"


class OrderItem:
    # TODO: @dataclass(frozen=True, slots=True) instead of __init__, __eq__ and __repr__ by hand
    # TODO: __post_init__ rejects quantity < 1 with ValueError
    # TODO: property total_cents
    def __init__(self, product_id: str, quantity: int, price_cents: int) -> None:
        self.product_id = product_id
        self.quantity = quantity
        self.price_cents = price_cents

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, OrderItem):
            return NotImplemented
        return (self.product_id, self.quantity, self.price_cents) == (
            other.product_id,
            other.quantity,
            other.price_cents,
        )

    def __repr__(self) -> str:
        return f"OrderItem({self.product_id!r}, {self.quantity}, {self.price_cents})"

    @property
    def total_cents(self) -> int:
        raise NotImplementedError


class Order:
    # TODO: @dataclass(slots=True); items with field(default_factory=list), status with default DRAFT
    def __init__(
        self,
        id: str,
        customer_id: str,
        items: list[OrderItem] = [],  # TODO: shared default list
        status: Status = Status.DRAFT,
    ) -> None:
        self.id = id
        self.customer_id = customer_id
        self.items = items
        self.status = status

    @property
    def total_cents(self) -> int:
        raise NotImplementedError

    def add_item(self, item: OrderItem) -> None:
        # TODO: only allowed in status draft, otherwise ValueError
        self.items.append(item)

    def place(self) -> None:
        # TODO: only from draft and only with at least one line item
        raise NotImplementedError

    def advance(self) -> None:
        """placed → paid → shipped, otherwise ValueError"""
        raise NotImplementedError

    def cancel(self) -> None:
        """only from draft or placed"""
        raise NotImplementedError
