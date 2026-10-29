# werkstatt-money

Geldbeträge in ganzen Cent parsen und formatieren.

```python
from werkstatt_money import format_cents, to_cents

format_cents(to_cents("12,34"))  # "12,34 €"
```

```bash
uvx --from ./dist/werkstatt_money-1.0.0-py3-none-any.whl werkstatt-money 12,34
```
