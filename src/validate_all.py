import inspect


def runner():
    """
    Imports and Validates all alphas
    """
    import src.alphas.all as all_alphas

    for i in dir(all_alphas):
        if i.startswith("alpha"):
            alpha = getattr(all_alphas, i)
            if callable(alpha):
                print(alpha, inspect.signature(alpha))


if __name__ == "__main__":
    runner()
