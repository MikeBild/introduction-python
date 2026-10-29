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
    with path.open(encoding="utf-8") as file:
        products: list[Product] = json.load(file)
    return products


def save_order(directory: Path, order: Order) -> Path:
    """Schreibt eine Bestellung als <id>.json; legt das Verzeichnis bei Bedarf an."""
    directory.mkdir(parents=True, exist_ok=True)
    target = directory / f"{order['id']}.json"
    temporary = target.with_suffix(".tmp")
    temporary.write_text(json.dumps(order, ensure_ascii=False, indent=2), encoding="utf-8")
    temporary.replace(target)  # erst vollständig schreiben, dann umbenennen
    return target


def load_orders(directory: Path) -> list[Order]:
    """Liest alle Bestellungen eines Verzeichnisses, sortiert nach Dateiname."""
    return [json.loads(path.read_text(encoding="utf-8")) for path in sorted(directory.glob("*.json"))]


def export_csv(orders: list[Order], path: Path) -> None:
    """Eine Zeile je Position, für die Tabellenkalkulation."""
    fields = ["orderId", "customerId", "productId", "quantity", "priceCents"]
    with path.open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        for order in orders:
            for item in order["items"]:
                writer.writerow({"orderId": order["id"], "customerId": order["customerId"], **item})
