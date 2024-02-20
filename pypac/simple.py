import numpy as np


def akumulace(x):
    return np.sum(x)


def po_prvku(xs, ys):
    return [x * y for x, y in zip(xs, ys)]
