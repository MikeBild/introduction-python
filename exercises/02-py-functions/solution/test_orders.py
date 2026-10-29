import pytest

from orders import Item, add_item, line_total, make_discount, order_total

hammer: Item = ("p-hammer", 2, 1299)
saw: Item = ("p-saw", 1, 2499)


def test_line_total_multiplies_quantity_and_price() -> None:
    assert line_total(3, 250) == 750


def test_order_total_sums_all_items() -> None:
    assert order_total([hammer, saw]) == 2 * 1299 + 2499
    assert order_total([]) == 0


def test_order_total_takes_discount_only_as_keyword() -> None:
    assert order_total([saw], discount_percent=10) == 2250
    with pytest.raises(TypeError):
        order_total([saw], 10)  # type: ignore[misc, unused-ignore]


def test_add_item_does_not_share_a_default_list() -> None:
    first = add_item(hammer)
    second = add_item(saw)
    assert first == [hammer]
    assert second == [saw]


def test_add_item_keeps_the_given_list_unchanged() -> None:
    items = [hammer]
    assert add_item(saw, items) == [hammer, saw]
    assert items == [hammer]


def test_make_discount_remembers_the_percent() -> None:
    ten_percent_off = make_discount(10)
    assert ten_percent_off(2000) == 1800
    assert make_discount(0)(2000) == 2000
