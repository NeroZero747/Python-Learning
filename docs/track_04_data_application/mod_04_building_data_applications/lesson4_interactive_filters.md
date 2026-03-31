# Module 8 — Building Data Applications

# Lesson 4 — Interactive Filters

---

# Lesson Objective

By the end of this lesson learners will understand:

• how to add **interactive filters** to a Streamlit dashboard  
• how user input dynamically changes displayed data  
• how filtering improves data exploration  
• how to build dashboards that respond to user selections  

Interactive filters are one of the most important features of data applications because they allow users to **explore datasets without writing queries**.

---

# Overview

Static dashboards display the same information every time a user opens them.

Example:

```text
Dashboard
   ↓
Fixed chart
   ↓
Fixed data table
```

This limits the usefulness of the dashboard.

Interactive dashboards allow users to modify what they see.

Example interactive workflow:

```text
User selects region
        ↓
Data filtered
        ↓
Charts update automatically
```

Instead of requesting new reports, users can adjust filters themselves.

Common dashboard filters include:

• region  
• product category  
• date range  
• customer segment  

These filters allow users to focus on the data that matters to them.

---

# Key Idea Cards (3 Cards)

## Filters Enable Data Exploration

Filters allow users to explore different parts of a dataset.

Example:

```text
Region = West
Region = East
Region = Central
```

Each selection displays a different subset of the data.

---

## Filters Control Dashboard Behavior

When a user changes a filter, the dashboard recalculates results.

Example:

```text
User changes filter
        ↓
Script reruns
        ↓
Charts update
```

This creates a reactive analytics experience.

---

## Filters Replace Many SQL Queries

Without filters, analysts often run multiple queries.

Example requests:

```text
Show sales for West
Show sales for East
Show sales for Central
```

Filters allow users to run these queries automatically through the interface.

---

# Key Concepts

## User Input Widgets

Streamlit provides widgets that capture user input.

Examples include:

• dropdown menus  
• sliders  
• date pickers  
• text inputs.

These widgets control how the dashboard behaves.

---

## Data Filtering

Filtering selects a subset of a dataset based on conditions.

Example filter:

```python
filtered = data[data["region"] == "West"]
```

This selects rows where the region is West.

---

## Reactive Dashboards

When a filter changes, Streamlit automatically reruns the script.

Example process:

```text
User selects value
        ↓
Script reruns
        ↓
Dashboard updates
```

This creates an interactive experience.

---

# Decision Flow

Designing dashboard filters typically follows this logic:

```text
What dimension should users explore?
            ↓
Add filter widget
            ↓
Apply filter to dataset
            ↓
Update charts and tables
```

This structure ensures the dashboard remains responsive.

---

# Code Examples

## Example 1 — Creating a Dropdown Filter

```python
import streamlit as st
import pandas as pd

data = pd.read_csv("sales.csv")

region = st.selectbox(
    "Select Region",
    data["region"].unique()
)
```

This creates a dropdown menu.

---

## Example 2 — Filtering the Dataset

```python
filtered_data = data[data["region"] == region]
```

The dataset updates based on the selected region.

---

## Example 3 — Displaying Filtered Results

```python
st.write(filtered_data)
```

The dashboard displays the filtered dataset.

---

## Example 4 — Combining Filters and Charts

```python
st.bar_chart(filtered_data["sales"])
```

The chart updates when the filter changes.

---

# SQL / Excel Comparison

Filtering exists in many data tools.

| Feature | Streamlit | SQL | Excel |
|------|------|------|------|
| filtering | selectbox | WHERE clause | filter |
| aggregation | Python functions | GROUP BY | pivot tables |
| visualization | charts | BI tools | charts |

Example SQL query:

```sql
SELECT *
FROM sales
WHERE region = 'West'
```

The Streamlit filter performs this query dynamically.

---

# Practice Exercises

## Exercise 1

Tags: Lists, Streamlit, Dashboards

Create a dropdown filter.

```python
region = st.selectbox(
    "Region",
    data["region"].unique()
)
```

---

## Exercise 2

Tags: Lists, Dashboards

Filter the dataset.

```python
filtered = data[data["region"] == region]
```

---

## Exercise 3

Tags: Streamlit, Dashboards

Display filtered data.

```python
st.write(filtered)
```

---

## Exercise 4

Tags: Lists, Visualization, Streamlit, Dashboards

Create a filtered chart.

```python
st.bar_chart(filtered["sales"])
```

---

# Common Mistakes

## Hardcoding Filter Values

Incorrect:

```python
st.selectbox("Region", ["West", "East"])
```

Better:

```python
data["region"].unique()
```

This ensures the filter always reflects the dataset.

---

## Filtering Before Loading Data

Data must be loaded before filters are applied.

Incorrect workflow:

```text
Filter
   ↓
Load Data
```

Correct workflow:

```text
Load Data
   ↓
Filter
```

---

## Displaying Too Much Data

Large datasets can slow dashboards.

Best practice:

```text
Display summary charts
Limit rows shown
```

---

# Real-World Use

Interactive filters are widely used in analytics dashboards.

Examples include:

• healthcare provider performance dashboards  
• sales analytics tools  
• financial reporting dashboards  
• marketing campaign analysis.

Example workflow:

```text
User selects region
        ↓
Dashboard filters data
        ↓
Charts update instantly
```

This allows business users to explore data without needing SQL knowledge.

---

# Lesson Recap

In this lesson you learned:

• how interactive filters work  
• how filters control dashboard behavior  
• how Streamlit widgets capture user input  
• how filtered dashboards enable data exploration  

Interactive filters transform dashboards into **dynamic data applications**.

---

# Next Lesson

Next we will learn:

# Lesson 5 — Exporting Data

You will learn:

• how users export data from dashboards  
• how to generate downloadable files  
• how data apps support reporting workflows.
