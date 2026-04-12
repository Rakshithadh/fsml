import torch
import timm
import torchvision.models as models
import torch.nn as nn
from PIL import Image
from src.preprocess import get_transforms
from src.features import feature_engineering

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

transform = get_transforms(False)

def load_model():
    checkpoint = torch.load("models/model_v1.pkl", map_location=device)

    if checkpoint["model_name"] == "vit":
        model = timm.create_model('vit_base_patch16_224', pretrained=False)
        model.head = nn.Linear(model.head.in_features, 2)
    else:
        model = models.resnet18(pretrained=False)
        model.fc = nn.Linear(model.fc.in_features, 2)

    model.load_state_dict(checkpoint["model_state"])
    model.to(device)
    model.eval()

    return model

model = load_model()

def predict(image_path):
    image = Image.open(image_path).convert("RGB")

    image = transform(image)
    image = feature_engineering(image)

    image = image.unsqueeze(0).to(device)

    with torch.no_grad():
        output = model(image)
        _, pred = torch.max(output, 1)

    return ["fake", "real"][pred.item()]