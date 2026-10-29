import dataclasses

import pytest

from order import Order, OrderItem, Status

pytestmark = pytest.mark.skip(reason="Entferne diese Zeile, um die Tests zu aktivieren.")

hammer = OrderItem("p-hammer", 2, 1299)
saw = OrderItem("p-saw", 1, 2499)


def test_order_item_is_a_value() -> None:
    assert OrderItem("p-hammer", 2, 1299) == hammer
    assert hammer.total_cents == 2598
    with pytest.raises(dataclasses.FrozenInstanceError):
        hammer.quantity = 3  # type: ignore[misc, unused-ignore]


def test_order_item_rejects_quantity_below_one() -> None:
    with pytest.raises(ValueError):
        OrderItem("p-hammer", 0, 1299)


def test_new_order_starts_as_empty_draft() -> None:
    order = Order("o-1", "c-ada")
    assert order.status is Status.DRAFT
    assert order.items == []
    assert Order("o-2", "c-ada").items is not order.items


def test_total_sums_all_items() -> None:
    order = Order("o-1", "c-ada", [hammer, saw])
    assert order.total_cents == 2598 + 2499


def test_place_needs_at_least_one_item() -> None:
    with pytest.raises(ValueError):
        Order("o-1", "c-ada").place()


def test_placed_order_cannot_change_items() -> None:
    order = Order("o-1", "c-ada", [hammer])
    order.place()
    assert order.status == "placed"
    with pytest.raises(ValueError):
        order.add_item(saw)


def test_status_follows_placed_paid_shipped() -> None:
    order = Order("o-1", "c-ada", [hammer])
    order.place()
    order.advance()
    order.advance()
    assert order.status is Status.SHIPPED
    with pytest.raises(ValueError):
        order.advance()


def test_cancel_only_from_draft_or_placed() -> None:
    draft = Order("o-1", "c-ada")
    draft.cancel()
    assert draft.status is Status.CANCELLED

    paid = Order("o-2", "c-ada", [hammer])
    paid.place()
    paid.advance()
    with pytest.raises(ValueError):
        paid.cancel()
