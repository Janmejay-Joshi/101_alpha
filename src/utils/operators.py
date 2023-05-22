import pandas as pd
import numpy as np
import math

# NOTE:
#  1. x, y -> TimeSeries Data
#  2. d -> Number Days of Past Today
#  3. Non-Integer number of days d is converted to floor(d)


def rank(x):
    """Cross-Sectional Rank"""
    pass


def delay(x: pd.DataFrame, d):
    """Value of x, d Days ago"""
    d = math.floor(d)
    return x.shift(periods=d)


def correlation(x, y, d):
    """Time-serial correlation of x and y for the Past d days"""
    pass


def covariance(x, y, d):
    """Time-serial covariance of x and y for the Past d days"""
    pass


def scale(x, a):
    """Rescaled x such that sum(abs(x)) = a (the default is a = 1)"""
    pass


def delta(x, d):
    """Today's value of x minus the value of x, d days ago"""
    pass


def decay_linear(x, d):
    """Weighted moving average over the Past d days
    with linearly decaying weights d, d - 1, …, 1 (rescaled to sum up to 1)"""
    pass


def indneutralize(x, g):
    """x cross-sectionally neutralized against groups g (subindustries, industries,sectors, etc.),
    i.e., x is cross-sectionally demeaned within each group g"""
    pass


def ts_min(x: pd.DataFrame, d):
    """Time-series min over the Past d days"""
    d = math.floor(d)
    return x.rolling(window=d).min()


def ts_max(x: pd.DataFrame, d):
    """Time-series max over the Past d days"""
    d = math.floor(d)
    return x.rolling(window=d).max()


def ts_argmax(x, d):
    """Which day ts_max(x, d) occurred on"""
    pass


def ts_argmin(x, d):
    """Which day ts_min(x, d) occurred on"""
    pass


def ts_rank(x, d):
    """Time-series rank in the Past d days"""
    pass


def sum(x: pd.DataFrame, d):
    """Time-series sum over the Past d days"""
    d = math.floor(d)
    return x.rolling(window=d).sum()


def product(x: pd.DataFrame, d):
    """Time-series product over the Past d days"""
    d = math.floor(d)
    return x.rolling(window=d).apply(np.prod, raw=True)


def stddev(x: pd.DataFrame, d):
    """Moving Time-series standard deviation over the Past d days"""
    d = math.floor(d)
    return x.rolling(window=d).std()


## Alias Functions


def log(x):
    """Alias for math.log(x)"""
    return math.log(x)


def sign(x):
    """Alias for np.sign(x)"""
    return np.sign(x)


def signedpower(x, a):
    """Alias for math.pow(x, a)"""
    return math.pow(x, a)


def min(x, d):
    """Alias for ts_min(x, d)"""
    return ts_min(x, d)


def max(x, d):
    """Alias for ts_max(x, d)"""
    return ts_max(x, d)
