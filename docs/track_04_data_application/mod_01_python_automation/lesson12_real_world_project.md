# Module 16 — Automation with Python  
## Lesson 13 — Building a Real-World Automation Project

---

# Lesson Objective

By the end of this lesson you will understand:

- How to design a **complete real-world automation project**
- How all automation components fit together
- How to structure an automation system from **data source → report delivery**
- How to build an automation workflow similar to those used in **analytics teams and data engineering environments**

This lesson demonstrates how everything learned in **Module 15** works together in practice.

---

# Overview

Throughout this module you learned how to:

- automate scripts
- schedule jobs
- generate reports
- manage files
- send emails
- log activity
- handle errors
- use configuration files
- structure projects
- deploy automation systems

Now we combine these concepts into a **complete automation pipeline**.

Example business scenario:

A company wants a **daily sales report delivered every morning**.

Manual process:

```text
Download sales data
Clean the data
Calculate metrics
Create Excel report
Send report to management
```

Time required: **30–60 minutes daily**

Automated process:

```text
Scheduler triggers script
        ↓
Load data
        ↓
Process metrics
        ↓
Generate report
        ↓
Send email
        ↓
Log pipeline activity
```

Total human time: **0 minutes**

---

# Key Concepts

## End-to-End Automation

An automation pipeline usually follows this structure:

```text
Data Source
     ↓
Data Processing
     ↓
Report Generation
     ↓
File Management
     ↓
Notification
```

Each step is implemented using Python modules.

---

## Real-World Automation Architecture

A typical automation project might look like this:

```text
automation_pipeline/

config/
    config.json

data/
    raw_data/

reports/
    sales_report.xlsx

logs/
    pipeline.log

scripts/
    load_data.py
    process_data.py
    generate_report.py
    send_email.py

main.py
```

This structure keeps projects **organized and maintainable**.

---

## Pipeline Workflow

The automation process typically works like this:

```text
Scheduler
     ↓
Run main.py
     ↓
Load data
     ↓
Process metrics
     ↓
Generate report
     ↓
Send report via email
     ↓
Write logs
```

This pipeline runs automatically.

---

# Decision Flow

When designing an automation project:

```text
Is the task repeated frequently?
        |
        Yes
        |
Does it follow predictable steps?
        |
        Yes
        |
Can each step be automated?
        |
        Yes
        |
Design an automation pipeline
```

Examples:

- daily reporting
- ETL pipelines
- KPI dashboards
- automated alerts

---

# Code Examples

## Step 1 — Load Data

File: `load_data.py`

```python
import pandas as pd

def load_data():

    df = pd.read_csv("data/sales_data.csv")

    return df
```

This module extracts the dataset.

---

## Step 2 — Process Data

File: `process_data.py`

```python
def process_data(df):

    summary = df.groupby("region")["sales"].sum()

    return summary
```

This calculates the business metrics.

---

## Step 3 — Generate Report

File: `generate_report.py`

```python
def generate_report(summary):

    report_file = "reports/sales_report.xlsx"

    summary.to_excel(report_file)

    return report_file
```

This creates the final Excel report.

---

## Step 4 — Send Email

File: `send_email.py`

```python
import smtplib
from email.message import EmailMessage

def send_email(report_file):

    msg = EmailMessage()

    msg["Subject"] = "Daily Sales Report"
    msg["From"] = "reports@example.com"
    msg["To"] = "team@example.com"

    msg.set_content("Attached is the daily sales report.")

    with open(report_file, "rb") as f:

        msg.add_attachment(
            f.read(),
            maintype="application",
            subtype="octet-stream",
            filename=report_file
        )

    with smtplib.SMTP("smtp.office365.com", 587) as server:

        server.starttls()

        server.login("reports@example.com", "password")

        server.send_message(msg)
```

This distributes the report.

---

## Step 5 — Main Pipeline Script

File: `main.py`

```python
from scripts.load_data import load_data
from scripts.process_data import process_data
from scripts.generate_report import generate_report
from scripts.send_email import send_email


def main():

    df = load_data()

    summary = process_data(df)

    report = generate_report(summary)

    send_email(report)

    print("Automation pipeline completed")


if __name__ == "__main__":

    main()
```

This script runs the entire pipeline.

---

# SQL / Excel Comparison

### Manual Reporting Workflow

```text
Run SQL query
Export results
Open Excel
Build report
Email stakeholders
```

Manual effort required daily.

---

### Automated Python Workflow

```text
Scheduler runs script
     ↓
Query data
     ↓
Generate report
     ↓
Email report
```

Fully automated.

---

# Practice Exercises

## Exercise 1

Tags: CI/CD, Automation

Create a folder structure for an automation project.

Example:

```text
automation_pipeline/

scripts/
config/
logs/
reports/
data/
```

---

## Exercise 2

Tags: Loops, Data I/O

Write separate modules for:

```text
load_data
process_data
generate_report
```

---

## Exercise 3

Tags: CI/CD, Scripts

Create a `main.py` script that runs the full pipeline.

---

## Exercise 4 (Real-World)

Tags: CI/CD, Arithmetic, Logging, Automation

Design an automation project that generates a **daily operational report**.

Your pipeline should include:

```text
data ingestion
metric calculation
report generation
email distribution
logging
```

---

# Common Mistakes

## Mistake 1 — Overcomplicating Automation

Start with simple automation before building complex systems.

---

## Mistake 2 — Not Logging Pipeline Runs

Without logs it is difficult to diagnose issues.

Always record pipeline activity.

---

## Mistake 3 — Poor Project Organization

A well-structured project is easier to maintain and extend.

---

# Real-World Use

Automation pipelines are widely used across industries.

Examples include:

---

### Business Intelligence

Automation pipelines generate:

```text
daily dashboards
sales reports
financial summaries
```

---

### Data Engineering

Pipelines perform:

```text
data extraction
data transformation
data loading
```

---

### Analytics Operations

Automation systems maintain:

```text
KPI tracking
data refresh pipelines
scheduled reporting
```

---

# Key Idea Cards

### Card 1

Automation pipelines combine multiple automated steps into a **single workflow**.

---

### Card 2

Organizing automation into modules improves **maintainability and scalability**.

---

### Card 3

Real-world automation pipelines replace **manual reporting processes**.

---

# Lesson Recap

In this lesson you learned:

- how real-world automation projects are structured
- how pipelines combine multiple automation tasks
- how Python automates reporting workflows end-to-end

You now understand how to build a **complete automation project using Python**.

---

# Next Lesson

Next you will learn:

**Module 15 — Lesson 14: Automation Best Practices**

This final lesson will cover:

- best practices for automation scripts
- maintaining automation systems
- designing scalable automation workflows.