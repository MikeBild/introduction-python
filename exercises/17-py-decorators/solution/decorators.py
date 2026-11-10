"""Cross-cutting behavior as decorators: measure, retry, cache."""

import functools
import time
from collections.abc import Callable


def timed[**P, R](log: Callable[[str], None]) -> Callable[[Callable[P, R]], Callable[P, R]]:
    """Decorator with an argument: reports the duration of every call to log."""

    def decorator(func: Callable[P, R]) -> Callable[P, R]:
        @functools.wraps(func)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            start = time.perf_counter()
            try:
                return func(*args, **kwargs)
            finally:
                log(f"{func.__name__} took {time.perf_counter() - start:.3f}s")

        return wrapper

    return decorator


def retry[**P, R](
    times: int, *, on: tuple[type[Exception], ...] = (ConnectionError,)
) -> Callable[[Callable[P, R]], Callable[P, R]]:
    """Retries on the given exceptions; others propagate immediately."""

    def decorator(func: Callable[P, R]) -> Callable[P, R]:
        @functools.wraps(func)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            for attempt in range(1, times + 1):
                try:
                    return func(*args, **kwargs)
                except on:
                    if attempt == times:
                        raise
            raise AssertionError("unreachable")

        return wrapper

    return decorator


@functools.cache
def shipping_cents(country: str) -> int:
    """Expensive calculation, result per country only once."""
    return {"DE": 490, "AT": 990, "CH": 1490}.get(country, 2490)
