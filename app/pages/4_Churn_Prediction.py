import streamlit as st
import pandas as pd
import joblib
from pathlib import Path
from sidebar_utils import add_sidebar_author

st.set_page_config(
    page_title="Churn Prediction",
    page_icon="🎯",
    layout="wide"
)

# =========================
# PATHS & CSS
# =========================

BASE_DIR = Path(__file__).resolve().parents[2]

with open(BASE_DIR / "app" / "assets" / "style.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

# =========================
# LOAD ALL MODELS
# =========================

models_dict = {
    "🌲 Random Forest (Recommended)": {
        "key": "Random Forest",
        "file": "rf_model.pkl",
    },
    "⚡ XGBoost": {
        "key": "XGBoost",
        "file": "xgb_model.pkl",
    },
    "📊 Logistic Regression": {
        "key": "Logistic Regression",
        "file": "lr_model.pkl",
    },
}

# Try loading multi-model setup, fallback to single model
try:
    loaded_models = {}
    for name, info in models_dict.items():
        loaded_models[name] = joblib.load(
            BASE_DIR / "models" / info["file"]
        )
    model_metadata = joblib.load(
        BASE_DIR / "models" / "model_metadata.pkl"
    )
    multi_model = True
except FileNotFoundError:
    loaded_models = {
        "🌲 Random Forest (Recommended)": joblib.load(
            BASE_DIR / "models" / "churn_model.pkl"
        )
    }
    model_metadata = None
    multi_model = False

feature_columns = joblib.load(
    BASE_DIR / "models" / "feature_columns.pkl"
)

scaler = joblib.load(
    BASE_DIR / "models" / "scaler.pkl"
)

# =========================
# MODEL INFO
# =========================

MODEL_INFO = {
    "Random Forest": {
        "icon": "🌲",
        "name_ar": "الغابة العشوائية",
        "description": "Ensemble of decision trees that votes on the final prediction.",
        "when_to_use": "الخيار الافتراضي والأفضل — أعلى توازن بين الدقة والاستدعاء.",
        "best_for": "Production & Balanced Predictions",
        "strengths": [
            "Highest F1 Score (best balance)",
            "Resistant to overfitting",
            "Handles complex interactions",
        ],
        "weaknesses": [
            "Slower prediction time",
            "Less interpretable",
        ],
        "color": "#10B981",
    },
    "XGBoost": {
        "icon": "⚡",
        "name_ar": "إكس جي بوست",
        "description": "Gradient-boosted trees optimized for catching churning customers.",
        "when_to_use": "عندما يكون اكتشاف أكبر عدد من العملاء المغادرين هو الأولوية.",
        "best_for": "Maximum Churn Detection",
        "strengths": [
            "Highest Recall (catches most churners)",
            "Strong with imbalanced data",
            "State-of-the-art algorithm",
        ],
        "weaknesses": [
            "Lower overall accuracy",
            "Requires careful tuning",
        ],
        "color": "#F59E0B",
    },
    "Logistic Regression": {
        "icon": "📊",
        "name_ar": "الانحدار اللوجستي",
        "description": "Statistical model that calculates churn probability using a linear equation.",
        "when_to_use": "عندما تحتاج تفسير سبب التنبؤ للإدارة أو التقارير الرسمية.",
        "best_for": "Interpretability & Transparency",
        "strengths": [
            "Fully interpretable",
            "Fast predictions",
            "Clear feature impact",
        ],
        "weaknesses": [
            "Cannot capture complex patterns",
            "Lower overall performance",
        ],
        "color": "#6366F1",
    },
}

# =========================
# ALL FEATURE DEFINITIONS
# =========================

ALL_FEATURES = {
    'gender':           {'label': 'Gender',           'type': 'select',       'options': ['Male', 'Female'],                                                                     'default': 'Male',               'group': 'Demographics'},
    'SeniorCitizen':    {'label': 'Senior Citizen',   'type': 'select',       'options': [0, 1],                                                                                  'default': 0,                    'group': 'Demographics'},
    'Partner':          {'label': 'Partner',           'type': 'select',       'options': ['Yes', 'No'],                                                                           'default': 'No',                 'group': 'Demographics'},
    'Dependents':       {'label': 'Dependents',       'type': 'select',       'options': ['Yes', 'No'],                                                                           'default': 'No',                 'group': 'Demographics'},
    'tenure':           {'label': 'Tenure (Months)',   'type': 'slider',       'min': 0, 'max': 72,                                                                               'default': 12,                   'group': 'Demographics'},
    'PhoneService':     {'label': 'Phone Service',    'type': 'select',       'options': ['Yes', 'No'],                                                                           'default': 'Yes',                'group': 'Core Services'},
    'MultipleLines':    {'label': 'Multiple Lines',   'type': 'select',       'options': ['No', 'Yes', 'No phone service'],                                                       'default': 'No',                 'group': 'Core Services'},
    'InternetService':  {'label': 'Internet Service', 'type': 'select',       'options': ['DSL', 'Fiber optic', 'No'],                                                            'default': 'DSL',                'group': 'Core Services'},
    'OnlineSecurity':   {'label': 'Online Security',  'type': 'select',       'options': ['No', 'Yes', 'No internet service'],                                                    'default': 'No',                 'group': 'Core Services'},
    'OnlineBackup':     {'label': 'Online Backup',    'type': 'select',       'options': ['No', 'Yes', 'No internet service'],                                                    'default': 'No',                 'group': 'Core Services'},
    'DeviceProtection': {'label': 'Device Protection','type': 'select',       'options': ['No', 'Yes', 'No internet service'],                                                    'default': 'No',                 'group': 'Extra Services'},
    'TechSupport':      {'label': 'Tech Support',     'type': 'select',       'options': ['No', 'Yes', 'No internet service'],                                                    'default': 'No',                 'group': 'Extra Services'},
    'StreamingTV':      {'label': 'Streaming TV',     'type': 'select',       'options': ['No', 'Yes', 'No internet service'],                                                    'default': 'No',                 'group': 'Extra Services'},
    'StreamingMovies':  {'label': 'Streaming Movies', 'type': 'select',       'options': ['No', 'Yes', 'No internet service'],                                                    'default': 'No',                 'group': 'Extra Services'},
    'Contract':         {'label': 'Contract',         'type': 'select',       'options': ['Month-to-month', 'One year', 'Two year'],                                              'default': 'Month-to-month',     'group': 'Billing & Payment'},
    'PaperlessBilling': {'label': 'Paperless Billing','type': 'select',       'options': ['Yes', 'No'],                                                                           'default': 'Yes',                'group': 'Billing & Payment'},
    'PaymentMethod':    {'label': 'Payment Method',   'type': 'select',       'options': ['Electronic check', 'Mailed check', 'Bank transfer (automatic)', 'Credit card (automatic)'], 'default': 'Electronic check', 'group': 'Billing & Payment'},
    'MonthlyCharges':   {'label': 'Monthly Charges',  'type': 'slider_float', 'min': 0.0, 'max': 150.0,                                                                          'default': 70.0,                 'group': 'Billing & Payment'},
    'TotalCharges':     {'label': 'Total Charges',    'type': 'number',       'min': 0.0,                                                                                         'default': 1000.0,               'group': 'Billing & Payment'},
}

# =========================
# HERO
# =========================

st.markdown("""
<div class="hero-title">
🎯 Customer Churn Prediction
</div>

<div class="hero-subtitle">
Predict whether a telecom customer is likely to leave
</div>
""", unsafe_allow_html=True)

st.write("")

# =========================
# MODEL SELECTOR
# =========================

st.markdown(
    '<p class="section-title">Select Prediction Model</p>',
    unsafe_allow_html=True
)

model_names = list(loaded_models.keys())
selected_model_name = st.selectbox(
    "🤖 Choose a Model",
    model_names,
    index=0,
    label_visibility="collapsed"
)

# Get model info
if multi_model:
    meta_key = models_dict[selected_model_name]["key"]
    info = MODEL_INFO[meta_key]
    meta = model_metadata[meta_key]
    top_features = meta["top_features"]
    metrics = meta["metrics"]
else:
    meta_key = "Random Forest"
    info = MODEL_INFO["Random Forest"]
    top_features = list(ALL_FEATURES.keys())
    metrics = None

model = loaded_models[selected_model_name]

# =========================
# MODEL INFO CARD
# =========================

strengths_html = "".join(
    [f'<span style="background:#ECFDF5; color:#065F46; padding:3px 10px; border-radius:20px; font-size:12px; margin:2px;">✅ {s}</span>' for s in info["strengths"]]
)
weaknesses_html = "".join(
    [f'<span style="background:#FEF2F2; color:#991B1B; padding:3px 10px; border-radius:20px; font-size:12px; margin:2px;">⚠️ {w}</span>' for w in info["weaknesses"]]
)

border_color = info['color']

st.markdown(f"""
<div style="background:#FFFFFF; border-radius:16px; padding:24px; box-shadow:0 4px 15px rgba(0,0,0,0.06); border-left:5px solid {border_color}; margin-bottom:20px;">
    <div style="display:flex; align-items:center; gap:12px; margin-bottom:8px;">
        <span style="font-size:32px;">{info['icon']}</span>
        <div>
            <div style="font-size:22px; font-weight:700; color:#163B65;">{meta_key}</div>
            <div style="font-size:13px; color:#6B7280;">{info['description']}</div>
        </div>
    </div>
    <div style="background:#EEF4FF; border-radius:10px; padding:10px 16px; margin:10px 0;">
        <span style="font-size:13px; font-weight:600; color:#2563EB;">🎯 Best For: {info['best_for']}</span>
        <span style="font-size:13px; color:#4B5563; margin-left:12px;">{info['when_to_use']}</span>
    </div>
    <div style="display:flex; gap:6px; flex-wrap:wrap; margin-top:8px;">
        {strengths_html} {weaknesses_html}
    </div>
</div>
""", unsafe_allow_html=True)

# Model Metrics - separate block
if metrics:
    acc_val = f"{metrics['Accuracy']:.1%}"
    rec_val = f"{metrics['Recall']:.1%}"
    f1_val = f"{metrics['F1']:.1%}"
    roc_val = f"{metrics['ROC_AUC']:.1%}"

    mc1, mc2, mc3, mc4 = st.columns(4)
    with mc1:
        st.markdown(f'<div class="kpi-card"><div class="kpi-title">Accuracy</div><div class="kpi-value" style="font-size:28px;">{acc_val}</div></div>', unsafe_allow_html=True)
    with mc2:
        st.markdown(f'<div class="kpi-card"><div class="kpi-title">Recall</div><div class="kpi-value" style="font-size:28px;">{rec_val}</div></div>', unsafe_allow_html=True)
    with mc3:
        st.markdown(f'<div class="kpi-card"><div class="kpi-title">F1 Score</div><div class="kpi-value" style="font-size:28px;">{f1_val}</div></div>', unsafe_allow_html=True)
    with mc4:
        st.markdown(f'<div class="kpi-card"><div class="kpi-title">ROC AUC</div><div class="kpi-value" style="font-size:28px;">{roc_val}</div></div>', unsafe_allow_html=True)

# =========================
# DYNAMIC FEATURE INPUTS
# =========================

st.markdown(
    '<p class="section-title">Customer Information</p>',
    unsafe_allow_html=True
)

# Show note about which features this model uses
feature_count = len(top_features)
total_count = len(ALL_FEATURES)

st.markdown(f"""
<div style="background:#EEF4FF; border-radius:10px; padding:10px 16px; margin-bottom:16px; font-size:14px; color:#163B65;">
    💡 <strong>{meta_key}</strong> uses <strong>{feature_count}</strong> key features out of {total_count} total.
    Only the most impactful features are shown below.
</div>
""", unsafe_allow_html=True)

# Group features by category
groups = {}
for feat in top_features:
    if feat in ALL_FEATURES:
        feat_info = ALL_FEATURES[feat]
        group = feat_info['group']
        if group not in groups:
            groups[group] = []
        groups[group].append(feat)

# Define group icons
GROUP_ICONS = {
    'Demographics': '👤',
    'Core Services': '📡',
    'Extra Services': '🛡️',
    'Billing & Payment': '💳',
}

# Render inputs in dynamic columns
values = {}
num_groups = len(groups)
cols = st.columns(min(num_groups, 4))

for i, (group_name, features) in enumerate(groups.items()):
    col_idx = i % min(num_groups, 4)
    with cols[col_idx]:
        icon = GROUP_ICONS.get(group_name, '📌')
        st.markdown(
            f'<p style="color:#163B65; font-size:16px; font-weight:700; margin-bottom:8px;">'
            f'{icon} {group_name}</p>',
            unsafe_allow_html=True
        )

        for feat in features:
            feat_info = ALL_FEATURES[feat]
            widget_key = f"{feat}_{meta_key}"

            if feat_info['type'] == 'select':
                values[feat] = st.selectbox(
                    feat_info['label'],
                    feat_info['options'],
                    key=widget_key
                )
            elif feat_info['type'] == 'slider':
                values[feat] = st.slider(
                    feat_info['label'],
                    feat_info['min'],
                    feat_info['max'],
                    feat_info['default'],
                    key=widget_key
                )
            elif feat_info['type'] == 'slider_float':
                values[feat] = st.slider(
                    feat_info['label'],
                    feat_info['min'],
                    feat_info['max'],
                    feat_info['default'],
                    key=widget_key
                )
            elif feat_info['type'] == 'number':
                values[feat] = st.number_input(
                    feat_info['label'],
                    min_value=feat_info['min'],
                    value=feat_info['default'],
                    key=widget_key
                )

# Fill defaults for features NOT shown
for feat, feat_info in ALL_FEATURES.items():
    if feat not in values:
        values[feat] = feat_info['default']

# =========================
# PREDICTION
# =========================

if st.button("🔮 Predict Churn Risk"):

    # Build full customer DataFrame with ALL features
    customer = pd.DataFrame([{
        "gender": values['gender'],
        "SeniorCitizen": values['SeniorCitizen'],
        "Partner": values['Partner'],
        "Dependents": values['Dependents'],
        "tenure": values['tenure'],
        "PhoneService": values['PhoneService'],
        "MultipleLines": values['MultipleLines'],
        "InternetService": values['InternetService'],
        "OnlineSecurity": values['OnlineSecurity'],
        "OnlineBackup": values['OnlineBackup'],
        "DeviceProtection": values['DeviceProtection'],
        "TechSupport": values['TechSupport'],
        "StreamingTV": values['StreamingTV'],
        "StreamingMovies": values['StreamingMovies'],
        "Contract": values['Contract'],
        "PaperlessBilling": values['PaperlessBilling'],
        "PaymentMethod": values['PaymentMethod'],
        "MonthlyCharges": values['MonthlyCharges'],
        "TotalCharges": values['TotalCharges'],
    }])

    customer_encoded = pd.get_dummies(
        customer
    )

    customer_encoded = customer_encoded.reindex(
        columns=feature_columns,
        fill_value=0
    )

    # Scale numerical columns
    num_cols = ["tenure", "MonthlyCharges", "TotalCharges"]
    customer_encoded[num_cols] = scaler.transform(
        customer_encoded[num_cols]
    )

    prediction = model.predict(
        customer_encoded
    )[0]

    probability = model.predict_proba(
        customer_encoded
    )[0][1]

    st.write("")
    st.markdown(
        '<p class="section-title">Prediction Result</p>',
        unsafe_allow_html=True
    )

    if prediction == 1:

        st.error(
            f"""
            ⚠️ High Churn Risk

            Probability:
            {probability:.1%}
            """
        )

    else:

        st.success(
            f"""
            ✅ Low Churn Risk

            Probability:
            {probability:.1%}
            """
        )

    st.write("")

    risk_percent = round(
        probability * 100,
        1
    )

    # Result cards
    col_r1, col_r2 = st.columns(2)

    with col_r1:
        risk_color = "#EF4444" if risk_percent >= 50 else "#10B981"
        st.markdown(
            f"""<div class="kpi-card">
<div class="kpi-title">
Churn Probability
</div>
<div class="kpi-value" style="color:{risk_color};">
{risk_percent}%
</div>
</div>""",
            unsafe_allow_html=True
        )

    with col_r2:
        st.markdown(
            f"""<div class="kpi-card">
<div class="kpi-title">
Model Used
</div>
<div class="kpi-value" style="font-size:24px;">
{info['icon']} {meta_key}
</div>
</div>""",
            unsafe_allow_html=True
        )

    st.write("")

    # =========================
    # RECOMMENDATIONS
    # =========================

    st.markdown(
        '<p class="section-title">Retention Recommendation</p>',
        unsafe_allow_html=True
    )

    if probability >= 0.70:

        st.markdown("""<div class="info-box">
<h4>🔴 High Priority Customer</h4>
<ul>
<li>Offer retention discount.</li>
<li>Provide loyalty incentives.</li>
<li>Assign customer success follow-up.</li>
<li>Review contract renewal options.</li>
</ul>
</div>""", unsafe_allow_html=True)

    elif probability >= 0.40:

        st.markdown("""<div class="info-box">
<h4>🟡 Medium Risk Customer</h4>
<ul>
<li>Send personalized offers.</li>
<li>Improve engagement campaigns.</li>
<li>Promote long-term contracts.</li>
</ul>
</div>""", unsafe_allow_html=True)

    else:

        st.markdown("""<div class="info-box">
<h4>🟢 Low Risk Customer</h4>
<ul>
<li>Maintain customer satisfaction.</li>
<li>Monitor usage trends.</li>
<li>Promote premium services.</li>
</ul>
</div>""", unsafe_allow_html=True)

# =========================
# ABOUT THIS TOOL
# =========================

st.write("")
st.write("")

st.markdown(
    '<p class="section-title">About This Tool</p>',
    unsafe_allow_html=True
)

st.markdown("""
<div class="info-box">

This page uses trained Machine Learning models
to estimate the probability that a customer will churn.

Choose between <strong>Random Forest</strong>, <strong>XGBoost</strong>,
or <strong>Logistic Regression</strong> — each optimized for
different business scenarios.

The prediction adapts to show only the features
most impactful for the selected model.

</div>
""", unsafe_allow_html=True)

# Add fixed sidebar author card
add_sidebar_author()