"""HTTP API with Flask 3. Start: uv run flask --app app run --debug"""

from flask import Flask
from flask.typing import ResponseReturnValue

from shop import Store, product_to_json


def create_app(store: Store | None = None) -> Flask:
    """App factory: every test gets its own app with its own store."""
    app = Flask(__name__)
    shop = store if store is not None else Store.with_demo_data()

    @app.get("/health")
    def health() -> ResponseReturnValue:
        return {"status": "ok"}

    @app.get("/products")
    def list_products() -> ResponseReturnValue:
        return [product_to_json(product) for product in shop.products.values()]

    # TODO: GET /orders/<order_id> → order_to_json(order) or 404 with {"error": "order not found"}

    # TODO: POST /orders
    #   - read the body with request.get_json(silent=True) and validate it with parse_place_order
    #   - call shop.place_order(...)
    #   - return 201 with the Location header /orders/<id>

    # TODO: error handlers with @app.errorhandler(...)
    #   - ValidationError → 400 {"error": "invalid input", "issues": [...]}
    #   - UnknownProduct → 422, InsufficientStock → 409
    #   - HTTPException (for example an unknown route) → JSON instead of HTML

    return app
