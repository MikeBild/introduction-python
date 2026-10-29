"""Produkte und Bestellungen als Dateien: pathlib, with, json und csv."""

import csv
import json
from pathlib import Path
from typing import TypedDict


class Product(TypedDict):
    id: str
    name: str
    priceCents: int
    stock: int


class OrderItem(TypedDict):
    productId: str
    quantity: int
    priceCents: int


class Order(TypedDict):
    id: str
    customerId: str
    status: str
    createdAt: str
    items: list[OrderItem]


def load_products(path: Path) -> list[Product]:
    """Liest eine JSON-Datei mit einer Liste von Produkten."""
    # TODO: with path.open(encoding="utf-8") as file: ... json.load(file)
    raise NotImplementedError


def save_order(directory: Path, order: Order) -> Path:
    """Schreibt eine Bestellung als <id>.json und gibt den Pfad zurück."""
    # TODO: Verzeichnis mit mkdir(parents=True, exist_ok=True) anlegen
    # TODO: erst in <id>.tmp schreiben, dann mit replace() umbenennen – so liest niemand halbe Dateien
    raise NotImplementedError


def load_orders(directory: Path) -> list[Order]:
    """Liest alle *.json eines Verzeichnisses, sortiert nach Dateiname."""
    # TODO: sorted(directory.glob("*.json")) und json.loads(path.read_text(...))
    raise NotImplementedError


def export_csv(orders: list[Order], path: Path) -> None:
    """Eine Zeile je Position mit orderId, customerId, productId, quantity, priceCents."""
    # TODO: csv.DictWriter; die Datei mit newline="" öffnen
    raise NotImplementedError
