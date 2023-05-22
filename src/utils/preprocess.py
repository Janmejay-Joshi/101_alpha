import ta
import pandas as pd

# TODO: Groupby

# TODO: Add To Day Candles
#
#   1. returns:
#       Daily close-to-close returns
#
#   2. vwap
#       Daily volume-weighted average price
#
#   3. cap:
#       Market Cap
#
#   4. adv{d}:
#      Average daily dollar volume for the past d days
#
#       d = {5, 10, 15, 20, 30, 40, 50, 60, 81, 120, 150, 180}
#
#   5. IndClass :
#       A generic placeholder for a binary industry classification such as GICS, BICS, NAICS,
#       SIC, etc., in indneutralize(x, IndClass.level), where level = sector, industry, subindustry, etc.
#       Multiple IndClass in the same alpha need not correspond to the same industry classification.


def returns(day_candles: pd.DataFrame):
    """
    Daily close-to-close returns
    """
    return ta.others.daily_return(close=day_candles.close)


def vwap(day_candles: pd.DataFrame):
    """
    Daily volume-weighted average price
    """
    return ta.volume.volume_weighted_average_price(
        high=day_candles.high,
        low=day_candles.low,
        close=day_candles.close,
        volume=day_candles.volume,
    )


def adv(day_candles: pd.DataFrame, window: int):
    """
    Average daily dollar volume for the past d days, i.e. ADTV
    """
    return (day_candles.volume.rolling(window=window).sum()) / window


def preprocess_candles(day_candles: pd.DataFrame):
    day_candles.loc[:, "vwap"] = vwap(day_candles)

    for d in [5, 10, 15, 20, 30, 40, 50, 60, 81, 120, 150, 180]:
        day_candles.loc[:, f"adv{d}"] = adv(day_candles, d)

    day_candles.loc[:, "returns"] = returns(day_candles)
    day_candles.iloc[0, -1] = 0

    return day_candles
