from pathlib import Path

import pytest
from mypy import api

from pricing import CustomerId, Order, OrderId, ProductId, invoice_total

ada = CustomerId("c-ada")
orders: list[Order] = [
    {
        "id": OrderId("o-1"),
        "customerId": ada,
        "status": "placed",
        "items": [{"productId": ProductId("p-saege"), "quantity": 2, "priceCents": 2500}],
    },
]


def test_invoice_total_without_discount() -> None:
    assert invoice_total(orders, OrderId("o-1"), set()) == 5000


def test_invoice_total_gives_vip_customers_ten_percent() -> None:
    assert invoice_total(orders, OrderId("o-1"), {ada}) == 4500


def test_invoice_total_of_an_unknown_order() -> None:
    with pytest.raises(LookupError):
        invoice_total(orders, OrderId("o-404"), set())


def test_pricing_passes_mypy_strict() -> None:
    module = Path(__file__).with_name("pricing.py")
    stdout, stderr, status = api.run(["--strict", "--no-incremental", str(module)])
    assert status == 0, stdout + stderr
