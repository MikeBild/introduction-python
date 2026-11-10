"""Functions around order line items: (product_id, quantity, price_cents)."""

from collections.abc import Callable, Iterable

type Item = tuple[str, int, int]


def line_total(quantity: int, price_cents: int) -> int:
    return quantity * price_cents


def order_total(items: Iterable[Item], discount_percent: int = 0) -> int:
    """Sum of all line items."""
    # TODO: Make discount_percent a keyword-only argument (star in the signature).
    # TODO: Sum line_total over all line items and subtract the discount in whole cents.
    raise NotImplementedError


def add_item(item: Item, items: list[Item] = []) -> list[Item]:
    """Should return a new list without changing the one passed in."""
    # TODO: The default [] is created only once and shared by all calls.
    #       Use None as the default and copy the list passed in.
    items.append(item)
    return items


def make_discount(percent: int) -> Callable[[int], int]:
    """Returns a function that reduces an amount by percent percent."""
    # TODO: define and return an inner function (closure)
    raise NotImplementedError
