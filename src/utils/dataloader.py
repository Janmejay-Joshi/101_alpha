import ta
import pandas as pd
from quantplay.services.market import Market

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


def load_candles():
    market = Market()
    day_candles = market.data_by_path(interval="day", symbols=market.symbols("NIFTY 500"), path=market.nse_equity_path)

    return preprocess_candles(day_candles)


def preprocess_candles(day_candles: pd.DataFrame):
    vwap = ta.volume.volume_weighted_average_price(
        high=day_candles.high,
        low=day_candles.low,
        close=day_candles.close,
        volume=day_candles.volume,
    )

    day_candles.loc[:, "vwap"] = vwap

    return day_candles


if __name__ == "__main__":
    print(load_candles())
