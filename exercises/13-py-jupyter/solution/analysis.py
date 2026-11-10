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
    items["revenueCents"] = items["quantity"] * items["priceCents"]
    return items


def completed(items: pd.DataFrame) -> pd.DataFrame:
    """Only orders that count: cancelled ones and drafts are dropped."""
    return items[~items["status"].isin(["cancelled", "draft"])]


def revenue_by_product(items: pd.DataFrame) -> pd.Series:
    """Revenue in cents per product, descending."""
    return completed(items).groupby("productId")["revenueCents"].sum().sort_values(ascending=False)


def revenue_by_month(items: pd.DataFrame) -> pd.Series:
    """Revenue in cents per month in the format 2026-07."""
    done = completed(items)
    month = done["createdAt"].dt.strftime("%Y-%m")
    return done.groupby(month)["revenueCents"].sum().sort_index()


def customer_summary(items: pd.DataFrame) -> pd.DataFrame:
    """Per customer: number of orders and revenue, sorted by revenue."""
    return (
        completed(items)
        .groupby("customerId")
        .agg(orders=("orderId", "nunique"), revenueCents=("revenueCents", "sum"))
        .sort_values("revenueCents", ascending=False)
    )
