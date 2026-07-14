import pandas as pd


def convert_comma_to_decimal(series):
    return pd.to_numeric(
        series.astype(str).str.replace(",", ".", regex=False),
        errors="coerce"
    )
