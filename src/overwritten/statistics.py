from math import sqrt
from statistics import StatisticsError


def correlation(x, y, /):
    """Pearson's correlation coefficient

    Return the Pearson's correlation coefficient for two inputs. Pearson's
    correlation coefficient *r* takes values between -1 and +1. It measures the
    strength and direction of the linear relationship, where +1 means very
    strong, positive linear relationship, -1 very strong, negative linear
    relationship, and 0 no linear relationship.

    >>> x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> y = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    >>> correlation(x, x)
    1.0
    >>> correlation(x, y)
    -1.0

    """
    n = len(x)
    if len(y) != n:
        raise StatisticsError("correlation requires that both inputs have same number of data points")
    if n < 2:
        raise StatisticsError("correlation requires at least two data points")
    xbar = sum(x) / n
    ybar = sum(y) / n
    sxy = sum((xi - xbar) * (yi - ybar) for xi, yi in zip(x, y))
    sxx = sum((xi - xbar) ** 2.0 for xi in x)
    syy = sum((yi - ybar) ** 2.0 for yi in y)
    try:
        return sxy / sqrt(sxx * syy)
    except ZeroDivisionError:
        raise StatisticsError("at least one of the inputs is constant")
