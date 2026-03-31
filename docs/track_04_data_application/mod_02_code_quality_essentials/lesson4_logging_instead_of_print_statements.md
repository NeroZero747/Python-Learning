# Module 9 — Professional Python Practices

# Lesson 7 — Logging Instead of Print Statements

---

# Lesson Objective

By the end of this lesson learners will understand:

• why professional applications use **logging instead of print statements**  
• how Python’s **logging module** works  
• how logs help diagnose problems in production systems  
• how to structure logging in Python applications  

Logging is a critical part of professional software development because it allows developers and operators to **monitor applications, diagnose issues, and understand system behavior** without modifying the code.

---

# Overview

When beginners write Python scripts, they often use `print()` to see what the program is doing.

Example:

```python
print("Loading data...")
print("Filtering records...")
print("Processing complete.")
```

This approach works for simple scripts but creates problems in larger applications:

• print statements cannot be easily disabled  
• they do not provide timestamps  
• they do not indicate severity levels  
• they do not write to log files.

Professional applications use **structured logging**.

Logging provides important information such as:

```text
Timestamp
Log Level
Message
Source
```

Example log entry:

```text
2024-06-01 10:12:34 INFO Loading sales data
```

Logging systems allow developers to track what happens inside applications over time.

---

# Key Idea Cards (3 Cards)

### Logs Provide Visibility Into Applications

Logs allow developers to observe application behavior.

Example:

```text
Application started
Database connection established
Data processing completed
```

This information helps diagnose problems quickly.

---

### Logs Have Severity Levels

Logging systems categorize messages by severity.

Common log levels include:

```text
DEBUG
INFO
WARNING
ERROR
CRITICAL
```

This allows systems to filter messages depending on importance.

---

### Logs Are Stored for Analysis

Unlike print statements, logs can be written to files or monitoring systems.

Example:

```text
logs/application.log
```

Operations teams can analyze logs to identify system issues.

---

# Key Concepts

## Log Levels

Python’s logging module uses different levels to classify messages.

| Level | Purpose |
|------|------|
| DEBUG | detailed debugging information |
| INFO | general application events |
| WARNING | potential issues |
| ERROR | errors affecting functionality |
| CRITICAL | severe system failures |

Example usage:

```python
logging.info("Application started")
```

---

## Logging Module

Python includes a built-in module for logging.

Example setup:

```python
import logging

logging.basicConfig(level=logging.INFO)

logging.info("Application started")
```

This prints structured log messages.

---

## Writing Logs to Files

Logs can also be written to files.

Example:

```python
logging.basicConfig(
    filename="app.log",
    level=logging.INFO
)
```

This stores log entries in a file instead of displaying them in the console.

---

# Decision Flow

Developers decide how to log messages using this logic:

```text
Is the message for debugging?
        ↓
      DEBUG

Is it a normal system event?
        ↓
      INFO

Is something wrong?
        ↓
      ERROR
```

This classification helps filter logs effectively.

---

# Code Examples

### Example 1 — Using Print Statements (Beginner)

```python
print("Starting application")
print("Loading data")
print("Processing complete")
```

Problems:

• difficult to disable  
• no timestamps  
• not structured.

---

### Example 2 — Basic Logging

```python
import logging

logging.basicConfig(level=logging.INFO)

logging.info("Application started")
logging.info("Loading data")
```

Output:

```text
INFO:root:Application started
INFO:root:Loading data
```

---

### Example 3 — Logging with Multiple Levels

```python
import logging

logging.basicConfig(level=logging.DEBUG)

logging.debug("Debugging information")
logging.info("Application started")
logging.warning("Low disk space")
logging.error("File not found")
```

This example demonstrates multiple log levels.

---

### Example 4 — Logging to File

```python
import logging

logging.basicConfig(
    filename="application.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Application started")
```

Example log file output:

```text
2024-06-01 10:12:34 - INFO - Application started
```

This provides structured logging information.

---

# SQL / Excel Comparison

Logging concepts also exist in other tools.

| Concept | Python | SQL | Excel |
|------|------|------|------|
| monitoring | application logs | database logs | workbook history |
| error tracking | error logs | query logs | error cells |
| debugging | debug logs | query plans | formula tracing |

Example SQL logs:

```text
Query execution time
Query errors
Connection events
```

These logs help database administrators diagnose issues.

---

# Practice Exercises

### Exercise 1

Tags: print(), Logging, Data I/O

Replace print statements with logging.

Original code:

```python
print("Loading data")
```

Rewrite using logging.

---

### Exercise 2

Tags: Logging, Imports

Create a basic logging configuration.

```python
import logging

logging.basicConfig(level=logging.INFO)
```

---

### Exercise 3

Tags: Logging, Debugging

Write logs with multiple severity levels.

```python
logging.debug("Debug message")
logging.info("Application started")
logging.error("Something went wrong")
```

---

### Exercise 4

Tags: File I/O, Logging, Configuration

Write logs to a file.

```python
logging.basicConfig(filename="app.log")
```

Run the program and inspect the log file.

---

# Common Mistakes

### Using Print Statements in Production

Print statements do not provide structured logging.

Use the logging module instead.

---

### Logging Too Much Information

Excessive logging can make logs difficult to analyze.

Use appropriate log levels.

---

### Logging Sensitive Information

Never log sensitive data such as:

```text
passwords
API keys
personal data
```

Logs should never expose confidential information.

---

# Real-World Use

Logging is essential in production systems.

Example workflow:

```text
Application runs
       ↓
Logs record events
       ↓
Operations team monitors logs
       ↓
Issues are detected and resolved
```

Example production log pipeline:

```text
Application
      ↓
Log Files
      ↓
Monitoring System
      ↓
Alert System
```

Tools like:

```text
ELK Stack
Datadog
Splunk
CloudWatch
```

collect and analyze logs from production systems.

---

# Lesson Recap

In this lesson you learned:

• why logging is used instead of print statements  
• how Python’s logging module works  
• how logs help diagnose production issues  
• how applications structure logging information.

Logging is a critical component of **reliable and maintainable software systems**.

---

# Next Lesson

Next we will learn:

# Lesson 8 — Testing Python Code

You will learn:

• why testing is important for production software  
• how Python testing frameworks work  
• how to write unit tests  
• how automated tests improve software reliability.
