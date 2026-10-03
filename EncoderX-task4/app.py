import streamlit as st
import pandas as pd
import plotly.express as px

# ==================================================
# PAGE CONFIGURATION
# ==================================================

st.set_page_config(
    page_title="Business Sales Performance Dashboard",
    page_icon="📊",
    layout="wide"
)

# ==================================================
# CUSTOM PAGE TITLE
# ==================================================

st.title("📊 Business Sales Performance Dashboard")

st.markdown(
    """
    **Interactive business dashboard** for monitoring sales, profit,
    customers, orders, product performance, and regional trends.
    """
)

# ==================================================
# LOAD DATA
# ==================================================

df = pd.read_excel("Sample - Superstore.xls")

# Convert dates
df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Ship Date"] = pd.to_datetime(df["Ship Date"])

# ==================================================
# SIDEBAR
# ==================================================

st.sidebar.header("🔎 Dashboard Filters")

st.sidebar.markdown(
    "Use the filters below to explore the business performance."
)

# --------------------------------------------------
# DATE FILTER
# --------------------------------------------------

date_range = st.sidebar.date_input(
    "📅 Select Date Range",
    value=(
        df["Order Date"].min().date(),
        df["Order Date"].max().date()
    ),
    min_value=df["Order Date"].min().date(),
    max_value=df["Order Date"].max().date()
)

# Handle one selected date
if len(date_range) == 1:
    start_date = pd.to_datetime(date_range[0])
    end_date = pd.to_datetime(date_range[0])
else:
    start_date = pd.to_datetime(date_range[0])
    end_date = pd.to_datetime(date_range[-1])

# --------------------------------------------------
# REGION FILTER
# --------------------------------------------------

region_filter = st.sidebar.multiselect(
    "🌎 Select Region",
    options=sorted(df["Region"].unique()),
    default=sorted(df["Region"].unique())
)

# --------------------------------------------------
# CATEGORY FILTER
# --------------------------------------------------

category_filter = st.sidebar.multiselect(
    "📦 Select Category",
    options=sorted(df["Category"].unique()),
    default=sorted(df["Category"].unique())
)

# --------------------------------------------------
# SEGMENT FILTER
# --------------------------------------------------

segment_filter = st.sidebar.multiselect(
    "👥 Select Customer Segment",
    options=sorted(df["Segment"].unique()),
    default=sorted(df["Segment"].unique())
)

# ==================================================
# APPLY FILTERS
# ==================================================

filtered_df = df[
    (df["Order Date"] >= start_date) &
    (df["Order Date"] <= end_date) &
    (df["Region"].isin(region_filter)) &
    (df["Category"].isin(category_filter)) &
    (df["Segment"].isin(segment_filter))
].copy()

# ==================================================
# FILTERED RECORDS
# ==================================================

st.info(
    f"📋 **Filtered Records:** {len(filtered_df):,}"
)

# ==================================================
# CHECK EMPTY DATA
# ==================================================

if filtered_df.empty:

    st.warning(
        "⚠️ No data is available for the selected filters. "
        "Please change the filters."
    )

    st.stop()

# ==================================================
# KPI CALCULATIONS
# ==================================================

total_sales = filtered_df["Sales"].sum()

total_profit = filtered_df["Profit"].sum()

total_orders = filtered_df["Order ID"].nunique()

total_customers = filtered_df["Customer ID"].nunique()

if total_sales != 0:
    profit_margin = (total_profit / total_sales) * 100
else:
    profit_margin = 0

if total_orders != 0:
    average_order_value = total_sales / total_orders
else:
    average_order_value = 0

# ==================================================
# KPI SECTION
# ==================================================

st.subheader("📊 Key Performance Indicators")

col1, col2, col3, col4, col5, col6 = st.columns(6)

with col1:

    st.metric(
        "💰 Total Sales",
        f"${total_sales:,.0f}"
    )

with col2:

    st.metric(
        "📈 Total Profit",
        f"${total_profit:,.0f}"
    )

with col3:

    st.metric(
        "🛒 Total Orders",
        f"{total_orders:,}"
    )

with col4:

    st.metric(
        "👥 Total Customers",
        f"{total_customers:,}"
    )

with col5:

    st.metric(
        "📊 Profit Margin",
        f"{profit_margin:.2f}%"
    )

with col6:

    st.metric(
        "💵 Average Order Value",
        f"${average_order_value:,.2f}"
    )

st.divider()

# ==================================================
# PERFORMANCE OVERVIEW
# ==================================================

st.subheader("📈 Performance Overview")

# --------------------------------------------------
# MONTHLY TREND
# --------------------------------------------------

filtered_df["Month_Date"] = (
    filtered_df["Order Date"]
    .dt.to_period("M")
    .dt.to_timestamp()
)

monthly_trend = (
    filtered_df
    .groupby("Month_Date")[["Sales", "Profit"]]
    .sum()
    .reset_index()
)

monthly_long = monthly_trend.melt(
    id_vars="Month_Date",
    value_vars=["Sales", "Profit"],
    var_name="Metric",
    value_name="Amount"
)

monthly_fig = px.line(
    monthly_long,
    x="Month_Date",
    y="Amount",
    color="Metric",
    markers=True,
    title="Monthly Sales & Profit Trend",
    labels={
        "Month_Date": "Month",
        "Amount": "Amount ($)",
        "Metric": "Metric"
    },
    hover_data={
        "Amount": ":$,.2f"
    }
)

monthly_fig.update_layout(
    hovermode="x unified"
)

st.plotly_chart(
    monthly_fig,
    use_container_width=True
)

# --------------------------------------------------
# YEARLY COMPARISON
# --------------------------------------------------

yearly_comparison = (
    filtered_df.assign(
        Year=filtered_df["Order Date"].dt.year
    )
    .groupby("Year")[["Sales", "Profit"]]
    .sum()
    .reset_index()
)

yearly_long = yearly_comparison.melt(
    id_vars="Year",
    value_vars=["Sales", "Profit"],
    var_name="Metric",
    value_name="Amount"
)

yearly_fig = px.bar(
    yearly_long,
    x="Year",
    y="Amount",
    color="Metric",
    barmode="group",
    title="Yearly Sales & Profit Comparison",
    text_auto=".2s",
    labels={
        "Amount": "Amount ($)",
        "Metric": "Metric"
    },
    hover_data={
        "Amount": ":$,.2f"
    }
)

st.plotly_chart(
    yearly_fig,
    use_container_width=True
)

# ==================================================
# CATEGORY & REGIONAL ANALYSIS
# ==================================================

st.subheader("🌎 Category & Regional Analysis")

col1, col2 = st.columns(2)

# --------------------------------------------------
# SALES BY CATEGORY
# --------------------------------------------------

with col1:

    category_analysis = (
        filtered_df
        .groupby("Category")[["Sales", "Profit"]]
        .sum()
        .reset_index()
    )

    category_analysis["Profit Margin (%)"] = (
        category_analysis["Profit"] /
        category_analysis["Sales"] * 100
    )

    category_fig = px.bar(
        category_analysis,
        x="Category",
        y="Sales",
        title="Sales by Category",
        text_auto=".2s",
        hover_data={
            "Sales": ":$,.2f",
            "Profit": ":$,.2f",
            "Profit Margin (%)": ":.2f"
        }
    )

    st.plotly_chart(
        category_fig,
        use_container_width=True
    )

# --------------------------------------------------
# PROFIT BY REGION
# --------------------------------------------------

with col2:

    region_analysis = (
        filtered_df
        .groupby("Region")[["Sales", "Profit"]]
        .sum()
        .reset_index()
    )

    region_analysis["Profit Margin (%)"] = (
        region_analysis["Profit"] /
        region_analysis["Sales"] * 100
    )

    region_fig = px.bar(
        region_analysis,
        x="Region",
        y="Profit",
        title="Profit by Region",
        text_auto=".2s",
        hover_data={
            "Sales": ":$,.2f",
            "Profit": ":$,.2f",
            "Profit Margin (%)": ":.2f"
        }
    )

    st.plotly_chart(
        region_fig,
        use_container_width=True
    )

# ==================================================
# CUSTOMER & PRODUCT ANALYSIS
# ==================================================

st.subheader("👥 Customer & Product Analysis")

col1, col2 = st.columns(2)

# --------------------------------------------------
# SALES BY CUSTOMER SEGMENT
# --------------------------------------------------

with col1:

    segment_analysis = (
        filtered_df
        .groupby("Segment")[["Sales", "Profit"]]
        .sum()
        .reset_index()
    )

    segment_analysis["Profit Margin (%)"] = (
        segment_analysis["Profit"] /
        segment_analysis["Sales"] * 100
    )

    segment_fig = px.bar(
        segment_analysis,
        x="Segment",
        y="Sales",
        title="Sales by Customer Segment",
        text_auto=".2s",
        hover_data={
            "Sales": ":$,.2f",
            "Profit": ":$,.2f",
            "Profit Margin (%)": ":.2f"
        }
    )

    st.plotly_chart(
        segment_fig,
        use_container_width=True
    )

# --------------------------------------------------
# TOP 10 PRODUCTS
# --------------------------------------------------

with col2:

    top_products = (
        filtered_df
        .groupby("Product Name")[["Sales", "Profit"]]
        .sum()
        .sort_values(
            "Sales",
            ascending=False
        )
        .head(10)
        .reset_index()
    )

    top_products["Profit Margin (%)"] = (
        top_products["Profit"] /
        top_products["Sales"] * 100
    )

    top_product_fig = px.bar(
        top_products,
        x="Sales",
        y="Product Name",
        orientation="h",
        title="Top 10 Products by Sales",
        text_auto=".2s",
        hover_data={
            "Sales": ":$,.2f",
            "Profit": ":$,.2f",
            "Profit Margin (%)": ":.2f"
        }
    )

    top_product_fig.update_layout(
        yaxis={
            "categoryorder": "total ascending"
        }
    )

    st.plotly_chart(
        top_product_fig,
        use_container_width=True
    )

# ==================================================
# SALES VS PROFIT
# ==================================================

st.subheader("🔍 Sales & Profit Relationship")

scatter_fig = px.scatter(
    filtered_df,
    x="Sales",
    y="Profit",
    color="Category",
    size="Quantity",
    hover_data=[
        "Product Name",
        "Region",
        "Segment",
        "Sales",
        "Profit",
        "Discount"
    ],
    title="Sales vs Profit Analysis",
    labels={
        "Sales": "Sales ($)",
        "Profit": "Profit ($)",
        "Quantity": "Quantity"
    }
)

st.plotly_chart(
    scatter_fig,
    use_container_width=True
)

# ==================================================
# AUTOMATIC BUSINESS INSIGHTS
# ==================================================

st.subheader("💡 Key Business Insights")

# --------------------------------------------------
# CATEGORY INSIGHT
# --------------------------------------------------

category_sales_max = category_analysis.loc[
    category_analysis["Sales"].idxmax()
]

category_profit_max = category_analysis.loc[
    category_analysis["Profit"].idxmax()
]

# --------------------------------------------------
# REGION INSIGHT
# --------------------------------------------------

region_sales_max = region_analysis.loc[
    region_analysis["Sales"].idxmax()
]

region_profit_max = region_analysis.loc[
    region_analysis["Profit"].idxmax()
]

# --------------------------------------------------
# SEGMENT INSIGHT
# --------------------------------------------------

segment_sales_max = segment_analysis.loc[
    segment_analysis["Sales"].idxmax()
]

# --------------------------------------------------
# YEAR INSIGHT
# --------------------------------------------------

year_sales_max = yearly_comparison.loc[
    yearly_comparison["Sales"].idxmax()
]

# --------------------------------------------------
# DISPLAY INSIGHTS
# --------------------------------------------------

insight_col1, insight_col2 = st.columns(2)

with insight_col1:

    st.markdown(
        f"""
        **📦 Category Performance**

        • Highest sales category: **{category_sales_max["Category"]}**  
        • Sales: **${category_sales_max["Sales"]:,.2f}**  
        • Highest profit category: **{category_profit_max["Category"]}**  
        • Profit: **${category_profit_max["Profit"]:,.2f}**
        """
    )

    st.markdown(
        f"""
        **🌎 Regional Performance**

        • Highest sales region: **{region_sales_max["Region"]}**  
        • Sales: **${region_sales_max["Sales"]:,.2f}**  
        • Highest profit region: **{region_profit_max["Region"]}**  
        • Profit: **${region_profit_max["Profit"]:,.2f}**
        """
    )

with insight_col2:

    st.markdown(
        f"""
        **👥 Customer Segment**

        • Highest sales segment: **{segment_sales_max["Segment"]}**  
        • Sales: **${segment_sales_max["Sales"]:,.2f}**
        """
    )

    st.markdown(
        f"""
        **📅 Yearly Performance**

        • Highest sales year in the selected data: **{int(year_sales_max["Year"])}**  
        • Sales: **${year_sales_max["Sales"]:,.2f}**  
        • Profit: **${year_sales_max["Profit"]:,.2f}**
        """
    )

# ==================================================
# DASHBOARD SUMMARY
# ==================================================

st.divider()

st.subheader("📌 Dashboard Summary")

st.markdown(
    f"""
    Based on the current filters, the dashboard contains **{len(filtered_df):,} records**.

    **Overall Performance**

    - 💰 Total Sales: **${total_sales:,.2f}**
    - 📈 Total Profit: **${total_profit:,.2f}**
    - 🛒 Total Orders: **{total_orders:,}**
    - 👥 Total Customers: **{total_customers:,}**
    - 📊 Profit Margin: **{profit_margin:.2f}%**
    - 💵 Average Order Value: **${average_order_value:,.2f}**
    """
)

# ==================================================
# DOWNLOAD FILTERED DATA
# ==================================================

st.subheader("⬇️ Download Filtered Data")

csv_data = filtered_df.drop(
    columns=["Month_Date"],
    errors="ignore"
).to_csv(index=False).encode("utf-8")

st.download_button(
    label="📥 Download Filtered Data (CSV)",
    data=csv_data,
    file_name="filtered_sales_data.csv",
    mime="text/csv"
)

# ==================================================
# FOOTER
# ==================================================

st.divider()

st.caption(
    "Business Sales Performance Dashboard | "
    "Python • Pandas • Plotly • Streamlit"
)