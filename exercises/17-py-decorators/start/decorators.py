"""Querschnittsverhalten als Decorator: messen, wiederholen, zwischenspeichern."""

import functools
import time
from collections.abc import Callable


def timed[**P, R](log: Callable[[str], None]) -> Callable[[Callable[P, R]], Callable[P, R]]:
    """Decorator mit Argument: meldet die Dauer jedes Aufrufs an log – auch wenn func wirft."""

    def decorator(func: Callable[P, R]) -> Callable[P, R]:
        # TODO: @functools.wraps(func) fehlt – ohne heißt die Funktion danach "wrapper"
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            start = time.perf_counter()
            result = func(*args, **kwargs)  # TODO: try/finally, damit auch Fehler geloggt werden
            log(f"{func.__name__} took {time.perf_counter() - start:.3f}s")
            return result

        return wrapper

    return decorator


def retry[**P, R](
    times: int, *, on: tuple[type[Exception], ...] = (ConnectionError,)
) -> Callable[[Callable[P, R]], Callable[P, R]]:
    """Wiederholt bis zu times-mal bei den Exceptions aus on; andere fliegen sofort weiter."""
    # TODO: wie timed aufbauen: decorator → wrapper mit for-Schleife und try/except on
    raise NotImplementedError


# TODO: Ergebnis je Land zwischenspeichern – mit einem Decorator aus functools
def shipping_cents(country: str) -> int:
    """Teure Berechnung, Ergebnis je Land nur einmal."""
    return {"DE": 490, "AT": 990, "CH": 1490}.get(country, 2490)
