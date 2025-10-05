# 🌲 Forest Cover Type Classification

## Project Overview

This is a **high-dimensional multi-class classification** project dedicated to accurately predicting one of seven forest cover types using 54 intricate geographic and environmental features. The solution involves rigorously comparing three robust classification models to ensure the highest predictive accuracy for environmental analysis.

---

## ⚙️ Technologies and Libraries Used

* **Python 3.x**
* **Pandas:** For data manipulation and analysis.
* **Matplotlib & Seaborn:** For data visualization.
* **Scikit-learn (sklearn):** For core machine learning tasks.

---

## 📁 Dataset Details

The dataset contains detailed information across 54 features, aiming to predict **7 distinct forest cover types**.

| Feature | Description |
| :--- | :--- |
| **Input Features** | 10 quantitative features (Elevation, Slope, etc.) and 44 binary features (Wilderness, Soil Type). |
| **Target Variable** | Cover Type (One of 7 classes). |

> 📂 File used: `covtype.csv` or similar dataset.

---

## 🔧 Steps Performed

1.  **Data Preparation** 🧹
    * Handled the large dataset size and verified data quality.
    * Applied **StandardScaler** to normalize numerical features.
    * Split the dataset into training and testing sets.

2.  **Model Comparison** 🧠
    * Evaluated three powerful classification models: **Logistic Regression**, **Decision Trees**, and **Random Forest Classifier**.

3.  **Comprehensive Evaluation** ⭐
    * Model performance was thoroughly validated using advanced metrics: **Accuracy Score**, **Confusion Matrix**, and the **Classification Report** (Precision, Recall, F1-Score).

---

## 📦 Libraries Used

```bash
pandas
matplotlib.pyplot
seaborn
sklearn.model_selection (train_test_split)
sklearn.preprocessing (StandardScaler)
sklearn.linear_model (LogisticRegression)
sklearn.tree (DecisionTreeClassifier)
sklearn.ensemble (RandomForestClassifier)
sklearn.metrics (accuracy_score, confusion_matrix, classification_report)
