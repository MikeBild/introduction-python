import pytest

from decorators import retry, shipping_cents, timed


def test_timed_logs_and_keeps_the_function_identity() -> None:
    messages: list[str] = []

    @timed(messages.append)
    def place_order(customer_id: str) -> str:
        """Gibt eine Bestell-ID zurück."""
        return f"o-for-{customer_id}"

    assert place_order("c-ada") == "o-for-c-ada"
    assert len(messages) == 1
    assert messages[0].startswith("place_order took ")
    assert place_order.__name__ == "place_order"
    assert place_order.__doc__ == "Gibt eine Bestell-ID zurück."


def test_timed_logs_even_when_the_function_fails() -> None:
    messages: list[str] = []

    @timed(messages.append)
    def broken() -> None:
        raise RuntimeError("boom")

    with pytest.raises(RuntimeError):
        broken()
    assert len(messages) == 1


def test_retry_tries_again_on_connection_errors() -> None:
    calls = 0

    @retry(3)
    def flaky() -> int:
        nonlocal calls
        calls += 1
        if calls < 3:
            raise ConnectionError("warehouse offline")
        return 12

    assert flaky() == 12
    assert calls == 3


def test_retry_gives_up_after_the_last_attempt() -> None:
    calls = 0

    @retry(2)
    def offline() -> int:
        nonlocal calls
        calls += 1
        raise ConnectionError("warehouse offline")

    with pytest.raises(ConnectionError):
        offline()
    assert calls == 2


def test_retry_does_not_hide_other_errors() -> None:
    calls = 0

    @retry(3)
    def buggy() -> int:
        nonlocal calls
        calls += 1
        raise KeyError("p-unbekannt")

    with pytest.raises(KeyError):
        buggy()
    assert calls == 1


def test_shipping_cents_is_cached() -> None:
    shipping_cents.cache_clear()
    assert shipping_cents("DE") == 490
    assert shipping_cents("DE") == 490
    assert shipping_cents.cache_info().hits == 1
