import torch
import torch.nn as nn
import timm
import torchvision.models as models
import logging
from src.features import feature_engineering

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

def train_model(model, train_loader, epochs=10):
    model = model.to(device)

    criterion = nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=1e-4)

    model.train()

    for epoch in range(epochs):
        total_loss = 0

        for images, labels in train_loader:
            images, labels = images.to(device), labels.to(device)

            images = feature_engineering(images)   # ✅ FEATURE USED

            outputs = model(images)
            loss = criterion(outputs, labels)

            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            total_loss += loss.item()

        logging.info(f"Epoch {epoch+1}, Loss: {total_loss}")

    return model


def evaluate(model, loader):
    model.eval()
    correct, total = 0, 0

    with torch.no_grad():
        for images, labels in loader:
            images, labels = images.to(device), labels.to(device)

            images = feature_engineering(images)   # ✅ SAME FEATURE

            outputs = model(images)
            _, preds = torch.max(outputs, 1)

            total += labels.size(0)
            correct += (preds == labels).sum().item()

    return 100 * correct / total


def train_and_select_best(train_loader, val_loader):

    logging.info("Training ViT...")
    vit = timm.create_model('vit_base_patch16_224', pretrained=True)
    vit.head = nn.Linear(vit.head.in_features, 2)
    vit = train_model(vit, train_loader)
    vit_acc = evaluate(vit, val_loader)

    logging.info(f"ViT Accuracy: {vit_acc}")

    logging.info("Training ResNet...")
    resnet = models.resnet18(pretrained=True)
    resnet.fc = nn.Linear(resnet.fc.in_features, 2)
    resnet = train_model(resnet, train_loader)
    resnet_acc = evaluate(resnet, val_loader)

    logging.info(f"ResNet Accuracy: {resnet_acc}")

    if vit_acc > resnet_acc:
        best_model = vit
        best_name = "vit"
    else:
        best_model = resnet
        best_name = "resnet"

    torch.save({
        "model_name": best_name,
        "model_state": best_model.state_dict()
    }, "models/model_v1.pkl")

    logging.info(f"Best model: {best_name} saved!")

    return best_model