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
    # TODO: leeres dict anlegen und jedes Produkt unter product["id"] ablegen
    raise NotImplementedError


def low_stock(products: list[Product], threshold: int = 3) -> list[str]:
    """Namen der Produkte mit Bestand unter threshold, alphabetisch."""
    # TODO: Namen in einer Liste sammeln, am Ende sorted() zurückgeben
    raise NotImplementedError


def customer_ids(orders: list[Order]) -> set[str]:
    """Jede Kundin nur einmal."""
    # TODO: Welche Collection entfernt Duplikate von selbst?
    raise NotImplementedError


def quantities_by_product(orders: list[Order]) -> Counter[str]:
    """Wie oft wurde jedes Produkt bestellt?"""
    # TODO: Counter() zählt fehlende Schlüssel als 0 – du kannst direkt += rechnen
    raise NotImplementedError


def price_list(products: list[Product]) -> frozendict[str, int]:
    """Unveränderliche Preisliste: Produkt-ID → priceCents."""
    # TODO: erst ein dict bauen, dann frozendict(prices) zurückgeben (eingebaut seit Python 3.15)
    raise NotImplementedError
