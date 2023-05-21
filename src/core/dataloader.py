from quantplay.services.market import Market
from src.utils.preprocess import preprocess_candles

from multiprocessing import Pool
import pandas as pd


day_candles = pd.DataFrame


def load_candles():
    global day_candles

    market = Market()
    day_candles = market.data_by_path(interval="day", symbols=market.symbols("NIFTY 500"), path=market.nse_equity_path)

    procesed_day_candles = pd.DataFrame(
        columns=[
            "date",
            "open",
            "high",
            "low",
            "close",
            "volume",
            "symbol",
            "vwap",
            "returns",
        ]
    )

    unique_symbols = day_candles.symbol.unique()

    with Pool(8) as p:
        processed_df = p.map(worker, unique_symbols)

    procesed_day_candles = pd.concat(
        processed_df,
        ignore_index=True,
        axis=0,
    )

    return procesed_day_candles


def worker(symbol):
    global day_candles

    symbol_day_candles = day_candles[day_candles.symbol == symbol].copy(deep=False)
    processed_df = preprocess_candles(symbol_day_candles)
    processed_df.iloc[0, -1] = 0

    return processed_df


if __name__ == "__main__":
    print(load_candles())
