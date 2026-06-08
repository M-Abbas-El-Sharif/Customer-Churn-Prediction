import streamlit as st
import pandas as pd
import plotly.express as px
from sidebar_utils import add_sidebar_author

st.set_page_config(
    page_title="Data Overview",
    page_icon="📂",
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

st.markdown(
    """
    <div class="hero-title">
    📂 Data Overview
    </div>

    <div class="hero-subtitle">
    Understanding the Telecom Customer Churn Dataset
    </div>
    """,
    unsafe_allow_html=True
)

st.write("")

# =========================
# KPI CARDS
# =========================

churn_rate = (
    df["Churn"]
    .value_counts(normalize=True)["Yes"] * 100
)

missing_values = int(
    df.isnull().sum().sum()
)

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown(
        f"""
        <div class="kpi-card">
            <div class="kpi-title">Rows</div>
            <div class="kpi-value">{df.shape[0]:,}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with c2:
    st.markdown(
        f"""
        <div class="kpi-card">
            <div class="kpi-title">Columns</div>
            <div class="kpi-value">{df.shape[1]}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with c3:
    st.markdown(
        f"""
        <div class="kpi-card">
            <div class="kpi-title">Missing Values</div>
            <div class="kpi-value">{missing_values}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with c4:
    st.markdown(
        f"""
        <div class="kpi-card">
            <div class="kpi-title">Churn Rate</div>
            <div class="kpi-value">{churn_rate:.1f}%</div>
        </div>
        """,
        unsafe_allow_html=True
    )

st.write("")
st.write("")

# =========================
# DATASET PREVIEW
# =========================

st.markdown(
    '<p class="section-title">Dataset Preview</p>',
    unsafe_allow_html=True
)

st.dataframe(
    df.head(10).style.set_properties(
        **{
            "background-color": "white",
            "color": "#1F2937"
        }
    ),
    use_container_width=True,
    height=350
)

st.write("")

# =========================
# FEATURE CATEGORIES
# =========================

st.markdown(
    '<p class="section-title">Feature Categories</p>',
    unsafe_allow_html=True
)

num_cols = len(
    df.select_dtypes(
        include=["int64", "float64"]
    ).columns
)

cat_cols = len(
    df.select_dtypes(
        include=["object"]
    ).columns
)

c1, c2 = st.columns(2)

with c1:
    st.markdown(
        f"""
        <div class="kpi-card">
            <div class="kpi-title">Numerical Features</div>
            <div class="kpi-value">{num_cols}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with c2:
    st.markdown(
        f"""
        <div class="kpi-card">
            <div class="kpi-title">Categorical Features</div>
            <div class="kpi-value">{cat_cols}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

st.write("")
st.write("")

# =========================
# DATA QUALITY
# =========================

st.markdown(
    '<p class="section-title">Data Quality</p>',
    unsafe_allow_html=True
)

st.markdown(
    f"""
    <div class="info-box">
        <h4>Total Missing Values: {missing_values}</h4>
        <p>
        Dataset is clean and ready for preprocessing and model training.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

st.write("")

# =========================
# DATA TYPES
# =========================

st.markdown(
    '<p class="section-title">Data Types</p>',
    unsafe_allow_html=True
)

dtype_df = pd.DataFrame({
    "Column": df.columns,
    "Data Type": df.dtypes.astype(str)
})

st.table(dtype_df)

st.write("")

# =========================
# TARGET DISTRIBUTION
# =========================

st.markdown(
    '<p class="section-title">Target Distribution</p>',
    unsafe_allow_html=True
)

churn_counts = df["Churn"].value_counts()

c1, c2 = st.columns(2)

with c1:
    st.success(
        f"Stayed Customers: {churn_counts['No']:,}"
    )

with c2:
    st.error(
        f"Churned Customers: {churn_counts['Yes']:,}"
    )

chart_df = churn_counts.reset_index()
chart_df.columns = ["Status", "Count"]

fig = px.bar(
    chart_df,
    x="Status",
    y="Count",
    color="Status",
    text="Count",
    color_discrete_map={
        "No": "#60A5FA",
        "Yes": "#2563EB"
    }
)

fig.update_traces(
    textposition="outside",
    textfont_size=20,
    textfont_color="#163B65"
)

fig.update_layout(
    height=500,
    paper_bgcolor="#F5F7FB",
    plot_bgcolor="#FFFFFF",

    font=dict(
        size=18,
        color="#1F2937"
    ),

    xaxis=dict(
        title="Customer Status",
        title_font=dict(size=20),
        tickfont=dict(size=18)
    ),

    yaxis=dict(
        title="Number of Customers",
        title_font=dict(size=20),
        tickfont=dict(size=18)
    ),

    margin=dict(
        l=40,
        r=40,
        t=30,
        b=40
    ),

    showlegend=False
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.write("")

# =========================
# STATISTICAL SUMMARY
# =========================

st.markdown(
    '<p class="section-title">Statistical Summary</p>',
    unsafe_allow_html=True
)

st.table(
    df.describe().round(2)
)

# Add fixed sidebar author card
add_sidebar_author()