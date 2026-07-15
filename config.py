from pathlib import Path

ROOT = Path(__file__).resolve().parent

DATA = ROOT / "data"

DATASET_RAW = DATA / "raw" / "dataset_raw.csv"
DATASET_CLEANED = DATA / "processed" / "dataset_cleaned.csv"
DATASET_SELECTED = DATA / "processed" / "dataset_selected.csv"
DATASET_FEATURES = DATA / "processed" / "model_features.csv"

LOGS = ROOT / "logs"
MODEL_RESULTS_LOG = LOGS / "model_results.csv"

MISSING_THRESHOLD = 0.90

# -------------------------------------------------------------------
# Sample selection (see 04_dataset_selection.ipynb)
# -------------------------------------------------------------------

RECHTSVORMEN = ["BV", "BVBA"]
NATURES = [1, 2, 7]
BOOKYEARS = [2017, 2018, 2019]

TARGET = "target"

# -------------------------------------------------------------------
# Train/test split
#
# A random row-level split leaks information: 91% of companies have
# more than one bookyear in the dataset, so the same company can end
# up in both the train and the test set. A time-based split avoids
# this and mirrors how the model would actually be used (predict the
# next, still-unseen year).
#
# TRAIN_YEARS is the baseline used by 07-10: a single training year
# (2018, the year closest to the 2019 test year), comparable to the
# single-year setup in Cultrera & Bredart. TRAIN_YEARS_EXTENDED adds
# 2017 and is used only in 11_train_window_sensitivity.ipynb, to check
# whether a second training year actually improves on the baseline.
# -------------------------------------------------------------------

TRAIN_YEARS = [2018]
TRAIN_YEARS_EXTENDED = [2017, 2018]
TEST_YEAR = 2019
RANDOM_STATE = 42

# -------------------------------------------------------------------
# Features
# -------------------------------------------------------------------

FEATURES_FINANCIAL = [
    "profitability",
    "liquidity",
    "solvency",
    "structure",
    "log_age",
    "size",
]

FEATURES_BEHAVIORAL = [
    "laat_dummy",
    "boete_dummy",
    "dgrmovestreet",
]

# Ratios that get outliers clipped (see utils/winsorizer.py)
WINSOR_COLUMNS = [
    "profitability",
    "liquidity",
    "solvency",
    "structure",
]
WINSOR_LOWER_QUANTILE = 0.01
WINSOR_UPPER_QUANTILE = 0.99
