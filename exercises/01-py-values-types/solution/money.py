"""Geldbeträge im Werkstatt-Shop: immer ganze Cent als int, nie float."""


def to_cents(euros: str) -> int:
    """Wandelt "12,34" oder "12.34" in 1234 Cent um."""
    whole, _, fraction = euros.strip().replace(",", ".").partition(".")
    if not whole.isdigit() or len(fraction) > 2 or (fraction and not fraction.isdigit()):
        raise ValueError(f"invalid amount: {euros!r}")
    return int(whole) * 100 + int(fraction.ljust(2, "0"))


def format_cents(cents: int) -> str:
    """Formatiert 1234 als "12,34 €"."""
    sign = "-" if cents < 0 else ""
    euros, rest = divmod(abs(cents), 100)
    return f"{sign}{euros},{rest:02d} €"


def is_free(price_cents: int | None) -> bool:
    """None heißt: Preis unbekannt. Das ist nicht dasselbe wie gratis."""
    return price_cents is not None and price_cents == 0
