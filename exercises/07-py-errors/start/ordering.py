"""Placing orders: domain errors as their own exception hierarchy."""

from dataclasses import dataclass


class OrderError(Exception):
    """Base for all domain errors when ordering."""


class InvalidQuantity(OrderError):
    def __init__(self, text: str) -> None:
        super().__init__(f"invalid quantity: {text!r}")
        self.text = text


class UnknownProduct(OrderError):
    # TODO: like InvalidQuantity, remembers product_id
    def __init__(self, product_id: str) -> None:
        super().__init__()
        self.product_id = product_id


class InsufficientStock(OrderError):
    # TODO: remembers product_id, requested and available and builds a readable message
    def __init__(self, product_id: str, requested: int, available: int) -> None:
        super().__init__()
        self.product_id = product_id
        self.requested = requested
        self.available = available


@dataclass(frozen=True, slots=True)
class Product:
    id: str
    price_cents: int
    stock: int


def parse_quantity(text: str) -> int:
    """Converts text into a quantity ≥ 1."""
    # TODO: int(text) in try/except ValueError, then raise InvalidQuantity(text) from error
    # TODO: reject quantities below 1 with InvalidQuantity as well
    return int(text)


def place_order(items: dict[str, int], catalog: dict[str, Product]) -> int:
    """Checks all line items and returns the total in cents."""
    # TODO: unknown products → UnknownProduct (from None: the KeyError adds nothing)
    # TODO: not enough stock → InsufficientStock
    raise NotImplementedError


def handle_place_order(items: dict[str, int], catalog: dict[str, Product]) -> tuple[int, dict[str, object]]:
    """Translates domain errors into status codes: 201, 404 (UnknownProduct), 409 (other OrderError)."""
    # TODO: try/except/else – catch only OrderError and its subclasses, never Exception
    raise NotImplementedError
