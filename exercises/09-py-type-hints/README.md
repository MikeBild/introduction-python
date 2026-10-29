# Typ-Hinweise prüft mypy, nicht Python

**Lernziel:** Danach annotierst du ein Modul mit NewType, Literal, TypedDict und X | None, sodass mypy --strict es ohne Fehler prüft.

**Aufgabe:** Annotier pricing.py mit NewType-IDs, Literal und TypedDict, bis uv run mypy --strict sauber ist, und behebe den Bug, den mypy dabei findet.

## Schritte

1. Führ `uv run mypy --strict pricing.py` in `start/` aus und lies die Meldungen.
2. Leg `OrderId`, `CustomerId` und `ProductId` als `NewType` an, den Status als `Literal`, `OrderItem` und `Order` als `TypedDict`.
3. Annotier alle Funktionen. `find_order` gibt `Order | None` zurück.
4. Behebe den Fehler in `invoice_total`, den mypy jetzt meldet, und pass die Tests an die NewTypes an.

Die Tests in `start/` sind zuerst übersprungen. Entferne die Zeile `pytestmark = pytest.mark.skip(...)`, sobald du mit der Übung beginnst.

## Prüfen

```bash
cd start
uv run pytest
uv run mypy --strict .
```

Eine mögliche Lösung steht in [`solution/`](solution/). Vom Root aus prüft `uv run python scripts/check.py 09` Start und Lösung dieser Übung.
