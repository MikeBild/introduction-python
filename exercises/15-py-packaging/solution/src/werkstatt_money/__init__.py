"""Geldbeträge in ganzen Cent parsen und formatieren."""

import sys
from importlib.metadata import version

__all__ = ["format_cents", "main", "to_cents"]


def to_cents(euros: str) -> int:
    whole, _, fraction = euros.strip().replace(",", ".").partition(".")
    if not whole.isdigit() or len(fraction) > 2 or (fraction and not fraction.isdigit()):
        raise ValueError(f"invalid amount: {euros!r}")
    return int(whole) * 100 + int(fraction.ljust(2, "0"))


def format_cents(cents: int) -> str:
    sign = "-" if cents < 0 else ""
    euros, rest = divmod(abs(cents), 100)
    # Tausenderpunkt: 123456 Cent → "1.234,56 €"
    return f"{sign}{euros:_}".replace("_", ".") + f",{rest:02d} €"


def main(argv: list[str] | None = None) -> int:
    """werkstatt-money 12,34 → 1234"""
    args = sys.argv[1:] if argv is None else argv
    if args == ["--version"]:
        print(version("werkstatt-money"))
        return 0
    for text in args:
        print(to_cents(text))
    return 0
