"""Money in the workshop shop: always whole cents as int, never float."""


def to_cents(euros: str) -> int:
    """Converts "12,34" or "12.34" into 1234 cents."""
    whole, _, fraction = euros.strip().replace(",", ".").partition(".")
    if not whole.isdigit() or len(fraction) > 2 or (fraction and not fraction.isdigit()):
        raise ValueError(f"invalid amount: {euros!r}")
    return int(whole) * 100 + int(fraction.ljust(2, "0"))


def format_cents(cents: int) -> str:
    """Formats 1234 as "12,34 €" and 123456 as "1.234,56 €"."""
    sign = "-" if cents < 0 else ""
    euros, rest = divmod(abs(cents), 100)
    # Thousands separator: 123456 cents → "1.234,56 €"
    return f"{sign}{euros:_}".replace("_", ".") + f",{rest:02d} €"


def is_free(price_cents: int | None) -> bool:
    """None means: price unknown. That is not the same as free."""
    return price_cents is not None and price_cents == 0
