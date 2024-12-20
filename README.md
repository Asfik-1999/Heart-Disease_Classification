

---

# 🎯 **Heart Disease Classification**  

![GitHub repo size](https://img.shields.io/github/repo-size/Asfik-1999/Heart-Disease_Classification)  
![GitHub last commit](https://img.shields.io/github/last-commit/Asfik-1999/Heart-Disease_Classification)  
![GitHub issues](https://img.shields.io/github/issues/Asfik-1999/Heart-Disease_Classification)  
![GitHub license](https://img.shields.io/github/license/Asfik-1999/Heart-Disease_Classification)  

---

## 🌟 **Overview**

Heart disease is a critical global health issue. This project leverages machine learning to develop a reliable classification system to predict heart disease based on medical attributes such as age, cholesterol, and resting blood pressure. The following classifiers are used:  
- 🔹 **K-Nearest Neighbors (KNN)**  
- 🔹 **Decision Tree**  
- 🔹 **Naive Bayes**  
- 🔹 **Support Vector Machine (SVM)**  

---

## 📚 **Features**

✔️ Preprocesses and normalizes the data for consistency.  
✔️ Implements and compares the performance of multiple classifiers.  
✔️ Evaluates results using metrics like accuracy, precision, recall, and F1-score.  
✔️ Visualizes results with confusion matrices and accuracy comparison charts.  

---

## 🗂️ **Dataset**

The dataset used is from the **UCI Machine Learning Repository**. It contains patient records with attributes like age, sex, cholesterol, and target (indicating heart disease presence).  

🔗 [Heart Disease Dataset - UCI](https://archive.ics.uci.edu/dataset/45/heart+disease)  

---

## ⚙️ **Setup Instructions**

### Step 1: Clone the Repository  
```bash
git clone https://github.com/Asfik-1999/Heart-Disease_Classification.git
cd Heart-Disease_Classification
```

### Step 2: Create a Virtual Environment  
```bash
python -m venv venv
source venv/bin/activate  # For Linux/macOS
venv\Scripts\activate     # For Windows
```

### Step 3: Install Dependencies  
```bash
pip install pandas scikit-learn matplotlib seaborn
```

---

## 🚀 **Run the Project**

1. Ensure the cleaned dataset (`heart_disease_cleaned.csv`) is in the project directory.  
2. Execute the Python script to preprocess the data, train classifiers, and evaluate models:  
   ```bash
   python classification.py
   ```
3. View the results:  
   - Confusion matrices for each classifier.  
   - Accuracy metrics printed in the terminal.  
   - A bar chart comparing classifier accuracy.  

---

## 📊 **Results**

| **Model**       | **Accuracy (%)** | **Precision** | **Recall** | **F1 Score** |
|------------------|------------------|---------------|------------|--------------|
| **KNN**         | 85.5             | 0.86          | 0.85       | 0.85         |
| **Decision Tree**| 83.0             | 0.83          | 0.83       | 0.83         |
| **Naive Bayes**  | 81.0             | 0.82          | 0.81       | 0.81         |
| **SVM**          | 90.0             | 0.91          | 0.90       | 0.90         |



---

## 📝 **References**

1. UCI Machine Learning Repository: [Heart Disease Dataset](https://archive.ics.uci.edu/dataset/45/heart+disease)  
2. Scikit-learn Documentation: [https://scikit-learn.org/stable/](https://scikit-learn.org/stable/)  

---

## 📜 **License**

This project is licensed under the MIT License. Feel free to use and modify the code as needed.  

---
