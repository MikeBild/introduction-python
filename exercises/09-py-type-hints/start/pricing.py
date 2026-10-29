"""Rechnungssummen – noch ohne Typ-Hinweise.

TODO:
1. uv run mypy --strict pricing.py ausführen und die Meldungen lesen.
2. IDs als NewType anlegen: OrderId, CustomerId, ProductId.
3. Status als Literal, OrderItem und Order als TypedDict beschreiben.
4. Alle Funktionen annotieren. find_order gibt Order | None zurück.
5. mypy findet danach den Fehler in invoice_total. Behebe ihn.
"""


def find_order(orders, order_id):
    for order in orders:
        if order["id"] == order_id:
            return order
    return None


def order_total(order):
    return sum(item["quantity"] * item["priceCents"] for item in order["items"])


def discount_percent(customer_id, vip_customers):
    return 10 if customer_id in vip_customers else 0


def invoice_total(orders, order_id, vip_customers):
    order = find_order(orders, order_id)
    total = order_total(order)
    return total - total * discount_percent(order["id"], vip_customers) // 100
