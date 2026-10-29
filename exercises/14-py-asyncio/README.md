# Mit asyncio warten, ohne zu blockieren

**Lernziel:** Danach fragst du mit asyncio mehrere Dienste gleichzeitig ab, begrenzt Dauer und Parallelität und behandelst Fehler aus TaskGroups.

**Aufgabe:** Frag in stock_for den Bestand aller Produkte gleichzeitig mit TaskGroup und asyncio.timeout ab und begrenz in stock_limited die Parallelität mit Semaphore.

## Schritte

1. Schreib `stock_for` mit `asyncio.timeout` und `asyncio.TaskGroup`.
2. Schreib `stock_limited` mit `asyncio.Semaphore`.
3. Die Tests rufen `asyncio.run` auf, ein Zusatzpaket brauchst du nicht.

Die Tests in `start/` sind zuerst übersprungen. Entferne die Zeile `pytestmark = pytest.mark.skip(...)`, sobald du mit der Übung beginnst.

## Prüfen

```bash
cd start
uv run pytest
uv run mypy --strict .
```

Eine mögliche Lösung steht in [`solution/`](solution/). Vom Hauptverzeichnis aus prüft `uv run python scripts/check.py 14` Startpunkt und Lösung dieser Übung.
