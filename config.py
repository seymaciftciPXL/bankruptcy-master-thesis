from pathlib import Path

ROOT = Path(__file__).resolve().parent

DATA = ROOT / "data"

RAW_DATA = DATA / "raw" / "dataset_raw.csv"

PROCESSED = DATA / "processed"

CLEANED_DATA = PROCESSED / "cleaned_data.csv"

MISSING_THRESHOLD = 0.90
