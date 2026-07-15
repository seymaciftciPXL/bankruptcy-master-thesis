import pandas as pd
from config import DATASET_FEATURES


def load_data_features():
    return pd.read_csv(
        DATASET_FEATURES,
        low_memory=False
    )
