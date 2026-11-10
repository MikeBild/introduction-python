"""Invoice totals – without type hints so far.

TODO:
1. Run uv run mypy --strict pricing.py and read the messages.
2. Define the IDs as NewType: OrderId, CustomerId, ProductId.
3. Describe the status as Literal, OrderItem and Order as TypedDict.
4. Annotate all functions. find_order returns Order | None.
5. mypy then finds the error in invoice_total. Fix it.
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
