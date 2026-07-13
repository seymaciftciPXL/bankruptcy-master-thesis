import pandas as pd

from pathlib import Path

ROOT = Path(__file__).resolve().parent

DATA_CLEANED = ROOT / "data" / "dataset_raw_cleaned.csv"

def load_data_cleaned():
    return pd.read_csv(
        DATA_CLEANED,
        low_memory=False
    )
