# Welche Exception fängst du, welche nicht?

**Lernziel:** Danach baust du eine eigene Exception-Hierarchie für fachliche Fehler und fängst nur, was du sinnvoll behandeln kannst.

**Aufgabe:** Wirf in place_order UnknownProduct und InsufficientStock, bewahr in parse_quantity die Ursache mit raise from und übersetz Fehler in Status Codes.

## Schritte

1. Gib `UnknownProduct` und `InsufficientStock` eine lesbare Meldung.
2. Wirf in `parse_quantity` bei ungültigem Text `InvalidQuantity(text) from error`.
3. Wirf in `place_order` `UnknownProduct` (mit `from None`) und `InsufficientStock`.
4. Übersetz in `handle_place_order` Fehler in Status Codes. Fang nur `OrderError` und Unterklassen.

Die Tests in `start/` sind zuerst übersprungen. Entferne die Zeile `pytestmark = pytest.mark.skip(...)`, sobald du mit der Übung beginnst.

## Prüfen

```bash
cd start
uv run pytest
uv run mypy --strict .
```

Eine mögliche Lösung steht in [`solution/`](solution/). Vom Root aus prüft `uv run python scripts/check.py 07` Start und Lösung dieser Übung.
