# Module 11 — Python Engineering Handbook

# Lesson 3 — Logging Standards

---

# Lesson Objective

By the end of this lesson learners will understand:

• why organizations define **logging standards**  
• how logs should be structured in professional applications  
• how logging improves **monitoring and debugging**  
• best practices for designing effective logging systems  

Logging standards ensure that applications generate **consistent, useful, and searchable logs** that help developers and operations teams monitor systems and diagnose issues.

---

# Overview

In earlier modules, you learned how Python’s `logging` module works.

However, in professional environments, teams usually define **logging standards** to ensure consistency across applications.

Without logging standards, logs might look like this:

```text
Started
Error
Something went wrong
```

These messages provide very little useful information.

Professional logging includes structured information such as:

```text
Timestamp
Log Level
Application Component
Message
Context Information
```

Example structured log:

```text
2024-06-01 10:15:34 INFO data_pipeline Loading customer dataset
```

Structured logging makes it easier to:

• debug production issues  
• monitor system health  
• analyze system behavior.

---

# Key Idea Cards (3 Cards)

### Logs Provide Observability

Logs allow teams to understand what is happening inside an application.

Example events:

```text
Application started
Data pipeline executed
API request received
Database connection established
```

Logs provide visibility into system behavior.

---

### Log Levels Communicate Severity

Logging systems categorize messages by severity.

Common log levels include:

```text
DEBUG
INFO
WARNING
ERROR
CRITICAL
```

This allows systems to filter important events.

---

### Structured Logs Are Easier to Analyze

Structured logs follow consistent formats.

Example:

```text
timestamp | level | component | message
```

This allows logs to be easily analyzed by monitoring systems.

---

# Key Concepts

## Log Structure

Professional logs typically include several fields.

Example structure:

```text
timestamp
log level
component
message
```

Example log entry:

```text
2024-06-01 10:12:30 INFO pipeline Loading data
```

This structure provides useful context.

---

## Logging Configuration

Logging configuration defines how logs are written.

Example configuration includes:

```text
log level
log format
log destination
```

Logs may be written to:

• console output  
• log files  
• monitoring systems.

---

## Log Aggregation

Large systems generate many logs.

Log aggregation systems collect logs from multiple sources.

Examples include:

```text
ELK Stack
Splunk
Datadog
CloudWatch
```

These systems allow teams to search and analyze logs.

---

# Decision Flow

Developers usually design logging systems using the following approach:

```text
Define logging standards
       ↓
Configure logging module
       ↓
Write structured logs
       ↓
Send logs to monitoring systems
```

Consistent logging improves system observability.

---

# Code Examples

### Example 1 — Basic Logging

```python
import logging

logging.basicConfig(level=logging.INFO)

logging.info("Application started")
```

This logs a simple message.

---

### Example 2 — Structured Logging Format

```python
import logging

logging.basicConfig(
    format="%(asctime)s %(levelname)s %(message)s",
    level=logging.INFO
)

logging.info("Loading data")
```

Example output:

```text
2024-06-01 10:12:30 INFO Loading data
```

---

### Example 3 — Logging With Components

```python
import logging

logger = logging.getLogger("data_pipeline")

logger.info("Extracting data")
logger.info("Transforming data")
logger.info("Loading data")
```

This separates logs by application component.

---

### Example 4 — Logging Errors

```python
try:
    process_data()
except Exception as e:
    logging.error(f"Pipeline failed: {e}")
```

Error logs help diagnose system failures.

---

# SQL / Excel Comparison

Logging and monitoring also exist in other tools.

| Concept | Python | SQL | Excel |
|------|------|------|------|
| logging | application logs | query logs | workbook history |
| monitoring | log monitoring systems | database monitoring | file version tracking |
| debugging | debug logs | query analysis | formula auditing |

Example SQL logs:

```text
Query executed
Query duration
Database error
```

These logs help diagnose database issues.

---

# Practice Exercises

### Exercise 1

Tags: Logging, Imports, Scripts

Write a Python script that logs application startup.

```python
import logging

logging.info("Application starting")
```

---

### Exercise 2

Tags: String Formatting, Logging

Configure a custom log format.

Example:

```python
logging.basicConfig(
    format="%(asctime)s %(levelname)s %(message)s"
)
```

---

### Exercise 3

Tags: Logging, Debugging

Create logs for different log levels.

Example:

```python
logging.debug("Debug info")
logging.info("Application running")
logging.error("Something failed")
```

---

### Exercise 4

Tags: CI/CD, Scripts, Logging

Add logging to a data pipeline script.

Log each step:

```text
Extract
Transform
Load
```

---

# Common Mistakes

### Logging Too Little Information

Logs should contain enough context to diagnose problems.

Avoid vague messages.

Example:

Bad:

```text
Error occurred
```

Better:

```text
Database connection failed
```

---

### Logging Sensitive Data

Logs should never contain sensitive information such as:

```text
passwords
API keys
personal data
```

Protecting user data is critical.

---

### Excessive Debug Logging

Too many debug logs can overwhelm monitoring systems.

Use appropriate log levels.

---

# Real-World Use

Logging standards are critical for production systems.

Example workflow:

```text
Application runs
       ↓
Logs generated
       ↓
Logs sent to monitoring system
       ↓
Alerts triggered if errors occur
```

Logging helps organizations monitor:

• data pipelines  
• web applications  
• cloud infrastructure  
• analytics platforms.

Without logging, diagnosing production issues becomes extremely difficult.

---

# Lesson Recap

In this lesson you learned:

• why logging standards are important  
• how structured logs improve monitoring  
• how applications generate consistent logs  
• how logs help diagnose system issues.

Logging standards ensure applications remain **observable and maintainable in production environments**.

---

# Next Lesson

Next we will continue Module 11 with:

# Lesson 4 — Branch Naming Standards

You will learn:

• how teams structure Git branches  
• why branch naming conventions matter  
• how branch workflows support CI/CD pipelines  
• how teams manage collaborative development.
