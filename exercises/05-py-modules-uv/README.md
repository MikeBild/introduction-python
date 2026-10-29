# Ein Projekt mit uv statt pip und venv von Hand

**Lernziel:** Danach legst du mit uv ein Paket im src-Layout an, teilst Code in Module und startest ihn als eigenen Befehl.

**Aufgabe:** Teil cli.py in die Module money und orders auf, trag den Befehl werkstatt in pyproject.toml ein und starte ihn mit uv run werkstatt 2x1299.

## Schritte

1. Wechsle nach `start/` und führ `uv sync` aus. Diese Übung ist ein eigenes uv-Projekt mit eigener `.venv`.
2. Teil `src/werkstatt/cli.py` in die Module `money.py` und `orders.py` auf und importiere sie absolut (`from werkstatt.money import format_cents`).
3. Pass `src/werkstatt/__init__.py` an, damit es die Funktionen aus den neuen Modulen exportiert.
4. Trag den Befehl `werkstatt = "werkstatt.cli:main"` unter `[project.scripts]` ein, führ `uv sync` aus und starte `uv run werkstatt 2x1299 1x2499`.

Die Tests in `start/` sind zuerst übersprungen. Entferne die Zeile `pytestmark = pytest.mark.skip(...)`, sobald du mit der Übung beginnst.

## Prüfen

```bash
cd start
uv sync
uv run pytest
uv run mypy --strict src tests
```

Eine mögliche Lösung steht in [`solution/`](solution/). Vom Hauptverzeichnis aus prüft `uv run python scripts/check.py 05` Startpunkt und Lösung dieser Übung.
