# Module 8 — Building Data Applications

# Lesson 2 — Introduction to Streamlit

---

# Lesson Objective

By the end of this lesson learners will understand:

• what **Streamlit** is  
• how Streamlit turns Python scripts into web applications  
• how Streamlit applications are structured  
• how to build a simple interactive dashboard  

Streamlit is one of the most popular tools for building **data applications in Python** because it allows developers to create interactive dashboards using simple Python code.

---

# Overview

Traditional web applications require multiple technologies:

```text
HTML
CSS
JavaScript
Backend Framework
Database
```

Building dashboards with these tools can be complex and time-consuming.

Streamlit simplifies this process by allowing developers to build web applications using **only Python**.

Example Streamlit workflow:

```text
Python Script
      ↓
Run Streamlit
      ↓
Web App Generated
```

When the script runs, Streamlit automatically creates a web interface.

Example command:

```bash
streamlit run app.py
```

This launches a local web server and opens the application in a browser.

Streamlit is commonly used for:

• data exploration tools  
• internal dashboards  
• machine learning demos  
• analytics applications.

---

# Key Idea Cards (3 Cards)

## Streamlit Converts Python Scripts into Web Apps

A Streamlit app is simply a Python script.

Example:

```python
import streamlit as st

st.title("My Data App")
```

When executed with Streamlit, the script becomes a web application.

---

## Streamlit Automatically Handles UI Components

Streamlit provides built-in interface components.

Examples include:

• buttons  
• dropdown menus  
• charts  
• tables  
• file uploads  

These components make it easy to create interactive applications.

---

## Streamlit Updates Automatically

When users interact with the application, Streamlit reruns the script and updates the interface.

Example workflow:

```text
User selects filter
       ↓
Streamlit reruns script
       ↓
Charts update automatically
```

This creates reactive dashboards with minimal code.

---

# Key Concepts

## Streamlit Application Structure

A typical Streamlit app includes:

```text
Load Data
Create Filters
Process Data
Display Results
```

Example structure:

```python
import streamlit as st
import pandas as pd

data = pd.read_csv("sales.csv")

st.title("Sales Dashboard")

st.write(data.head())
```

---

## Streamlit Components

Streamlit includes many built-in UI components.

Examples:

| Component | Purpose |
|------|------|
| st.title() | page title |
| st.write() | display text or data |
| st.selectbox() | dropdown selection |
| st.slider() | numeric selection |
| st.button() | trigger actions |

These components allow developers to build interfaces quickly.

---

## Streamlit Layout

Streamlit displays components **from top to bottom** in the order they appear in the script.

Example:

```python
st.title("Dashboard")

st.write("Welcome")

st.bar_chart(data)
```

The interface will render in the same order.

---

# Decision Flow

Choosing a framework for building data apps often follows this logic:

```text
Need quick data dashboard?
         ↓
       YES
         ↓
     Use Streamlit

Need complex custom UI?
         ↓
       YES
         ↓
Use React / Web Framework
```

Streamlit is ideal for **internal analytics tools and prototypes**.

---

# Code Examples

## Example 1 — Simple Streamlit App

```python
import streamlit as st

st.title("My First Streamlit App")

st.write("Welcome to my dashboard.")
```

Run the application:

```bash
streamlit run app.py
```

This launches a web app.

---

## Example 2 — Displaying Data

```python
import streamlit as st
import pandas as pd

data = pd.read_csv("sales.csv")

st.write(data)
```

This displays a table in the application.

---

## Example 3 — Displaying Charts

```python
st.bar_chart(data["sales"])
```

This creates a bar chart.

---

## Example 4 — User Input

```python
region = st.selectbox(
    "Select Region",
    data["region"].unique()
)
```

Users can interact with the dashboard through dropdown menus.

---

# SQL / Excel Comparison

Streamlit functionality resembles tools users may already know.

| Feature | Streamlit | SQL | Excel |
|------|------|------|------|
| filtering | selectbox | WHERE | filter |
| aggregations | Python functions | GROUP BY | pivot table |
| charts | st.bar_chart | BI tools | charts |

Example SQL query:

```sql
SELECT *
FROM sales
WHERE region = 'West'
```

A Streamlit filter performs the same logic interactively.

---

# Practice Exercises

## Exercise 1

Tags: Imports, Scripts, Data Processing, Streamlit

Create a Streamlit script.

```python
import streamlit as st

st.title("My Dashboard")
```

Run the script using:

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

Display the dataset using Streamlit.

---

## Exercise 3

Tags: Lists, Data Processing, Streamlit

Add a dropdown filter.

```python
region = st.selectbox(
    "Region",
    data["region"].unique()
)
```

Filter the dataset based on the selected region.

---

# Common Mistakes

## Forgetting to Run Streamlit

Running the script with Python will not launch the web app.

Incorrect:

```bash
python app.py
```

Correct:

```bash
streamlit run app.py
```

---

## Loading Large Datasets in the App

Large datasets can slow down applications.

Best practice:

• load aggregated data  
• cache results  
• limit rows displayed.

---

## Mixing UI Logic and Data Logic

Apps should separate:

```text
data processing
user interface
```

This keeps applications easier to maintain.

---

# Real-World Use

Streamlit is widely used for internal data tools.

Examples include:

• sales dashboards  
• machine learning model interfaces  
• operational analytics tools  
• data quality monitoring dashboards.

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
Charts Update
```

This allows teams to interact with analytics data without writing SQL.

---

# Lesson Recap

In this lesson you learned:

• what Streamlit is  
• how Streamlit converts Python scripts into web applications  
• how Streamlit dashboards are structured  
• how to build simple interactive dashboards  

Streamlit provides one of the **fastest ways to build data applications in Python**.

---

# Next Lesson

Next we will learn:

# Lesson 3 — Building a Simple Dashboard

You will learn:

• how to structure a full Streamlit dashboard  
• how to display charts and metrics  
• how to organize dashboard layouts  
• how to build a production-ready analytics dashboard.
