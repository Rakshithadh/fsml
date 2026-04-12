from fastapi import FastAPI
from app.schema import InputData
from src.predict import predict
from src.utils import setup_logging
import logging

app = FastAPI()

setup_logging()

@app.post("/predict")
def get_prediction(data: InputData):
    try:
        result = predict(data.image_path)
        logging.info(f"{data.image_path} -> {result}")
        return {"prediction": result}
    except Exception as e:
        logging.error(str(e))
        return {"error": str(e)}