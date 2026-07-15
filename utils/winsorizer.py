from sklearn.base import BaseEstimator, TransformerMixin

from config import WINSOR_LOWER_QUANTILE, WINSOR_UPPER_QUANTILE


class Winsorizer(BaseEstimator, TransformerMixin):
    """Clip outliers in `columns` to the [lower_q, upper_q] percentile range.

    Other columns in X pass through unchanged. Used as a pipeline step
    (instead of clipping the full dataset up front) so the clip bounds
    are learned on the training fold only - computing them on the full
    dataset would leak test-set information into preprocessing.
    """

    def __init__(self, columns, lower_q=WINSOR_LOWER_QUANTILE, upper_q=WINSOR_UPPER_QUANTILE):
        self.columns = columns
        self.lower_q = lower_q
        self.upper_q = upper_q

    def fit(self, X, y=None):
        self.lower_ = X[self.columns].quantile(self.lower_q)
        self.upper_ = X[self.columns].quantile(self.upper_q)
        return self

    def transform(self, X):
        X = X.copy()
        X[self.columns] = X[self.columns].clip(lower=self.lower_, upper=self.upper_, axis=1)
        return X
