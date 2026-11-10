"""Money in the workshop shop: always whole cents as int, never float."""


def to_cents(euros: str) -> int:
    """Converts "12,34" or "12.34" into 1234 cents."""
    # TODO: Strip whitespace, replace the comma with a dot, split with partition(".").
    # TODO: Reject invalid input ("", "abc", "1,234", "-3") with ValueError.
    # Tip: float("12.34") * 100 gives 1233.9999999999998 – calculate with int.
    raise NotImplementedError


def format_cents(cents: int) -> str:
    """Formats 1234 as "12,34 €" and 123456 as "1.234,56 €"."""
    # TODO: divmod(abs(cents), 100) and an f-string with {rest:02d}
    # Tip: f"{123456:_}" gives "123_456" – that becomes the thousands separator.
    raise NotImplementedError


def is_free(price_cents: int | None) -> bool:
    """None means: price unknown. That is not the same as free."""
    # TODO: Careful, `not price_cents` is also true for None.
    raise NotImplementedError
