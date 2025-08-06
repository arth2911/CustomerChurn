# CostumerChurnML
# 📉 Customer Churn Prediction with Explainable AI

Predicting customer churn using machine learning models with built-in interpretability to support data-driven business decisions.

---

## 📌 Overview

This project aims to predict whether a customer is likely to churn using a combination of traditional ML algorithms and modern explainability techniques. The goal is not only to achieve high accuracy but also to provide transparent and actionable insights into *why* a customer may leave.

---

## 🚀 Features

- Predictive models: Logistic Regression, XGBoost, and Neural Networks
- Model explainability using **SHAP** and **LIME**
- Interactive web dashboard with **Streamlit**
- Data preprocessing & EDA with visualization
- Performance metrics: ROC-AUC, confusion matrix, precision-recall
- Deployed on **AWS EC2**

---

## 🧠 Tech Stack

- **Languages**: Python
- **Libraries**: pandas, numpy, scikit-learn, xgboost, shap, lime, matplotlib, seaborn, streamlit
- **Deployment**: Streamlit on AWS EC2
- **Explainability**: SHAP, LIME

---

## 📊 Dataset

- **Source**: [Telco Customer Churn Dataset](https://www.kaggle.com/blastchar/telco-customer-churn)
- **Size**: ~7,000 customer records
- **Target**: `Churn` (Yes/No)

---

## 📈 Model Performance

| Model               | ROC-AUC Score |
|--------------------|---------------|
| Logistic Regression| 0.80          |
| XGBoost            | 0.88          |
| Neural Network     | 0.86          |

---

## 🔍 Explainability Insights

- **SHAP Summary Plots** show that contract type, tenure, and monthly charges are the strongest indicators of churn.
- **LIME** provides local interpretability for individual customer predictions on the dashboard.

---

## 🖥️ Web App Preview

A simple and intuitive **Streamlit dashboard** for:
- Real-time churn prediction
- SHAP visualizations for each prediction
- User-friendly interface

![App Screenshot](demo/screenshot.png) *(Add your screenshot here)*

---

## 📁 Project Structure

