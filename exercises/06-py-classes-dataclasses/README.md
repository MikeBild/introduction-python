# Dataclasses statt Klassen voller Boilerplate

**Lernziel:** Danach modellierst du Bestellung und Position als Dataclasses mit StrEnum-Status und Methoden, die Regeln prüfen.

**Aufgabe:** Mach aus OrderItem eine frozen Dataclass und aus Order eine Dataclass mit Statusregeln für place, advance und cancel.

## Schritte

1. Mach aus `OrderItem` eine `@dataclass(frozen=True, slots=True)` und lösch `__init__`, `__eq__` und `__repr__`.
2. Prüf in `__post_init__`, dass `quantity` mindestens 1 ist, und ergänze die Property `total_cents`.
3. Mach aus `Order` eine Dataclass mit `field(default_factory=list)` und schreib `place`, `advance` und `cancel` nach den Regeln aus `docs/beispiel-domaene.md`.

Die Tests in `start/` sind zuerst übersprungen. Entferne die Zeile `pytestmark = pytest.mark.skip(...)`, sobald du mit der Übung beginnst.

## Prüfen

```bash
cd start
uv run pytest
uv run mypy --strict .
```

Eine mögliche Lösung steht in [`solution/`](solution/). Vom Hauptverzeichnis aus prüft `uv run python scripts/check.py 06` Startpunkt und Lösung dieser Übung.
