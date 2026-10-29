import json
from pathlib import Path

import pytest

from analysis import customer_summary, load_items, revenue_by_month, revenue_by_product

pytestmark = pytest.mark.skip(reason="Entferne diese Zeile, um die Tests zu aktivieren.")

ORDERS = [
    {
        "id": "o-1",
        "customerId": "c-ada",
        "status": "paid",
        "createdAt": "2026-07-03T10:00:00Z",
        "items": [
            {"productId": "p-hammer", "quantity": 2, "priceCents": 1299},
            {"productId": "p-saege", "quantity": 1, "priceCents": 2499},
        ],
    },
    {
        "id": "o-2",
        "customerId": "c-linus",
        "status": "cancelled",
        "createdAt": "2026-07-05T10:00:00Z",
        "items": [{"productId": "p-bohrer", "quantity": 1, "priceCents": 8999}],
    },
    {
        "id": "o-3",
        "customerId": "c-ada",
        "status": "shipped",
        "createdAt": "2026-08-01T10:00:00Z",
        "items": [{"productId": "p-hammer", "quantity": 1, "priceCents": 1299}],
    },
]


@pytest.fixture
def orders_file(tmp_path: Path) -> Path:
    path = tmp_path / "orders.json"
    path.write_text(json.dumps(ORDERS), encoding="utf-8")
    return path


def test_load_items_has_one_row_per_item(orders_file: Path) -> None:
    items = load_items(orders_file)
    assert len(items) == 4
    assert {"orderId", "customerId", "productId", "revenueCents"} <= set(items.columns)
    assert items["revenueCents"].tolist() == [2598, 2499, 8999, 1299]


def test_revenue_by_product_ignores_cancelled_orders(orders_file: Path) -> None:
    revenue = revenue_by_product(load_items(orders_file))
    assert revenue.to_dict() == {"p-hammer": 3897, "p-saege": 2499}


def test_revenue_by_month(orders_file: Path) -> None:
    assert revenue_by_month(load_items(orders_file)).to_dict() == {"2026-07": 5097, "2026-08": 1299}


def test_customer_summary_counts_orders_not_items(orders_file: Path) -> None:
    summary = customer_summary(load_items(orders_file))
    assert summary.loc["c-ada"].to_dict() == {"orders": 2, "revenueCents": 6396}
    assert "c-linus" not in summary.index


def test_works_with_the_shared_sample_data() -> None:
    items = load_items(Path(__file__).resolve().parents[3] / "data" / "orders.json")
    assert revenue_by_product(items).sum() == revenue_by_month(items).sum()
