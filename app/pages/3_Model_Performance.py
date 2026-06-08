import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from sidebar_utils import add_sidebar_author

st.set_page_config(
    page_title="Model Performance",
    page_icon="🤖",
    layout="wide"
)

# =========================
# LOAD CSS
# =========================

with open("app/assets/style.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

# =========================
# HERO SECTION
# =========================

st.markdown("""
<div class="hero-title">
🤖 Model Performance
</div>

<div class="hero-subtitle">
Machine Learning Evaluation & Performance Metrics
</div>
""", unsafe_allow_html=True)

st.write("")

# =========================
# MODEL RESULTS
# =========================

accuracy = 76.1
precision = 53.4
recall = 78.3
f1_score = 63.5

# =========================
# KPI CARDS
# =========================

c1, c2, c3, c4 = st.columns(4)

metrics = [
    ("Accuracy", f"{accuracy}%"),
    ("Precision", f"{precision}%"),
    ("Recall", f"{recall}%"),
    ("F1 Score", f"{f1_score}%")
]

for col, (title, value) in zip(
    [c1, c2, c3, c4],
    metrics
):
    with col:
        st.markdown(
            f"""
            <div class="kpi-card">
                <div class="kpi-title">{title}</div>
                <div class="kpi-value">{value}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

st.write("")
st.write("")

# =========================
# PERFORMANCE METRICS
# =========================

st.markdown(
    '<p class="section-title">Performance Metrics Comparison</p>',
    unsafe_allow_html=True
)

metrics_df = pd.DataFrame({
    "Metric": [
        "Accuracy",
        "Precision",
        "Recall",
        "F1 Score"
    ],
    "Score": [
        accuracy,
        precision,
        recall,
        f1_score
    ]
})

fig = px.bar(
    metrics_df,
    x="Metric",
    y="Score",
    text="Score",
    color="Metric",
    color_discrete_sequence=[
        "#2563EB",
        "#3B82F6",
        "#60A5FA",
        "#93C5FD"
    ]
)

fig.update_traces(
    textposition="inside",
    textfont=dict(
        size=20,
        color="white",
        family="Arial Black"
    )
)

fig.update_layout(
    height=500,
    showlegend=False,
    paper_bgcolor="#F5F7FB",
    plot_bgcolor="white",
    font=dict(
        size=18,
        color="#1F2937"
    ),
    xaxis_title="Metric",
    yaxis_title="Score (%)"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.write("")

# =========================
# CONFUSION MATRIX
# =========================

st.markdown(
    '<p class="section-title">Confusion Matrix</p>',
    unsafe_allow_html=True
)

conf_matrix = [
    [779, 256],
    [81, 293]
]

fig = px.imshow(
    conf_matrix,
    text_auto=True,
    color_continuous_scale="Blues",
    x=[
        "Predicted No",
        "Predicted Yes"
    ],
    y=[
        "Actual No",
        "Actual Yes"
    ]
)

fig.update_layout(
    height=600,
    paper_bgcolor="#F5F7FB",
    font=dict(
        size=18
    )
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.markdown("""
<div class="info-box">
Most customers were classified correctly.
False negatives remain the primary area for improvement.
</div>
""", unsafe_allow_html=True)

st.write("")

# =========================
# ROC CURVE
# =========================

st.markdown(
    '<p class="section-title">ROC Curve</p>',
    unsafe_allow_html=True
)

fpr = [0.0, 0.055, 0.126, 0.222, 0.393, 0.992, 1.0]
tpr = [0.0, 0.393, 0.586, 0.741, 0.888, 1.0, 1.0]

fig = go.Figure()

fig.add_trace(
    go.Scatter(
        x=fpr,
        y=tpr,
        mode="lines",
        name="Random Forest (Tuned)",
        line=dict(
            width=4,
            color="#2563EB"
        )
    )
)

fig.add_trace(
    go.Scatter(
        x=[0, 1],
        y=[0, 1],
        mode="lines",
        name="Random",
        line=dict(
            dash="dash",
            color="gray"
        )
    )
)

fig.update_layout(
    height=500,
    paper_bgcolor="#F5F7FB",
    plot_bgcolor="white",
    xaxis_title="False Positive Rate",
    yaxis_title="True Positive Rate",
    font=dict(
        size=18
    )
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.write("")

# =========================
# FEATURE IMPORTANCE
# =========================

st.markdown(
    '<p class="section-title">Top Feature Importance</p>',
    unsafe_allow_html=True
)

importance_df = pd.DataFrame({
    "Feature": [
        "tenure",
        "Contract",
        "TotalCharges",
        "MonthlyCharges",
        "InternetService",
        "PaymentMethod",
        "OnlineSecurity",
        "TechSupport"
    ],
    "Importance": [
        0.18,
        0.15,
        0.14,
        0.10,
        0.08,
        0.06,
        0.04,
        0.03
    ]
})

fig = px.bar(
    importance_df,
    x="Importance",
    y="Feature",
    orientation="h",
    text="Importance",
    color="Importance",
    color_continuous_scale="Blues"
)

fig.update_traces(
    textposition="outside"
)

fig.update_layout(
    height=600,
    paper_bgcolor="#F5F7FB",
    plot_bgcolor="white",
    font=dict(
        size=18
    ),
    coloraxis_showscale=False
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.write("")

# =========================
# MODEL SUMMARY
# =========================

st.markdown(
    '<p class="section-title">Model Summary</p>',
    unsafe_allow_html=True
)

st.markdown("""
<div class="info-box">

<h4>Best Model: Tuned Random Forest</h4>

<ul>
<li>Robust handling of class imbalance (Recall improved from 51.6% to 78.3%).</li>
<li>Optimized using GridSearchCV to maximize F1-score (0.635).</li>
<li>Strong and balanced predictive power across both classes.</li>
<li>Tenure and contract type remain the strongest predictors.</li>
<li>Highly suitable for production deployment to prevent customer churn.</li>

</ul>

</div>
""", unsafe_allow_html=True)

# Add fixed sidebar author card
add_sidebar_author()