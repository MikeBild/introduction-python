"""Große Bestelldateien lazy verarbeiten: eine Zeile nach der anderen.

Heute lädt jede Funktion alles in eine Liste. TODO: Mach daraus Generatoren mit yield.
"""

import json
from collections.abc import Iterable, Iterator
from pathlib import Path
from typing import Any

type Order = dict[str, Any]


def read_orders(path: Path) -> Iterator[Order]:
    # TODO: Zeile für Zeile lesen und yielden statt read_text().splitlines()
    lines = path.read_text(encoding="utf-8").splitlines()
    return iter([json.loads(line) for line in lines if line.strip()])


def with_status(orders: Iterable[Order], *statuses: str) -> Iterator[Order]:
    # TODO: Generator Expression statt Liste
    return iter([order for order in orders if order["status"] in statuses])


def totals(orders: Iterable[Order]) -> Iterator[tuple[str, int]]:
    # TODO: je Bestellung (id, Summe) yielden
    raise NotImplementedError


def running_total(amounts: Iterable[tuple[str, int]]) -> Iterator[int]:
    # TODO: laufende Summe yielden
    raise NotImplementedError


def in_batches(orders: Iterable[Order], size: int) -> Iterator[list[str]]:
    # TODO: itertools.batched (seit Python 3.12) nutzen
    raise NotImplementedError


def first_paid(path: Path, n: int) -> list[str]:
    # TODO: itertools.islice – liest nur so viele Zeilen wie nötig
    raise NotImplementedError
