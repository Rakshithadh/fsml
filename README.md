# Deepfake Detection 
_ _ _


## 📌 Problem Statement
Deepfake images are digitally manipulated media that can mislead people.
This project aims to classify whether an image is REAL or FAKE using deep learning models such as using **CNN (ResNet) and Vision Transformer (ViT)**.
_ _ _

## 📂 Dataset
- Original dataset: 100,000+ images
- Used subset: ~5,000 images

### Structure:

``` small_dataset/
│
├── Train/
│   ├── real/
│   └── fake/
│
├── Validation/
│   ├── real/
│   └── fake/
│
└── Test/
    ├── real/
    └── fake/
```
_ _ _


## ⚙️ Feature Engineering
- Custom feature engineering applied to images
- Applied consistently in:
    - Training
    - Validation
    - Prediction
_ _ _ 

## 🧠 Models Used

### 1. ResNet (CNN)
- Architecture: **ResNet18**
- Pretrained on ImageNet
- Modified final layer for binary classification

### 2. Vision Transformer (ViT)
- Model: **vit_base_patch16_224**
- Pretrained using timm
- Fine-tuned for classification

_ _ _

## 🔍 Model Comparison
Both models are trained and evaluated on the same dataset.
| Model  | Type        | Accuracy |
|--------|------------|----------|
| ResNet | CNN         | Logged during training |
| ViT    | Transformer | Logged during training |

👉 The best-performing model is automatically selected and saved.

_ _ _

## 🏋️ Training Details
- Epochs: 10
- Batch size: 32
- Loss Function: CrossEntropyLoss
- Optimizer: Adam

_ _ _

## 📊 Evaluation
Accuracy used as evaluation metric
Model performance logged for each epoch

_ _ _ 

## 💾 Model Saving
Best model is saved as: **models/model_v1.pkl**
Saved details include:
    - Model type (ResNet / ViT)
    - Model weights

_ _ _ 

## 🔮 Prediction Pipeline
- Loads the saved best model
- Applies feature engineering
- Predicts:
      - **REAL**
      - **FAKE**
_ _ _

## 🚀 API (FastAPI)
### Run API:
**uvicorn app.app:app --reload**

## Endpoints:
/predict → JSON input prediction
/docs → Swagger UI
_ _ _

## 🐳 Docker
Build image:
    docker build -t deepfake-app .
Run container:
    docker run -p 8000:8000 deepfake-app

    
## 📁 Project Structure
``` project/
│
├── app/
├── src/
├── pipeline/
├── models/
├── logs/
├── Dockerfile
├── requirements.txt
├── README.md
```
_ _ _ 

## ▶️ How to Run
1. Create virtual environment
    python3 -m venv venv
    source venv/bin/activate

2. Install dependencies
    pip install -r requirements.txt

3. Train models
    python -m pipeline.pipeline

4. Run API
    uvicorn app.app:app --reload

_ _ _

## ✅ Output
- Predicts whether an image is **REAL** or **FAKE**
- Best model is used automatically for prediction

_ _ _ 

## 📌 Future Improvements
- Increase dataset size
- Improve feature engineering
- Add more models for comparison
- Deploy to cloud

_ _ _ 

## 👩‍💻 Author
- Rakshitha D H 
- Nithin Kumar S N 
- Bhuvan S Maligi
