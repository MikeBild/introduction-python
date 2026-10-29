# Funktionen mit klarer Signatur statt Flag-Parametern

**Lernziel:** Danach schreibst du Funktionen mit Defaults und Keyword-only-Argumenten und vermeidest geteilte Default-Listen.

**Aufgabe:** Mach den Rabatt in order_total zum Keyword-only-Argument, repariere die geteilte Default-Liste in add_item und schreib make_discount als Closure.

## Schritte

1. Mach `discount_percent` in `order_total` zum Keyword-only-Argument und summiere die Positionen.
2. Repariere `add_item`: `None` als Default, die übergebene Liste bleibt unverändert.
3. Schreib `make_discount` als Closure.

Die Tests in `start/` sind zuerst übersprungen. Entferne die Zeile `pytestmark = pytest.mark.skip(...)`, sobald du mit der Übung beginnst.

## Prüfen

```bash
cd start
uv run pytest
uv run mypy --strict .
```

Eine mögliche Lösung steht in [`solution/`](solution/). Vom Hauptverzeichnis aus prüft `uv run python scripts/check.py 02` Startpunkt und Lösung dieser Übung.
