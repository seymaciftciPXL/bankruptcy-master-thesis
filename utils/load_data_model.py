import pandas as pd
from config import  DATA_MODEL


def load_data_model():
    return pd.read_csv(
        DATA_MODEL,
        low_memory=False
    )
