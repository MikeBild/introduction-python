import pytest
from reports import (
    Order,
    all_items,
    open_order_ids,
    order_total,
    products_sold,
    top_orders,
    totals_by_order,
)

pytestmark = pytest.mark.skip(reason="Entferne diese Zeile, um die Tests zu aktivieren.")

orders: list[Order] = [
    {
        "id": "o-1",
        "customerId": "c-ada",
        "status": "placed",
        "items": [
            {"productId": "p-hammer", "quantity": 2, "priceCents": 1299},
            {"productId": "p-saw", "quantity": 1, "priceCents": 2499},
        ],
    },
    {
        "id": "o-2",
        "customerId": "c-linus",
        "status": "cancelled",
        "items": [{"productId": "p-drill", "quantity": 1, "priceCents": 8999}],
    },
    {
        "id": "o-3",
        "customerId": "c-ada",
        "status": "paid",
        "items": [{"productId": "p-hammer", "quantity": 1, "priceCents": 1299}],
    },
    {"id": "o-4", "customerId": "c-grace", "status": "draft", "items": []},
]


def test_order_total_sums_quantity_times_price() -> None:
    assert order_total(orders[0]) == 2 * 1299 + 2499
    assert order_total(orders[3]) == 0


def test_totals_by_order_maps_each_id() -> None:
    assert totals_by_order(orders) == {"o-1": 5097, "o-2": 8999, "o-3": 1299, "o-4": 0}


def test_open_order_ids_keeps_placed_and_paid() -> None:
    assert open_order_ids(orders) == ["o-1", "o-3"]


def test_products_sold_ignores_cancelled_orders() -> None:
    assert products_sold(orders) == {"p-hammer", "p-saw"}


def test_all_items_flattens_the_items() -> None:
    assert [item["productId"] for item in all_items(orders)] == [
        "p-hammer",
        "p-saw",
        "p-drill",
        "p-hammer",
    ]


def test_top_orders_sorts_by_total() -> None:
    assert top_orders(orders, 2) == [("o-2", 8999), ("o-1", 5097)]
