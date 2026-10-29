"""Bestellungen aufgeben: fachliche Fehler als eigene Exception-Hierarchie."""

from dataclasses import dataclass


class OrderError(Exception):
    """Basis für alle fachlichen Fehler beim Bestellen."""


class InvalidQuantity(OrderError):
    def __init__(self, text: str) -> None:
        super().__init__(f"invalid quantity: {text!r}")
        self.text = text


class UnknownProduct(OrderError):
    def __init__(self, product_id: str) -> None:
        super().__init__(f"unknown product: {product_id}")
        self.product_id = product_id


class InsufficientStock(OrderError):
    def __init__(self, product_id: str, requested: int, available: int) -> None:
        super().__init__(f"only {available} of {product_id} in stock, requested {requested}")
        self.product_id = product_id
        self.requested = requested
        self.available = available


@dataclass(frozen=True, slots=True)
class Product:
    id: str
    price_cents: int
    stock: int


def parse_quantity(text: str) -> int:
    """Wandelt Text in eine Menge ≥ 1; die Ursache bleibt per raise ... from erhalten."""
    try:
        quantity = int(text)
    except ValueError as error:
        raise InvalidQuantity(text) from error
    if quantity < 1:
        raise InvalidQuantity(text)
    return quantity


def place_order(items: dict[str, int], catalog: dict[str, Product]) -> int:
    """Prüft alle Positionen und gibt die Gesamtsumme in Cent zurück."""
    total = 0
    for product_id, quantity in items.items():
        try:
            product = catalog[product_id]
        except KeyError:
            raise UnknownProduct(product_id) from None
        if quantity > product.stock:
            raise InsufficientStock(product_id, quantity, product.stock)
        total += quantity * product.price_cents
    return total


def handle_place_order(items: dict[str, int], catalog: dict[str, Product]) -> tuple[int, dict[str, object]]:
    """Übersetzt fachliche Fehler in Status Codes. Alles andere fliegt weiter."""
    try:
        total = place_order(items, catalog)
    except UnknownProduct as error:
        return 404, {"error": str(error), "productId": error.product_id}
    except OrderError as error:
        return 409, {"error": str(error)}
    else:
        return 201, {"totalCents": total}
