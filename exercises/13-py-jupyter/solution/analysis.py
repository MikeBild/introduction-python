"""Bestellungen mit pandas auswerten: eine Zeile je Position, dann gruppieren."""

import json
from pathlib import Path

import pandas as pd


def load_items(path: Path) -> pd.DataFrame:
    """Flacht die verschachtelten Bestellungen ab: eine Zeile je Position."""
    orders = json.loads(path.read_text(encoding="utf-8"))
    items = pd.json_normalize(
        orders, record_path="items", meta=["id", "customerId", "status", "createdAt"]
    )
    items = items.rename(columns={"id": "orderId"})
    items["createdAt"] = pd.to_datetime(items["createdAt"])
    items["revenueCents"] = items["quantity"] * items["priceCents"]
    return items


def completed(items: pd.DataFrame) -> pd.DataFrame:
    """Nur Bestellungen, die zählen: stornierte und Entwürfe fallen weg."""
    return items[~items["status"].isin(["cancelled", "draft"])]


def revenue_by_product(items: pd.DataFrame) -> pd.Series:
    """Umsatz in Cent je Produkt, absteigend."""
    return completed(items).groupby("productId")["revenueCents"].sum().sort_values(ascending=False)


def revenue_by_month(items: pd.DataFrame) -> pd.Series:
    """Umsatz in Cent je Monat im Format 2026-07."""
    done = completed(items)
    month = done["createdAt"].dt.strftime("%Y-%m")
    return done.groupby(month)["revenueCents"].sum().sort_index()


def customer_summary(items: pd.DataFrame) -> pd.DataFrame:
    """Je Kundin: Anzahl Bestellungen und Umsatz, nach Umsatz sortiert."""
    return (
        completed(items)
        .groupby("customerId")
        .agg(orders=("orderId", "nunique"), revenueCents=("revenueCents", "sum"))
        .sort_values("revenueCents", ascending=False)
    )
