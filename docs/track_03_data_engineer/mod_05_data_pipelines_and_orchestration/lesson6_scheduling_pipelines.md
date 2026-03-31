# Module 18 — Data Pipelines & Orchestration  
## Lesson 9 — Scheduling Pipelines

---

# Lesson Objective

By the end of this lesson you will understand:

- Why data pipelines must run on **automated schedules**
- How scheduling systems **trigger pipeline execution**
- Common scheduling tools used in data engineering
- How Python pipelines can be scheduled automatically

Scheduling ensures pipelines run **consistently and reliably without manual intervention**.

---

# Overview

Most pipelines must run repeatedly.

Examples:

```text
Daily sales processing
Hourly API data ingestion
Weekly analytics reports
Monthly financial summaries
```

Running these pipelines manually would be inefficient and error-prone.

Scheduling systems allow pipelines to run automatically.

Example pipeline schedule:

```text
12:00 AM → Pipeline runs
12:05 AM → Data processed
12:10 AM → Dashboard refreshed
```

Automation ensures data is **always up to date**.

---

# What is a Scheduler?

A scheduler is a system that **runs tasks automatically at specific times or intervals**.

Example scheduling triggers:

```text
Every hour
Every day
Every Monday
Every month
```

Schedulers monitor time and launch pipelines when the schedule is reached.

---

# Example Scheduled Pipeline

Example daily pipeline:

```text
Sales Database
      ↓
Nightly Pipeline
      ↓
Data Warehouse
      ↓
Dashboard Refresh
```

This pipeline might run every night at midnight.

---

# Simple Scheduling Example

Example Python script:

```python
def run_pipeline():
    print("Pipeline executed")
```

Instead of running this manually, a scheduler can trigger the script automatically.

---

# Cron Scheduling

One of the most common scheduling tools is **cron**.

Cron is widely used in Linux systems.

Example cron schedule:

```text
0 0 * * *
```

This schedule means:

```text
Run the pipeline every day at midnight
```

Cron syntax defines **when jobs run**.

---

# Cron Schedule Format

Cron uses five time fields:

```text
Minute Hour Day Month Day-of-week
```

Example:

```text
0 12 * * *
```

This means:

```text
Run every day at 12:00 PM
```

---

# Example Cron Job

Example cron entry:

```text
0 0 * * * python pipeline.py
```

This command runs the pipeline script every night.

---

# Scheduling with Python

Some pipelines use Python libraries for scheduling.

Example using the **schedule** library:

```python
import schedule
import time

def run_pipeline():
    print("Pipeline executed")

schedule.every().day.at("00:00").do(run_pipeline)

while True:
    schedule.run_pending()
    time.sleep(60)
```

This script runs the pipeline daily at midnight.

---

# Enterprise Scheduling Tools

Large organizations often use advanced workflow schedulers.

Examples include:

```text
Apache Airflow
Prefect
Dagster
Luigi
```

These tools manage complex pipeline workflows.

---

# Example Airflow Workflow

Example pipeline workflow:

```text
Extract Data
      ↓
Validate Data
      ↓
Transform Data
      ↓
Load Data
```

Airflow schedules and monitors each stage.

---

# Why Scheduling Matters

Scheduling provides several important benefits.

```text
Automated execution
Consistent pipeline runs
Reduced manual effort
Reliable data updates
```

Without scheduling, pipelines would require manual execution.

---

# Decision Flow

When designing a pipeline:

```text
Does the pipeline run repeatedly?
        |
       Yes
        |
Add scheduling
```

If pipelines run on a schedule, automation is required.

---

# Code Example — Scheduled Pipeline

Example pipeline script:

```python
import pandas as pd

df = pd.read_csv("sales.csv")

df["revenue"] = df["price"] * df["quantity"]

df.to_sql("sales_table")
```

Cron command:

```text
0 0 * * * python pipeline.py
```

The scheduler runs the pipeline automatically.

---

# SQL / Excel Comparison

Manual workflow:

```text
Open spreadsheet
Download data
Clean data
Refresh dashboard
```

Automated workflow:

```text
Scheduler
 ↓
Pipeline runs automatically
 ↓
Dashboard updates
```

Automation eliminates repetitive work.

---

# Practice Exercises

### Exercise 1

Tags: CI/CD, Scheduling

Write a cron schedule that runs a pipeline every day at midnight.

Example:

```text
0 0 * * *
```

---

### Exercise 2

Tags: print(), Functions, CI/CD, Scheduling

Write a Python function that prints a message when a pipeline runs.

Example:

```python
def run_pipeline():
    print("Pipeline executed")
```

---

### Exercise 3

Tags: CI/CD, Orchestration, Scheduling

Research one workflow orchestration tool such as:

```text
Airflow
Prefect
Dagster
```

---

# Common Mistakes

### Mistake 1 — Manual Pipeline Execution

Manual processes increase the risk of missed pipeline runs.

---

### Mistake 2 — Poor Scheduling Frequency

Running pipelines too frequently may overload systems.

---

### Mistake 3 — No Monitoring

Scheduled pipelines must still be monitored to detect failures.

---

# Real-World Use

Pipeline scheduling is used across many industries.

Examples include:

---

### Marketing Analytics

```text
Daily campaign performance pipelines
```

---

### Financial Systems

```text
Hourly market data ingestion
```

---

### Healthcare Systems

```text
Nightly claims processing pipelines
```

Scheduling ensures data systems remain **automated and reliable**.

---

# Key Idea Cards

### Card 1

Scheduling systems trigger pipeline execution automatically.

---

### Card 2

Cron is a widely used scheduling system for running scripts.

---

### Card 3

Enterprise systems use orchestration tools such as **Airflow or Prefect**.

---

# Lesson Recap

In this lesson you learned:

- why pipelines must run on schedules  
- how schedulers automate pipeline execution  
- how cron scheduling works  
- tools used for pipeline orchestration

Scheduling ensures pipelines run **automatically and consistently**.

---

# Next Lesson

Next you will learn:

**Module 18 — Lesson 10: Building a Simple Python Pipeline**

You will learn:

- how to combine pipeline concepts into a complete script  
- how extraction, transformation, and loading work together  
- how to build a **fully functioning pipeline**.