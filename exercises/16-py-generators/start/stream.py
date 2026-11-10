"""Process large order files lazily: one line after another.

Today every function loads everything into a list. TODO: Turn them into generators with yield.
"""

import json
from collections.abc import Iterable, Iterator
from pathlib import Path
from typing import Any

type Order = dict[str, Any]


def read_orders(path: Path) -> Iterator[Order]:
    # TODO: read and yield line by line instead of read_text().splitlines()
    lines = path.read_text(encoding="utf-8").splitlines()
    return iter([json.loads(line) for line in lines if line.strip()])


def with_status(orders: Iterable[Order], *statuses: str) -> Iterator[Order]:
    # TODO: generator expression instead of a list
    return iter([order for order in orders if order["status"] in statuses])


def totals(orders: Iterable[Order]) -> Iterator[tuple[str, int]]:
    # TODO: yield (id, total) per order
    raise NotImplementedError


def running_total(amounts: Iterable[tuple[str, int]]) -> Iterator[int]:
    # TODO: yield the running total
    raise NotImplementedError


def in_batches(orders: Iterable[Order], size: int) -> Iterator[list[str]]:
    # TODO: use itertools.batched (since Python 3.12)
    raise NotImplementedError


def first_paid(path: Path, n: int) -> list[str]:
    # TODO: itertools.islice – reads only as many lines as needed
    raise NotImplementedError
