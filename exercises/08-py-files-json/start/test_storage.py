import pytest
import csv
from pathlib import Path

from storage import Order, export_csv, load_orders, load_products, save_order

pytestmark = pytest.mark.skip(reason="Entferne diese Zeile, um die Tests zu aktivieren.")

DATA = Path(__file__).resolve().parents[3] / "data"

order: Order = {
    "id": "o-1001",
    "customerId": "c-ada",
    "status": "placed",
    "createdAt": "2026-10-01T09:30:00Z",
    "items": [
        {"productId": "p-hammer", "quantity": 2, "priceCents": 1299},
        {"productId": "p-saege", "quantity": 1, "priceCents": 2499},
    ],
}


def test_load_products_reads_the_catalog() -> None:
    products = load_products(DATA / "products.json")
    assert products[0] == {"id": "p-hammer", "name": "Hammer", "priceCents": 1299, "stock": 12}
    assert any(product["name"] == "Säge" for product in products)


def test_save_order_creates_the_directory(tmp_path: Path) -> None:
    target = save_order(tmp_path / "orders", order)
    assert target == tmp_path / "orders" / "o-1001.json"
    assert '"customerId": "c-ada"' in target.read_text(encoding="utf-8")
    assert list((tmp_path / "orders").glob("*.tmp")) == []


def test_saved_orders_can_be_loaded_again(tmp_path: Path) -> None:
    save_order(tmp_path, {**order, "id": "o-1002"})
    save_order(tmp_path, order)
    assert [loaded["id"] for loaded in load_orders(tmp_path)] == ["o-1001", "o-1002"]
    assert load_orders(tmp_path)[0] == order


def test_load_orders_of_an_empty_directory(tmp_path: Path) -> None:
    assert load_orders(tmp_path) == []


def test_export_csv_writes_one_row_per_item(tmp_path: Path) -> None:
    path = tmp_path / "orders.csv"
    export_csv([order], path)
    with path.open(encoding="utf-8", newline="") as file:
        rows = list(csv.DictReader(file))
    assert len(rows) == 2
    assert rows[1] == {
        "orderId": "o-1001",
        "customerId": "c-ada",
        "productId": "p-saege",
        "quantity": "1",
        "priceCents": "2499",
    }
