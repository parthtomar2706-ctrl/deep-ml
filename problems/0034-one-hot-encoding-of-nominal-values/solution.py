import numpy as np

def to_categorical(x, n_col=None):
    if n_col is None:
        n_col = np.max(x) + 1

    result = np.zeros((len(x), n_col), dtype=int)

    for i in range(len(x)):
        result[i, x[i]] = 1

    return result