def format_cents(cents: int) -> str:
    """Formatiert 1234 als "12,34 €" und 123456 als "1.234,56 €"."""
    sign = "-" if cents < 0 else ""
    euros, rest = divmod(abs(cents), 100)
    # Tausenderpunkt: 123456 Cent → "1.234,56 €"
    return f"{sign}{euros:_}".replace("_", ".") + f",{rest:02d} €"
