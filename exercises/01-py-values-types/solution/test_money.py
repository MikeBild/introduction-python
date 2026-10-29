import pytest

from money import format_cents, is_free, to_cents


@pytest.mark.parametrize(
    ("text", "cents"),
    [("12,34", 1234), ("12.34", 1234), ("7", 700), ("0,5", 50), (" 3,99 ", 399)],
)
def test_to_cents_reads_euro_amounts(text: str, cents: int) -> None:
    assert to_cents(text) == cents


@pytest.mark.parametrize("text", ["", "abc", "1,234", "-3", "1,2a"])
def test_to_cents_rejects_invalid_amounts(text: str) -> None:
    with pytest.raises(ValueError):
        to_cents(text)


def test_to_cents_avoids_float_rounding() -> None:
    assert to_cents("0,10") + to_cents("0,20") == to_cents("0,30")


def test_format_cents_formats_euros() -> None:
    assert format_cents(1234) == "12,34 €"
    assert format_cents(5) == "0,05 €"
    assert format_cents(-250) == "-2,50 €"


def test_is_free_distinguishes_zero_and_none() -> None:
    assert is_free(0)
    assert not is_free(None)
    assert not is_free(199)
