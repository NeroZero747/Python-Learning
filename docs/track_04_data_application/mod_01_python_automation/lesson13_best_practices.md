# Module 16 — Automation with Python  
## Lesson 14 — Automation Best Practices

---

# Lesson Objective

By the end of this lesson you will understand:

- Best practices for writing **reliable automation scripts**
- How to design automation systems that are **maintainable and scalable**
- How to avoid common automation mistakes
- How professional teams maintain **production automation pipelines**

This lesson summarizes the principles that make automation systems **stable, maintainable, and production-ready**.

---

# Overview

Automation scripts can start simple but quickly grow into **critical business systems**.

Examples:

- automated reports sent to executives
- nightly data warehouse pipelines
- operational monitoring systems
- automated financial processes

If these systems fail, they can disrupt business operations.

Therefore, automation should follow **best practices** to ensure reliability.

Example poor automation system:

```text
One large script
Hardcoded values
No logging
No error handling
Runs manually
```

Example professional automation system:

```text
Modular code
Configuration files
Logging system
Error handling
Version control
Scheduled execution
```

Best practices ensure automation systems are **robust and maintainable**.

---

# Key Concepts

## Write Small, Focused Functions

Automation scripts should be broken into **small functions**.

Example:

Bad approach:

```text
500-line script doing everything
```

Better approach:

```text
load_data()
process_data()
generate_report()
send_email()
```

Small functions improve readability and maintainability.

---

## Use Configuration Files

Avoid hardcoding values in scripts.

Bad example:

```python
email = "manager@example.com"
file_path = "C:/reports/sales.csv"
```

Better approach:

```text
config.json
```

Configuration files allow scripts to run in **different environments** without code changes.

---

## Add Logging

Automation scripts should record activity.

Example log entries:

```text
Pipeline started
Data loaded successfully
Report generated
Email sent
```

Logging helps diagnose problems when automation fails.

---

## Handle Errors Gracefully

Automation scripts should **expect failures**.

Example:

- missing files
- database connection errors
- network interruptions
- invalid data

Use error handling to prevent scripts from crashing unexpectedly.

Example:

```python
try:
    load_data()
except Exception as e:
    logging.error(e)
```

---

## Use Version Control

Automation projects should always use **Git**.

Benefits include:

- tracking code changes
- restoring previous versions
- collaborating with teams

Version control ensures automation systems are **traceable and maintainable**.

---

## Schedule Automation Properly

Automation scripts should run using schedulers such as:

| Scheduler | Example |
|------|------|
| Task Scheduler | Windows automation |
| Cron | Linux automation |
| CI/CD pipelines | automated job runners |

Scheduling ensures scripts run **without manual intervention**.

---

# Decision Flow

Before deploying automation, check the following:

```text
Is the script modular?
        |
        Yes
        |
Does it use configuration files?
        |
        Yes
        |
Does it log activity?
        |
        Yes
        |
Does it handle errors?
        |
        Yes
        |
Automation is production-ready
```

These checks improve reliability.

---

# Code Examples

## Example 1 — Structured Automation Pipeline

```python
def main():

    df = load_data()

    summary = process_data(df)

    report = generate_report(summary)

    send_email(report)

if __name__ == "__main__":
    main()
```

This design keeps automation **clear and modular**.

---

## Example 2 — Logging Pipeline Activity

```python
import logging

logging.basicConfig(
    filename="pipeline.log",
    level=logging.INFO
)

logging.info("Pipeline started")
```

Logging records automation activity.

---

## Example 3 — Error Handling

```python
try:
    df = load_data()

except Exception as e:

    logging.error("Data load failed")

    logging.error(e)
```

This prevents silent failures.

---

## Example 4 — Using Configuration

```python
import json

with open("config.json") as f:
    config = json.load(f)

report_path = config["report_output"]
```

Configuration separates settings from code.

---

# SQL / Excel Comparison

### Manual Reporting Systems

Manual processes often rely on:

```text
Excel macros
Manual queries
Human intervention
```

These systems are fragile and difficult to scale.

---

### Automated Python Systems

Automation pipelines provide:

```text
repeatability
scalability
reliability
```

This is why automation is widely used in analytics and data engineering.

---

# Practice Exercises

## Exercise 1

Tags: Logging, Automation

Review your automation scripts and ensure they include:

```text
functions
logging
error handling
configuration
```

---

## Exercise 2

Tags: Scripts, Refactoring, Data I/O

Refactor a large script into smaller functions.

Example structure:

```text
load_data()
process_data()
generate_report()
```

---

## Exercise 3

Tags: CI/CD, Scripts, Logging

Add logging to track:

```text
script start
data loading
report generation
pipeline completion
```

---

## Exercise 4 (Real-World)

Tags: CI/CD, Logging, Automation, Notifications

Design a production-ready automation pipeline that includes:

```text
data ingestion
processing
report generation
email distribution
logging
error handling
configuration files
```

---

# Common Mistakes

## Mistake 1 — Hardcoding Everything

Hardcoded scripts become difficult to maintain.

Use configuration files instead.

---

## Mistake 2 — No Logging

Without logs it becomes impossible to debug automation failures.

---

## Mistake 3 — Writing Monolithic Scripts

Large scripts are difficult to maintain.

Use modular design.

---

## Mistake 4 — No Version Control

Automation systems should always be tracked using Git.

---

# Real-World Use

Automation best practices are used across many industries.

Examples include:

---

### Data Engineering

Production pipelines follow structured design principles.

Example:

```text
extract
transform
load
monitor
```

---

### Analytics Operations

Automation systems maintain:

```text
daily dashboards
automated reports
data refresh pipelines
```

---

### Enterprise Automation

Large organizations rely on automation systems for:

```text
financial reporting
operational monitoring
data integration
```

---

# Key Idea Cards

### Card 1

Automation scripts should be **modular and maintainable**.

---

### Card 2

Logging and error handling improve **reliability**.

---

### Card 3

Configuration files make automation **flexible and reusable**.

---

# Lesson Recap

In this lesson you learned:

- best practices for automation systems
- how to design reliable automation pipelines
- how professional teams maintain automation projects

These principles help ensure automation systems remain **stable, scalable, and maintainable**.

---

# Module 15 Complete

You have now completed **Module 15 — Automation with Python**.

Skills learned in this module include:

- automation scripts
- scheduling jobs
- Excel report automation
- email automation
- file management
- pipeline design
- logging and monitoring
- error handling
- configuration management
- project structure
- version control
- deployment
- automation best practices

These skills are widely used in:

- analytics teams
- data engineering pipelines
- reporting systems
- operational automation

---

# Next Module

The next module in the learning path is:

# Module 16 — Building Dashboards with Python

In this module you will learn how to:

- build dashboards with **Streamlit**
- build dashboards with **Shiny for Python**
- create interactive charts
- build data-driven web applications

This module focuses on **turning automated data into interactive dashboards**.