# Welche Collection passt zu deinen Daten?

**Lernziel:** Danach wählst du für Produkte und Bestellungen list, tuple, dict, set oder Counter passend zum Zugriff.

**Aufgabe:** Bau einen Index der Produkte per ID, finde knappe Produkte, sammle Kunden-IDs ohne Duplikate und zähl Mengen je Produkt mit Counter.

## Schritte

1. Bau mit `index_by_id` ein dict von der Produkt-ID auf das Produkt.
2. Liefere mit `low_stock` die Namen knapper Produkte alphabetisch sortiert.
3. Sammle mit `customer_ids` jede Kunden-ID genau einmal.
4. Zähl mit `quantities_by_product` und `Counter` die bestellten Mengen.
5. Gib mit `price_list` ein `frozendict` zurück (eingebaut seit Python 3.15).

Die Tests in `start/` sind zuerst übersprungen. Entferne die Zeile `pytestmark = pytest.mark.skip(...)`, sobald du mit der Übung beginnst.

## Prüfen

```bash
cd start
uv run pytest
uv run mypy --strict .
```

Eine mögliche Lösung steht in [`solution/`](solution/). Vom Hauptverzeichnis aus prüft `uv run python scripts/check.py 03` Startpunkt und Lösung dieser Übung.
