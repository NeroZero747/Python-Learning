# Module 16 — Automation with Python  
## Lesson 7 — Logging and Monitoring Automation Scripts

---

# Lesson Objective

By the end of this lesson you will understand:

- Why automation scripts need **logging**
- How Python records **script activity and errors**
- How to monitor automated pipelines
- How logging helps debug problems in production systems

Logging is one of the most important steps when moving automation from **personal scripts to production systems**.

---

# Overview

Automation scripts often run **without human supervision**.

Examples:

- Nightly data pipelines
- Daily reporting jobs
- Automated email reports
- Scheduled ETL processes

When these scripts fail, someone needs to know **what happened and when**.

Without logging:

```text
Script runs
     ↓
Fails silently
     ↓
No one knows why
```

With logging:

```text
Script runs
     ↓
Events recorded in log file
     ↓
Errors tracked
     ↓
Issues can be diagnosed
```

Logging provides **visibility into automated systems**.

---

# Key Concepts

## What is Logging?

Logging means **recording events that occur during program execution**.

Example events:

- script started
- data loaded
- report generated
- email sent
- error occurred

Logs allow developers and analysts to **trace what happened during execution**.

---

## Log Files

Automation scripts usually write logs to **text files**.

Example log file:

```text
job_log.txt
```

Example content:

```text
2026-03-10 08:00 Script started
2026-03-10 08:00 Data loaded successfully
2026-03-10 08:01 Report generated
2026-03-10 08:01 Email sent
```

These records help track pipeline activity.

---

## Python Logging Module

Python includes a built-in module for logging.

```python
import logging
```

This module allows scripts to record messages with different severity levels.

---

## Logging Levels

Logging systems categorize messages by importance.

| Level | Purpose |
|------|------|
| DEBUG | Detailed debugging information |
| INFO | General script activity |
| WARNING | Potential issues |
| ERROR | Failures in execution |
| CRITICAL | Major system failures |

Example:

```text
INFO: Report generated
ERROR: Database connection failed
```

---

# Decision Flow

Logging should be added when:

```text
Does the script run automatically?
        |
        Yes
        |
Could the script fail?
        |
        Yes
        |
Do you need to know what happened?
        |
        Yes
        |
Add logging
```

Logging is critical for:

- scheduled jobs
- ETL pipelines
- reporting automation
- production applications

---

# Code Examples

## Example 1 — Basic Logging

```python
import logging

logging.basicConfig(
    filename="automation.log",
    level=logging.INFO
)

logging.info("Script started")
```

This script writes messages to:

```text
automation.log
```

---

## Example 2 — Logging Script Steps

```python
import logging

logging.basicConfig(
    filename="pipeline.log",
    level=logging.INFO
)

logging.info("Pipeline started")

logging.info("Loading data")

logging.info("Generating report")

logging.info("Pipeline completed")
```

Example log output:

```text
INFO: Pipeline started
INFO: Loading data
INFO: Generating report
INFO: Pipeline completed
```

---

## Example 3 — Logging Errors

```python
import logging

logging.basicConfig(
    filename="pipeline.log",
    level=logging.INFO
)

try:

    df = pd.read_csv("sales.csv")

    logging.info("File loaded successfully")

except Exception as e:

    logging.error("Failed to load data")

    logging.error(e)
```

This records both the failure and the error message.

---

## Example 4 — Logging with Timestamps

```python
import logging

logging.basicConfig(
    filename="automation.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Script started")
```

Example log output:

```text
2026-03-10 08:00:01 - INFO - Script started
```

Timestamps make logs much easier to analyze.

---

# SQL / Excel Comparison

### Without Logging

```text
Script scheduled
      ↓
Script fails
      ↓
No record of failure
```

Users only notice when **reports are missing**.

---

### With Logging

```text
Script scheduled
      ↓
Script runs
      ↓
Logs recorded
      ↓
Errors captured
```

Logs make it easier to **diagnose issues quickly**.

---

# Practice Exercises

## Exercise 1

Tags: Scripts, Logging

Write a script that logs:

```text
Script started
Script completed
```

Save logs in a file called:

```text
job_log.txt
```

---

## Exercise 2

Tags: Scripts, Logging, Notifications

Modify the script to log:

- data loading
- report generation
- email delivery

---

## Exercise 3

Tags: Missing Data, SQL Queries, Databases, Scripts

Add error handling so the script logs when:

- a file is missing
- a database query fails

---

## Exercise 4 (Real-World)

Tags: Loops, CI/CD, Logging, Notifications

Design a logging system for a reporting pipeline that records:

```text
Pipeline started
Data loaded
Report generated
Email sent
Pipeline completed
```

---

# Common Mistakes

## Mistake 1 — Using `print()` Instead of Logging

Example:

```python
print("Script started")
```

This only shows output in the console.

Logging writes messages to **permanent log files**.

Better:

```python
logging.info("Script started")
```

---

## Mistake 2 — Not Logging Errors

Scripts should log both **success and failure events**.

Without error logs, debugging becomes difficult.

---

## Mistake 3 — Overwriting Log Files

Default logging may overwrite logs.

Better approach:

Use **append mode** or rotating logs.

---

# Real-World Use

Logging is essential in professional data systems.

Examples include:

---

### Data Pipeline Monitoring

Logs record:

```text
Data extraction started
Transformation completed
Warehouse load finished
```

---

### System Alerts

Logs can trigger alerts when:

- pipelines fail
- data is missing
- thresholds are exceeded

---

### Audit Trails

Logs also serve as **audit records** showing when reports were generated.

---

# Key Idea Cards

### Card 1

Logging records what happens during script execution.

---

### Card 2

Python's **logging module** provides structured logging.

---

### Card 3

Logs make automated pipelines **easier to monitor and debug**.

---

# Lesson Recap

In this lesson you learned:

- why automation scripts need logging
- how to record events and errors
- how logs help diagnose problems
- how logging improves reliability

Logging is a critical step in making automation **production-ready**.

---

# Next Lesson

Next you will learn:

**Module 15 — Lesson 8: Error Handling in Automation Scripts**

You will learn how Python can:

- handle unexpected errors
- prevent automation jobs from crashing
- recover gracefully when problems occur

This makes automation systems **more reliable and resilient**.