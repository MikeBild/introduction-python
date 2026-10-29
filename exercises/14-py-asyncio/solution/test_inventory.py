"""Tests ohne Zusatzpaket: asyncio.run startet die Coroutine im synchronen Test."""

import asyncio
import time

import pytest

from inventory import stock_for, stock_limited, stock_one_by_one

STOCK = {"p-hammer": 12, "p-saege": 4, "p-bohrer": 2, "p-zange": 20}
PRODUCTS = list(STOCK)


class FakeWarehouse:
    """Antwortet nach delay Sekunden und zählt, wie viele Abfragen gleichzeitig laufen."""

    def __init__(self, delay: float = 0.05) -> None:
        self.delay = delay
        self.running = 0
        self.max_running = 0

    async def lookup(self, product_id: str) -> int:
        self.running += 1
        self.max_running = max(self.max_running, self.running)
        try:
            await asyncio.sleep(self.delay)
            return STOCK[product_id]
        finally:
            self.running -= 1


def test_one_by_one_waits_for_each_lookup() -> None:
    warehouse = FakeWarehouse()
    assert asyncio.run(stock_one_by_one(PRODUCTS, warehouse.lookup)) == STOCK
    assert warehouse.max_running == 1


def test_stock_for_runs_all_lookups_at_once() -> None:
    warehouse = FakeWarehouse(delay=0.1)
    started = time.perf_counter()
    assert asyncio.run(stock_for(PRODUCTS, warehouse.lookup)) == STOCK
    assert warehouse.max_running == len(PRODUCTS)
    assert time.perf_counter() - started < 0.3


def test_stock_for_gives_up_after_the_timeout() -> None:
    warehouse = FakeWarehouse(delay=1)
    with pytest.raises(TimeoutError):
        asyncio.run(stock_for(PRODUCTS, warehouse.lookup, timeout=0.05))


def test_stock_for_reports_failing_lookups() -> None:
    warehouse = FakeWarehouse()
    with pytest.raises(ExceptionGroup) as info:
        asyncio.run(stock_for(["p-unbekannt", *PRODUCTS], warehouse.lookup))
    assert info.group_contains(KeyError)


def test_stock_limited_respects_the_limit() -> None:
    warehouse = FakeWarehouse()
    assert asyncio.run(stock_limited(PRODUCTS, warehouse.lookup, limit=2)) == STOCK
    assert warehouse.max_running == 2
