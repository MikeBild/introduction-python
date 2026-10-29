import pytest

from ordering import (
    InsufficientStock,
    InvalidQuantity,
    OrderError,
    Product,
    UnknownProduct,
    handle_place_order,
    parse_quantity,
    place_order,
)

catalog = {
    "p-hammer": Product("p-hammer", 1299, 5),
    "p-saw": Product("p-saw", 2499, 1),
}


def test_parse_quantity_reads_positive_numbers() -> None:
    assert parse_quantity("3") == 3


@pytest.mark.parametrize("text", ["drei", "", "0", "-1"])
def test_parse_quantity_raises_invalid_quantity(text: str) -> None:
    with pytest.raises(InvalidQuantity):
        parse_quantity(text)


def test_parse_quantity_keeps_the_cause() -> None:
    with pytest.raises(InvalidQuantity) as info:
        parse_quantity("drei")
    assert isinstance(info.value.__cause__, ValueError)


def test_all_domain_errors_share_one_base_class() -> None:
    assert issubclass(InvalidQuantity, OrderError)
    assert issubclass(UnknownProduct, OrderError)
    assert issubclass(InsufficientStock, OrderError)


def test_place_order_returns_the_total() -> None:
    assert place_order({"p-hammer": 2, "p-saw": 1}, catalog) == 2 * 1299 + 2499


def test_place_order_rejects_unknown_products() -> None:
    with pytest.raises(UnknownProduct) as info:
        place_order({"p-drill": 1}, catalog)
    assert info.value.product_id == "p-drill"
    assert info.value.__cause__ is None


def test_place_order_rejects_more_than_the_stock() -> None:
    with pytest.raises(InsufficientStock) as info:
        place_order({"p-saw": 2}, catalog)
    assert (info.value.requested, info.value.available) == (2, 1)


def test_handle_place_order_maps_errors_to_status_codes() -> None:
    assert handle_place_order({"p-hammer": 1}, catalog) == (201, {"totalCents": 1299})
    assert handle_place_order({"p-drill": 1}, catalog)[0] == 404
    assert handle_place_order({"p-saw": 9}, catalog)[0] == 409


def test_handle_place_order_lets_bugs_through() -> None:
    broken_catalog = {"p-hammer": None}
    with pytest.raises(AttributeError):
        handle_place_order({"p-hammer": 1}, broken_catalog)  # type: ignore[arg-type]
