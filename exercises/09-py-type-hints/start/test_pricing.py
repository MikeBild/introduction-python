from pathlib import Path

import pytest
from mypy import api

from pricing import invoice_total

pytestmark = pytest.mark.skip(reason="Entferne diese Zeile, um die Tests zu aktivieren.")

# TODO: Sobald pricing.py NewTypes hat, erzeuge die IDs mit OrderId("o-1"), CustomerId("c-ada") …
orders = [
    {
        "id": "o-1",
        "customerId": "c-ada",
        "status": "placed",
        "items": [{"productId": "p-saege", "quantity": 2, "priceCents": 2500}],
    },
]


def test_invoice_total_without_discount() -> None:
    assert invoice_total(orders, "o-1", set()) == 5000


def test_invoice_total_gives_vip_customers_ten_percent() -> None:
    assert invoice_total(orders, "o-1", {"c-ada"}) == 4500


def test_invoice_total_of_an_unknown_order() -> None:
    with pytest.raises(LookupError):
        invoice_total(orders, "o-404", set())


def test_pricing_passes_mypy_strict() -> None:
    module = Path(__file__).with_name("pricing.py")
    stdout, stderr, status = api.run(["--strict", "--no-incremental", str(module)])
    assert status == 0, stdout + stderr
