import matplotlib.pyplot as plt
import numpy as np


def validate_alpha(day_candles, alpha, num_buckets=10):
    alpha_name = alpha.__name__

    alpha_bucket_name = "{}_bucket".format(alpha_name)
    day_candles.loc[:, alpha_name] = alpha
    day_candles.loc[:, f"{alpha_name}_rank"] = day_candles.groupby("date")[alpha_name].rank(ascending=False)
    day_candles.loc[:, "is_top500"] = np.where((day_candles[f"{alpha_name}_rank"] <= 500), True, False)

    day_candles.loc[:, "intraday_return"] = day_candles.close / day_candles.open - 1
    day_candles.loc[:, "next_day_intraday_return"] = day_candles.intraday_return.shift(-1)

    day_candles.loc[:, alpha_bucket_name] = 1 + 10 * day_candles.groupby(["is_top500", "date"])[alpha_name].rank(
        method="first", pct=True
    )
    day_candles.loc[:, alpha_bucket_name] = np.where(day_candles["is_top500"] == False, np.nan, day_candles[alpha_bucket_name])
    day_candles.loc[:, alpha_bucket_name] = (
        day_candles[alpha_bucket_name]
        .replace([np.inf, -np.inf, np.nan], 0)
        .astype(int)
        .replace([0], np.nan)
        .replace([num_buckets + 1], num_buckets)
    )

    # plotting
    t_df = day_candles.groupby(alpha_bucket_name).next_day_intraday_return.mean().reset_index()

    plt.bar(t_df[alpha_bucket_name], t_df.next_day_intraday_return)
    plt.show()
