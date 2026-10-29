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
    # TODO: Spalte revenueCents = quantity × priceCents, ohne Schleife (vektorisiert)
    return items


def completed(items: pd.DataFrame) -> pd.DataFrame:
    """Nur Bestellungen, die zählen: stornierte und Entwürfe fallen weg."""
    # TODO: Boolean-Maske mit items["status"].isin([...]) und ~ für „nicht“
    raise NotImplementedError


def revenue_by_product(items: pd.DataFrame) -> pd.Series:
    """Umsatz in Cent je Produkt, absteigend."""
    # TODO: completed(...).groupby("productId")["revenueCents"].sum(), dann sort_values
    raise NotImplementedError


def revenue_by_month(items: pd.DataFrame) -> pd.Series:
    """Umsatz in Cent je Monat im Format 2026-07."""
    # TODO: Monat mit .dt.strftime("%Y-%m") bilden und danach gruppieren
    raise NotImplementedError


def customer_summary(items: pd.DataFrame) -> pd.DataFrame:
    """Je Kundin: Anzahl Bestellungen (orders) und Umsatz (revenueCents), nach Umsatz sortiert."""
    # TODO: groupby("customerId").agg(orders=("orderId", "nunique"), revenueCents=(...))
    raise NotImplementedError
