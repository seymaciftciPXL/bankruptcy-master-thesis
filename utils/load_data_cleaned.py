import pandas as pd
from config import DATASET_CLEANED


def load_data_cleaned():
    return pd.read_csv(
        DATASET_CLEANED,
        low_memory=False
    )
