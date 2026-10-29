"""Geldbeträge im Werkstatt-Shop: immer ganze Cent als int, nie float."""


def to_cents(euros: str) -> int:
    """Wandelt "12,34" oder "12.34" in 1234 Cent um."""
    # TODO: Leerzeichen entfernen, Komma durch Punkt ersetzen, mit partition(".") teilen.
    # TODO: Ungültige Eingaben ("", "abc", "1,234", "-3") mit ValueError ablehnen.
    # Tipp: float("12.34") * 100 ergibt 1233.9999999999998 – rechne mit int.
    raise NotImplementedError


def format_cents(cents: int) -> str:
    """Formatiert 1234 als "12,34 €" und 123456 als "1.234,56 €"."""
    # TODO: divmod(abs(cents), 100) und ein f-String mit {rest:02d}
    # Tipp: f"{123456:_}" ergibt "123_456" – daraus wird der Tausenderpunkt.
    raise NotImplementedError


def is_free(price_cents: int | None) -> bool:
    """None heißt: Preis unbekannt. Das ist nicht dasselbe wie gratis."""
    # TODO: Achtung, `not price_cents` ist auch für None wahr.
    raise NotImplementedError
