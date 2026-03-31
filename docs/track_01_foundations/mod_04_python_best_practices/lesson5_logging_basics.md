# Module 5 — Writing Cleaner Python Code

# Lesson 6 — Logging Basics

---

# Lesson Objective

By the end of this lesson learners will understand:

• what logging is  
• why logging is important in Python programs  
• how logging helps debugging and monitoring  
• how to implement basic logging in Python  

Logging is essential because it allows developers and analysts to **track what a program is doing while it runs**, especially when scripts run automatically in pipelines.

---

# Overview

When beginners write Python scripts, they often use `print()` statements to understand what the program is doing.

Example:

```python
print("Starting analysis")
print("Loading data")
print("Calculating totals")
print("Exporting results")
```

This works during development, but `print()` has limitations:

• messages are not structured  
• output is hard to search  
• messages are not saved to a file  
• there is no severity level  

Professional Python applications use **logging instead of print statements**.

Example logging output:

```text
INFO: Starting analysis
INFO: Loading dataset
WARNING: Missing values detected
ERROR: Failed to connect to database
```

Logging provides:

• structured messages  
• severity levels  
• timestamp tracking  
• log file storage  

This makes debugging and monitoring much easier.

---

# Key Idea Cards (3 Cards)

## Logging Tracks Program Activity

Logging records what a program is doing while it runs.

Example log output:

```text
INFO: Loading dataset
INFO: Cleaning data
INFO: Exporting results
```

This helps developers understand the workflow.

---

## Logging Uses Severity Levels

Logs include severity levels that describe how serious a message is.

Common levels include:

```text
DEBUG
INFO
WARNING
ERROR
CRITICAL
```

These levels help categorize messages.

---

## Logging Can Save Messages to Files

Unlike `print()`, logging can write messages to a file.

Example log file:

```text
2024-01-10 INFO Starting pipeline
2024-01-10 INFO Dataset loaded
2024-01-10 ERROR Database connection failed
```

Log files are extremely useful when diagnosing problems.

---

# Key Concepts

## Logging Module

Python includes a built-in logging module.

Example:

```python
import logging
```

This module allows programs to create structured log messages.

---

## Logging Levels

Logging messages can be categorized by severity.

| Level | Meaning |
|------|------|
| DEBUG | Detailed diagnostic information |
| INFO | Normal program activity |
| WARNING | Something unexpected occurred |
| ERROR | A problem occurred |
| CRITICAL | A serious failure |

Example:

```python
logging.info("Starting analysis")
```

---

## Basic Logging Configuration

Before logging messages, logging must be configured.

Example:

```python
import logging

logging.basicConfig(level=logging.INFO)

logging.info("Program started")
```

Output:

```text
INFO:root:Program started
```

---

# Decision Flow

Logging typically follows this workflow:

```text
Program starts
      ↓
Log important events
      ↓
Log warnings or errors
      ↓
Review logs if issues occur
```

Example workflow:

```python
logging.info("Loading data")
logging.warning("Missing values detected")
logging.error("Database connection failed")
```

---

# Code Examples

## Example 1 — Basic Logging

```python
import logging

logging.basicConfig(level=logging.INFO)

logging.info("Starting program")
```

Output:

```text
INFO:root:Starting program
```

---

## Example 2 — Logging Multiple Messages

```python
import logging

logging.basicConfig(level=logging.INFO)

logging.info("Loading data")
logging.warning("Missing values detected")
logging.error("Failed to connect to database")
```

---

## Example 3 — Writing Logs to a File

Logs can be stored in a file.

```python
import logging

logging.basicConfig(
    filename="app.log",
    level=logging.INFO
)

logging.info("Application started")
```

This writes log messages to **app.log**.

---

## Example 4 — Logging in a Data Workflow

```python
import logging

logging.basicConfig(level=logging.INFO)

logging.info("Reading CSV file")

df = pd.read_csv("sales.csv")

logging.info("Calculating totals")
```

This records the workflow steps.

---

# SQL / Excel Comparison

Logging concepts also exist in other systems.

| Concept | Python | SQL | Excel |
|------|------|------|------|
| activity tracking | logging | audit logs | macro logs |
| error monitoring | error logs | database logs | error messages |
| workflow tracking | pipeline logs | job logs | VBA debugging |

Example database log entry:

```text
2024-01-10 09:00 Query executed
```

Python logging serves a similar purpose.

---

# Practice Exercises

## Exercise 1

Tags: Logging, Imports, Scripts

Create a simple logging script.

```python
import logging

logging.basicConfig(level=logging.INFO)

logging.info("Starting analysis")
```

---

## Exercise 2

Tags: Logging, Data I/O

Log multiple steps in a program.

```python
logging.info("Loading dataset")
logging.info("Cleaning data")
logging.info("Exporting results")
```

---

## Exercise 3

Tags: File I/O, Scripts, Logging

Write logs to a file.

```python
logging.basicConfig(
    filename="analysis.log",
    level=logging.INFO
)
```

Run the script and inspect the log file.

---

# Common Mistakes

## Using Print Instead of Logging

Incorrect:

```python
print("Loading data")
```

Better:

```python
logging.info("Loading data")
```

Logging provides structured output.

---

## Logging Too Little Information

Example:

```python
logging.info("Done")
```

Better:

```python
logging.info("Data cleaning completed successfully")
```

More context helps debugging.

---

## Ignoring Errors

Programs should log important errors.

Example:

```python
logging.error("Database connection failed")
```

Without logging, diagnosing failures becomes difficult.

---

# Real-World Use

Logging is widely used in production systems.

Examples include:

• monitoring data pipelines  
• diagnosing ETL failures  
• tracking API calls  
• recording application activity  

Example data pipeline:

```python
logging.info("Pipeline started")

df = pd.read_csv("claims.csv")

logging.info("Claims data loaded")

process_claims(df)

logging.info("Pipeline finished")
```

If something fails, logs help identify the issue.

---

# Lesson Recap

In this lesson you learned:

• what logging is  
• why logging is important in Python applications  
• how to use the logging module  
• how logging helps debugging and monitoring  

Logging is essential because it allows developers to **monitor program behavior and diagnose issues quickly**.

---

# Next Module

You have now completed:

# Module 5 — Writing Cleaner Python Code

You learned how to:

• write reusable functions  
• organize code into modules  
• structure Python projects  
• use Git for version control  
• manage Git inside VS Code  
• implement logging in Python programs  

These practices help transform simple scripts into **clean, maintainable, professional Python projects**.

---

# Next Module

You will next begin:

# Module 6 — Object-Oriented Programming

First lesson:

**Why Classes Help Data Projects**

This module will introduce:

• classes  
• attributes  
• methods  
• how OOP improves project structure.
