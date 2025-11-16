import numpy as np
from src.utils import normalize_features

def test_normalize_basic():
    x = np.array([[1.0, 2.0], [3.0, 4.0]])
    x_norm = normalize_features(x)
    # zero mean per column
    assert abs(x_norm.mean(axis=0)).sum() < 1e-9
    # unit variance per column
    assert abs(x_norm.std(axis=0) - 1.0).sum() < 1e-9

def test_normalize_constant_column():
    x = np.array([[1.0, 2.0], [1.0, 4.0]])
    x_norm = normalize_features(x)
    # constant column should not create nan (std replaced with 1)
    assert not np.isnan(x_norm).any()
