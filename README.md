*English · [Deutsch](README.de.md)*

# Exercises: Python

Exercise repository for the workshop “Python for developers with uv, pytest and Flask”. Each of the 17 lessons has an exercise with a starting point, tests and a reference solution. All exercises play in the workshop shop with products and orders.

## What you learn

- Use values, functions, collections and dataclasses with type hints
- Handle errors deliberately, read files, and check code with pytest and mypy
- Set up projects with uv and build an HTTP API with Flask 3

## Prerequisites

- **uv** – manages Python versions, environments and packages ([installation](https://docs.astral.sh/uv/getting-started/installation/)). Check with `uv --version`.
- **Python 3.15** – `uv sync` reads the version from [`.python-version`](.python-version) and installs it when needed.

## Setup

```bash
git clone https://github.com/MikeBild/introduction-python.git
cd introduction-python
uv sync                          # installs Python 3.15 from .python-version if needed
uv run python scripts/check.py   # pytest and mypy --strict for all exercises
```

## How to work on an exercise

```text
exercises/
  01-py-values-types/
    README.md          task, steps, check
    start/             your starting point with TODO comments
      money.py
      test_money.py    tests with pytestmark = skip – remove the line to activate them
    solution/          one possible solution, same structure
data/                  sample data: products.json, orders.json, orders.jsonl
docs/                  the domain of the workshop shop
scripts/check.py       checks the starting point and the solution of every exercise
```

1. Read the exercise's `README.md` and open the starting point in `start/`.
2. Remove the line `pytestmark = pytest.mark.skip(...)` in the test file and work through the TODOs until pytest and mypy are green.
3. Then compare with `solution/`.

```bash
cd exercises/04-py-comprehensions/start
uv run pytest            # tests of this exercise
uv run mypy --strict .   # type check
```

All exercises share one `pyproject.toml` and one `.venv` in the root folder. The exceptions are 05 and 15: there you learn to create your own package, so the exercise has its own uv project.

From the root folder:

| Command | What it does |
| --- | --- |
| `uv run python scripts/check.py` | pytest and mypy for all starting points and solutions |
| `uv run python scripts/check.py 04 11` | only exercises 04 and 11 |
| `uv run python scripts/check.py --solution` | only the solutions |

## Exercises

| No. | Lesson | Exercise |
| --- | --- | --- |
| 01 | Names point to values, values have types | [01-py-values-types](exercises/01-py-values-types) |
| 02 | Clear function signatures instead of flag parameters | [02-py-functions](exercises/02-py-functions) |
| 03 | Which collection fits your data? | [03-py-collections](exercises/03-py-collections) |
| 04 | Comprehensions instead of loops with append | [04-py-comprehensions](exercises/04-py-comprehensions) |
| 05 | A project with uv instead of manual pip and venv | [05-py-modules-uv](exercises/05-py-modules-uv) |
| 06 | Dataclasses instead of boilerplate-heavy classes | [06-py-classes-dataclasses](exercises/06-py-classes-dataclasses) |
| 07 | Which exception do you catch, and which do you not? | [07-py-errors](exercises/07-py-errors) |
| 08 | Read and write JSON and CSV safely with pathlib | [08-py-files-json](exercises/08-py-files-json) |
| 09 | mypy checks type hints, not Python | [09-py-type-hints](exercises/09-py-type-hints) |
| 10 | Check behavior with pytest, not details | [10-py-testing-pytest](exercises/10-py-testing-pytest) |
| 11 | An HTTP API with Flask for the workshop shop | [11-py-http-api-flask](exercises/11-py-http-api-flask) |

### Extra chapters

| No. | Lesson | Exercise |
| --- | --- | --- |
| 12 | Analyze orders with pandas instead of loops | [12-py-pandas-orders](exercises/12-py-pandas-orders) |
| 13 | Explore in notebooks, keep logic in modules | [13-py-jupyter](exercises/13-py-jupyter) |
| 14 | Wait with asyncio without blocking | [14-py-asyncio](exercises/14-py-asyncio) |
| 15 | Build a package others can install | [15-py-packaging](exercises/15-py-packaging) |
| 16 | Generators return values only on demand | [16-py-generators](exercises/16-py-generators) |
| 17 | Decorators add behavior without changing code | [17-py-decorators](exercises/17-py-decorators) |

## The workshop shop

An order consists of line items with `productId`, `quantity` and `priceCents`. Money is always in whole cents. The whole domain is described in [`docs/beispiel-domaene.md`](docs/beispiel-domaene.md).

## Stack and packages

**Stack (October 2026):** Python 3.15 · uv as the only tool for Python versions, environments and packages · pytest · type hints with mypy `--strict` · Flask 3 · pandas 3 and JupyterLab for data analysis

Deliberately few packages:

| Package | For | Why this one |
| --- | --- | --- |
| `flask` | HTTP API | routing, JSON and test client in one package; FastAPI would also need Starlette, Pydantic, an ASGI server and httpx for tests |
| `pytest` | tests | tests as plain functions with `assert`, fixtures and `parametrize` |
| `mypy` | type checking | runs as a Python package directly with uv, without an extra runtime |
| `pandas`, `pandas-stubs`, `jupyterlab` | extra chapters on data analysis | group `data`, only for exercises 12 and 13 |

For asyncio, files, JSON, CSV, generators and decorators the standard library is enough.

## Workshop and slides

- Workshop (held in German): [“Python for developers with uv, pytest, and Flask”](https://workshops.mikebild.dev/w/python/remote/)
- Slides: [slides.mikebild.dev/introduction-python.en](https://slides.mikebild.dev/introduction-python.en.html)
- PDF: [introduction-python.en.pdf](https://media.mikebild.dev/site/mikebild/decks/introduction-python/introduction-python.en.pdf)
- Video: [introduction-python.en.mp4](https://media.mikebild.dev/site/mikebild/decks/introduction-python/introduction-python.en.mp4)
- Posts on mikebild.dev:
  - [Advanced Python: Decorators, Magic Methods and Generators](https://www.mikebild.dev/en/blog/advanced-python-decorators-magic-methods-generators/)
  - [Functional Patterns in Python: Comprehensions, itertools and functools](https://www.mikebild.dev/en/blog/functional-patterns-in-python/)
  - [Web APIs with Flask: From the App to a JSON API](https://www.mikebild.dev/en/blog/web-apis-with-flask/)
  - [Testing Flask Apps: The Test Client and Reliable Endpoints](https://www.mikebild.dev/en/blog/testing-flask-apps/)
  - [Reading Data in Python: CSV, JSON, Excel and Databases](https://www.mikebild.dev/en/blog/reading-data-in-python/)
  - [Data Analysis with NumPy, Pandas, and Matplotlib](https://www.mikebild.dev/en/blog/data-analysis-with-numpy-pandas-and-matplotlib/)

## Archive

The material from 2018 (Python 3.6, Flask, NumPy, Matplotlib, pandas) sits unchanged in [`archive/`](archive/) and is no longer maintained.

## License

[MIT](LICENSE)
