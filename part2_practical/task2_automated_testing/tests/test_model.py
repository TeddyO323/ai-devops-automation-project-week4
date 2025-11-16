import torch
from src.model import SimpleClassifier

def test_model_forward_shape():
    model = SimpleClassifier(input_dim=10, num_classes=3)
    x = torch.randn(4, 10)  # batch of 4
    out = model(x)
    assert out.shape == (4, 3), "Expected output shape (batch, num_classes)"

def test_model_deterministic_forward():
    model = SimpleClassifier(input_dim=10, num_classes=3)
    torch.manual_seed(0)
    x = torch.randn(2, 10)
    o1 = model(x).detach().numpy().copy()
    torch.manual_seed(0)
    o2 = model(x).detach().numpy().copy()
    assert (o1 == o2).all(), "Model with same init and input should produce same outputs"
