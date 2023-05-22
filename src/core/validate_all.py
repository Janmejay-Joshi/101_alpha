from src.core.dataloader import load_candles
from src.alphas.runner import alpha_runner

import inspect


def runner(include=[], exclude=[]):
    """
    Imports and Validates all alphas
    """
    import src.alphas.all as all_alphas

    day_candles = load_candles(load_from_cache=True)

    counter = 0

    for i in dir(all_alphas):
        if i.startswith("alpha") and (i not in exclude):
            if (include != []) and (i not in include):
                continue

            alpha = getattr(all_alphas, i)
            if callable(alpha):
                try:
                    alpha_runner(alpha=alpha, day_candles=day_candles)
                except Exception as e:
                    print(alpha, inspect.signature(alpha), e)
                finally:
                    counter += 1
                    print(f"{counter}/101  ({(counter / 101 * 100):0,.2f}%)", end="\r")


if __name__ == "__main__":
    # Excluded Due to missing Inputs:
    #   Market Cap, IndClass
    excludes = [
        48,
        56,
        58,
        59,
        63,
        67,
        69,
        70,
        76,
        79,
        80,
        82,
        87,
        89,
        90,
        91,
        93,
        97,
        100,
    ]
    includes = [101, 41]

    excluded_alphas = [f"alpha_{i}" for i in excludes]
    included_alphas = [f"alpha_{i}" for i in includes]

    runner(exclude=excluded_alphas)
