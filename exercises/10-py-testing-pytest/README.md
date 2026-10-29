# Mit pytest Verhalten prüfen statt Details

**Lernziel:** Danach schreibst du pytest-Tests mit assert, Fixtures, parametrize, pytest.raises und tmp_path für Code mit fester Zeit.

**Aufgabe:** Schreib Tests für place_order mit den Fixtures aus conftest.py, einen parametrisierten Test für drei Fehlerfälle und einen Test für den Beleg mit tmp_path.

## Schritte

1. Lies `shop.py` und die Fixtures in `conftest.py`. Der Code ist fertig, du schreibst nur Tests. Geld rechnet er in ganzen Cent als `int`, erst `format_cents` macht daraus „1.234,56 €“.
2. Ergänze in `test_shop.py` die Prüfungen für Summe, ID und Zeitpunkt.
3. Schreib einen Test mit `@pytest.mark.parametrize` für drei Fehlerfälle und `pytest.raises`.
4. Prüf den Beleg mit `tmp_path` vollständig.

Die Tests in `start/` sind zuerst übersprungen. Entferne die Zeile `pytestmark = pytest.mark.skip(...)`, sobald du mit der Übung beginnst.

## Prüfen

```bash
cd start
uv run pytest
uv run mypy --strict .
```

Eine mögliche Lösung steht in [`solution/`](solution/). Vom Hauptverzeichnis aus prüft `uv run python scripts/check.py 10` Startpunkt und Lösung dieser Übung.
