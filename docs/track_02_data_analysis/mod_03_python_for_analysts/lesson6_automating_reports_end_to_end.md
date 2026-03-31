# Module 15 — Python for Analysts

# Lesson 6 — Automating Reports End-to-End

---

# Lesson Objective

By the end of this lesson learners will understand:

• how to build a **complete automated reporting pipeline**  
• how Python scripts can run **end-to-end reporting workflows**  
• how to generate reports automatically for stakeholders  
• how to schedule reports to run **daily, weekly, or monthly**

This lesson shows how analysts can turn manual reporting processes into **fully automated pipelines**.

---

# Overview

Many reporting processes involve several steps.

Example manual workflow:

```text
Export data from database
Download CSV file
Clean the dataset
Create summary tables
Build Excel report
Email report to stakeholders
```

These tasks may need to be repeated **every day or week**.

Python allows analysts to automate the entire process.

Example automated pipeline:

```text
Database / Data Source
        ↓
Python Reporting Script
        ↓
Data Cleaning & Transformations
        ↓
Excel / Dashboard Output
        ↓
Automated Email Delivery
```

Once the automation is built, the report can run automatically without manual intervention.

---

# Key Idea Cards (3 Cards)

### Automated Pipelines Replace Manual Work

A Python script can perform the entire reporting workflow.

Example process:

```text
Extract → Transform → Report → Deliver
```

This is commonly called a **data pipeline**.

---

### Scheduled Scripts Run Automatically

Automated scripts can run at scheduled times.

Examples:

```text
Daily reports
Weekly summaries
Monthly financial reports
```

Scheduling ensures reports are always generated on time.

---

### Automated Reports Improve Reliability

Automation ensures:

```text
Consistent calculations
Accurate transformations
No skipped steps
```

This improves reporting reliability.

---

# Key Concepts

## End-to-End Reporting Pipeline

An automated reporting pipeline usually contains four steps:

```text
1 Extract data
2 Transform data
3 Generate report
4 Deliver report
```

Python can handle each of these steps.

---

## Step 1 — Extract Data

Data may come from:

```text
Database queries
CSV files
Excel files
APIs
```

Example:

```python
import pandas as pd

df = pd.read_csv("sales_data.csv")
```

---

## Step 2 — Transform Data

Transformations prepare data for reporting.

Examples include:

```text
Filtering rows
Creating calculated columns
Aggregating metrics
Cleaning values
```

Example:

```python
df["tax"] = df["sales"] * 0.08
```

---

## Step 3 — Generate Report

Reports usually summarize the data.

Example:

```python
summary = df.groupby("region")["sales"].sum()
```

Result:

| region | sales |
|---|---|
| East | 300 |
| West | 200 |
| South | 400 |

---

## Step 4 — Export the Report

The report can be exported to a file.

Example:

```python
summary.to_excel("weekly_sales_report.xlsx")
```

This creates the final report.

---

# Scheduling Automated Reports

Scripts can be scheduled to run automatically.

Common scheduling tools include:

```text
Windows Task Scheduler
Cron jobs (Linux)
CI/CD pipelines
Data orchestration tools
```

Example schedule:

```text
Run every day at 6:00 AM
```

Example command:

```bash
python generate_report.py
```

---

# Decision Flow

When deciding to automate a report:

```text
Does the report run regularly?
        ↓
Automate with Python
```

```text
Does the report require multiple steps?
        ↓
Build reporting pipeline
```

```text
Do stakeholders rely on timely delivery?
        ↓
Schedule automated reporting
```

Example pipeline:

```text
Source Data
      ↓
Python Script
      ↓
Clean Dataset
      ↓
Excel Report
      ↓
Email Delivery
```

---

# Code Examples

### Example 1 — Extract Data

```python
import pandas as pd

df = pd.read_csv("sales_data.csv")
```

---

### Example 2 — Transform Data

```python
df["tax"] = df["sales"] * 0.08
```

---

### Example 3 — Generate Summary

```python
summary = df.groupby("region")["sales"].sum()
```

---

### Example 4 — Export Report

```python
summary.to_excel("sales_report.xlsx")
```

Running the script creates the report automatically.

---

# SQL / Excel Comparison

### Excel Workflow

```text
Download data
Clean spreadsheet
Create pivot table
Save report
```

---

### SQL Workflow

```sql
SELECT region, SUM(sales)
FROM transactions
GROUP BY region;
```

---

### Python Workflow

```python
summary = df.groupby("region")["sales"].sum()
summary.to_excel("sales_report.xlsx")
```

Python allows the entire workflow to run automatically.

---

# Practice Exercises

### Exercise 1

Tags: Scripts, Arithmetic, Automation, Data I/O

Create a script that loads a dataset and calculates total sales.

---

### Exercise 2

Tags: Automation, Data Analysis

Generate a summary table by category.

---

### Exercise 3

Tags: Excel, Automation

Export the summary results to an Excel file.

---

### Exercise 4

Tags: Scripts, Automation, Scheduling

Describe how this script could be scheduled to run automatically.

---

# Common Mistakes

### Running Scripts Manually Every Time

The goal of automation is to **schedule scripts automatically**.

---

### Hardcoding File Locations

Scripts should reference configurable file paths.

Example:

```python
data_path = "data/sales.csv"
```

---

### Ignoring Error Handling

Scripts should handle errors such as missing files or invalid data.

---

# Real-World Use

Automated reporting pipelines are used across many industries.

Examples include:

```text
Daily revenue reporting
Marketing performance dashboards
Inventory monitoring reports
Customer analytics summaries
```

Example automation workflow:

```text
Data Warehouse
       ↓
Python Reporting Script
       ↓
Excel / Dashboard Dataset
       ↓
Automated Delivery to Stakeholders
```

Automation allows teams to focus on **analysis rather than manual reporting tasks**.

---

# Lesson Recap

In this lesson you learned:

• how to build an end-to-end reporting pipeline  
• how Python automates extraction, transformation, and reporting  
• how automated scripts improve reliability  
• how scheduled reporting pipelines work

Automated reporting is one of the **most practical and valuable applications of Python for analysts**.

---

# Module 15 Complete

This module introduced Python from the perspective of an analyst.

You learned:

```text
Why analysts use Python
Replacing Excel workflows
Using Python with SQL queries
Automating repetitive data tasks
Building reporting scripts
Automating reports end-to-end
```

These skills allow analysts to transition from **manual workflows to automated data pipelines**.

---

# Next Module

Next we will build a module that analysts frequently request:

# Module 16 — Python Automation

This module will cover:

```text
Automating file workflows
Batch processing files
Generating Excel reports
Sending automated emails
Scheduling automation jobs
```

This module builds directly on the skills learned in **Python for Analysts**.
