"""Kommandozeile: uv run werkstatt 2x1299 1x2499"""

import argparse

from werkstatt.money import format_cents
from werkstatt.orders import order_total, parse_item


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="werkstatt", description="Summe einer Bestellung")
    parser.add_argument("items", nargs="+", help="Positionen als MENGExPREIS_IN_CENT, z. B. 2x1299")
    args = parser.parse_args(argv)
    print(format_cents(order_total(parse_item(item) for item in args.items)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
