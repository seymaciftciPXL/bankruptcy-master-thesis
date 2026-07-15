import pandas as pd
from config import DATASET_RAW


def load_data_raw():
    return pd.read_csv(
        DATASET_RAW,
        low_memory=False,
        encoding="latin1",
    )
