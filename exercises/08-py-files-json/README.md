# Dateien mit pathlib und with sicher lesen und schreiben

**Lernziel:** Danach liest und schreibst du Produkte und Bestellungen als JSON und CSV mit pathlib, with und expliziter Kodierung.

**Aufgabe:** Lies den Katalog aus data/products.json, speichere Bestellungen atomar als <id>.json und exportiere alle Positionen als CSV.

## Schritte

1. Lies in `load_products` die Datei mit `path.open(encoding="utf-8")` und `json.load`.
2. Schreib in `save_order` erst `<id>.tmp`, dann benenne mit `replace` um.
3. Lies in `load_orders` alle `*.json` sortiert ein.
4. Exportiere in `export_csv` eine Zeile je Position mit `csv.DictWriter` (Datei mit `newline=""` öffnen).

Die Tests in `start/` sind zuerst übersprungen. Entferne die Zeile `pytestmark = pytest.mark.skip(...)`, sobald du mit der Übung beginnst.

## Prüfen

```bash
cd start
uv run pytest
uv run mypy --strict .
```

Eine mögliche Lösung steht in [`solution/`](solution/). Vom Root aus prüft `uv run python scripts/check.py 08` Start und Lösung dieser Übung.
