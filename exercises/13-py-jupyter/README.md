*English · [Deutsch](README.de.md)*

# Explore in notebooks, keep logic in modules

**Learning goal:** After this, you use JupyterLab for exploration, move logic into a tested module, and run the notebook in CI.

**Task:** Move the functions from bestellungen.ipynb to analysis.py, call them from the notebook only, and commit the notebook without outputs.

## Steps

1. Start JupyterLab with `uv run jupyter lab` and open `start/bestellungen.ipynb`.
2. Move `load_items` and the analyses to `analysis.py` and annotate them.
3. Import the functions in the notebook and delete all cells with `def`.
4. Check with “Restart Kernel and Run All Cells” and delete the outputs before the commit.

The tests in `start/` are skipped at first. Remove the line `pytestmark = pytest.mark.skip(...)` as soon as you start the exercise.

## Check

```bash
cd start
uv run pytest
uv run mypy --strict .
```

One possible solution is in [`solution/`](solution/). From the root folder, `uv run python scripts/check.py 13` checks the starting point and the solution of this exercise.
