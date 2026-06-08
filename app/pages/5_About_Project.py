import streamlit as st
from sidebar_utils import add_sidebar_author

st.set_page_config(
    page_title="About Project",
    page_icon="📘",
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
📘 About Project
</div>

<div class="hero-subtitle">
Customer Churn Prediction Using Machine Learning
</div>
""", unsafe_allow_html=True)

st.write("")
st.write("")

# =========================
# PROJECT OVERVIEW
# =========================

st.markdown(
    '<p class="section-title">Project Overview</p>',
    unsafe_allow_html=True
)

st.markdown("""
<div class="info-box">

<h4>Business Problem</h4>

<p>
Customer churn is one of the biggest challenges facing telecom companies.
Losing customers directly impacts revenue and growth.

This project aims to identify customers who are likely to leave by
using Machine Learning techniques and predictive analytics.
</p>

</div>
""", unsafe_allow_html=True)

st.write("")

# =========================
# PROJECT OBJECTIVES
# =========================

st.markdown(
    '<p class="section-title">Project Objectives</p>',
    unsafe_allow_html=True
)

st.markdown("""
<div class="info-box">

<ul>
<li>Analyze customer behavior patterns.</li>
<li>Identify factors contributing to churn.</li>
<li>Build predictive machine learning models.</li>
<li>Improve customer retention strategies.</li>
<li>Support data-driven business decisions.</li>
</ul>

</div>
""", unsafe_allow_html=True)

st.write("")

# =========================
# PROJECT WORKFLOW
# =========================

st.markdown(
    '<p class="section-title">Project Workflow</p>',
    unsafe_allow_html=True
)

st.markdown("""
<div class="info-box">

<h4>End-to-End Data Science Workflow</h4>

<ol>
<li>Data Collection</li>
<li>Data Cleaning</li>
<li>Exploratory Data Analysis (EDA)</li>
<li>Feature Engineering</li>
<li>Data Preprocessing</li>
<li>Model Training</li>
<li>Model Evaluation</li>
<li>Deployment with Streamlit</li>
</ol>

</div>
""", unsafe_allow_html=True)

st.write("")

# =========================
# DATASET INFORMATION
# =========================

st.markdown(
    '<p class="section-title">Dataset Information</p>',
    unsafe_allow_html=True
)

c1, c2, c3, c4 = st.columns(4)

cards = [
    ("Customers", "7,043"),
    ("Features", "20"),
    ("Target", "Churn"),
    ("Industry", "Telecom")
]

for col, (title, value) in zip(
    [c1, c2, c3, c4],
    cards
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
# TECHNOLOGY STACK
# =========================

st.markdown(
    '<p class="section-title">Technology Stack</p>',
    unsafe_allow_html=True
)

tech1, tech2, tech3 = st.columns(3)

with tech1:
    st.markdown("""
    <div class="info-box">
    <h4>Data Analysis</h4>

    <ul>
    <li>Python</li>
    <li>Pandas</li>
    <li>NumPy</li>
    </ul>

    </div>
    """, unsafe_allow_html=True)

with tech2:
    st.markdown("""
    <div class="info-box">
    <h4>Machine Learning</h4>

    <ul>
    <li>Scikit-Learn</li>
    <li>XGBoost</li>
    <li>Model Evaluation</li>
    </ul>

    </div>
    """, unsafe_allow_html=True)

with tech3:
    st.markdown("""
    <div class="info-box">
    <h4>Visualization & Deployment</h4>

    <ul>
    <li>Plotly</li>
    <li>Streamlit</li>
    <li>GitHub</li>
    </ul>

    </div>
    """, unsafe_allow_html=True)

st.write("")
st.write("")

# =========================
# KEY FINDINGS
# =========================

st.markdown(
    '<p class="section-title">Key Findings</p>',
    unsafe_allow_html=True
)

st.markdown("""
<div class="info-box">

<ul>
<li>Month-to-month contracts have the highest churn rate.</li>
<li>Customers with shorter tenure are more likely to leave.</li>
<li>Higher monthly charges increase churn risk.</li>
<li>Contract type is one of the strongest predictors.</li>
<li>Customer retention should focus on high-risk segments.</li>
</ul>

</div>
""", unsafe_allow_html=True)

st.write("")

# =========================
# PROJECT IMPACT
# =========================

st.markdown(
    '<p class="section-title">Business Impact</p>',
    unsafe_allow_html=True
)

st.markdown("""
<div class="info-box">

<h4>Expected Benefits</h4>

<ul>
<li>Reduce customer churn.</li>
<li>Increase customer lifetime value.</li>
<li>Improve retention campaigns.</li>
<li>Enhance customer satisfaction.</li>
<li>Support strategic business planning.</li>
</ul>

</div>
""", unsafe_allow_html=True)

st.write("")

# =========================
# FOOTER
# =========================

st.markdown("""
<div style="text-align:center; color:#6B7280; margin-top: 40px;">

Built using Python, Machine Learning, Plotly and Streamlit

</div>
""", unsafe_allow_html=True)

# Add fixed sidebar author card
add_sidebar_author()