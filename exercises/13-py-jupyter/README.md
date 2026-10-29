# Im Notebook erkunden, im Modul festhalten

**Lernziel:** Danach nutzt du JupyterLab für Erkundung, verschiebst die Logik in ein getestetes Modul und führst das Notebook in der CI aus.

**Aufgabe:** Verschieb die Funktionen aus bestellungen.ipynb nach analysis.py, ruf sie im Notebook nur noch auf und commite das Notebook ohne Outputs.

## Schritte

1. Starte JupyterLab mit `uv run jupyter lab` und öffne `start/bestellungen.ipynb`.
2. Verschieb `load_items` und die Auswertungen nach `analysis.py` und annotiere sie.
3. Importiere die Funktionen im Notebook und lösch alle Zellen mit `def`.
4. Prüf mit „Restart Kernel and Run All Cells“ und lösch die Outputs vor dem Commit.

Die Tests in `start/` sind zuerst übersprungen. Entferne die Zeile `pytestmark = pytest.mark.skip(...)`, sobald du mit der Übung beginnst.

## Prüfen

```bash
cd start
uv run pytest
uv run mypy --strict .
```

Eine mögliche Lösung steht in [`solution/`](solution/). Vom Root aus prüft `uv run python scripts/check.py 13` Start und Lösung dieser Übung.
