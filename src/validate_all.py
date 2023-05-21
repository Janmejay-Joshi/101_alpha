import inspect


def runner(include=[], exclude=[]):
    """
    Imports and Validates all alphas
    """
    import src.alphas.all as all_alphas

    for i in dir(all_alphas):
        if i.startswith("alpha") and (i not in exclude):
            if (include != []) and (i not in include):
                continue

            alpha = getattr(all_alphas, i)
            if callable(alpha):
                print(alpha, inspect.signature(alpha))


if __name__ == "__main__":
    runner()
