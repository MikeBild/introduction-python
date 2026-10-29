"""Funktionen rund um Bestellpositionen: (product_id, quantity, price_cents)."""

from collections.abc import Callable, Iterable

type Item = tuple[str, int, int]


def line_total(quantity: int, price_cents: int) -> int:
    return quantity * price_cents


def order_total(items: Iterable[Item], discount_percent: int = 0) -> int:
    """Summe aller Positionen."""
    # TODO: Mach discount_percent zu einem Keyword-only-Argument (Stern in der Signatur).
    # TODO: Summiere line_total über alle Positionen und zieh den Rabatt in ganzen Cent ab.
    raise NotImplementedError


def add_item(item: Item, items: list[Item] = []) -> list[Item]:
    """Soll eine neue Liste zurückgeben, ohne die übergebene zu ändern."""
    # TODO: Der Default [] wird nur einmal erzeugt und von allen Aufrufen geteilt.
    #       Nutze None als Default und kopiere die übergebene Liste.
    items.append(item)
    return items


def make_discount(percent: int) -> Callable[[int], int]:
    """Gibt eine Funktion zurück, die einen Betrag um percent Prozent reduziert."""
    # TODO: innere Funktion definieren und zurückgeben (Closure)
    raise NotImplementedError
