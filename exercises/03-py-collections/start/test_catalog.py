import pytest

from catalog import (
    Order,
    Product,
    customer_ids,
    index_by_id,
    low_stock,
    price_list,
    quantities_by_product,
)

pytestmark = pytest.mark.skip(reason="Entferne diese Zeile, um die Tests zu aktivieren.")

products: list[Product] = [
    {"id": "p-hammer", "name": "Hammer", "priceCents": 1299, "stock": 5},
    {"id": "p-saw", "name": "Säge", "priceCents": 2499, "stock": 1},
    {"id": "p-drill", "name": "Bohrer", "priceCents": 899, "stock": 0},
]

orders: list[Order] = [
    {"id": "o-1", "customerId": "c-ada", "items": [{"productId": "p-hammer", "quantity": 2}]},
    {"id": "o-2", "customerId": "c-linus", "items": [{"productId": "p-saw", "quantity": 1}]},
    {
        "id": "o-3",
        "customerId": "c-ada",
        "items": [{"productId": "p-hammer", "quantity": 1}, {"productId": "p-saw", "quantity": 3}],
    },
]


def test_index_by_id_finds_products_by_id() -> None:
    index = index_by_id(products)
    assert index["p-saw"]["name"] == "Säge"
    assert "p-unknown" not in index


def test_low_stock_lists_names_sorted() -> None:
    assert low_stock(products) == ["Bohrer", "Säge"]
    assert low_stock(products, threshold=1) == ["Bohrer"]


def test_customer_ids_contains_each_customer_once() -> None:
    assert customer_ids(orders) == {"c-ada", "c-linus"}


def test_quantities_by_product_counts_all_items() -> None:
    counts = quantities_by_product(orders)
    assert counts["p-hammer"] == 3
    assert counts["p-saw"] == 4
    assert counts["p-drill"] == 0
    assert counts.most_common(1) == [("p-saw", 4)]


def test_price_list_cannot_be_changed() -> None:
    prices = price_list(products)
    assert prices["p-hammer"] == 1299
    with pytest.raises(TypeError):
        prices["p-hammer"] = 1  # type: ignore[index]
