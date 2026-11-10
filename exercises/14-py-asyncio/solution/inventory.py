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
    """At the same time: TaskGroup starts all queries, asyncio.timeout limits the total duration."""
    async with asyncio.timeout(timeout):
        async with asyncio.TaskGroup() as group:
            tasks = {product_id: group.create_task(lookup(product_id)) for product_id in product_ids}
    return {product_id: task.result() for product_id, task in tasks.items()}


async def stock_limited(product_ids: list[str], lookup: StockLookup, *, limit: int = 3) -> dict[str, int]:
    """At the same time, but at most limit queries at once."""
    semaphore = asyncio.Semaphore(limit)

    async def guarded(product_id: str) -> int:
        async with semaphore:
            return await lookup(product_id)

    async with asyncio.TaskGroup() as group:
        tasks = {product_id: group.create_task(guarded(product_id)) for product_id in product_ids}
    return {product_id: task.result() for product_id, task in tasks.items()}
