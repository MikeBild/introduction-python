# Eine HTTP API mit Flask für den Werkstatt-Shop

**Lernziel:** Danach baust du mit Flask 3 eine HTTP API mit App Factory, geprüftem JSON-Body, Error Handlern und Tests per Test Client.

**Aufgabe:** Ergänze GET /orders/<order_id> und POST /orders mit 201 und Location, übersetz Fehler per Error Handler in 400, 409 und 422 und lass die Tests grün werden.

## Schritte

1. Starte die App mit `uv run flask --app app run --debug` und ruf `http://127.0.0.1:5000/products` auf.
2. Ergänze `GET /orders/<order_id>` mit 404 für unbekannte Bestellungen.
3. Ergänze `POST /orders`: Body mit `parse_place_order` prüfen, bestellen, 201 mit `Location` zurückgeben.
4. Übersetz Fehler mit `@app.errorhandler` in 400, 409, 422 und JSON für unbekannte Routes.

Die Tests in `start/` sind zuerst übersprungen. Entferne die Zeile `pytestmark = pytest.mark.skip(...)`, sobald du mit der Übung beginnst.

## Prüfen

```bash
cd start
uv run pytest
uv run mypy --strict .
```

Eine mögliche Lösung steht in [`solution/`](solution/). Vom Hauptverzeichnis aus prüft `uv run python scripts/check.py 11` Startpunkt und Lösung dieser Übung.
