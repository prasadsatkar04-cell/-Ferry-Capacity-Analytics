# ⛴️ Ferry Capacity Utilization & Operational Efficiency Analytics System

## 📌 Project Overview

The **Ferry Capacity Utilization & Operational Efficiency Analytics System** is a data analytics project that analyzes Toronto Island Ferry ticket activity from 2015 to 2025.

The project uses Python, Pandas, NumPy, Plotly, and Streamlit to identify activity patterns, seasonal trends, peak periods, and operational insights through an interactive dashboard.

The objective is to support better operational planning using historical ferry ticket activity data.

## 🎯 Project Objectives

- Analyze historical ferry ticket sales and redemption activity.
- Identify peak and low-activity periods.
- Understand daily, monthly, and seasonal trends.
- Compare yearly ferry activity.
- Develop activity-based operational indicators.
- Build an interactive dashboard for data visualization.
- Generate insights to support operational planning.

## 📂 Dataset Information

**Dataset:** Toronto Island Ferry Tickets

**Period:** 2015–2025

**Dataset Columns:**

| Column | Description |
|---|---|
| `_id` | Unique record identifier |
| `Timestamp` | 15-minute interval end time |
| `Sales Count` | Number of tickets sold |
| `Redemption Count` | Number of tickets redeemed |

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Plotly
- Streamlit
- Jupyter Notebook
- Git & GitHub

## 📊 Exploratory Data Analysis

The project includes:

1. Dataset overview and statistical analysis.
2. Sales and redemption analysis.
3. Year-wise activity analysis.
4. Monthly and seasonal analysis.
5. Day-wise and hourly analysis.
6. Weekday vs weekend comparison.
7. Operational activity analysis.
8. Heatmap visualizations.
9. Peak and low-activity identification.

## 📈 Key Performance Indicators

The project calculates the following indicators:

- Total Sales
- Total Redemptions
- Total Activity Load
- Average Redemption Activity
- High Activity Percentage
- Low Activity Percentage
- Operational Load Index (OLI)

These indicators help understand historical ticket activity and operational patterns.

## 📊 Streamlit Dashboard

The interactive dashboard contains four major sections:

**1. Overview**
- Total sales and redemptions.
- KPI cards.
- Yearly activity trends.

**2. Time Analysis**
- Hourly activity.
- Day-wise activity.

**3. Seasonal Analysis**
- Monthly activity.
- Seasonal comparisons.

**4. Operational Insights**
- High and low activity periods.
- Daily activity trends.
- Business recommendations.

## 📁 Project Structure

```text
Ferry_Capacity_Analytics/
│
├── dataset/
│   └── Toronto Island Ferry Tickets.csv
│
├── notebooks/
│   └── EDA.ipynb
│
├── dashboard/
│   └── app.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

## ⚙️ Installation and Setup

**Step 1: Clone the repository**

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

**Step 2: Open the project folder**

```bash
cd Ferry-Capacity-Analytics
```

**Step 3: Install dependencies**

```bash
pip install -r requirements.txt
```

**Step 4: Run the Streamlit dashboard**

```bash
streamlit run dashboard/app.py
```

The dashboard will open in your web browser.

## 💡 Business Insights

The analysis helps identify:

- Periods with high ticket redemption activity.
- Seasonal changes in ferry ticket activity.
- Differences between weekday and weekend activity.
- Potentially busy operating hours.
- Periods with consistently low ticket activity.

These insights can help support operational resource planning.

## ⚠️ Project Limitations

The dataset contains ticket sales and redemption counts but does not include actual vessel capacity, departure-level passenger counts, or onboard occupancy.

Therefore, this project uses ticket redemption activity as a proxy for passenger usage.

Actual vessel capacity utilization, overcrowding, and idle vessel capacity cannot be directly measured using the available dataset.

## 👨‍💻 Project Information

**Project Title:** Ferry Capacity Utilization & Operational Efficiency Analytics System

**Project Domain:** Data Analytics

**Project Type:** Internship Project

**Tools:** Python, Pandas, NumPy, Plotly, Streamlit

## 🏁 Conclusion

This project demonstrates how historical ferry ticket activity data can be analyzed using Python and visualized through an interactive Streamlit dashboard.

It provides useful insights into seasonal patterns, activity trends, and potentially busy operating periods to support data-driven operational planning.