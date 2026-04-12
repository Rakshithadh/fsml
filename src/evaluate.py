import torch
from sklearn.metrics import confusion_matrix
import logging
from src.features import feature_engineering

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

def evaluate_model(model, test_loader):
    model.eval()

    y_true = []
    y_pred = []

    with torch.no_grad():
        for images, labels in test_loader:
            images = images.to(device)

            images = feature_engineering(images)

            outputs = model(images)
            _, preds = torch.max(outputs, 1)

            y_true.extend(labels.numpy())
            y_pred.extend(preds.cpu().numpy())

    cm = confusion_matrix(y_true, y_pred)

    logging.info(f"Confusion Matrix:\n{cm}")
    print("Confusion Matrix:\n", cm)