from collections.abc import Iterable


def parse_item(text: str) -> tuple[int, int]:
    """Reads "2x1299" as (quantity, price_cents)."""
    quantity, _, price = text.partition("x")
    return int(quantity), int(price)


def order_total(items: Iterable[tuple[int, int]]) -> int:
    return sum(quantity * price_cents for quantity, price_cents in items)
