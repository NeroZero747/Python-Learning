# Module 8 — Building Data Applications

# Lesson 3 — Building a Simple Dashboard

---

# Lesson Objective

By the end of this lesson learners will understand:

• how to structure a complete Streamlit dashboard  
• how to display charts and metrics  
• how to organize dashboard layout  
• how to build a basic analytics dashboard using Python  

This lesson focuses on building a **complete working dashboard**, which is the foundation for many internal analytics tools.

---

# Overview

A typical analytics dashboard displays:

• summary metrics  
• charts  
• tables  
• filters  

Example dashboard structure:

```text
Dashboard Title
      ↓
Filters
      ↓
Summary Metrics
      ↓
Charts
      ↓
Detailed Data Table
```

Dashboards allow users to quickly understand data patterns.

Example use cases:

• sales dashboards  
• healthcare analytics dashboards  
• operational reporting tools  
• financial performance monitoring.

Streamlit makes it easy to build dashboards using simple Python code.

---

# Key Idea Cards (3 Cards)

## Dashboards Provide High-Level Insights

Dashboards summarize key metrics.

Example metrics:

```text
Total Revenue
Total Orders
Average Price
```

These metrics help users quickly understand performance.

---

## Charts Help Identify Patterns

Charts allow users to visually explore data.

Common chart types:

• bar charts  
• line charts  
• scatter plots  
• pie charts.

Visualizations make data easier to interpret.

---

## Dashboards Combine Multiple Data Views

Most dashboards include several components:

```text
Filters
Metrics
Charts
Tables
```

Combining these elements allows users to explore data interactively.

---

# Key Concepts

## Dashboard Layout

A typical dashboard layout includes:

```text
Header
Filters
Summary Metrics
Charts
Detailed Data
```

This structure helps users quickly navigate the data.

---

## Summary Metrics

Summary metrics highlight key values.

Examples:

• total sales  
• number of transactions  
• average order value.

These metrics are often displayed at the top of the dashboard.

---

## Data Visualization

Charts help identify patterns and trends.

Examples:

• sales by region  
• revenue over time  
• product performance.

Visualizations provide quick insights into the data.

---

# Decision Flow

Designing a dashboard usually follows this process:

```text
Identify key metrics
        ↓
Determine useful charts
        ↓
Add filters
        ↓
Display detailed data
```

This ensures the dashboard provides both **summary insights and detailed exploration**.

---

# Code Examples

## Example 1 — Basic Dashboard Structure

```python
import streamlit as st
import pandas as pd

data = pd.read_csv("sales.csv")

st.title("Sales Dashboard")

st.write(data.head())
```

This creates a basic dashboard with a title and dataset preview.

---

## Example 2 — Displaying Summary Metrics

```python
total_sales = data["sales"].sum()

st.metric("Total Sales", total_sales)
```

Metrics provide quick insights at the top of the dashboard.

---

## Example 3 — Creating Charts

```python
st.bar_chart(data["sales"])
```

This displays a bar chart of sales data.

---

## Example 4 — Combining Components

```python
import streamlit as st
import pandas as pd

data = pd.read_csv("sales.csv")

st.title("Sales Dashboard")

st.metric("Total Sales", data["sales"].sum())

st.bar_chart(data["sales"])

st.write(data)
```

This example creates a simple dashboard with:

• a title  
• summary metric  
• chart  
• data table.

---

# SQL / Excel Comparison

Dashboard functionality also exists in other tools.

| Feature | Streamlit | SQL | Excel |
|------|------|------|------|
| metrics | Python calculations | aggregate queries | formulas |
| charts | built-in charts | BI tools | chart tools |
| filtering | interactive widgets | WHERE clause | filters |

Example SQL aggregation:

```sql
SELECT SUM(sales)
FROM orders
```

This is similar to calculating metrics in a Streamlit dashboard.

---

# Practice Exercises

## Exercise 1

Tags: Imports, Scripts, Data Processing, Streamlit

Create a basic Streamlit dashboard.

```python
import streamlit as st

st.title("My Dashboard")
```

Run the app using:

```bash
streamlit run app.py
```

---

## Exercise 2

Tags: pandas, Imports, read_csv(), CSV

Load a dataset.

```python
import pandas as pd

data = pd.read_csv("sales.csv")
```

Display the dataset in the dashboard.

---

## Exercise 3

Tags: Lists, Tuples, Aggregations, Streamlit

Add a metric.

```python
st.metric("Total Sales", data["sales"].sum())
```

---

## Exercise 4

Tags: Lists, Visualization, Streamlit, Dashboards

Add a chart.

```python
st.bar_chart(data["sales"])
```

---

# Common Mistakes

## Overloading Dashboards with Too Many Charts

Too many charts can make dashboards difficult to interpret.

Good dashboards focus on **key insights**.

---

## Displaying Raw Data Without Context

Tables should support charts and metrics.

Users should understand **why the data is shown**.

---

## Ignoring Layout Structure

Unstructured dashboards can be confusing.

Always organize dashboards with clear sections.

---

# Real-World Use

Dashboards are widely used in business operations.

Examples include:

• sales performance dashboards  
• healthcare claims analytics  
• customer behavior analysis  
• financial reporting tools.

Example workflow:

```text
Data Warehouse
      ↓
Python Query
      ↓
Streamlit Dashboard
      ↓
User Filters Data
      ↓
Charts Update Automatically
```

This allows teams to monitor performance in real time.

---

# Lesson Recap

In this lesson you learned:

• how to structure a Streamlit dashboard  
• how to display summary metrics  
• how to create charts  
• how to combine multiple dashboard components  

Dashboards provide a powerful way to turn raw data into **interactive insights**.

---

# Next Lesson

Next we will learn:

# Lesson 4 — Interactive Filters

You will learn:

• how to add filters to dashboards  
• how user inputs change displayed data  
• how to build dynamic analytics applications.
