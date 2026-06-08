# Customer Churn Prediction

## Overview

Customer churn is one of the most important business challenges in the telecommunications industry. This project uses Machine Learning techniques to identify customers who are likely to leave a telecom service provider and helps support customer retention strategies through predictive analytics.

The project includes:
- Data Understanding
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Model Training
- Model Evaluation
- Interactive Streamlit Dashboard

---

## Dataset

**Telco Customer Churn**

### Dataset Information
- **Customers:** 7,043
- **Features:** 20+
- **Target Variable:** Churn (Yes / No)

The dataset contains customer demographics, subscription information, contract details, billing data, and service usage attributes.

---

## Project Structure

```text
customer-churn-prediction/

├── app/
│   ├── Home.py
│   ├── sidebar_utils.py
│   ├── pages/
│   │   ├── 1_Data_Overview.py
│   │   ├── 2_EDA_Insights.py
│   │   ├── 3_Model_Performance.py
│   │   ├── 4_Churn_Prediction.py
│   │   └── 5_About_Project.py
│   └── assets/
│       ├── diagrams/
│       ├── author_image.jpg
│       ├── churn_banner.png
│       ├── churn_dashboard.png
│       ├── style.css
│       └── telecom.jpg
│
├── data/
│   └── WA_Fn-UseC_-Telco-Customer-Churn.csv
│
├── models/
│   ├── churn_model.pkl
│   ├── feature_columns.pkl
│   ├── lr_model.pkl
│   ├── model_metadata.pkl
│   ├── rf_model.pkl
│   ├── scaler.pkl
│   └── xgb_model.pkl
│
├── notebooks/
│   ├── 01_Data_Understanding_Customer_Churn.ipynb
│   ├── 02_EDA_Customer_Churn.ipynb
│   ├── 03_Feature_Engineering_Customer_Churn.ipynb
│   ├── 04_Model_Training_Customer_Churn.ipynb
│   └── 04_Model_Training_Customer_Churn_v2.ipynb
│
├── reports/
├── requirements.txt
├── save_all_models.py
├── .gitignore
└── README.md
```

---

## Models Trained

Three classification models were trained and compared:

| Model | Algorithm | Type |
|---|---|---|
| **Logistic Regression** | Linear Classification | Baseline |
| **Random Forest** | Ensemble (Tree-based) | Non-linear |
| **XGBoost** | Gradient Boosting | Advanced |

All models were evaluated and compared using the same metrics to identify the best performer for customer churn prediction.

---

## Technologies Used

- **Python**
- **Pandas**
- **NumPy**
- **Scikit-Learn**
- **XGBoost**
- **Plotly**
- **Streamlit**

---

## Key Insights

- **Month-to-month contracts** have the highest churn rate.
- **Customers with short tenure** are more likely to leave.
- **Higher monthly charges** are associated with increased churn.
- **Contract type** is one of the strongest churn predictors.
- **Customer retention efforts** should focus on early-stage customers.

---

## Model Performance

### Evaluation Metrics
- **Accuracy** - Overall correctness of predictions
- **Precision** - Of predicted churners, how many actually churned
- **Recall** - Of actual churners, how many were identified
- **F1 Score** - Harmonic mean of precision and recall

All three models (Logistic Regression, Random Forest, and XGBoost) were evaluated using standard classification metrics, confusion matrix analysis, and feature importance analysis for model interpretability.

---

## Run Locally

### Clone Repository

```bash
git clone https://github.com/M-Abbas-El-Sharif/Customer-Churn-Prediction.git
cd Customer-Churn-Prediction
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Streamlit App

```bash
streamlit run app/Home.py
```

---

## Author

**Mohamed Abbas El Sharif**  
Data Scientist & Machine Learning Engineer

📧 [m.abbaas22@gmail.com](mailto:m.abbaas22@gmail.com)  
📱 +20 101 026 2040  
📍 Cairo, Egypt  
LinkedIn: https://www.linkedin.com/in/m-abbas-el-sharif/  
GitHub: https://github.com/M-Abbas-El-Sharif
