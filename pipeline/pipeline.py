from src.utils import setup_logging
import logging
from src.data_loader import get_data_loaders
from src.train import train_and_select_best
from src.evaluate import evaluate_model

def run_pipeline():
    setup_logging()

    logging.info("Pipeline started")

    train_loader, val_loader, test_loader = get_data_loaders()

    model = train_and_select_best(train_loader, val_loader)

    evaluate_model(model, test_loader)

    logging.info("Pipeline completed")

if __name__ == "__main__":
    run_pipeline()