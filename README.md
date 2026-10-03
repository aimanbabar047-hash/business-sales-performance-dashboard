# 📊 Business Sales Performance Dashboard

An interactive **Business Sales Performance Dashboard** developed using Python, Pandas, Plotly, and Streamlit. The dashboard helps users monitor sales performance, profitability, customer segments, product performance, and regional trends through interactive visualizations and filters.

🔗 **Live Dashboard:** https://business-sales-performance-dashboard-grwg6aoannft7wsn7z2urj.streamlit.app/

---

## 🎯 Project Objective

The objective of this project is to transform raw business sales data into an interactive dashboard that allows stakeholders to:

* Monitor important business KPIs
* Analyze sales and profit trends
* Compare yearly performance
* Explore category and regional performance
* Understand customer segment behavior
* Identify top-performing products
* Filter data interactively
* Download filtered data for further analysis

---

## 📂 Dataset

The project uses the **Sample Superstore dataset**, which contains sales transaction information including:

* Order and shipping dates
* Customer information
* Product details
* Categories and sub-categories
* Regions
* Customer segments
* Sales
* Quantity
* Discount
* Profit

The dataset contains **10,194 records and 21 columns**.

---

## 🛠️ Technologies Used

| Technology      | Purpose                                            |
| --------------- | -------------------------------------------------- |
| Python          | Data processing and dashboard development          |
| Pandas          | Data loading, cleaning, filtering, and aggregation |
| Plotly          | Interactive data visualizations                    |
| Streamlit       | Interactive web dashboard                          |
| Excel           | Source dataset                                     |
| GitHub          | Version control and project hosting                |
| Streamlit Cloud | Dashboard deployment                               |

---

## 📊 Key Performance Indicators

The dashboard includes six major KPIs:

1. 💰 **Total Sales**
2. 📈 **Total Profit**
3. 🛒 **Total Orders**
4. 👥 **Total Customers**
5. 📊 **Profit Margin**
6. 💵 **Average Order Value**

These KPIs update automatically according to the selected dashboard filters.

---

## 🔎 Interactive Filters

Users can interact with the dashboard using:

* 📅 Date Range
* 🌎 Region
* 📦 Category
* 👥 Customer Segment

All major KPIs and visualizations update based on the selected filters.

---

## 📈 Dashboard Visualizations

### 1. Monthly Sales & Profit Trend

A line chart showing how sales and profit change over time.

### 2. Yearly Sales & Profit Comparison

A grouped bar chart comparing yearly sales and profit.

### 3. Sales by Category

Shows sales performance across different product categories. Hovering over the bars also provides profit and profit margin information.

### 4. Profit by Region

Compares profit across different geographical regions while providing additional sales and profit margin details.

### 5. Sales by Customer Segment

Shows sales contribution from different customer segments.

### 6. Top 10 Products by Sales

Identifies the ten products generating the highest sales.

### 7. Sales vs Profit Analysis

An interactive scatter plot used to examine the relationship between sales and profit. Quantity is represented through bubble size.

---

## 💡 Key Business Insights

Based on the complete dataset:

* **Technology** generated the highest total sales among the three categories.
* **Technology** also generated the highest total profit.
* **Furniture** generated substantial sales but had a considerably lower profit margin than Office Supplies and Technology.
* **West** was the highest-performing region by both total sales and total profit.
* **Consumer** was the largest customer segment by sales and profit.
* **2025** recorded the highest annual sales and profit in the dataset.
* The dashboard also allows users to generate updated insights after applying filters.

> Note: Business insights change dynamically when users apply different filters.

---

## 📌 Overall Dataset Performance

For the complete dataset:

| KPI                 |         Value |
| ------------------- | ------------: |
| Total Sales         | $2,326,534.35 |
| Total Profit        |   $292,296.81 |
| Total Orders        |         5,111 |
| Total Customers     |           804 |
| Profit Margin       |        12.56% |
| Average Order Value |       $455.20 |

---

## 📁 Project Structure

```text
business-sales-performance-dashboard/
│
├── EncoderX-task4/
│   ├── Sales_Dashboard.ipynb
│   ├── Sample - Superstore.xls
│   └── app.py
│
├── README.md
└── requirements.txt
```

---

## ▶️ How to Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/aimanbabar047-hash/business-sales-performance-dashboard.git
```

### 2. Move into the project folder

```bash
cd business-sales-performance-dashboard
```

### 3. Install the required libraries

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit dashboard

```bash
streamlit run EncoderX-task4/app.py
```

The dashboard will open in your browser.

---

## 🌐 Live Dashboard

The deployed dashboard is available here:

**https://business-sales-performance-dashboard-grwg6aoannft7wsn7z2urj.streamlit.app/**

---

## 🎓 Internship Information

**Program:** EncoderX Remote Internship
**Track:** Data Science
**Batch:** Batch 02
**Week:** Week 04
**Task:** Task 4 — Interactive Dashboard Development

---

## 🚀 Project Highlights

* Interactive KPI dashboard
* Dynamic filters
* Interactive Plotly charts
* Automatic business insights
* Sales and profit trend analysis
* Regional and category analysis
* Customer segment analysis
* Top product analysis
* Filtered data download
* Cloud deployment using Streamlit

---

## 👩‍💻 Author

**Aiman Babar**

BS Bioinformatics Student
Interested in Data Science, Machine Learning, Bioinformatics, and Computational Research.
