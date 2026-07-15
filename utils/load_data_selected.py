import pandas as pd
from config import DATASET_SELECTED


def load_data_selected():
    return pd.read_csv(
        DATASET_SELECTED,
        low_memory=False
    )
