import numpy as np
from src.pipeline import load_model, predict_from_numpy

def test_predict_pipeline(saved_model_file, sample_numpy):
    model = load_model(saved_model_file, device='cpu')
    probs = predict_from_numpy(model, sample_numpy)
    # probs should have shape (n_samples, num_classes)
    assert probs.shape == (sample_numpy.shape[0], 3)
    # probabilities should sum to 1 for each sample
    sums = probs.sum(axis=1)
    assert np.allclose(sums, 1.0, atol=1e-6)
