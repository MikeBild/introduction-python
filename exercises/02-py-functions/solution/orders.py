"""Functions around order line items: (product_id, quantity, price_cents)."""

from collections.abc import Callable, Iterable

type Item = tuple[str, int, int]


def line_total(quantity: int, price_cents: int) -> int:
    return quantity * price_cents


def order_total(items: Iterable[Item], *, discount_percent: int = 0) -> int:
    """Sum of all line items; the discount is a keyword-only argument."""
    subtotal = 0
    for _product_id, quantity, price_cents in items:
        subtotal += line_total(quantity, price_cents)
    return subtotal - subtotal * discount_percent // 100


def add_item(item: Item, items: list[Item] | None = None) -> list[Item]:
    """Returns a new list without changing the one passed in."""
    result = [] if items is None else list(items)
    result.append(item)
    return result


def make_discount(percent: int) -> Callable[[int], int]:
    """Closure: the inner function remembers percent."""

    def discount(total_cents: int) -> int:
        return total_cents - total_cents * percent // 100

    return discount
