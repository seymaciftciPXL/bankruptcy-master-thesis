import pandas as pd
from pathlib import Path

ROOT = Path(__file__).resolve().parent

DATA_RAW = ROOT / "data" / "dataset_raw.csv"


def load_data_raw():
    return pd.read_csv(
        DATA_RAW,
        low_memory=False,
        encoding="latin1",
    )