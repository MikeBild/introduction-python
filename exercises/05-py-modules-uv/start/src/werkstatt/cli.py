"""Everything in one file. TODO: Split it into modules.

- werkstatt/money.py   → format_cents
- werkstatt/orders.py  → parse_item, order_total
- werkstatt/cli.py     → only main, imports the two modules
"""

import argparse
from collections.abc import Iterable


def format_cents(cents: int) -> str:
    sign = "-" if cents < 0 else ""
    euros, rest = divmod(abs(cents), 100)
    # Thousands separator: 123456 cents → "1.234,56 €"
    return f"{sign}{euros:_}".replace("_", ".") + f",{rest:02d} €"


def parse_item(text: str) -> tuple[int, int]:
    quantity, _, price = text.partition("x")
    return int(quantity), int(price)


def order_total(items: Iterable[tuple[int, int]]) -> int:
    return sum(quantity * price_cents for quantity, price_cents in items)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="werkstatt", description="Summe einer Bestellung")
    parser.add_argument("items", nargs="+", help="Positionen als MENGExPREIS_IN_CENT, z. B. 2x1299")
    args = parser.parse_args(argv)
    print(format_cents(order_total(parse_item(item) for item in args.items)))
    return 0


# TODO: Add the block that calls main() only when started directly (__name__ == "__main__").
