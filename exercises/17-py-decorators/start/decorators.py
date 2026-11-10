"""Cross-cutting behavior as decorators: measure, retry, cache."""

import functools
import time
from collections.abc import Callable


def timed[**P, R](log: Callable[[str], None]) -> Callable[[Callable[P, R]], Callable[P, R]]:
    """Decorator with an argument: reports the duration of every call to log – even when func raises."""

    def decorator(func: Callable[P, R]) -> Callable[P, R]:
        # TODO: @functools.wraps(func) is missing – without it the function is called "wrapper" afterwards
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            start = time.perf_counter()
            result = func(*args, **kwargs)  # TODO: try/finally so that errors are logged too
            log(f"{func.__name__} took {time.perf_counter() - start:.3f}s")
            return result

        return wrapper

    return decorator


def retry[**P, R](
    times: int, *, on: tuple[type[Exception], ...] = (ConnectionError,)
) -> Callable[[Callable[P, R]], Callable[P, R]]:
    """Retries up to times times on the exceptions in on; others propagate immediately."""
    # TODO: build like timed: decorator → wrapper with a for loop and try/except on
    raise NotImplementedError


# TODO: cache the result per country – with a decorator from functools
def shipping_cents(country: str) -> int:
    """Expensive calculation, result per country only once."""
    return {"DE": 490, "AT": 990, "CH": 1490}.get(country, 2490)
