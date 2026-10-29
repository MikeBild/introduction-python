"""Große Bestelldateien lazy verarbeiten: eine Zeile nach der anderen."""

import json
from collections.abc import Iterable, Iterator
from itertools import batched, islice
from pathlib import Path
from typing import Any

type Order = dict[str, Any]


def read_orders(path: Path) -> Iterator[Order]:
    """Liest JSON Lines: je Zeile eine Bestellung. Die Datei bleibt nur so lange offen wie nötig."""
    with path.open(encoding="utf-8") as file:
        for line in file:
            if line.strip():
                yield json.loads(line)


def with_status(orders: Iterable[Order], *statuses: str) -> Iterator[Order]:
    return (order for order in orders if order["status"] in statuses)


def totals(orders: Iterable[Order]) -> Iterator[tuple[str, int]]:
    for order in orders:
        yield order["id"], sum(item["quantity"] * item["priceCents"] for item in order["items"])


def running_total(amounts: Iterable[tuple[str, int]]) -> Iterator[int]:
    total = 0
    for _order_id, amount in amounts:
        total += amount
        yield total


def in_batches(orders: Iterable[Order], size: int) -> Iterator[list[str]]:
    """IDs in Paketen zu size Stück, etwa für einen Bulk-Request."""
    for batch in batched(orders, size):
        yield [order["id"] for order in batch]


def first_paid(path: Path, n: int) -> list[str]:
    """Liest nur so viele Zeilen, wie für n bezahlte Bestellungen nötig sind."""
    return [order["id"] for order in islice(with_status(read_orders(path), "paid"), n)]
