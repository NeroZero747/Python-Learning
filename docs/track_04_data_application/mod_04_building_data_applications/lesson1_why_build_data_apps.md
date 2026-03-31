# Module 8 — Building Data Applications

# Lesson 1 — Why Build Data Apps?

---

# Lesson Objective

By the end of this lesson learners will understand:

• what a **data application** is  
• why organizations build data apps instead of static reports  
• how data apps improve analytics workflows  
• common tools used to build data applications in Python  

Data applications allow users to **interact with data directly**, rather than relying only on static dashboards or reports.

---

# Overview

Traditional analytics workflows often look like this:

```text
Database
   ↓
SQL Query
   ↓
Export Data
   ↓
Excel Report
```

While this process works, it has several limitations:

• reports quickly become outdated  
• users cannot explore the data themselves  
• analysts must repeatedly run queries for new requests  

To solve this problem, organizations build **data applications**.

A data application allows users to interact with data directly through a web interface.

Example workflow:

```text
Database
     ↓
Data Application
     ↓
User Filters Data
     ↓
Charts / Tables Update Instantly
```

Instead of asking an analyst for every new report, users can:

• search data  
• filter datasets  
• generate charts  
• export results  

This dramatically improves productivity.

Data applications are commonly used for:

• operational dashboards  
• analytics exploration  
• reporting tools  
• internal business applications.

---

# Key Idea Cards (3 Cards)

## Data Apps Enable Interactive Analytics

Traditional reports are static.

Example:

```text
Excel Report → fixed data
```

Data applications allow users to interact with data dynamically.

Example:

```text
Filter data
Search records
Update charts
```

This makes analytics more flexible.

---

## Data Apps Reduce Analyst Workload

Without data apps, analysts often receive requests like:

```text
"Can you run this report again?"
"Can you filter it by region?"
"Can you export the data?"
```

A data app allows users to perform these tasks themselves.

---

## Data Apps Connect Data to Decision Making

Interactive tools help decision makers explore data quickly.

Example workflow:

```text
User opens dashboard
       ↓
Applies filters
       ↓
Views updated charts
       ↓
Makes business decision
```

This speeds up insight generation.

---

# Key Concepts

## Data Applications

A **data application** is a web-based tool that allows users to interact with data.

Examples include:

• dashboards  
• reporting portals  
• analytics search tools  
• internal data utilities.

---

## Interactive Analytics

Interactive analytics allows users to modify views dynamically.

Examples include:

• filtering data  
• selecting date ranges  
• adjusting chart parameters  
• exporting data.

---

## Python Data App Frameworks

Several Python frameworks allow developers to build data applications.

Popular tools include:

• **Streamlit**  
• **Shiny for Python**  
• **Dash**  
• **Panel**

These tools generate web interfaces directly from Python code.

---

# Decision Flow

Choosing between analytics tools often follows this logic:

```text
Need static report?
      ↓
    YES
      ↓
  Use Excel / PDF

Need interactive analytics?
      ↓
    YES
      ↓
 Build a Data App
```

Interactive tools provide significantly more flexibility.

---

# Code Examples

## Example 1 — Simple Streamlit App

```python
import streamlit as st
import pandas as pd

data = pd.read_csv("sales.csv")

st.title("Sales Dashboard")

st.write(data.head())
```

Running this script creates a simple data application.

---

## Example 2 — Adding a Filter

```python
import streamlit as st
import pandas as pd

data = pd.read_csv("sales.csv")

region = st.selectbox("Select Region", data["region"].unique())

filtered = data[data["region"] == region]

st.write(filtered)
```

Users can filter the dataset interactively.

---

## Example 3 — Creating a Chart

```python
st.bar_chart(filtered["sales"])
```

Charts update automatically when filters change.

---

## Example 4 — Exporting Data

```python
st.download_button(
    label="Download Data",
    data=filtered.to_csv(index=False),
    file_name="filtered_data.csv"
)
```

Users can export filtered results.

---

# SQL / Excel Comparison

Data apps provide similar functionality to tools users may already know.

| Feature | Python Data App | SQL | Excel |
|------|------|------|------|
| filtering | interactive UI | WHERE clause | filter |
| aggregation | Python code | GROUP BY | pivot tables |
| visualization | built-in charts | BI tools | charts |

Example SQL query:

```sql
SELECT *
FROM sales
WHERE region = 'West'
```

A data app allows the user to perform this filter interactively.

---

# Practice Exercises

## Exercise 1

Tags: Imports, Scripts, Data Processing, Streamlit

Create a basic Streamlit application.

```python
import streamlit as st

st.title("My First Data App")
```

Run the application using:

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

Display the dataset in Streamlit.

---

## Exercise 3

Tags: Lists, Tuples, Streamlit

Add a filter.

Allow users to filter by region.

```python
region = st.selectbox("Region", data["region"].unique())
```

Observe how the dataset changes.

---

# Common Mistakes

## Overloading Apps with Too Much Data

Large datasets can slow down applications.

Best practice:

```text
Load summary data
Filter server-side
Limit displayed rows
```

---

## Ignoring User Experience

A good data app should be easy to navigate.

Poor UX can make tools difficult to use.

---

## Hardcoding Filters

Apps should dynamically populate filter values from the dataset.

Example:

```python
data["region"].unique()
```

---

# Real-World Use

Many organizations build internal data applications.

Examples include:

• provider analytics dashboards  
• sales performance tools  
• customer segmentation platforms  
• operational reporting systems.

Example workflow:

```text
Data Warehouse
       ↓
Streamlit Application
       ↓
Business User Filters Data
       ↓
Interactive Charts Update
```

These tools allow teams to explore data without writing SQL.

---

# Lesson Recap

In this lesson you learned:

• what data applications are  
• how they improve analytics workflows  
• common tools used to build them  
• how Streamlit can create interactive dashboards  

Data apps allow organizations to **turn raw data into interactive decision tools**.

---

# Next Lesson

Next we will learn:

# Lesson 2 — Introduction to Streamlit

You will learn:

• how Streamlit works  
• how to build a complete data dashboard  
• how to structure Streamlit applications  
• how to deploy Streamlit apps for users.
