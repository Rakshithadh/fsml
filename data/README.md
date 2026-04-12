<<<<<<< HEAD
# 📂 Deepfake Detection Dataset

---

## 📌 Overview

This dataset is used for training and evaluating deep learning models for **deepfake image detection**.
It consists of labeled images categorized into **REAL** and **FAKE** classes.

The dataset is a curated subset of a larger dataset (100,000+ images), reduced to improve training efficiency while maintaining class balance.

---

## 📊 Dataset Size

* Original dataset: 100,000+ images
* Current subset used: ~5,000 images

---

## 🗂️ Directory Structure

```
small_dataset/
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

---

## 🧾 Data Split

The dataset is divided into three parts:

* **Train Set** → Used for model training
* **Validation Set** → Used for tuning and evaluation during training
* **Test Set** → Used for final model evaluation

Each split contains two classes:

* `real` → Authentic images
* `fake` → Deepfake/manipulated images

---

## 🖼️ Image Details

* Format: JPG/PNG
* Type: Face images (real and manipulated)
* Labels: Binary classification

  * `0 → REAL`
  * `1 → FAKE`

---

## ⚙️ Preprocessing

The following preprocessing steps are applied before training:

* Image resizing (e.g., 224×224)
* Normalization
* Conversion to tensors

These steps ensure compatibility with models like:

* **ResNet**
* **Vision Transformer (ViT)**

---

## ⚠️ Notes

* The dataset is a **subset** and may not fully represent all types of deepfakes
* Class balance is maintained to avoid bias
* `.idea/` and other IDE files are excluded from the dataset

---

## 🚀 Usage

This dataset is used in:

* Training deep learning models
* Model evaluation and comparison
* Testing prediction pipelines

Example usage:

```
python -m pipeline.pipeline
```

---

## 📌 Future Improvements

* Increase dataset size
* Include more diverse deepfake techniques
* Add metadata (source, method of manipulation)

---

## 👩‍💻 Contributors

* Rakshitha D H
* Nithin Kumar S N
* Bhuvan S Maligi

---
=======
# 📂 Deepfake Detection Dataset

---

## 📌 Overview

This dataset is used for training and evaluating deep learning models for **deepfake image detection**.
It consists of labeled images categorized into **REAL** and **FAKE** classes.

The dataset is a curated subset of a larger dataset (100,000+ images), reduced to improve training efficiency while maintaining class balance.

---

## 📊 Dataset Size

* Original dataset: 100,000+ images
* Current subset used: ~5,000 images

---

## 🗂️ Directory Structure

```
small_dataset/
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

---

## 🧾 Data Split

The dataset is divided into three parts:

* **Train Set** → Used for model training
* **Validation Set** → Used for tuning and evaluation during training
* **Test Set** → Used for final model evaluation

Each split contains two classes:

* `real` → Authentic images
* `fake` → Deepfake/manipulated images

---

## 🖼️ Image Details

* Format: JPG/PNG
* Type: Face images (real and manipulated)
* Labels: Binary classification

  * `0 → REAL`
  * `1 → FAKE`

---

## ⚙️ Preprocessing

The following preprocessing steps are applied before training:

* Image resizing (e.g., 224×224)
* Normalization
* Conversion to tensors

These steps ensure compatibility with models like:

* **ResNet**
* **Vision Transformer (ViT)**

---

## ⚠️ Notes

* The dataset is a **subset** and may not fully represent all types of deepfakes
* Class balance is maintained to avoid bias
* `.idea/` and other IDE files are excluded from the dataset

---

## 🚀 Usage

This dataset is used in:

* Training deep learning models
* Model evaluation and comparison
* Testing prediction pipelines

Example usage:

```
python -m pipeline.pipeline
```

---

## 📌 Future Improvements

* Increase dataset size
* Include more diverse deepfake techniques
* Add metadata (source, method of manipulation)

---

## 👩‍💻 Contributors

* Rakshitha D H
* Nithin Kumar S N
* Bhuvan S Maligi

---
>>>>>>> d2213c6 (Initial commit - Deepfake Detection project)
