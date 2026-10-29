# Comprehensions statt Schleifen mit append

**Lernziel:** Danach schreibst du Auswertungen über Bestellungen als List-, Dict- und Set-Comprehensions und Generator Expressions.

**Aufgabe:** Ersetz in reports.py jede Schleife mit append durch eine Comprehension und sortier die größten Bestellungen mit sorted und key.

## Schritte

1. Ersetz in `order_total` und `totals_by_order` die Schleifen durch `sum(...)` und eine Dict Comprehension.
2. Schreib `open_order_ids`, `products_sold` und `all_items` als Comprehensions.
3. Sortier in `top_orders` mit `sorted`, `key` und `reverse=True`.

Die Tests in `start/` sind zuerst übersprungen. Entferne die Zeile `pytestmark = pytest.mark.skip(...)`, sobald du mit der Übung beginnst.

## Prüfen

```bash
cd start
uv run pytest
uv run mypy --strict .
```

Eine mögliche Lösung steht in [`solution/`](solution/). Vom Hauptverzeichnis aus prüft `uv run python scripts/check.py 04` Startpunkt und Lösung dieser Übung.
