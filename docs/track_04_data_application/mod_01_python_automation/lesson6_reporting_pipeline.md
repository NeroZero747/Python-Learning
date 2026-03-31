# Module 16 — Automation with Python  
## Lesson 6 — Building a Complete Automated Reporting Pipeline

---

# Lesson Objective

By the end of this lesson you will understand:

- How to combine multiple automation steps into a **complete reporting pipeline**
- How automated reporting systems work in real organizations
- How to design a workflow that includes:
  - data loading
  - data transformation
  - report generation
  - email delivery
  - scheduling
- How Python scripts become **end-to-end automated systems**

This lesson brings together everything you learned in **Module 15**.

---

# Overview

In real business environments, automation rarely involves just one step.

Instead, multiple steps are combined into a **pipeline**.

Example daily reporting workflow:

```text
Download Data
      ↓
Process Data
      ↓
Generate Report
      ↓
Save Output File
      ↓
Send Email
```

Manually, this might take **30–60 minutes every day**.

With Python, the entire process can run automatically in **seconds**.

Automation pipelines are used for:

- business reporting
- financial reporting
- data warehouse updates
- analytics dashboards
- ETL workflows

---

# Key Concepts

## Automation Pipeline

An automation pipeline is a **series of automated steps** that transform raw data into final results.

Example pipeline:

```text
Extract Data
     ↓
Transform Data
     ↓
Generate Report
     ↓
Distribute Results
```

In data engineering this pattern is known as:

**ETL (Extract, Transform, Load)**

---

## Pipeline Components

A reporting pipeline usually includes several components.

| Step | Description |
|------|-------------|
| Data Extraction | Load data from files or databases |
| Data Processing | Clean and transform data |
| Report Generation | Create Excel or CSV reports |
| File Management | Save and organize reports |
| Email Delivery | Send reports to stakeholders |
| Scheduling | Run automatically on schedule |

Each step is handled by Python.

---

## Modular Automation Scripts

Automation pipelines are easier to manage when broken into **separate functions or modules**.

Example structure:

```text
pipeline/
    load_data.py
    process_data.py
    generate_report.py
    send_email.py
    main.py
```

This makes scripts easier to maintain and reuse.

---

# Decision Flow

When designing an automation pipeline:

```text
Does the process follow repeatable steps?
        |
        Yes
        |
Can each step be automated?
        |
        Yes
        |
Can the steps run sequentially?
        |
        Yes
        |
Build an automation pipeline
```

Examples:

- daily operational reports
- financial summaries
- inventory tracking
- KPI dashboards

---

# Code Examples

## Example 1 — Pipeline Structure

Example reporting pipeline:

```text
load_data()
process_data()
generate_report()
send_email()
```

Each step performs a different task.

---

## Example 2 — Loading Data

```python
import pandas as pd

def load_data():

    df = pd.read_csv("sales_data.csv")

    return df
```

This function extracts data from a file.

---

## Example 3 — Processing Data

```python
def process_data(df):

    summary = df.groupby("region")["sales"].sum()

    return summary
```

This step transforms the raw data.

---

## Example 4 — Generating a Report

```python
def generate_report(summary):

    report_file = "sales_summary.xlsx"

    summary.to_excel(report_file)

    return report_file
```

This step creates the Excel report.

---

## Example 5 — Sending the Report

```python
import smtplib
from email.message import EmailMessage

def send_email(report_file):

    msg = EmailMessage()

    msg["Subject"] = "Daily Sales Report"
    msg["From"] = "email@example.com"
    msg["To"] = "team@example.com"

    msg.set_content("Attached is the daily report.")

    with open(report_file, "rb") as f:

        msg.add_attachment(
            f.read(),
            maintype="application",
            subtype="octet-stream",
            filename=report_file
        )

    with smtplib.SMTP("smtp.office365.com", 587) as server:

        server.starttls()

        server.login("email@example.com", "password")

        server.send_message(msg)
```

This step distributes the report.

---

## Example 6 — Running the Pipeline

The **main script** connects everything together.

```python
def main():

    df = load_data()

    summary = process_data(df)

    report = generate_report(summary)

    send_email(report)

    print("Pipeline completed successfully")

main()
```

This script executes the full workflow.

---

# SQL / Excel Comparison

### Manual Reporting Workflow

1. Run SQL query
2. Export results
3. Clean data
4. Build Excel report
5. Send email

Time: **30–60 minutes**

---

### Python Automation Pipeline

```text
Script Runs
     ↓
Data Loaded
     ↓
Report Generated
     ↓
Email Sent
```

Time: **seconds**

---

# Practice Exercises

## Exercise 1

Tags: CI/CD, Scripts, Arithmetic, Data I/O

Write a Python script that:

1. Loads a dataset
2. Calculates summary statistics
3. Saves a report file

---

## Exercise 2

Tags: CI/CD, Scripts, Notifications

Extend the script to:

1. Send the report via email.

---

## Exercise 3

Tags: CI/CD, Scripts, Data I/O

Break the script into functions:

```text
load_data()
process_data()
generate_report()
```

---

## Exercise 4 (Real-World)

Tags: Excel, CI/CD, Arithmetic, Automation

Design an automated pipeline that:

1. Loads daily sales data
2. Calculates total revenue
3. Generates an Excel report
4. Emails the report

Imagine this runs **every morning at 8 AM**.

---

# Common Mistakes

## Mistake 1 — Writing One Large Script

Large scripts are difficult to maintain.

Better approach:

Break scripts into **functions or modules**.

---

## Mistake 2 — Not Logging Pipeline Runs

Automation pipelines should record when they run.

Example:

```python
import datetime

print("Pipeline ran at:", datetime.datetime.now())
```

---

## Mistake 3 — Not Handling Errors

Production pipelines should catch errors.

Example:

```python
try:
    main()
except Exception as e:
    print("Pipeline failed:", e)
```

---

# Real-World Use

Automation pipelines are used across many industries.

Examples include:

---

### Business Intelligence

Automated pipelines generate:

- daily dashboards
- KPI reports
- executive summaries

---

### Data Engineering

Large-scale systems run pipelines that:

```text
Extract data
Transform records
Load data warehouse
```

---

### Analytics Platforms

Reporting pipelines feed:

- dashboards
- APIs
- data products

---

# Key Idea Cards

### Card 1

Automation pipelines combine multiple steps into **a single automated workflow**.

---

### Card 2

Breaking pipelines into functions makes code **easier to maintain**.

---

### Card 3

Automated reporting pipelines save **hours of manual work**.

---

# Lesson Recap

In this lesson you learned:

- What an automation pipeline is
- How Python combines multiple automation tasks
- How to build a complete automated reporting system

You now understand how Python scripts become **end-to-end automation workflows**.

---

# Next Lesson

Next you will learn:

**Module 15 — Lesson 7: Logging and Monitoring Automation Scripts**

You will learn how to:

- track when automation jobs run
- record errors
- monitor automated pipelines

This is an important step in making automation **reliable and production-ready**.