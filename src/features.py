import torch

def feature_engineering(image):
    # Feature 1: brightness scaling
    image = image * 1.1

    # Feature 2: clamp values
    image = torch.clamp(image, 0, 1)

    return image