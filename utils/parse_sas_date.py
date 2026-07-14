import pandas as pd

def parse_sas_date(series: pd.Series) -> pd.Series:
    """Parse a SAS-style date column (days since 1960-01-01)."""
    return pd.to_datetime(series, unit='D', origin='1960-01-01', errors='coerce')
