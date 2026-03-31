# Module 16 — Automation with Python  
## Lesson 3 — Automating Excel Reports with Python

---

# Lesson Objective

By the end of this lesson you will understand:

- How Python can **automatically generate Excel reports**
- How to **read Excel files** using Python
- How to **write data to Excel**
- How to **create formatted Excel reports**
- How Python can replace **manual Excel reporting workflows**

This lesson focuses on one of the **most practical real-world uses of Python** for analysts and reporting teams.

---

# Overview

Excel is one of the most widely used tools in business.

Many analysts spend hours every week performing repetitive Excel tasks:

- Downloading data
- Cleaning spreadsheets
- Calculating totals
- Creating pivot tables
- Formatting reports
- Sending reports to stakeholders

Python can automate these tasks.

Instead of manually editing Excel files, Python can:

1. Load Excel data
2. Transform it
3. Generate a formatted report
4. Save the final workbook

All in **seconds**.

---

# Key Concepts

## Reading Excel Files

Python can read Excel files using the **pandas** library.

Excel files usually have the extension:

```text
.xlsx
```

Pandas can load these files into a **DataFrame**.

Example:

```python
import pandas as pd

df = pd.read_excel("sales_report.xlsx")
```

Now the Excel data is available inside Python.

---

## Writing Excel Files

Python can also create Excel files.

Example:

```python
df.to_excel("output_report.xlsx")
```

This allows Python to generate reports automatically.

---

## Excel Libraries

Common Python libraries used with Excel:

| Library | Purpose |
|------|------|
| pandas | Read and write Excel files |
| openpyxl | Modify Excel files |
| xlsxwriter | Create formatted Excel reports |

In most reporting automation tasks:

**pandas + xlsxwriter** is the best combination.

---

# Decision Flow

Use Python for Excel automation when:

```text
Do you regularly update Excel reports?
        |
        Yes
        |
Do you repeat the same steps each time?
        |
        Yes
        |
Can the process be described step-by-step?
        |
        Yes
        |
Automate it with Python
```

Common automation tasks:

- Monthly reports
- Sales summaries
- Financial reports
- KPI dashboards
- Operational metrics

---

# Code Examples

## Example 1 — Reading an Excel File

```python
import pandas as pd

df = pd.read_excel("sales.xlsx")

print(df.head())
```

This script:

1. Opens the Excel file
2. Loads it into a DataFrame
3. Displays the first rows

---

## Example 2 — Creating a Simple Excel Report

```python
import pandas as pd

df = pd.read_csv("sales_data.csv")

summary = df.groupby("region")["sales"].sum()

summary.to_excel("sales_summary.xlsx")

print("Report created successfully")
```

This script:

1. Loads sales data
2. Calculates total sales per region
3. Exports results to Excel

---

## Example 3 — Creating a Multi-Sheet Excel Report

Python can generate Excel workbooks with multiple sheets.

```python
import pandas as pd

sales = pd.read_csv("sales.csv")
customers = pd.read_csv("customers.csv")

with pd.ExcelWriter("business_report.xlsx") as writer:

    sales.to_excel(writer, sheet_name="Sales")
    customers.to_excel(writer, sheet_name="Customers")

print("Excel report generated")
```

The final Excel file contains:

| Sheet | Content |
|-----|-----|
| Sales | Sales data |
| Customers | Customer information |

---

## Example 4 — Formatting Excel Reports

Using **xlsxwriter**, you can format Excel files.

```python
import pandas as pd

df = pd.read_csv("sales.csv")

with pd.ExcelWriter("sales_report.xlsx", engine="xlsxwriter") as writer:

    df.to_excel(writer, sheet_name="Sales")

    workbook = writer.book
    worksheet = writer.sheets["Sales"]

    currency_format = workbook.add_format({'num_format': '$#,##0'})

    worksheet.set_column("B:B", 15, currency_format)

print("Formatted Excel report created")
```

This script:

- Writes Excel data
- Formats numbers as currency
- Adjusts column width

---

# SQL / Excel Comparison

### Manual Excel Workflow

1. Export SQL data
2. Open Excel
3. Create pivot table
4. Format report
5. Save workbook

Time: **30–60 minutes**

---

### Python Automation

```python
df = pd.read_sql(query, connection)

summary = df.groupby("region")["sales"].sum()

summary.to_excel("sales_report.xlsx")
```

Time: **3 seconds**

---

# Practice Exercises

## Exercise 1

Tags: Excel, File I/O, HTTP Methods, Scripts

Write a Python script that:

1. Reads an Excel file
2. Calculates total revenue
3. Saves the results in a new Excel file.

Example output:

```text
revenue_summary.xlsx
```

---

## Exercise 2

Tags: Excel, File I/O, HTTP Methods, Scripts

Create a script that:

1. Reads two CSV files
2. Writes them into different Excel sheets

Example output:

```text
company_report.xlsx
```

Sheets:

```text
Sales
Customers
```

---

## Exercise 3 (Real-World)

Tags: GROUP BY, Excel, Scripts, Arithmetic

Create a Python script that:

1. Loads sales data
2. Groups by region
3. Calculates total revenue
4. Exports a formatted Excel report

Imagine this report runs **automatically every morning**.

---

# Common Mistakes

## Mistake 1 — Forgetting the Excel Engine

Sometimes pandas needs a specific engine.

Example:

```python
pd.read_excel("file.xlsx", engine="openpyxl")
```

---

## Mistake 2 — Exporting Without Index Control

By default pandas includes an index.

Example problem:

```text
Unnamed: 0 column
```

Better approach:

```python
df.to_excel("report.xlsx", index=False)
```

---

## Mistake 3 — Overwriting Important Files

Automation scripts should avoid overwriting important files.

Better approach:

```text
report_2026_03_10.xlsx
```

Instead of:

```text
report.xlsx
```

---

# Real-World Use

Excel automation is used heavily in business analytics.

Examples include:

---

### Financial Reporting

Python generates:

- Monthly financial reports
- Revenue summaries
- Budget comparisons

---

### Operational Reporting

Python scripts generate:

- daily operational dashboards
- production metrics
- KPI tracking spreadsheets

---

### Automated Excel Distribution

Python can generate reports and email them automatically to teams.

Example workflow:

```text
Python Script
     ↓
Create Excel Report
     ↓
Attach Report to Email
     ↓
Send to Stakeholders
```

---

# Key Idea Cards

### Card 1

Python can **automatically generate Excel reports**.

---

### Card 2

Libraries like **pandas and xlsxwriter** make Excel automation easy.

---

### Card 3

Excel automation saves **hours of manual reporting work**.

---

# Lesson Recap

In this lesson you learned:

- How Python reads Excel files
- How Python writes Excel reports
- How to generate multi-sheet reports
- How to format Excel output automatically

Python can replace **many repetitive Excel reporting workflows**.

---

# Next Lesson

In the next lesson you will learn:

**Module 15 — Lesson 4: Automating Emails with Python**

You will learn how to:

- Send automated emails
- Attach reports to emails
- Build a fully automated reporting workflow.