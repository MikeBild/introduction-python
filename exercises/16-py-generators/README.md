# Generatoren liefern Werte erst auf Nachfrage

**Lernziel:** Danach verarbeitest du große Bestelldateien mit Generatoren, itertools.batched und islice in konstantem Speicher.

**Aufgabe:** Mach aus read_orders und with_status Generatoren, ergänz totals und running_total mit yield und teil Bestellungen mit itertools.batched in Pakete.

## Schritte

1. Mach aus `read_orders` und `with_status` Generatoren.
2. Schreib `totals` und `running_total` mit `yield`.
3. Nutze `itertools.batched` in `in_batches` und `itertools.islice` in `first_paid`.

Die Tests in `start/` sind zuerst übersprungen. Entferne die Zeile `pytestmark = pytest.mark.skip(...)`, sobald du mit der Übung beginnst.

## Prüfen

```bash
cd start
uv run pytest
uv run mypy --strict .
```

Eine mögliche Lösung steht in [`solution/`](solution/). Vom Hauptverzeichnis aus prüft `uv run python scripts/check.py 16` Startpunkt und Lösung dieser Übung.
