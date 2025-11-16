import numpy as np

def normalize_features(x):
    """
    Normalize features to zero mean and unit variance (per-column).
    Accepts numpy arrays.
    """
    x = np.asarray(x, dtype=float)
    mean = x.mean(axis=0)
    std = x.std(axis=0)
    std_repl = np.where(std == 0, 1.0, std)  # avoid divide-by-zero
    return (x - mean) / std_repl
