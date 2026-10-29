"""Produkte und Bestellungen als dict, list, tuple und set."""

from collections import Counter

# Produkte und Bestellungen kommen als JSON-artige dicts. Was TypedDict bedeutet,
# zeigt die Lektion zu Typ-Hinweisen; hier reicht: so sehen die dicts aus.
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
    """dict für schnellen Zugriff per ID statt Suche in der Liste."""
    index: dict[str, Product] = {}
    for product in products:
        index[product["id"]] = product
    return index


def low_stock(products: list[Product], threshold: int = 3) -> list[str]:
    """Namen der Produkte mit wenig Bestand, alphabetisch."""
    names = []
    for product in products:
        if product["stock"] < threshold:
            names.append(product["name"])
    return sorted(names)


def customer_ids(orders: list[Order]) -> set[str]:
    """Jede Kundin nur einmal: ein set entfernt Duplikate."""
    ids = set()
    for order in orders:
        ids.add(order["customerId"])
    return ids


def quantities_by_product(orders: list[Order]) -> Counter[str]:
    """Wie oft wurde jedes Produkt bestellt?"""
    counts: Counter[str] = Counter()
    for order in orders:
        for item in order["items"]:
            counts[item["productId"]] += item["quantity"]
    return counts


def price_list(products: list[Product]) -> frozendict[str, int]:
    """Unveränderliche Preisliste (frozendict ist seit Python 3.15 eingebaut)."""
    prices = {}
    for product in products:
        prices[product["id"]] = product["priceCents"]
    return frozendict(prices)
