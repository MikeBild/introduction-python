import json
from collections.abc import Iterator
from pathlib import Path

import pytest

from stream import first_paid, in_batches, read_orders, running_total, totals, with_status

ORDERS = [
    {"id": f"o-{n}", "status": status, "items": [{"productId": "p-hammer", "quantity": n, "priceCents": 100}]}
    for n, status in enumerate(["paid", "cancelled", "paid", "shipped", "paid"], start=1)
]


@pytest.fixture
def orders_file(tmp_path: Path) -> Path:
    path = tmp_path / "orders.jsonl"
    path.write_text("".join(json.dumps(order) + "\n" for order in ORDERS) + "\n", encoding="utf-8")
    return path


def test_read_orders_is_lazy(orders_file: Path) -> None:
    orders = read_orders(orders_file)
    assert isinstance(orders, Iterator)
    assert next(orders)["id"] == "o-1"
    assert len(list(orders)) == 4


def test_generators_chain_to_a_pipeline(orders_file: Path) -> None:
    pipeline = running_total(totals(with_status(read_orders(orders_file), "paid", "shipped")))
    assert list(pipeline) == [100, 400, 800, 1300]


def test_in_batches(orders_file: Path) -> None:
    assert list(in_batches(read_orders(orders_file), 2)) == [["o-1", "o-2"], ["o-3", "o-4"], ["o-5"]]


def test_a_generator_is_exhausted_after_one_pass() -> None:
    paid = with_status(ORDERS, "paid")
    assert len(list(paid)) == 3
    assert list(paid) == []


def test_first_paid_stops_reading_early(tmp_path: Path) -> None:
    path = tmp_path / "orders.jsonl"
    path.write_text(json.dumps(ORDERS[0]) + "\n" + "kein JSON\n", encoding="utf-8")
    assert first_paid(path, 1) == ["o-1"]


def test_works_with_the_shared_sample_data() -> None:
    path = Path(__file__).resolve().parents[3] / "data" / "orders.jsonl"
    assert len(first_paid(path, 3)) == 3
