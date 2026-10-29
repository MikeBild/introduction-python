"""Die Bestellung als Klasse. TODO: Mach daraus Dataclasses mit klaren Regeln."""

from enum import StrEnum


class Status(StrEnum):
    DRAFT = "draft"
    PLACED = "placed"
    PAID = "paid"
    SHIPPED = "shipped"
    CANCELLED = "cancelled"


class OrderItem:
    # TODO: @dataclass(frozen=True, slots=True) statt __init__, __eq__ und __repr__ von Hand
    # TODO: __post_init__ lehnt quantity < 1 mit ValueError ab
    # TODO: Property total_cents
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
    # TODO: @dataclass(slots=True); items mit field(default_factory=list), status mit Default DRAFT
    def __init__(
        self,
        id: str,
        customer_id: str,
        items: list[OrderItem] = [],  # TODO: geteilte Default-Liste!
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
        # TODO: nur im Status draft erlaubt, sonst ValueError
        self.items.append(item)

    def place(self) -> None:
        # TODO: nur aus draft und nur mit mindestens einer Position
        raise NotImplementedError

    def advance(self) -> None:
        """placed → paid → shipped, sonst ValueError"""
        raise NotImplementedError

    def cancel(self) -> None:
        """nur aus draft oder placed"""
        raise NotImplementedError
