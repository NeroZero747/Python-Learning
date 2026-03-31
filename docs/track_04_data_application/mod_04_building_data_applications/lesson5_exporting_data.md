# Module 8 — Building Data Applications

# Lesson 5 — Exporting Data

---

# Lesson Objective

By the end of this lesson learners will understand:

• how users export data from data applications  
• how to generate downloadable files from dashboards  
• how exporting supports reporting and analysis workflows  
• how to implement export functionality in Streamlit applications  

Exporting data is a critical feature in many analytics applications because it allows users to **take filtered or processed data and use it in other tools such as Excel, BI platforms, or reporting systems**.

---

# Overview

Data applications often allow users to explore data interactively.

Example workflow:

```text
User opens dashboard
       ↓
Applies filters
       ↓
Views results
```

However, users frequently need to **download the data they are viewing**.

Example use cases:

• exporting filtered reports  
• sharing results with colleagues  
• importing data into Excel  
• creating presentations or documents.

A typical export workflow looks like this:

```text
User applies filters
       ↓
Dashboard generates dataset
       ↓
User clicks download
       ↓
File exported (CSV / Excel)
```

Data applications often provide export options such as:

• CSV files  
• Excel files  
• PDF reports  
• images of charts.

For most analytics dashboards, **CSV export is the most common option**.

---

# Key Idea Cards (3 Cards)

## Exporting Makes Data Portable

Exporting allows users to move data into other tools.

Example workflow:

```text
Dashboard
   ↓
Export CSV
   ↓
Open in Excel
```

This allows users to perform additional analysis outside the application.

---

## Exports Reflect Current Filters

Exported data usually reflects the **current state of the dashboard filters**.

Example:

```text
Region Filter = West
```

Exported dataset will only include **West region data**.

This ensures that exported reports match the user’s selections.

---

## Export Features Improve Adoption

When dashboards allow exporting:

• users can easily share data  
• analysts spend less time generating reports  
• business teams gain more flexibility.

This increases the usefulness of data applications.

---

# Key Concepts

## Downloadable Files

Many dashboards generate downloadable files dynamically.

Example formats include:

• CSV  
• Excel (.xlsx)  
• JSON  
• PDF reports.

CSV files are commonly used because they are simple and widely supported.

---

## Dynamic File Generation

Exported files are usually generated **at the moment the user clicks download**.

Example process:

```text
User filters dashboard
       ↓
Dashboard prepares dataset
       ↓
User clicks export
       ↓
File generated and downloaded
```

This ensures the exported file contains **up-to-date data**.

---

## Data Serialization

Before data can be exported, it must be converted into a file format.

Example conversion:

```python
data.to_csv()
```

This converts a DataFrame into CSV format.

---

# Decision Flow

Export features typically follow this design process:

```text
User filters data
        ↓
Generate filtered dataset
        ↓
Convert dataset to file format
        ↓
Provide download button
```

This workflow ensures exported data matches the current dashboard state.

---

# Code Examples

## Example 1 — Converting Data to CSV

```python
csv_data = filtered_data.to_csv(index=False)
```

This converts a dataset into CSV format.

---

## Example 2 — Streamlit Download Button

```python
st.download_button(
    label="Download CSV",
    data=csv_data,
    file_name="filtered_data.csv"
)
```

This creates a button that allows users to download the data.

---

## Example 3 — Full Export Example

```python
import streamlit as st
import pandas as pd

data = pd.read_csv("sales.csv")

region = st.selectbox("Region", data["region"].unique())

filtered = data[data["region"] == region]

csv = filtered.to_csv(index=False)

st.download_button(
    label="Download Data",
    data=csv,
    file_name="sales_data.csv"
)
```

This example exports filtered data.

---

## Example 4 — Exporting Excel Files

```python
filtered.to_excel("sales.xlsx")
```

Excel files may be useful when users prefer working with spreadsheets.

---

# SQL / Excel Comparison

Exporting data also exists in other tools.

| Feature | Streamlit | SQL | Excel |
|------|------|------|------|
| exporting | download button | export query result | save workbook |
| filtering | widgets | WHERE clause | filter |
| reporting | dashboards | BI tools | reports |

Example SQL export workflow:

```sql
SELECT *
FROM sales
WHERE region = 'West'
```

The query result may then be exported.

---

# Practice Exercises

## Exercise 1

Tags: Booleans, to_csv(), Indexes, Data I/O

Convert a dataset to CSV.

```python
csv_data = data.to_csv(index=False)
```

---

## Exercise 2

Tags: Streamlit, Data I/O

Create a download button.

```python
st.download_button(
    "Download CSV",
    data=csv_data
)
```

---

## Exercise 3

Tags: Data I/O, Applications

Combine filters with export.

Allow users to:

• filter the dataset  
• download the filtered results.

---

# Common Mistakes

## Exporting Unfiltered Data

If the export ignores filters, users may download incorrect data.

Correct approach:

```text
Export filtered dataset
```

---

## Large File Exports

Very large datasets may slow the application.

Best practice:

• export aggregated data  
• limit rows  
• generate reports instead of full datasets.

---

## Hardcoding File Names

File names should reflect the dataset.

Example:

```text
sales_report.csv
filtered_orders.csv
```

Clear names help users identify files.

---

# Real-World Use

Export features are essential in many analytics systems.

Examples include:

• healthcare provider reports  
• financial analysis tools  
• sales performance dashboards  
• marketing analytics platforms.

Example workflow:

```text
User filters data
      ↓
Dashboard updates
      ↓
User downloads report
      ↓
File used in Excel or presentation
```

This allows users to integrate analytics results into their workflow.

---

# Lesson Recap

In this lesson you learned:

• how exporting works in data applications  
• how dashboards generate downloadable files  
• how Streamlit implements download functionality  
• how export features support reporting workflows  

Exporting data allows dashboards to **serve both interactive exploration and traditional reporting needs**.

---

# Next Lesson

Next we will learn:

# Lesson 6 — Deployment Basics

You will learn:

• how to deploy data applications  
• how users access dashboards  
• how to host Streamlit applications  
• how analytics apps are delivered to business users.
