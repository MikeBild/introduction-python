import pytest
from flask.testing import FlaskClient

from app import create_app
from shop import Store


@pytest.fixture
def store() -> Store:
    return Store.with_demo_data()


@pytest.fixture
def client(store: Store) -> FlaskClient:
    app = create_app(store)
    app.config["TESTING"] = True
    return app.test_client()


def test_health(client: FlaskClient) -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}


def test_list_products(client: FlaskClient) -> None:
    products = client.get("/products").get_json()
    assert [product["id"] for product in products] == ["p-hammer", "p-saege"]


def test_post_order_creates_the_order(client: FlaskClient, store: Store) -> None:
    response = client.post(
        "/orders", json={"customerId": "c-ada", "items": [{"productId": "p-hammer", "quantity": 2}]}
    )
    assert response.status_code == 201
    order = response.get_json()
    assert order["totalCents"] == 2598
    assert response.headers["Location"] == f"/orders/{order['id']}"
    assert client.get(f"/orders/{order['id']}").get_json() == order
    assert store.products["p-hammer"].stock == 10


@pytest.mark.parametrize(
    "body",
    [
        None,
        {"customerId": "c-ada", "items": []},
        {"customerId": "", "items": [{"productId": "p-hammer", "quantity": 1}]},
        {"customerId": "c-ada", "items": [{"productId": "p-hammer", "quantity": 0}]},
        {"customerId": "c-ada", "items": [{"productId": "p-hammer", "quantity": True}]},
        {"customerId": "c-ada", "items": [{"productId": "p-hammer", "quantity": 1}], "admin": True},
    ],
)
def test_post_order_rejects_invalid_input(client: FlaskClient, body: object) -> None:
    response = client.post("/orders", json=body)
    assert response.status_code == 400
    assert response.get_json()["issues"]


def test_post_order_with_unknown_product(client: FlaskClient) -> None:
    body = {"customerId": "c-ada", "items": [{"productId": "p-bohrer", "quantity": 1}]}
    assert client.post("/orders", json=body).status_code == 422


def test_post_order_with_too_little_stock(client: FlaskClient, store: Store) -> None:
    body = {"customerId": "c-ada", "items": [{"productId": "p-saege", "quantity": 5}]}
    assert client.post("/orders", json=body).status_code == 409
    assert store.products["p-saege"].stock == 4


def test_unknown_order_and_unknown_route_answer_with_json(client: FlaskClient) -> None:
    assert client.get("/orders/o-404").status_code == 404
    response = client.get("/does-not-exist")
    assert response.status_code == 404
    assert response.get_json() == {"error": "not found"}
