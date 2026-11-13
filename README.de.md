*[English](README.md) · Deutsch*

# Übungen: Python

Übungs-Repo zum Workshop „Python für Entwickler mit uv, pytest und Flask“. Zu jeder der 17 Lektionen gibt es eine Übung mit Startpunkt, Tests und Lösung. Alle Übungen spielen im Werkstatt-Shop mit Produkten und Bestellungen.

## Was du lernst

- Werte, Funktionen, Collections und Dataclasses mit Type Hints nutzen
- Fehler gezielt behandeln, Dateien lesen und mit pytest und mypy prüfen
- Projekte mit uv anlegen und mit Flask 3 eine HTTP-API bauen

## Voraussetzungen

- **uv** – verwaltet Python-Versionen, Umgebungen und Pakete ([Installation](https://docs.astral.sh/uv/getting-started/installation/)). Prüfen mit `uv --version`.
- **Python 3.15** – `uv sync` liest die Version aus [`.python-version`](.python-version) und installiert sie bei Bedarf.

## Einrichten

```bash
git clone https://github.com/MikeBild/introduction-python.git
cd introduction-python
uv sync                          # installiert Python 3.15 aus .python-version, falls nötig
uv run python scripts/check.py   # pytest und mypy --strict für alle Übungen
```

## So arbeitest du mit einer Übung

```text
exercises/
  01-py-values-types/
    README.md          Aufgabe, Schritte, Prüfen
    start/             dein Startpunkt mit TODO-Kommentaren
      money.py
      test_money.py    Tests mit pytestmark = skip – entferne die Zeile, um sie zu aktivieren
    solution/          eine mögliche Lösung, gleiche Struktur
data/                  Beispieldaten: products.json, orders.json, orders.jsonl
docs/                  die Domäne des Werkstatt-Shops
scripts/check.py       prüft Startpunkt und Lösung aller Übungen
```

1. Lies das `README.md` der Übung und öffne den Startpunkt in `start/`.
2. Entferne in der Testdatei die Zeile `pytestmark = pytest.mark.skip(...)` und bearbeite die TODOs, bis pytest und mypy grün sind.
3. Vergleiche danach mit `solution/`.

```bash
cd exercises/04-py-comprehensions/start
uv run pytest            # Tests dieser Übung
uv run mypy --strict .   # Typprüfung
```

Alle Übungen teilen sich eine `pyproject.toml` und eine `.venv` im Hauptverzeichnis. Ausnahmen sind 05 und 15: Dort lernst du, ein eigenes Paket anzulegen, deshalb hat die Übung ihr eigenes uv-Projekt.

Vom Hauptverzeichnis aus:

| Befehl | Was es tut |
| --- | --- |
| `uv run python scripts/check.py` | pytest und mypy für alle Startpunkte und Lösungen |
| `uv run python scripts/check.py 04 11` | nur die Übungen 04 und 11 |
| `uv run python scripts/check.py --solution` | nur die Lösungen |

## Übungen

| Nr. | Lektion | Übung |
| --- | --- | --- |
| 01 | Namen zeigen auf Werte, Werte haben Typen | [01-py-values-types](exercises/01-py-values-types/README.de.md) |
| 02 | Funktionen mit klarer Signatur statt Flag-Parametern | [02-py-functions](exercises/02-py-functions/README.de.md) |
| 03 | Welche Collection passt zu deinen Daten? | [03-py-collections](exercises/03-py-collections/README.de.md) |
| 04 | Comprehensions statt Schleifen mit append | [04-py-comprehensions](exercises/04-py-comprehensions/README.de.md) |
| 05 | Ein Projekt mit uv statt pip und venv von Hand | [05-py-modules-uv](exercises/05-py-modules-uv/README.de.md) |
| 06 | Dataclasses statt Klassen voller Boilerplate | [06-py-classes-dataclasses](exercises/06-py-classes-dataclasses/README.de.md) |
| 07 | Welche Exception fängst du, welche nicht? | [07-py-errors](exercises/07-py-errors/README.de.md) |
| 08 | Dateien mit pathlib und with sicher lesen und schreiben | [08-py-files-json](exercises/08-py-files-json/README.de.md) |
| 09 | Type Hints prüft mypy, nicht Python | [09-py-type-hints](exercises/09-py-type-hints/README.de.md) |
| 10 | Mit pytest Behavior prüfen statt Details | [10-py-testing-pytest](exercises/10-py-testing-pytest/README.de.md) |
| 11 | Eine HTTP-API mit Flask für den Werkstatt-Shop | [11-py-http-api-flask](exercises/11-py-http-api-flask/README.de.md) |

### Zusatzkapitel

| Nr. | Lektion | Übung |
| --- | --- | --- |
| 12 | Bestellungen mit pandas auswerten statt mit Schleifen | [12-py-pandas-orders](exercises/12-py-pandas-orders/README.de.md) |
| 13 | Im Notebook erkunden, im Modul festhalten | [13-py-jupyter](exercises/13-py-jupyter/README.de.md) |
| 14 | Mit asyncio warten, ohne zu blockieren | [14-py-asyncio](exercises/14-py-asyncio/README.de.md) |
| 15 | Ein Paket bauen, das andere installieren können | [15-py-packaging](exercises/15-py-packaging/README.de.md) |
| 16 | Generatoren liefern Werte erst auf Nachfrage | [16-py-generators](exercises/16-py-generators/README.de.md) |
| 17 | Decorators fügen Verhalten hinzu, ohne Code zu ändern | [17-py-decorators](exercises/17-py-decorators/README.de.md) |

## Der Werkstatt-Shop

Eine Bestellung besteht aus Positionen mit `productId`, `quantity` und `priceCents`. Geld steht immer in ganzen Cent. Die ganze Domäne beschreibt [`docs/beispiel-domaene.de.md`](docs/beispiel-domaene.de.md).

## Stack und Pakete

**Stack (Oktober 2026):** Python 3.15 · uv als einziges Tool für Python-Versionen, Umgebungen und Pakete · pytest · Type Hints mit mypy `--strict` · Flask 3 · pandas 3 und JupyterLab für die Datenanalyse

Bewusst wenige Pakete:

| Paket | Wofür | Warum dieses |
| --- | --- | --- |
| `flask` | HTTP-API | Routing, JSON und Test Client in einem Paket; FastAPI bräuchte zusätzlich Starlette, Pydantic, einen ASGI-Server und httpx für Tests |
| `pytest` | Tests | Tests als einfache Funktionen mit `assert`, Fixtures und `parametrize` |
| `mypy` | Typprüfung | läuft als Python-Paket direkt mit uv, ohne zusätzliche Laufzeit |
| `pandas`, `pandas-stubs`, `jupyterlab` | Zusatzkapitel Datenanalyse | Gruppe `data`, nur für die Übungen 12 und 13 |

Für asyncio, Dateien, JSON, CSV, Generatoren und Decorators reicht die Standardbibliothek.

## Workshop und Folien

- Workshop: [„Python für Entwickler mit uv, pytest und Flask“](https://workshops.mikebild.dev/w/python/remote/)
- Folien: [slides.mikebild.dev/introduction-python](https://slides.mikebild.dev/introduction-python.html)
- PDF: [introduction-python.pdf](https://media.mikebild.dev/site/mikebild/decks/introduction-python/introduction-python.pdf)
- Video: [introduction-python.mp4](https://media.mikebild.dev/site/mikebild/decks/introduction-python/introduction-python.mp4)
- Beiträge auf mikebild.dev:
  - [Fortgeschrittenes Python: Decorators, Magic Methods und Generatoren](https://www.mikebild.dev/de/blog/python-advanced-decorators-generatoren/)
  - [Funktionale Muster in Python: Comprehensions, itertools und functools](https://www.mikebild.dev/de/blog/funktionale-muster-in-python/)
  - [Web-APIs mit Flask: von der App zur JSON-API](https://www.mikebild.dev/de/blog/web-apis-mit-flask/)
  - [Flask-Apps testen: der Test-Client und zuverlässige Endpoints](https://www.mikebild.dev/de/blog/flask-apps-testen/)
  - [Daten einlesen in Python: CSV, JSON, Excel und Datenbank](https://www.mikebild.dev/de/blog/python-daten-einlesen/)
  - [Datenanalyse mit NumPy, Pandas und Matplotlib](https://www.mikebild.dev/de/blog/datenanalyse-mit-pandas/)

## Archiv

Das Material von 2018 (Python 3.6, Flask, NumPy, Matplotlib, pandas) liegt unverändert in [`archive/`](archive/) und wird nicht mehr gepflegt.

## Lizenz

[MIT](LICENSE)
