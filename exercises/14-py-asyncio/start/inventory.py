"""Bestand mehrerer Produkte gleichzeitig abfragen – mit Zeitlimit und Obergrenze."""

import asyncio
from collections.abc import Callable, Coroutine

type StockLookup = Callable[[str], Coroutine[None, None, int]]


async def stock_one_by_one(product_ids: list[str], lookup: StockLookup) -> dict[str, int]:
    """Nacheinander: die Wartezeiten addieren sich."""
    return {product_id: await lookup(product_id) for product_id in product_ids}


async def stock_for(
    product_ids: list[str], lookup: StockLookup, *, timeout: float = 1.0
) -> dict[str, int]:
    """Alle Abfragen gleichzeitig, insgesamt höchstens timeout Sekunden."""
    # TODO: async with asyncio.timeout(timeout): und darin async with asyncio.TaskGroup() as group:
    # TODO: je Produkt group.create_task(lookup(product_id)); nach dem Block task.result() lesen
    raise NotImplementedError


async def stock_limited(product_ids: list[str], lookup: StockLookup, *, limit: int = 3) -> dict[str, int]:
    """Gleichzeitig, aber höchstens limit Abfragen auf einmal."""
    # TODO: asyncio.Semaphore(limit) und eine innere Coroutine mit async with semaphore:
    raise NotImplementedError
