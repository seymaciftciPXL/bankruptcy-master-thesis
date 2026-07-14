import pandas as pd


def parse_yyyymmdd(series):
    cleaned = series.replace(0, pd.NA)

    return pd.to_datetime(
        cleaned.astype("Int64").astype(str),
        format="%Y%m%d",
        errors="coerce"
    )
