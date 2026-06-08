import pandas as pd
import numpy as np
import joblib
import os
from pathlib import Path

from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score,
    f1_score, roc_auc_score
)

# Resolve paths relative to this script's location
PROJECT_DIR = Path(__file__).resolve().parent
DATA_PATH = PROJECT_DIR / 'data' / 'WA_Fn-UseC_-Telco-Customer-Churn.csv'
MODELS_DIR = PROJECT_DIR / 'models'

print("=" * 50)
print("Training all 3 models...")
print("=" * 50)

# 1. Load & Preprocess
df = pd.read_csv(DATA_PATH)
df['TotalCharges'] = df['TotalCharges'].replace(' ', np.nan)
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'])
df['TotalCharges'] = df['TotalCharges'].fillna(0)

df_ml = df.drop('customerID', axis=1)
df_ml['Churn'] = df_ml['Churn'].map({'No': 0, 'Yes': 1})
df_encoded = pd.get_dummies(df_ml, drop_first=True)

X = df_encoded.drop('Churn', axis=1)
y = df_encoded['Churn']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

scaler = StandardScaler()
num_cols = ['tenure', 'MonthlyCharges', 'TotalCharges']
X_train[num_cols] = scaler.fit_transform(X_train[num_cols])
X_test[num_cols] = scaler.transform(X_test[num_cols])

ratio = sum(y_train == 0) / sum(y_train == 1)
print(f"Class ratio (0/1): {ratio:.2f}")

# 2. Map encoded columns to original features
ORIGINAL_FEATURES = [
    'gender', 'SeniorCitizen', 'Partner', 'Dependents',
    'PhoneService', 'MultipleLines', 'InternetService',
    'OnlineSecurity', 'OnlineBackup', 'DeviceProtection',
    'TechSupport', 'StreamingTV', 'StreamingMovies',
    'Contract', 'PaperlessBilling', 'PaymentMethod'
]

encoded_to_original = {}
for col in X.columns:
    matched = False
    for orig in ORIGINAL_FEATURES:
        if col.startswith(orig + '_') or col == orig:
            encoded_to_original[col] = orig
            matched = True
            break
    if not matched:
        encoded_to_original[col] = col

def get_original_importance(model, feature_names, is_lr=False):
    if is_lr:
        importances = np.abs(model.coef_[0])
    else:
        importances = model.feature_importances_
    orig_imp = {}
    for fname, imp in zip(feature_names, importances):
        orig = encoded_to_original[fname]
        orig_imp[orig] = orig_imp.get(orig, 0) + imp
    return sorted(orig_imp.items(), key=lambda x: x[1], reverse=True)

def evaluate(model, X_t, y_t):
    pred = model.predict(X_t)
    prob = model.predict_proba(X_t)[:, 1]
    return {
        'Accuracy': round(float(accuracy_score(y_t, pred)), 4),
        'Precision': round(float(precision_score(y_t, pred)), 4),
        'Recall': round(float(recall_score(y_t, pred)), 4),
        'F1': round(float(f1_score(y_t, pred)), 4),
        'ROC_AUC': round(float(roc_auc_score(y_t, prob)), 4),
    }

# 3. Train Models
print("\nTraining Logistic Regression...")
lr_grid = GridSearchCV(
    LogisticRegression(class_weight='balanced', random_state=42, max_iter=1000),
    {'C': [0.01, 0.1, 1, 10], 'solver': ['liblinear', 'lbfgs']},
    scoring='f1', cv=5, n_jobs=1
)
lr_grid.fit(X_train, y_train)
best_lr = lr_grid.best_estimator_
print(f"  Best params: {lr_grid.best_params_}")

print("Training Random Forest...")
rf_grid = GridSearchCV(
    RandomForestClassifier(class_weight='balanced', random_state=42),
    {'n_estimators': [100, 200], 'max_depth': [5, 10, None], 'min_samples_split': [2, 5]},
    scoring='f1', cv=5, n_jobs=1
)
rf_grid.fit(X_train, y_train)
best_rf = rf_grid.best_estimator_
print(f"  Best params: {rf_grid.best_params_}")

print("Training XGBoost...")
xgb_grid = GridSearchCV(
    XGBClassifier(scale_pos_weight=ratio, random_state=42, eval_metric='logloss'),
    {'n_estimators': [50, 100, 200], 'max_depth': [3, 5, 7], 'learning_rate': [0.01, 0.05, 0.1]},
    scoring='f1', cv=5, n_jobs=1
)
xgb_grid.fit(X_train, y_train)
best_xgb = xgb_grid.best_estimator_
print(f"  Best params: {xgb_grid.best_params_}")

# 4. Feature Importance
feature_names = list(X.columns)
lr_importance = get_original_importance(best_lr, feature_names, is_lr=True)
rf_importance = get_original_importance(best_rf, feature_names)
xgb_importance = get_original_importance(best_xgb, feature_names)

def top_features(importance_list, top_n=10):
    return [f[0] for f in importance_list[:top_n]]

# 5. Save Everything
os.makedirs(MODELS_DIR, exist_ok=True)
joblib.dump(best_lr, os.path.join(MODELS_DIR, 'lr_model.pkl'))
joblib.dump(best_rf, os.path.join(MODELS_DIR, 'rf_model.pkl'))
joblib.dump(best_xgb, os.path.join(MODELS_DIR, 'xgb_model.pkl'))
joblib.dump(best_rf, os.path.join(MODELS_DIR, 'churn_model.pkl'))
joblib.dump(scaler, os.path.join(MODELS_DIR, 'scaler.pkl'))
joblib.dump(feature_names, os.path.join(MODELS_DIR, 'feature_columns.pkl'))

metadata = {
    'Random Forest': {
        'metrics': evaluate(best_rf, X_test, y_test),
        'top_features': top_features(rf_importance),
        'importance': [(f, round(float(v), 4)) for f, v in rf_importance],
    },
    'XGBoost': {
        'metrics': evaluate(best_xgb, X_test, y_test),
        'top_features': top_features(xgb_importance),
        'importance': [(f, round(float(v), 4)) for f, v in xgb_importance],
    },
    'Logistic Regression': {
        'metrics': evaluate(best_lr, X_test, y_test),
        'top_features': top_features(lr_importance),
        'importance': [(f, round(float(v), 4)) for f, v in lr_importance],
    },
}
joblib.dump(metadata, os.path.join(MODELS_DIR, 'model_metadata.pkl'))

# 6. Print Summary
print("\n" + "=" * 50)
print("ALL MODELS SAVED SUCCESSFULLY!")
print("=" * 50)
for name, meta in metadata.items():
    print(f"\n{name}:")
    print(f"   Metrics: {meta['metrics']}")
    print(f"   Top Features: {meta['top_features']}")

print("\nDone!")
