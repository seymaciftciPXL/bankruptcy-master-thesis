import pandas as pd

from config import MODEL_RESULTS_LOG


def save_model_results(model_name, metrics):
    """Append (or update) one model's metrics in the shared results log.

    Keeping this in one file instead of hardcoding numbers in
    12_model_comparison.ipynb means the comparison table always reflects
    the last run of each model notebook.
    """
    row = {"model": model_name, **metrics}

    if MODEL_RESULTS_LOG.exists():
        results = pd.read_csv(MODEL_RESULTS_LOG)
        results = results[results["model"] != model_name]
        results = pd.concat([results, pd.DataFrame([row])], ignore_index=True)
    else:
        results = pd.DataFrame([row])

    MODEL_RESULTS_LOG.parent.mkdir(parents=True, exist_ok=True)
    results.to_csv(MODEL_RESULTS_LOG, index=False)


def load_model_results():
    return pd.read_csv(MODEL_RESULTS_LOG)
