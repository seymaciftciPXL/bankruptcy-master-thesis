import pandas as pd


from config import RAW_DATA


def load_data_raw():
    return pd.read_csv(
        RAW_DATA,
        low_memory=False,
        encoding="latin1"
    )
