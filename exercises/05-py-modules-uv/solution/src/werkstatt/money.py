def format_cents(cents: int) -> str:
    """Formats 1234 as "12,34 €" and 123456 as "1.234,56 €"."""
    sign = "-" if cents < 0 else ""
    euros, rest = divmod(abs(cents), 100)
    # Thousands separator: 123456 cents → "1.234,56 €"
    return f"{sign}{euros:_}".replace("_", ".") + f",{rest:02d} €"
