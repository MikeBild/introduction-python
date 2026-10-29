"""HTTP API mit Flask 3. Start: uv run flask --app app run --debug"""

from flask import Flask
from flask.typing import ResponseReturnValue

from shop import Store, product_to_json


def create_app(store: Store | None = None) -> Flask:
    """App Factory: jeder Test bekommt eine eigene App mit eigenem Store."""
    app = Flask(__name__)
    shop = store if store is not None else Store.with_demo_data()

    @app.get("/health")
    def health() -> ResponseReturnValue:
        return {"status": "ok"}

    @app.get("/products")
    def list_products() -> ResponseReturnValue:
        return [product_to_json(product) for product in shop.products.values()]

    # TODO: GET /orders/<order_id> → order_to_json(order) oder 404 mit {"error": "order not found"}

    # TODO: POST /orders
    #   - Body mit request.get_json(silent=True) lesen und mit parse_place_order prüfen
    #   - shop.place_order(...) aufrufen
    #   - 201 mit Location-Header /orders/<id> zurückgeben

    # TODO: Error Handler mit @app.errorhandler(...)
    #   - ValidationError → 400 {"error": "invalid input", "issues": [...]}
    #   - UnknownProduct → 422, InsufficientStock → 409
    #   - HTTPException (z. B. unbekannte Route) → JSON statt HTML

    return app
