# Module 10 — Automation & CI/CD

# Lesson 3 — Scheduling Data Jobs

---

# Lesson Objective

By the end of this lesson learners will understand:

• why **scheduled jobs** are used in data systems  
• how organizations automate recurring data processes  
• how Python scripts can run on schedules  
• common scheduling tools used in data engineering  

Most real-world data systems rely on scheduled processes that run automatically at regular intervals. These scheduled tasks ensure that data pipelines, reports, and analytics systems remain **up-to-date without manual intervention**.

---

# Overview

In small projects, developers may manually run scripts when needed.

Example:

```bash
python process_sales_data.py
```

However, in real production environments, many processes must run automatically.

Examples of scheduled processes:

```text
Nightly ETL pipelines
Hourly data refresh jobs
Daily report generation
Weekly analytics dashboards
```

Without scheduling, developers would need to manually execute these scripts.

Scheduling tools automate this process.

Example workflow:

```text
Data arrives
      ↓
Scheduled job triggers script
      ↓
Data pipeline processes data
      ↓
Results stored in database
      ↓
Dashboard updated
```

Scheduling allows organizations to maintain **reliable automated workflows**.

---

# Key Idea Cards (3 Cards)

### Scheduling Automates Repetitive Tasks

Many data workflows must run repeatedly.

Examples include:

```text
Daily data ingestion
Weekly reporting
Monthly financial analytics
```

Scheduling ensures these processes run automatically.

---

### Jobs Run at Specific Intervals

Scheduling systems allow tasks to run at defined times.

Example intervals:

```text
Every hour
Every day
Every week
```

This allows consistent automated processing.

---

### Scheduled Jobs Power Data Pipelines

Most data pipelines rely on automated scheduling.

Example pipeline:

```text
Extract Data
     ↓
Transform Data
     ↓
Load Data
```

Each step may run automatically at scheduled intervals.

---

# Key Concepts

## Cron Jobs

Cron is a common scheduling system used in Linux environments.

Example cron schedule:

```text
0 2 * * *
```

This means:

```text
Run every day at 2:00 AM
```

Cron jobs trigger scripts automatically.

---

## Task Schedulers

Various tools exist to schedule jobs.

Common scheduling tools include:

```text
Cron
Airflow
Prefect
Dagster
Windows Task Scheduler
```

These tools manage automated workflows.

---

## Data Pipeline Scheduling

In data engineering, scheduled jobs often run pipelines.

Example pipeline schedule:

```text
Daily ETL Job
```

Workflow:

```text
Extract Data
Transform Data
Load Data
```

This ensures systems stay updated.

---

# Decision Flow

Developers often decide to schedule jobs using the following logic:

```text
Does the script run repeatedly?
        ↓
       YES
        ↓
Create a scheduled job
```

Scheduling reduces manual work and improves reliability.

---

# Code Examples

### Example 1 — Python Script for Scheduled Job

```python
def run_pipeline():
    extract_data()
    transform_data()
    load_data()

run_pipeline()
```

This script can be scheduled to run automatically.

---

### Example 2 — Cron Job Command

Example cron entry:

```text
0 2 * * * python /scripts/process_data.py
```

This runs the script every day at 2 AM.

---

### Example 3 — Python Scheduler Library

Python includes libraries for scheduling tasks.

Example using `schedule` library:

```python
import schedule
import time

def job():
    print("Running scheduled task")

schedule.every().day.at("02:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
```

This script runs a task daily at 2 AM.

---

### Example 4 — Automated Data Pipeline

Example pipeline automation:

```python
def pipeline():
    extract_data()
    clean_data()
    load_data()

pipeline()
```

This pipeline can be triggered by a scheduler.

---

# SQL / Excel Comparison

Scheduling concepts exist in other tools as well.

| Concept | Python | SQL | Excel |
|------|------|------|------|
| automation | scheduled jobs | SQL Agent jobs | macros |
| pipeline execution | Python scripts | stored procedures | workbook refresh |
| recurring tasks | cron jobs | database jobs | scheduled reports |

Example SQL scheduling:

```text
SQL Server Agent Job
```

This runs database processes automatically.

---

# Practice Exercises

### Exercise 1

Tags: print(), Functions, CI/CD, Scripts

Create a Python script that runs a simple pipeline.

Example:

```python
def pipeline():
    print("Extract")
    print("Transform")
    print("Load")
```

---

### Exercise 2

Tags: pip install, Scheduling

Install the Python scheduling library:

```bash
pip install schedule
```

---

### Exercise 3

Tags: Scripts, Scheduling

Write a script that runs every minute using the schedule library.

---

### Exercise 4

Tags: Orchestration, Scheduling

Research scheduling tools such as:

```text
Apache Airflow
Prefect
Dagster
```

These tools are widely used in data engineering.

---

# Common Mistakes

### Running Jobs Manually

Manual execution is unreliable and prone to human error.

Automated scheduling improves reliability.

---

### Poor Monitoring of Scheduled Jobs

Scheduled jobs should include logging and monitoring.

Otherwise failures may go unnoticed.

---

### Scheduling Jobs Too Frequently

Running jobs too often can overload systems.

Schedules should match data processing requirements.

---

# Real-World Use

Scheduling is fundamental to modern data systems.

Example analytics workflow:

```text
Raw Data Arrives
        ↓
Scheduled Pipeline Runs
        ↓
Database Updated
        ↓
Dashboard Refreshes
```

Examples of scheduled systems include:

• data warehouses  
• analytics dashboards  
• financial reporting systems  
• machine learning pipelines.

Automated scheduling ensures systems stay updated without manual effort.

---

# Lesson Recap

In this lesson you learned:

• why scheduled jobs are used in data systems  
• how cron jobs automate scripts  
• how Python tasks can run automatically  
• how scheduling powers data pipelines.

Scheduling allows organizations to **run reliable automated data workflows**.

---

# Next Lesson

Next we will learn:

# Lesson 4 — Secrets Management

You will learn:

• why secrets management is critical in automation pipelines  
• how credentials are stored securely  
• how CI/CD systems manage secrets  
• best practices for protecting sensitive data.
