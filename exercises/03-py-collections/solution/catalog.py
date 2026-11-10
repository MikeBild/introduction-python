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
    index: dict[str, Product] = {}
    for product in products:
        index[product["id"]] = product
    return index


def low_stock(products: list[Product], threshold: int = 3) -> list[str]:
    """Names of the products with low stock, alphabetically."""
    names = []
    for product in products:
        if product["stock"] < threshold:
            names.append(product["name"])
    return sorted(names)


def customer_ids(orders: list[Order]) -> set[str]:
    """Every customer only once: a set removes duplicates."""
    ids = set()
    for order in orders:
        ids.add(order["customerId"])
    return ids


def quantities_by_product(orders: list[Order]) -> Counter[str]:
    """How often was each product ordered?"""
    counts: Counter[str] = Counter()
    for order in orders:
        for item in order["items"]:
            counts[item["productId"]] += item["quantity"]
    return counts


def price_list(products: list[Product]) -> frozendict[str, int]:
    """Immutable price list (frozendict is built in since Python 3.15)."""
    prices = {}
    for product in products:
        prices[product["id"]] = product["priceCents"]
    return frozendict(prices)
