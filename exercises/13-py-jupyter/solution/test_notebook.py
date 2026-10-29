import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).parent
NOTEBOOK = HERE / "bestellungen.ipynb"


def code_cells(path: Path) -> list[dict[str, object]]:
    notebook = json.loads(path.read_text(encoding="utf-8"))
    return [cell for cell in notebook["cells"] if cell["cell_type"] == "code"]


def source(cell: dict[str, object]) -> str:
    text = cell["source"]
    return "".join(text) if isinstance(text, list) else str(text)


def test_notebook_only_calls_functions_from_the_module() -> None:
    cells = code_cells(NOTEBOOK)
    assert not any("def " in source(cell) for cell in cells), "Funktionen gehören nach analysis.py"
    assert any("from analysis import" in source(cell) for cell in cells)


def test_notebook_is_committed_without_outputs() -> None:
    for cell in code_cells(NOTEBOOK):
        assert cell["outputs"] == [], "Outputs vor dem Commit löschen"
        assert cell["execution_count"] is None


def test_notebook_runs_from_top_to_bottom(tmp_path: Path) -> None:
    subprocess.run(
        [sys.executable, "-m", "jupyter", "nbconvert", "--to", "notebook", "--execute",
         "--output-dir", str(tmp_path), str(NOTEBOOK)],
        cwd=HERE,
        check=True,
        capture_output=True,
    )
    executed = code_cells(tmp_path / NOTEBOOK.name)
    assert all(cell["outputs"] for cell in executed)
