# Namen zeigen auf Werte, Werte haben Typen

**Lernziel:** Danach rechnest du Geldbeträge exakt in ganzen Cent und unterscheidest 0, None und leere Werte sicher.

**Aufgabe:** Schreib to_cents, das „12,34“ exakt in 1234 Cent umrechnet, format_cents für die Ausgabe und is_free, das 0 und None unterscheidet.

## Schritte

1. Öffne `start/money.py`.
2. Schreib `to_cents`: Leerzeichen entfernen, Komma durch Punkt ersetzen, mit `partition` in Euro und Cent teilen. Ungültige Eingaben lösen `ValueError` aus.
3. Schreib `format_cents` mit `divmod` und einem f-String.
4. Schreib `is_free` so, dass `0` gratis ist und `None` nicht.

Die Tests in `start/` sind zuerst übersprungen. Entferne die Zeile `pytestmark = pytest.mark.skip(...)`, sobald du mit der Übung beginnst.

## Prüfen

```bash
cd start
uv run pytest
uv run mypy --strict .
```

Eine mögliche Lösung steht in [`solution/`](solution/). Vom Hauptverzeichnis aus prüft `uv run python scripts/check.py 01` Startpunkt und Lösung dieser Übung.
