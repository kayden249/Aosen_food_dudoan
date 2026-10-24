"""Helper functions for the Ao Sen Food ML project."""
from pathlib import Path
import pandas as pd

REQUIRED_COLUMNS = {
    "food_category", "price_min", "price_max", "price_avg",
    "sales_min", "sales_max", "sales_avg", "data_source"
}


def load_food_data(path: str | Path = "data/food_data.csv") -> pd.DataFrame:
    """Load data and run basic schema/range checks."""
    df = pd.read_csv(path)
    missing_columns = REQUIRED_COLUMNS - set(df.columns)
    if missing_columns:
        raise ValueError(f"Missing required columns: {sorted(missing_columns)}")
    if df["food_category"].duplicated().any():
        raise ValueError("food_category should be unique in this grouped demo dataset.")
    if (df["price_min"] > df["price_max"]).any():
        raise ValueError("Found price_min greater than price_max.")
    if (df["sales_min"] > df["sales_max"]).any():
        raise ValueError("Found sales_min greater than sales_max.")
    return df


def add_midpoint_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Return a copy with midpoint-based representative values."""
    out = df.copy()
    out["price_avg"] = (out["price_min"] + out["price_max"]) / 2
    out["sales_avg"] = (out["sales_min"] + out["sales_max"]) / 2
    return out
