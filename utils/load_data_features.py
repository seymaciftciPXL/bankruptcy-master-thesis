import pandas as pd
from config import DATA_FEATURES


def load_data_features():
    return pd.read_csv(
        DATA_FEATURES,
        low_memory=False
    )
