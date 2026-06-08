import streamlit as st
from sidebar_utils import add_sidebar_author

st.set_page_config(
    page_title="Customer Churn Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load CSS
with open("app/assets/style.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

# Hero Section (Now at the very top)
st.markdown(
    """
    <div class="hero-title">
        📊 Telecom Customer Churn Dashboard
    </div>

    <div class="hero-subtitle">
        Customer Retention Analytics & Churn Prediction System
    </div>
    """,
    unsafe_allow_html=True
)

st.write("")

# Banner (Now below the title, centered and smaller)
col_space1, col_img, col_space2 = st.columns([1, 3, 1])
with col_img:
    st.image(
         "app/assets/churn_banner.png",
         use_container_width=True
    )

st.write("")
st.write("")

# KPI Cards
c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown(
        """
        <div class="kpi-card">
            <div class="kpi-title">Customers</div>
            <div class="kpi-value">7,043</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with c2:
    st.markdown(
        """
        <div class="kpi-card">
            <div class="kpi-title">Features</div>
            <div class="kpi-value">20</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with c3:
    st.markdown(
        """
        <div class="kpi-card">
            <div class="kpi-title">Target</div>
            <div class="kpi-value">Churn</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with c4:
    st.markdown(
        """
        <div class="kpi-card">
            <div class="kpi-title">Best Model</div>
            <div class="kpi-value">Random Forest</div>
        </div>
        """,
        unsafe_allow_html=True
    )

st.write("")
st.write("")

# Business Problem
st.markdown(
    '<p class="section-title">Business Problem</p>',
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="info-box">
        Telecom companies lose revenue when customers leave.
        <br><br>
        This project predicts churn risk and helps identify customers who require proactive retention actions.
    </div>
    """,
    unsafe_allow_html=True
)

st.write("")

# Workflow
st.markdown(
    '<p class="section-title">Project Workflow</p>',
    unsafe_allow_html=True
)

st.markdown("""
1. Data Understanding

2. Exploratory Data Analysis

3. Feature Engineering

4. Model Training

5. Model Evaluation

6. Customer Churn Prediction
""")

st.write("")

# Technology Stack
st.markdown(
    '<p class="section-title">Technology Stack</p>',
    unsafe_allow_html=True
)

t1, t2, t3, t4, t5 = st.columns(5)

with t1:
    st.success("Python")

with t2:
    st.success("Pandas")

with t3:
    st.success("Scikit-Learn")

with t4:
    st.success("XGBoost")

with t5:
    st.success("Streamlit")

st.write("")

# Footer
st.markdown("""
<div style="text-align:center; color:#6B7280; margin-top: 40px;">

Built using Python, Machine Learning, Plotly and Streamlit

</div>
""", unsafe_allow_html=True)

# Add fixed sidebar author card
add_sidebar_author()