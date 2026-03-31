# Module 16 — Automation with Python  
## Lesson 2 — Scheduling Python Jobs (Running Scripts Automatically)

---

# Lesson Objective

By the end of this lesson you will understand:

- Why automation becomes powerful when **scheduled**
- How Python scripts can run **automatically without manual execution**
- How to schedule Python jobs using:
  - **Task Scheduler (Windows)**
  - **Cron jobs (Linux / Mac)**
- How automated jobs power **daily reporting and ETL pipelines**

This lesson introduces the concept of **automated scheduling**, which is one of the most common real-world uses of Python in business environments.

---

# Overview

In the previous lesson you learned how to **automate tasks using Python scripts**.

However, many tasks still require someone to manually run the script.

Example:

```bash
python daily_report.py
```

If someone forgets to run the script, the report does not get generated.

Scheduling solves this problem.

Instead of running scripts manually, your computer or server can run them **automatically at specific times**.

Examples:

| Task | Schedule |
|-----|-----|
| Sales report | Every day at 8:00 AM |
| Data warehouse load | Every night at midnight |
| Email notifications | Every Monday |
| Dashboard refresh | Every hour |

This is the foundation of **data pipelines and automated reporting systems**.

---

# Key Concepts

## Scheduled Jobs

A **scheduled job** is a program that runs automatically at a defined time.

Example schedule:

| Script | Schedule |
|------|------|
| daily_sales.py | Every morning |
| update_database.py | Every hour |
| weekly_report.py | Every Friday |

Instead of someone running the script manually, the system runs it automatically.

---

## Job Scheduler

A **job scheduler** is software that runs scripts at specific times.

Common schedulers:

| System | Scheduler |
|------|------|
| Windows | Task Scheduler |
| Linux | Cron |
| Mac | Cron / Launchd |
| Cloud | Airflow / Prefect / Dagster |

For beginners, the most common tool is:

**Windows Task Scheduler**

---

## Automation Pipeline

In real workflows, automation often follows this pattern:

```text
Schedule Trigger
        ↓
Python Script Runs
        ↓
Data is Loaded
        ↓
Data is Processed
        ↓
Results Saved or Sent
```

Example:

```text
8:00 AM
     ↓
Run daily_report.py
     ↓
Query database
     ↓
Calculate metrics
     ↓
Export Excel file
     ↓
Email report
```

---

# Decision Flow

Use scheduled automation when:

```text
Does the task happen repeatedly?
        |
        Yes
        |
Does it follow predictable steps?
        |
        Yes
        |
Does it need to run on a schedule?
        |
        Yes
        |
Schedule the Python script
```

Common use cases:

- Daily reports
- Nightly database updates
- Data warehouse ETL
- API data pulls
- File cleanup jobs

---

# Code Examples

## Example 1 — A Daily Automation Script

Example script:

```python
import pandas as pd
from datetime import datetime

df = pd.read_csv("sales_data.csv")

total_sales = df["sales"].sum()

today = datetime.today().date()

print(f"Daily Sales ({today}): {total_sales}")
```

Saved as:

```text
daily_sales_report.py
```

This script can now be **scheduled to run every morning**.

---

## Example 2 — Saving Automated Reports

Automation scripts usually **generate output files**.

```python
import pandas as pd
from datetime import datetime

df = pd.read_csv("sales_data.csv")

summary = df.groupby("region")["sales"].sum()

today = datetime.today().strftime("%Y-%m-%d")

summary.to_csv(f"sales_summary_{today}.csv")

print("Report generated")
```

This automatically creates a **dated report file**.

---

## Example 3 — Logging Job Runs

Automation scripts often log activity.

```python
import datetime

log_time = datetime.datetime.now()

with open("job_log.txt", "a") as log:
    log.write(f"Job ran at {log_time}\n")
```

This helps track when jobs executed.

---

# SQL / Excel Comparison

### Manual Reporting Process

1. Open Excel
2. Run SQL query
3. Export results
4. Clean data
5. Send report

Time: **30–60 minutes**

---

### Python Scheduled Process

```text
8:00 AM
Script runs automatically
Report generated
Email sent automatically
```

Time: **0 minutes of manual work**

---

# Scheduling on Windows (Task Scheduler)

Windows includes a built-in job scheduler.

Steps:

1. Open **Task Scheduler**
2. Click **Create Basic Task**
3. Choose a name

Example:

```text
Daily Sales Report
```

4. Choose schedule

Example:

```text
Daily at 8:00 AM
```

5. Choose **Start a Program**

Program:

```text
python
```

Arguments:

```text
daily_sales_report.py
```

Now the script runs **every morning automatically**.

---

# Scheduling on Linux / Mac (Cron)

Linux and Mac systems use **Cron**.

Cron syntax example:

```bash
0 8 * * * python daily_sales_report.py
```

Meaning:

| Field | Value | Meaning |
|-----|-----|-----|
| Minute | 0 | On the hour |
| Hour | 8 | 8 AM |
| Day | * | Every day |
| Month | * | Every month |
| Weekday | * | Every day |

Result:

The script runs **every day at 8 AM**.

---

# Practice Exercises

## Exercise 1

Tags: CSV, HTTP Methods, Scripts, Arithmetic

Write a script that:

1. Loads a CSV file
2. Calculates total revenue
3. Saves a daily summary file

Example output:

```text
daily_summary_2026-03-10.csv
```

---

## Exercise 2

Tags: Scripts, Scheduling

Modify the script to:

1. Add the current date
2. Log when the script ran

Example log file:

```text
job_log.txt
```

Contents:

```text
Job ran at 2026-03-10 08:00
```

---

## Exercise 3 (Real-World)

Tags: SQL Queries, Scripts, Automation, Scheduling

Create a script that:

1. Runs a SQL query
2. Saves the results to a CSV file
3. Logs execution time

Imagine this script runs **every morning automatically**.

---

# Common Mistakes

## Mistake 1 — Using Relative Paths Incorrectly

Scheduled jobs may run from a different working directory.

Bad:

```python
df = pd.read_csv("sales.csv")
```

Better:

```python
import os

base_dir = os.path.dirname(__file__)
file_path = os.path.join(base_dir, "sales.csv")

df = pd.read_csv(file_path)
```

---

## Mistake 2 — Not Logging Errors

If a scheduled job fails silently, no one knows.

Better approach:

```python
try:
    run_job()
except Exception as e:
    print("Job failed:", e)
```

---

## Mistake 3 — Overwriting Reports

Avoid overwriting output files.

Bad:

```python
report.csv
```

Better:

```python
report_2026_03_10.csv
```

---

# Real-World Use

Scheduling is used heavily in **data engineering and analytics workflows**.

Examples:

---

### Daily Data Warehouse Load

Every night:

1. Extract data
2. Transform data
3. Load into warehouse

This process is called:

**ETL (Extract, Transform, Load)**

---

### Automated Reporting

Python jobs automatically:

- Query databases
- Generate Excel reports
- Send emails to stakeholders

---

### Data Pipeline Monitoring

Scheduled scripts monitor:

- data freshness
- job failures
- pipeline delays

---

# Key Idea Cards

### Card 1

Automation becomes powerful when scripts run **without human interaction**.

---

### Card 2

Schedulers like **Task Scheduler and Cron** run Python scripts automatically.

---

### Card 3

Scheduling is the foundation of **data pipelines and ETL systems**.

---

# Lesson Recap

In this lesson you learned:

- What scheduled jobs are
- How Python scripts can run automatically
- How schedulers trigger automation
- How scheduling powers real-world reporting systems

You now understand how to move from **manual scripts to fully automated workflows**.

---

# Next Lesson

In the next lesson you will learn:

**Module 15 — Lesson 3: Automating Excel Reports with Python**

You will learn how to:

- Generate Excel reports with Python
- Format spreadsheets automatically
- Replace manual Excel reporting workflows.