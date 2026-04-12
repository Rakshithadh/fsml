from pydantic import BaseModel

class InputData(BaseModel):
    image_path: str