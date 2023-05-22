from src.core.dataloader import load_candles
from src.utils.validate import validate_alpha

from multiprocessing import Pool


def runner(include=[], exclude=[]):
    """
    Imports and Validates all alphas
    """
    import src.alphas.all as all_alphas

    runnables = []

    for i in dir(all_alphas):
        if i.startswith("alpha") and (i not in exclude):
            if (include != []) and (i not in include):
                continue

            alpha = getattr(all_alphas, i)
            if callable(alpha):
                runnables.append(alpha)

    with Pool(8) as p:
        p.map(validate_alpha, runnables)


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
