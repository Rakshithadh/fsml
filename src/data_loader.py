from torchvision import datasets
from torch.utils.data import DataLoader
from src.preprocess import get_transforms

def get_data_loaders(data_path="data/small_dataset"):

    train_data = datasets.ImageFolder(
        f"{data_path}/Train",
        transform=get_transforms(True)
    )

    val_data = datasets.ImageFolder(
        f"{data_path}/Validation",
        transform=get_transforms(False)
    )

    test_data = datasets.ImageFolder(
        f"{data_path}/Test",
        transform=get_transforms(False)
    )

    train_loader = DataLoader(train_data, batch_size=16, shuffle=True)
    val_loader   = DataLoader(val_data, batch_size=16)
    test_loader  = DataLoader(test_data, batch_size=16)

    return train_loader, val_loader, test_loader