from config import TRAIN_YEARS, TEST_YEAR


def time_based_split(df, features, target, train_years=TRAIN_YEARS, test_year=TEST_YEAR):
    """Split by bookyear instead of by row.

    A random row split leaks information here: most companies appear in
    several bookyears, so the same company could end up in both train and
    test. Splitting on bookyear keeps the test set a genuinely unseen,
    future period, like the model would face in practice.
    """
    train = df[df["bookyear"].isin(train_years)]
    test = df[df["bookyear"] == test_year]

    X_train, y_train = train[features], train[target]
    X_test, y_test = test[features], test[target]

    return X_train, X_test, y_train, y_test
