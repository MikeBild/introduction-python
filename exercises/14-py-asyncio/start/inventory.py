"""Query the stock of several products at the same time – with a time limit and an upper bound."""

import asyncio
from collections.abc import Callable, Coroutine

type StockLookup = Callable[[str], Coroutine[None, None, int]]


async def stock_one_by_one(product_ids: list[str], lookup: StockLookup) -> dict[str, int]:
    """One after another: the waiting times add up."""
    return {product_id: await lookup(product_id) for product_id in product_ids}


async def stock_for(
    product_ids: list[str], lookup: StockLookup, *, timeout: float = 1.0
) -> dict[str, int]:
    """All queries at the same time, at most timeout seconds in total."""
    # TODO: async with asyncio.timeout(timeout): and inside it async with asyncio.TaskGroup() as group:
    # TODO: group.create_task(lookup(product_id)) per product; read task.result() after the block
    raise NotImplementedError


async def stock_limited(product_ids: list[str], lookup: StockLookup, *, limit: int = 3) -> dict[str, int]:
    """At the same time, but at most limit queries at once."""
    # TODO: asyncio.Semaphore(limit) and an inner coroutine with async with semaphore:
    raise NotImplementedError
