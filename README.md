# Task-1-News-Topic-Classifier-Using-BERT

A News Topic Classification system built using **BERT (bert-base-uncased)** and fine-tuned on the **AG News** dataset. The model classifies news headlines into one of four categories:

* 🌍 World
* ⚽ Sports
* 💼 Business
* 🔬 Science & Technology

The project includes model training, evaluation, inference, and deployment using **Gradio** and **Streamlit**.

---

## 📌 Project Overview

This project demonstrates how to fine-tune a pre-trained BERT model for multi-class text classification using the Hugging Face Transformers library.

The model learns from thousands of news headlines and predicts the correct topic for unseen headlines.

---

## 🚀 Features

* Fine-tuned **bert-base-uncased**
* Uses the **AG News** dataset
* Four-class news classification
* Accuracy and F1-score evaluation
* Interactive Gradio web interface
* Optional Streamlit deployment
* Easy inference on custom news headlines

---

## 🛠 Technologies Used

* Python
* PyTorch
* Hugging Face Transformers
* Hugging Face Datasets
* Scikit-learn
* Evaluate
* Gradio
* Streamlit (Optional)
* Google Colab


---

## 📊 Dataset

**Dataset:** AG News

The dataset contains approximately:

* **120,000** training samples
* **7,600** testing samples

### Categories

| Label | Category           |
| ----- | ------------------ |
| 0     | World              |
| 1     | Sports             |
| 2     | Business           |
| 3     | Science/Technology |

---

## 📈 Evaluation Metrics

The model is evaluated using:

* Accuracy
* Weighted F1-score

These metrics provide a reliable measure of classification performance on the AG News test dataset.

---

## 🧠 Model

Base Model:

```
bert-base-uncased
```

Fine-tuned using the Hugging Face Trainer API for multi-class sequence classification.

---

## 💡 Example Predictions

| News Headline                      | Predicted Category |
| ---------------------------------- | ------------------ |
| NASA discovers new exoplanet       | Science/Technology |
| Pakistan wins Asia Cup final       | Sports             |
| Stock market closes at record high | Business           |
| UN discusses climate change        | World              |

---

## 📦 Deployment

This project supports two deployment options:

### Gradio

Runs directly inside Google Colab or locally.

### Streamlit

Generate `app.py` from the notebook and deploy it on Streamlit Community Cloud.

---

## 📚 Future Improvements

* Support multilingual news classification
* Fine-tune larger transformer models
* Add confidence scores
* Deploy using Hugging Face Spaces
* Dockerize the application
* REST API using FastAPI

---


