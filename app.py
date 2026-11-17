import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from pathlib import Path

# -----------------------------------
# PAGE CONFIGURATION
# -----------------------------------

st.set_page_config(
    page_title="Ferry Analytics Dashboard",
    page_icon="⛴️",
    layout="wide"
)

# -----------------------------------
# LOAD DATA
# -----------------------------------

@st.cache_data
def load_data():

    file_path = (
        Path(__file__).resolve().parent.parent
        / "dataset"
        / "Toronto Island Ferry Tickets.csv"
    )

    data = pd.read_csv(file_path)

    data['Timestamp'] = pd.to_datetime(data['Timestamp'])

    data['Total Activity'] = (
        data['Sales Count'] + data['Redemption Count']
    )

    data['Year'] = data['Timestamp'].dt.year
    data['Month'] = data['Timestamp'].dt.month
    data['Month Name'] = data['Timestamp'].dt.month_name()
    data['Hour'] = data['Timestamp'].dt.hour
    data['Day'] = data['Timestamp'].dt.day_name()

    data['Season'] = data['Month'].map({
        12: 'Winter', 1: 'Winter', 2: 'Winter',
        3: 'Spring', 4: 'Spring', 5: 'Spring',
        6: 'Summer', 7: 'Summer', 8: 'Summer',
        9: 'Autumn', 10: 'Autumn', 11: 'Autumn'
    })

    return data


df = load_data()

# -----------------------------------
# SIDEBAR FILTERS
# -----------------------------------

st.sidebar.title("Dashboard Filters")

years = sorted(df['Year'].unique())

selected_years = st.sidebar.multiselect(
    "Select Year",
    years,
    default=years
)

months = list(range(1, 13))

selected_months = st.sidebar.multiselect(
    "Select Month",
    months,
    default=months,
    format_func=lambda x: pd.Timestamp(
        month=x, day=1, year=2025
    ).strftime('%B')
)

filtered_df = df[
    (df['Year'].isin(selected_years)) &
    (df['Month'].isin(selected_months))
].copy()

if filtered_df.empty:
    st.warning("No data available for the selected filters.")
    st.stop()

# -----------------------------------
# DASHBOARD HEADER
# -----------------------------------

st.title("⛴️ Toronto Island Ferry Analytics")

st.markdown(
    "### Ferry Activity, Seasonal Trends & Operational Efficiency"
)

st.caption(
    "Data-driven analysis of Toronto Island Ferry ticket activity (2015–2025)"
)

st.divider()

# -----------------------------------
# KPI CALCULATIONS
# -----------------------------------

total_sales = filtered_df['Sales Count'].sum()

total_redemptions = filtered_df['Redemption Count'].sum()

total_activity = filtered_df['Total Activity'].sum()

avg_redemptions = filtered_df['Redemption Count'].mean()

high_threshold = df['Redemption Count'].quantile(0.90)

high_activity_percentage = (
    filtered_df['Redemption Count'] >= high_threshold
).mean() * 100

low_threshold = df['Redemption Count'].quantile(0.10)

low_activity_percentage = (
    filtered_df['Redemption Count'] <= low_threshold
).mean() * 100

# -----------------------------------
# KPI CARDS
# -----------------------------------

st.subheader("📊 Key Performance Indicators")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Sales",
    f"{total_sales:,.0f}"
)

col2.metric(
    "Total Redemptions",
    f"{total_redemptions:,.0f}"
)

col3.metric(
    "Total Activity",
    f"{total_activity:,.0f}"
)

col4.metric(
    "Average Redemptions",
    f"{avg_redemptions:,.2f}"
)

col5, col6 = st.columns(2)

col5.metric(
    "High Activity Intervals",
    f"{high_activity_percentage:.2f}%"
)

col6.metric(
    "Low Activity Intervals",
    f"{low_activity_percentage:.2f}%"
)

st.divider()

# -----------------------------------
# TABS
# -----------------------------------

tab1, tab2, tab3, tab4 = st.tabs([
    "Overview",
    "Time Analysis",
    "Seasonal Analysis",
    "Operational Insights"
])

# ===================================
# TAB 1: OVERVIEW
# ===================================

with tab1:

    st.subheader("Sales vs Redemptions")

    comparison = pd.DataFrame({
        'Category': ['Sales', 'Redemptions'],
        'Count': [total_sales, total_redemptions]
    })

    fig = px.bar(
        comparison,
        x='Category',
        y='Count',
        color='Category',
        text_auto='.2s',
        title='Total Sales vs Total Redemptions'
    )

    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Yearly Activity Trend")

    yearly = filtered_df.groupby('Year')[
        ['Sales Count', 'Redemption Count']
    ].sum().reset_index()

    fig = px.line(
        yearly,
        x='Year',
        y=['Sales Count', 'Redemption Count'],
        markers=True,
        title='Year-wise Ferry Ticket Activity'
    )

    st.plotly_chart(fig, use_container_width=True)

# ===================================
# TAB 2: TIME ANALYSIS
# ===================================

with tab2:

    st.subheader("Hourly Activity")

    hourly = filtered_df.groupby('Hour')[
        'Redemption Count'
    ].mean().reset_index()

    fig = px.line(
        hourly,
        x='Hour',
        y='Redemption Count',
        markers=True,
        title='Average Redemption Activity by Hour'
    )

    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Day-wise Activity")

    day_order = [
        'Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday', 'Saturday', 'Sunday'
    ]

    daily = filtered_df.groupby('Day')[
        'Redemption Count'
    ].mean().reindex(day_order).reset_index()

    fig = px.bar(
        daily,
        x='Day',
        y='Redemption Count',
        title='Average Redemption Activity by Day'
    )

    st.plotly_chart(fig, use_container_width=True)

# ===================================
# TAB 3: SEASONAL ANALYSIS
# ===================================

with tab3:

    st.subheader("Monthly Activity")

    monthly = filtered_df.groupby('Month')[
        'Redemption Count'
    ].mean().reset_index()

    monthly['Month Name'] = monthly['Month'].apply(
        lambda x: pd.Timestamp(
            month=x, day=1, year=2025
        ).strftime('%B')
    )

    fig = px.bar(
        monthly,
        x='Month Name',
        y='Redemption Count',
        title='Average Monthly Redemption Activity'
    )

    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Seasonal Comparison")

    seasonal = filtered_df.groupby('Season')[
        'Redemption Count'
    ].mean().reindex([
        'Spring', 'Summer', 'Autumn', 'Winter'
    ]).reset_index()

    fig = px.bar(
        seasonal,
        x='Season',
        y='Redemption Count',
        color='Season',
        title='Average Redemption Activity by Season'
    )

    st.plotly_chart(fig, use_container_width=True)

# ===================================
# TAB 4: OPERATIONAL INSIGHTS
# ===================================

with tab4:

    st.subheader("High and Low Activity Analysis")

    filtered_df['Activity Status'] = np.select(
        [
            filtered_df['Redemption Count'] >= high_threshold,
            filtered_df['Redemption Count'] <= low_threshold
        ],
        [
            'High Activity',
            'Low Activity'
        ],
        default='Normal Activity'
    )

    status_counts = filtered_df[
        'Activity Status'
    ].value_counts().reset_index()

    status_counts.columns = ['Status', 'Intervals']

    fig = px.pie(
        status_counts,
        names='Status',
        values='Intervals',
        title='Distribution of Activity Intervals',
        hole=0.4
    )

    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Operational Activity Trend")

    daily_activity = filtered_df.groupby(
        filtered_df['Timestamp'].dt.date
    )['Redemption Count'].sum().reset_index()

    daily_activity.columns = ['Date', 'Redemption Count']

    fig = px.line(
        daily_activity,
        x='Date',
        y='Redemption Count',
        title='Daily Redemption Activity'
    )

    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Business Recommendations")

    st.markdown("""
    - Monitor periods with consistently high ticket redemption activity.
    - Plan operational resources according to seasonal demand.
    - Compare weekday and weekend activity patterns.
    - Investigate unusually low activity periods.
    - Use historical activity trends for operational planning.
    """)

# -----------------------------------
# FOOTER
# -----------------------------------

st.divider()

st.caption(
    "Developed using Python, Pandas, Plotly and Streamlit."
)

st.caption(
    "Note: Ticket redemption activity is a proxy for passenger usage. "
    "Actual vessel capacity utilization cannot be calculated "
    "without vessel capacity and onboard passenger data."
)