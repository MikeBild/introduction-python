# Ein Paket bauen, das andere installieren können

**Lernziel:** Danach baust du mit uv build ein typisiertes Wheel mit Metadaten und Befehl und prüfst es, bevor du es veröffentlichst.

**Aufgabe:** Ergänz in pyproject.toml Version, Beschreibung, Lizenz und den Befehl werkstatt-money, leg py.typed an und prüf das Wheel mit den Tests.

## Schritte

1. Wechsle nach `start/` und führ `uv sync` aus. Diese Übung ist ein eigenes uv-Projekt.
2. Ergänz in `pyproject.toml` Version `1.0.0`, `description`, `readme`, `license = "MIT"` und den Befehl `werkstatt-money`.
3. Leg die leere Datei `src/werkstatt_money/py.typed` an.
4. Bau mit `uv build` und probier `uvx --from ./dist/werkstatt_money-1.0.0-py3-none-any.whl werkstatt-money 12,34`.

Die Tests in `start/` sind zuerst übersprungen. Entferne die Zeile `pytestmark = pytest.mark.skip(...)`, sobald du mit der Übung beginnst.

## Prüfen

```bash
cd start
uv sync
uv run pytest
uv run mypy --strict src tests
```

Eine mögliche Lösung steht in [`solution/`](solution/). Vom Root aus prüft `uv run python scripts/check.py 15` Start und Lösung dieser Übung.
