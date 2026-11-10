"""Products and orders as dict, list, tuple and set."""

from collections import Counter

# Products and orders arrive as JSON-like dicts. What TypedDict means
# is shown in the lesson on type hints; here it is enough to know what the dicts look like.
from typing import TypedDict


class Product(TypedDict):
    id: str
    name: str
    priceCents: int
    stock: int


class OrderItem(TypedDict):
    productId: str
    quantity: int


class Order(TypedDict):
    id: str
    customerId: str
    items: list[OrderItem]


def index_by_id(products: list[Product]) -> dict[str, Product]:
    """dict for fast access by ID instead of searching the list."""
    # TODO: create an empty dict and store each product under product["id"]
    raise NotImplementedError


def low_stock(products: list[Product], threshold: int = 3) -> list[str]:
    """Names of the products with stock below threshold, alphabetically."""
    # TODO: collect the names in a list, return sorted() at the end
    raise NotImplementedError


def customer_ids(orders: list[Order]) -> set[str]:
    """Every customer only once."""
    # TODO: Which collection removes duplicates by itself?
    raise NotImplementedError


def quantities_by_product(orders: list[Order]) -> Counter[str]:
    """How often was each product ordered?"""
    # TODO: Counter() counts missing keys as 0 – you can use += directly
    raise NotImplementedError


def price_list(products: list[Product]) -> frozendict[str, int]:
    """Immutable price list: product ID → priceCents."""
    # TODO: build a dict first, then return frozendict(prices) (built in since Python 3.15)
    raise NotImplementedError
