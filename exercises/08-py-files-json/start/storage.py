"""Products and orders as files: pathlib, with, json and csv."""

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
    """Reads a JSON file with a list of products."""
    # TODO: with path.open(encoding="utf-8") as file: ... json.load(file)
    raise NotImplementedError


def save_order(directory: Path, order: Order) -> Path:
    """Writes an order as <id>.json and returns the path."""
    # TODO: create the directory with mkdir(parents=True, exist_ok=True)
    # TODO: write to <id>.tmp first, then rename with replace() – so nobody reads half-written files
    raise NotImplementedError


def load_orders(directory: Path) -> list[Order]:
    """Reads all *.json files of a directory, sorted by file name."""
    # TODO: sorted(directory.glob("*.json")) and json.loads(path.read_text(...))
    raise NotImplementedError


def export_csv(orders: list[Order], path: Path) -> None:
    """One row per line item with orderId, customerId, productId, quantity, priceCents."""
    # TODO: csv.DictWriter; open the file with newline=""
    raise NotImplementedError
