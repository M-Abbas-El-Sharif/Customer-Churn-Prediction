import streamlit as st
import pandas as pd
import plotly.express as px
from sidebar_utils import add_sidebar_author

st.set_page_config(
    page_title="EDA Insights",
    page_icon="📊",
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
# LOAD DATA
# =========================

df = pd.read_csv(
    "data/WA_Fn-UseC_-Telco-Customer-Churn.csv"
)

# =========================
# HERO SECTION
# =========================

st.markdown("""
<div class="hero-title">
📊 EDA Insights
</div>

<div class="hero-subtitle">
Exploratory Data Analysis & Business Insights
</div>
""", unsafe_allow_html=True)

st.write("")

# =========================
# KPI CARDS
# =========================

avg_monthly = round(df["MonthlyCharges"].mean(), 1)
avg_tenure = round(df["tenure"].mean(), 1)

churn_rate = round(
    df["Churn"].value_counts(normalize=True)["Yes"] * 100,
    1
)

senior_pct = round(
    df["SeniorCitizen"].mean() * 100,
    1
)

c1, c2, c3, c4 = st.columns(4)

cards = [
    ("Avg Monthly Charges", f"${avg_monthly}"),
    ("Avg Tenure", avg_tenure),
    ("Churn Rate", f"{churn_rate}%"),
    ("Senior Citizens", f"{senior_pct}%")
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
# CHURN DISTRIBUTION
# =========================

st.markdown(
    '<p class="section-title">Customer Churn Distribution</p>',
    unsafe_allow_html=True
)

churn_counts = df["Churn"].value_counts()

fig = px.bar(
    x=churn_counts.index,
    y=churn_counts.values,
    text=churn_counts.values,
    color=churn_counts.index,
    color_discrete_map={
        "No": "#60A5FA",
        "Yes": "#2563EB"
    }
)

fig.update_traces(
    textposition="inside",
    textfont=dict(
        size=24,
        color="white",
        family="Arial Black"
    )
)

fig.update_layout(
    height=450,
    showlegend=False,
    paper_bgcolor="#F5F7FB",
    plot_bgcolor="white",
    font=dict(size=18),
    xaxis_title="Customer Status",
    yaxis_title="Customers"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# =========================
# GENDER VS CHURN
# =========================

st.markdown(
    '<p class="section-title">Gender vs Churn</p>',
    unsafe_allow_html=True
)

fig = px.histogram(
    df,
    x="gender",
    color="Churn",
    barmode="group",
    text_auto=True,
    color_discrete_map={
        "No": "#60A5FA",
        "Yes": "#2563EB"
    }
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
    height=450,
    paper_bgcolor="#F5F7FB",
    plot_bgcolor="white",
    font=dict(size=18),
    xaxis_title="Gender",
    yaxis_title="Customers"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.markdown("""
<div class="info-box">
Male and Female customers show similar churn behavior.
</div>
""", unsafe_allow_html=True)

st.write("")

# =========================
# CONTRACT VS CHURN
# =========================

st.markdown(
    '<p class="section-title">Contract Type vs Churn</p>',
    unsafe_allow_html=True
)

fig = px.histogram(
    df,
    x="Contract",
    color="Churn",
    barmode="group",
    text_auto=True,
    color_discrete_map={
        "No": "#60A5FA",
        "Yes": "#2563EB"
    }
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
    paper_bgcolor="#F5F7FB",
    plot_bgcolor="white",
    font=dict(size=18),
    xaxis_title="Contract Type",
    yaxis_title="Customers"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.markdown("""
<div class="info-box">
Month-to-Month customers have the highest churn rate.
Long-term contracts retain customers significantly better.
</div>
""", unsafe_allow_html=True)

st.write("")

# =========================
# TENURE DISTRIBUTION
# =========================

st.markdown(
    '<p class="section-title">Tenure Distribution</p>',
    unsafe_allow_html=True
)

fig = px.histogram(
    df,
    x="tenure",
    nbins=30,
    color_discrete_sequence=["#2563EB"]
)

fig.update_layout(
    height=450,
    paper_bgcolor="#F5F7FB",
    plot_bgcolor="white",
    font=dict(size=18),
    xaxis_title="Tenure (Months)",
    yaxis_title="Customers"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.markdown("""
<div class="info-box">
Customers with shorter tenure are more likely to churn.
</div>
""", unsafe_allow_html=True)

st.write("")

# =========================
# MONTHLY CHARGES
# =========================

st.markdown(
    '<p class="section-title">Monthly Charges Distribution</p>',
    unsafe_allow_html=True
)

fig = px.histogram(
    df,
    x="MonthlyCharges",
    nbins=30,
    color_discrete_sequence=["#2563EB"]
)

fig.update_layout(
    height=450,
    paper_bgcolor="#F5F7FB",
    plot_bgcolor="white",
    font=dict(size=18),
    xaxis_title="Monthly Charges ($)",
    yaxis_title="Customers"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.write("")

# =========================
# CORRELATION HEATMAP
# =========================

st.markdown(
    '<p class="section-title">Correlation Heatmap</p>',
    unsafe_allow_html=True
)

numeric_df = df.select_dtypes(
    include=["int64", "float64"]
)

corr = numeric_df.corr()

fig = px.imshow(
    corr,
    text_auto=True,
    color_continuous_scale="Blues",
    aspect="auto"
)

fig.update_layout(
    height=600,
    paper_bgcolor="#F5F7FB",
    font=dict(size=14)
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.write("")

# =========================
# KEY BUSINESS INSIGHTS
# =========================

st.markdown(
    '<p class="section-title">Key Business Insights</p>',
    unsafe_allow_html=True
)

st.markdown("""
<div class="info-box">

<h4>Key Findings</h4>

<ul>
<li>Month-to-month contracts have the highest churn rate.</li>
<li>Short-tenure customers are more likely to leave.</li>
<li>Higher monthly charges are associated with increased churn.</li>
<li>Gender has minimal impact on churn behavior.</li>
<li>Customer retention efforts should focus on early-stage customers.</li>
</ul>

</div>
""", unsafe_allow_html=True)

# Add fixed sidebar author card
add_sidebar_author()