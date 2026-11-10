"""Analyze orders with pandas: one row per line item, then group."""

import json
from pathlib import Path

import pandas as pd


def load_items(path: Path) -> pd.DataFrame:
    """Flattens the nested orders: one row per line item."""
    orders = json.loads(path.read_text(encoding="utf-8"))
    items = pd.json_normalize(
        orders, record_path="items", meta=["id", "customerId", "status", "createdAt"]
    )
    items = items.rename(columns={"id": "orderId"})
    items["createdAt"] = pd.to_datetime(items["createdAt"])
    # TODO: column revenueCents = quantity × priceCents, without a loop (vectorized)
    return items


def completed(items: pd.DataFrame) -> pd.DataFrame:
    """Only orders that count: cancelled ones and drafts are dropped."""
    # TODO: boolean mask with items["status"].isin([...]) and ~ for “not”
    raise NotImplementedError


def revenue_by_product(items: pd.DataFrame) -> pd.Series:
    """Revenue in cents per product, descending."""
    # TODO: completed(...).groupby("productId")["revenueCents"].sum(), then sort_values
    raise NotImplementedError


def revenue_by_month(items: pd.DataFrame) -> pd.Series:
    """Revenue in cents per month in the format 2026-07."""
    # TODO: build the month with .dt.strftime("%Y-%m") and group by it
    raise NotImplementedError


def customer_summary(items: pd.DataFrame) -> pd.DataFrame:
    """Per customer: number of orders (orders) and revenue (revenueCents), sorted by revenue."""
    # TODO: groupby("customerId").agg(orders=("orderId", "nunique"), revenueCents=(...))
    raise NotImplementedError
