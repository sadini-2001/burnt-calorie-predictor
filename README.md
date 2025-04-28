# Calories Burnt Prediction App

## 📌 Overview
This is a solo project where I built a machine learning web application that predicts the number of calories burnt based on user input features.  
It uses a highly accurate model (**R² ≈ 0.999**) and is deployed using **Streamlit Cloud**.

## 📊 Dataset
- **Source**: [Kaggle](https://www.kaggle.com/datasets/ruchikakumbhar/calories-burnt-prediction/data)
- **Features**:
  - Age
  - Gender
  - Height
  - Weight
  - Heart Rate
  - Exercise Duration (min)
  - Body Temperature (°C)
    
## 🔎 Exploratory Data Analysis (EDA)
Performed comprehensive EDA to better understand the dataset:
- **Univariate analysis** to explore individual feature distributions
- **Bivariate analysis** to study relationships between variables
- **Correlation heatmap** to visualize feature correlations
- **Outlier detection** using Isolation Forest algorithm

## 🛠️ Model Building
- Preprocessed data (No duplicates and missing values in the oiginal data set)
- Trained multiple regression models (Random Forest and SVR)
- Selected the best-performing model based on R² score (SVR)
- Achieved a **high R² value of 0.999**, indicating excellent model performance

## 🚀 Application
- Developed an interactive web application using **Streamlit**
- Users can input their details (age, weight, heart rate, etc.) to predict calories burnt instantly

## 🌐 Deployment
- Deployed using **Streamlit Cloud** with source code hosted on **GitHub**

## 🔗 Links
- **Live App**: [Click Here](https://burnt-calorie-predictor-hp2zvwkcyednrbpgjc7svd.streamlit.app/)
