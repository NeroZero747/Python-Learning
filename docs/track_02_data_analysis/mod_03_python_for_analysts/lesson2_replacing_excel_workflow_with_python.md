# Module 15 — Python for Analysts

# Lesson 2 — Replacing Excel Workflows with Python

---

# Lesson Objective

By the end of this lesson learners will understand:

• how Python can replace repetitive **Excel workflows**  
• how to **read Excel files into Python**  
• how to perform common spreadsheet operations using **Pandas**  
• how to **write results back to Excel**

Python allows analysts to automate many tasks traditionally done in Excel.

---

# Overview

Excel is widely used for:

```text
Cleaning datasets
Creating pivot tables
Performing calculations
Combining spreadsheets
Generating reports
```

However, Excel workflows often involve **manual steps**.

Example workflow in Excel:

```text
Download data
Open spreadsheet
Clean columns
Apply formulas
Create pivot table
Save new report
Email results
```

This process may need to be repeated **daily or weekly**.

Python allows analysts to automate the same workflow.

Example automated workflow:

```text
Excel File → Python Script → Data Transformations → Automated Excel Report
```

Instead of repeating manual steps, the script performs them automatically.

---

# Key Idea Cards (3 Cards)

### Python Reads Excel Files

Python can load Excel spreadsheets directly into memory.

Libraries used:

```text
pandas
openpyxl
xlsxwriter
```

Example:

```python
import pandas as pd

df = pd.read_excel("sales_data.xlsx")
```

The spreadsheet becomes a **DataFrame**.

---

### DataFrames Replace Spreadsheet Tables

A **DataFrame** works like a spreadsheet table.

Example:

| region | sales |
|------|------|
| East | 100 |
| West | 150 |
| South | 200 |

Python can filter, transform, and calculate values just like Excel.

---

### Python Can Generate Excel Reports

Python can write processed results back to Excel.

Example:

```python
df.to_excel("report.xlsx", index=False)
```

This allows automated **report generation**.

---

# Key Concepts

## Reading Excel Files

The Pandas library can read Excel files.

Example:

```python
import pandas as pd

df = pd.read_excel("sales.xlsx")

print(df.head())
```

This loads the spreadsheet into a DataFrame.

---

## Inspecting the Data

Once loaded, the dataset can be inspected.

Example:

```python
print(df.columns)
print(df.shape)
print(df.head())
```

This helps analysts understand the dataset.

---

## Performing Calculations

Python can calculate totals or averages.

Example:

```python
total_sales = df["sales"].sum()

print(total_sales)
```

---

## Filtering Rows

Python can filter rows similar to Excel filters.

Example:

```python
high_sales = df[df["sales"] > 100]

print(high_sales)
```

---

## Creating New Columns

Python can create calculated fields.

Example:

```python
df["sales_tax"] = df["sales"] * 0.08
```

---

## Writing Data Back to Excel

After transformations, the results can be exported.

Example:

```python
df.to_excel("clean_sales.xlsx", index=False)
```

This generates a new Excel report automatically.

---

# Decision Flow

When deciding whether to automate Excel workflows:

```text
Is the spreadsheet process repeated frequently?
        ↓
Automate with Python
```

```text
Does the file contain large datasets?
        ↓
Python may be more efficient
```

```text
Does the workflow require multiple files?
        ↓
Python simplifies automation
```

Example automation pipeline:

```text
Raw Excel Files
      ↓
Python Script
      ↓
Clean Dataset
      ↓
Automated Report
```

---

# Code Examples

### Example 1 — Read an Excel File

```python
import pandas as pd

df = pd.read_excel("sales.xlsx")

print(df.head())
```

---

### Example 2 — Calculate Total Sales

```python
total_sales = df["sales"].sum()

print(total_sales)
```

---

### Example 3 — Filter High Sales

```python
high_sales = df[df["sales"] > 100]

print(high_sales)
```

---

### Example 4 — Export Results

```python
df.to_excel("report.xlsx", index=False)
```

---

# SQL / Excel Comparison

### Excel Example

```text
=SUM(B2:B100)
```

---

### SQL Example

```sql
SELECT SUM(sales)
FROM sales_table
```

---

### Python Example

```python
df["sales"].sum()
```

All three methods perform the same calculation.

---

# Practice Exercises

### Exercise 1

Tags: Excel, CI/CD

Load an Excel file using Pandas.

---

### Exercise 2

Tags: Excel, CI/CD, Arithmetic

Calculate the average value of a column.

---

### Exercise 3

Tags: WHERE, Excel, CI/CD

Filter rows where sales exceed 200.

---

### Exercise 4

Tags: Excel, CI/CD, Data I/O

Export the filtered dataset to a new Excel file.

---

# Common Mistakes

### Forgetting to Install Required Libraries

Excel support requires:

```text
pandas
openpyxl
```

Install them using:

```bash
pip install pandas openpyxl
```

---

### Overwriting Important Files

Always write results to a **new file** instead of replacing the original.

---

### Loading Extremely Large Excel Files

Large datasets may perform better when stored as **CSV or database tables**.

---

# Real-World Use

Many organizations automate Excel reporting with Python.

Examples include:

```text
Monthly financial reports
Sales performance reports
Operational dashboards
Inventory summaries
```

Example workflow:

```text
Database Export
      ↓
Python Transformation
      ↓
Excel Report
      ↓
Automated Email
```

Python reduces manual reporting effort.

---

# Lesson Recap

In this lesson you learned:

• how Python reads Excel spreadsheets  
• how Pandas replaces spreadsheet calculations  
• how to filter and transform Excel data  
• how to generate automated Excel reports

Python can transform manual spreadsheet processes into **automated data workflows**.

---

# Next Lesson

Next we will continue Module 15 with:

# Lesson 3 — Using Python with SQL Queries

You will learn:

• how Python connects to databases  
• how to execute SQL queries from Python  
• how to load query results into DataFrames  
• how Python and SQL work together for reporting.
