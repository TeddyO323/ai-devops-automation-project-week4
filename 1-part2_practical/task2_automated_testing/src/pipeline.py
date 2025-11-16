import torch
import numpy as np
from .model import SimpleClassifier
from .utils import normalize_features

def load_model(path, device='cpu'):
    model = SimpleClassifier()
    model.load_state_dict(torch.load(path, map_location=device))
    model.to(device)
    model.eval()
    return model

def predict_from_numpy(model, X_np):
    """
    Preprocess numpy input, run model, return softmax probabilities as numpy array.
    """
    X_norm = normalize_features(X_np)
    X_tensor = torch.from_numpy(X_norm.astype('float32'))
    with torch.no_grad():
        logits = model(X_tensor)
        probs = torch.softmax(logits, dim=1).numpy()
    return probs
