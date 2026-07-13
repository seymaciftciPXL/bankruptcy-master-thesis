import pandas as pd
from config import DATA_CLEANED


def load_data_cleaned():
    return pd.read_csv(
        DATA_CLEANED,
        low_memory=False
    )
