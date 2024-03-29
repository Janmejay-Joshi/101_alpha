from quantplay.services.market import Market
from src.utils.preprocess import preprocess_candles

from multiprocessing import Pool
from datetime import datetime
import pandas as pd
import os

from datetime import date, datetime

day_candles = pd.DataFrame


def load_candles(load_from_cache=False):
    if load_from_cache and os.path.exists("./cache/processed_candles.csv"):
        return pd.read_csv("./cache/processed_candles.csv")

    global day_candles

    market = Market()

    # day_candles = market.data_by_path(
    #     interval="day", symbols=market.symbols("NIFTY 500"), path=market.nse_equity_path
    # )

    day_candles = market.data_by_path(
        interval="day", symbols=market.symbols("NIFTY MIDCAP 100"), path=market.nse_equity_path
    )
    day_candles['date'] = pd.to_datetime(day_candles['date'])
    day_candles = day_candles[day_candles['date'].dt.date > date(2020, 5, 1)]
    day_candles.reset_index(inplace=True, drop=True)

    procesed_day_candles = pd.DataFrame()

    unique_symbols = day_candles.symbol.unique()

    with Pool(12) as p:
        processed_df = p.map(worker, unique_symbols)

    procesed_day_candles = pd.concat(
        processed_df,
        ignore_index=True,
        axis=0,
    )

    if not os.path.exists("./cache"):
        os.makedirs(os.path.join("./cache", "out"))

    procesed_day_candles.to_csv("./cache/processed_candles.csv")

    return procesed_day_candles


def worker(symbol):
    global day_candles
    
    symbol_day_candles = day_candles[day_candles.symbol == symbol].copy(deep=False)
    processed_df = preprocess_candles(symbol_day_candles)

    return processed_df


if __name__ == "__main__":
    print(load_candles())
