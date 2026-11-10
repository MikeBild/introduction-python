*English · [Deutsch](README.de.md)*

# An HTTP API with Flask for the workshop shop

**Learning goal:** Afterwards you build an HTTP API with Flask 3 with an app factory, a validated JSON body, error handlers and tests via the test client.

**Task:** Add GET /orders/<order_id> and POST /orders with 201 and Location, map errors through error handlers to 400, 409, and 422, and make the tests pass.

## Steps

1. Start the app with `uv run flask --app app run --debug` and open `http://127.0.0.1:5000/products`.
2. Add `GET /orders/<order_id>` with 404 for unknown orders.
3. Add `POST /orders`: validate the body with `parse_place_order`, place the order, return 201 with `Location`.
4. Translate errors with `@app.errorhandler` into 400, 409, 422, and JSON for unknown routes.

The tests in `start/` are skipped at first. Remove the line `pytestmark = pytest.mark.skip(...)` as soon as you start the exercise.

## Check

```bash
cd start
uv run pytest
uv run mypy --strict .
```

One possible solution is in [`solution/`](solution/). From the root folder, `uv run python scripts/check.py 11` checks the starting point and the solution of this exercise.
