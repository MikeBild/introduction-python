# Bestellungen mit pandas auswerten statt mit Schleifen

**Lernziel:** Danach flachst du verschachtelte Bestellungen mit pandas ab und berechnest Umsatz je Produkt, Monat und Kunde mit groupby.

**Aufgabe:** Berechne in analysis.py revenueCents vektorisiert, filtere stornierte Bestellungen und werte Umsatz je Produkt, je Monat und je Kunde mit groupby aus.

## Schritte

1. Ergänze in `load_items` die Spalte `revenueCents`, vektorisiert ohne Schleife.
2. Filtere in `completed` stornierte Bestellungen und Entwürfe mit einer Boolean-Maske.
3. Schreib `revenue_by_product`, `revenue_by_month` und `customer_summary` mit `groupby`.

Die Tests in `start/` sind zuerst übersprungen. Entferne die Zeile `pytestmark = pytest.mark.skip(...)`, sobald du mit der Übung beginnst.

## Prüfen

```bash
cd start
uv run pytest
uv run mypy --strict .
```

Eine mögliche Lösung steht in [`solution/`](solution/). Vom Hauptverzeichnis aus prüft `uv run python scripts/check.py 12` Startpunkt und Lösung dieser Übung.
