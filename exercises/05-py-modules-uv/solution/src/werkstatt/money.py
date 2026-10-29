def format_cents(cents: int) -> str:
    """Formatiert 1234 als "12,34 €"."""
    sign = "-" if cents < 0 else ""
    euros, rest = divmod(abs(cents), 100)
    return f"{sign}{euros},{rest:02d} €"
