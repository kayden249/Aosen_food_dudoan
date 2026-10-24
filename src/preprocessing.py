"""Basic data loading and validation for the Ao Sen food ML demo."""
from pathlib import Path
import pandas as pd

REQUIRED_COLUMNS = {
    "food_category", "price_min", "price_max", "price_avg",
    "sales_min", "sales_max", "sales_avg", "data_source"
}

def load_food_data(path=None):
    """Load the CSV and perform basic consistency checks."""
    if path is None:
        path = Path(__file__).resolve().parents[1] / "data" / "food_data.csv"
    data = pd.read_csv(path)

    missing_columns = REQUIRED_COLUMNS - set(data.columns)
    if missing_columns:
        raise ValueError(f"Missing required columns: {sorted(missing_columns)}")

    if data["food_category"].duplicated().any():
        raise ValueError("food_category must be unique in this group-level demo.")

    if (data["price_min"] > data["price_max"]).any():
        raise ValueError("Found price_min greater than price_max.")

    if (data["sales_min"] > data["sales_max"]).any():
        raise ValueError("Found sales_min greater than sales_max.")

    return data
