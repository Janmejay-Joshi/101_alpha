import pandas as pd
import typing


def alpha_runner(alpha: typing.Callable, day_candles: pd.DataFrame):
    return alpha(
        open=day_candles.open,
        low=day_candles.low,
        high=day_candles.high,
        close=day_candles.close,
        volume=day_candles.volume,
        vwap=day_candles.vwap,
        returns=day_candles.returns,
        adv5=day_candles.adv5,
        adv10=day_candles.adv10,
        adv15=day_candles.adv15,
        adv20=day_candles.adv20,
        adv30=day_candles.adv30,
        adv40=day_candles.adv40,
        adv50=day_candles.adv50,
        adv60=day_candles.adv60,
        adv81=day_candles.adv81,
        adv120=day_candles.adv120,
        adv150=day_candles.adv150,
        adv180=day_candles.adv180,
    )
