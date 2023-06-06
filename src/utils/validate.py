import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import inspect

from src.alphas.runner import alpha_runner
from src.core.dataloader import load_candles

pd.options.mode.chained_assignment = None  # default='warn'


day_candles = load_candles(load_from_cache=True)


def validate_alpha(alpha, num_buckets=10):
    global day_candles

    try:
        alpha_name = alpha.__name__
        alpha_bucket_name = "{}_bucket".format(alpha_name)

        alpha_candles = day_candles[["date"]]

        alpha_candles.loc[:, alpha_name] = alpha_runner(
            alpha=alpha, day_candles=day_candles
        )
        
        alpha_candles.loc[:, f"{alpha_name}_rank"] = alpha_candles.groupby("date")[
            alpha_name
        ].rank(ascending=False)
        
        alpha_candles.loc[:,'liquidity'] = day_candles.volume*day_candles.close
            

        alpha_candles.loc[:, 'liquidity_20'] = day_candles.groupby('symbol')['liquidity'].transform(
            lambda x: x.rolling(20).mean())

        alpha_candles.loc[:, "liquidity_rank"] = day_candles.groupby("date")[
                "liquidity_20"
            ].rank(ascending=False)
        
        alpha_candles.loc[:, "is_top500"] = np.where(
                (day_candles["liquidity_rank"] <= 500), True, False
            )

        alpha_candles.loc[:, "intraday_return"] = (
            day_candles.close / day_candles.open - 1
        )
        alpha_candles.loc[
            :, "next_day_intraday_return"
        ] = alpha_candles.intraday_return.shift(-1)

        alpha_candles.loc[:, alpha_bucket_name] = 1 + 10 * alpha_candles.groupby(
            ["is_top500", "date"]
        )[alpha_name].rank(method="first", pct=True)

        alpha_candles.loc[:, alpha_bucket_name] = np.where(
            alpha_candles["is_top500"] == False,
            np.nan,
            alpha_candles[alpha_bucket_name],
        )

        alpha_candles.loc[:, alpha_bucket_name] = (
            alpha_candles[alpha_bucket_name]
            .replace([np.inf, -np.inf, np.nan], 0)
            .astype(int)
            .replace([0], np.nan)
            .replace([num_buckets + 1], num_buckets)
        )

        # plotting
        t_df = (
            alpha_candles.groupby(alpha_bucket_name)
            .next_day_intraday_return.mean()
            .reset_index()
        )

        plt.clf()
        plt.title(alpha_name)
        plt.bar(t_df[alpha_bucket_name], t_df.next_day_intraday_return)
        plt.savefig(f"./cache/out/{alpha_name}.png")

    except Exception as e:
        print(alpha, inspect.signature(alpha), e)
