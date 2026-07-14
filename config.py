from pathlib import Path

ROOT = Path(__file__).resolve().parent

DATA = ROOT / "data"

DATA_RAW = DATA / "raw" / "dataset_raw.csv"

DATA_CLEANED = DATA / "processed" / "data_cleaned.csv"

DATA_MODEL = DATA / "processed" / "model_dataset.csv"

MISSING_THRESHOLD = 0.90