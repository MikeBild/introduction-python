# Decorators fügen Verhalten hinzu, ohne Code zu ändern

**Lernziel:** Danach schreibst du typisierte Decorators mit Argumenten für Zeitmessung und Retry und nutzt functools.cache gezielt.

**Aufgabe:** Repariere timed mit functools.wraps und try/finally, schreib retry für ConnectionError und speichere shipping_cents mit functools.cache zwischen.

## Schritte

1. Ergänze in `timed` `@functools.wraps(func)` und `try`/`finally`.
2. Schreib `retry` nach demselben Muster. Andere Exceptions als die aus `on` fliegen sofort weiter.
3. Speichere `shipping_cents` mit `@functools.cache` zwischen und lösch im Test die `type: ignore`-Kommentare.

Die Tests in `start/` sind zuerst übersprungen. Entferne die Zeile `pytestmark = pytest.mark.skip(...)`, sobald du mit der Übung beginnst.

## Prüfen

```bash
cd start
uv run pytest
uv run mypy --strict .
```

Eine mögliche Lösung steht in [`solution/`](solution/). Vom Hauptverzeichnis aus prüft `uv run python scripts/check.py 17` Startpunkt und Lösung dieser Übung.
