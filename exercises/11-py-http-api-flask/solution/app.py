"""HTTP-API mit Flask 3. Start: uv run flask --app app run --debug"""

from flask import Flask, request
from flask.typing import ResponseReturnValue
from werkzeug.exceptions import HTTPException

from shop import (
    InsufficientStock,
    Store,
    UnknownProduct,
    ValidationError,
    order_to_json,
    parse_place_order,
    product_to_json,
)


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

    @app.get("/orders/<order_id>")
    def get_order(order_id: str) -> ResponseReturnValue:
        order = shop.orders.get(order_id)
        if order is None:
            return {"error": "order not found"}, 404
        return order_to_json(order)

    @app.post("/orders")
    def post_order() -> ResponseReturnValue:
        customer_id, items = parse_place_order(request.get_json(silent=True))
        order = shop.place_order(customer_id, items)
        return order_to_json(order), 201, {"Location": f"/orders/{order.id}"}

    @app.errorhandler(ValidationError)
    def invalid_input(error: ValidationError) -> ResponseReturnValue:
        return {"error": "invalid input", "issues": error.issues}, 400

    @app.errorhandler(UnknownProduct)
    def unknown_product(error: UnknownProduct) -> ResponseReturnValue:
        return {"error": str(error)}, 422

    @app.errorhandler(InsufficientStock)
    def insufficient_stock(error: InsufficientStock) -> ResponseReturnValue:
        return {"error": str(error)}, 409

    @app.errorhandler(HTTPException)
    def http_error(error: HTTPException) -> ResponseReturnValue:
        return {"error": error.name.lower()}, error.code or 500

    return app
