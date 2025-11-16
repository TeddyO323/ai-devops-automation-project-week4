import torch
import torch.nn as nn

class SimpleClassifier(nn.Module):
    """
    Minimal PyTorch classification model for testing purposes.
    Input: tensor of shape (batch_size, input_dim)
    Output: logits tensor of shape (batch_size, num_classes)
    """
    def __init__(self, input_dim=10, num_classes=3):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(input_dim, 32),
            nn.ReLU(),
            nn.Linear(32, num_classes)
        )

    def forward(self, x):
        return self.net(x)
