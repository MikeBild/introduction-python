"""Bestellungen aufgeben: fachliche Fehler als eigene Exception-Hierarchie."""

from dataclasses import dataclass


class OrderError(Exception):
    """Basis für alle fachlichen Fehler beim Bestellen."""


class InvalidQuantity(OrderError):
    def __init__(self, text: str) -> None:
        super().__init__(f"invalid quantity: {text!r}")
        self.text = text


class UnknownProduct(OrderError):
    # TODO: wie InvalidQuantity, merkt sich product_id
    def __init__(self, product_id: str) -> None:
        super().__init__()
        self.product_id = product_id


class InsufficientStock(OrderError):
    # TODO: merkt sich product_id, requested und available und baut eine lesbare Meldung
    def __init__(self, product_id: str, requested: int, available: int) -> None:
        super().__init__()
        self.product_id = product_id
        self.requested = requested
        self.available = available


@dataclass(frozen=True, slots=True)
class Product:
    id: str
    price_cents: int
    stock: int


def parse_quantity(text: str) -> int:
    """Wandelt Text in eine Menge ≥ 1."""
    # TODO: int(text) in try/except ValueError, dann raise InvalidQuantity(text) from error
    # TODO: Mengen kleiner 1 ebenfalls mit InvalidQuantity ablehnen
    return int(text)


def place_order(items: dict[str, int], catalog: dict[str, Product]) -> int:
    """Prüft alle Positionen und gibt die Gesamtsumme in Cent zurück."""
    # TODO: Unbekannte Produkte → UnknownProduct (from None: der KeyError ist kein Mehrwert)
    # TODO: Zu wenig Bestand → InsufficientStock
    raise NotImplementedError


def handle_place_order(items: dict[str, int], catalog: dict[str, Product]) -> tuple[int, dict[str, object]]:
    """Übersetzt fachliche Fehler in Status Codes: 201, 404 (UnknownProduct), 409 (andere OrderError)."""
    # TODO: try/except/else – fang nur OrderError und Unterklassen, nie Exception
    raise NotImplementedError
