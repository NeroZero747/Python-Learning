# Module 16 — Automation with Python  
## Lesson 8 — Error Handling in Automation Scripts

---

# Lesson Objective

By the end of this lesson you will understand:

- What **errors and exceptions** are in Python
- How to prevent automation scripts from **crashing**
- How to use **try / except blocks**
- How to build **more reliable automation systems**

Error handling is essential for automation scripts that run **without human supervision**.

---

# Overview

Automation scripts often interact with many external systems:

- files
- databases
- APIs
- email systems
- network services

These systems can fail.

Examples:

- file not found
- database connection fails
- API request times out
- report file missing
- email server unavailable

Without error handling, a Python script will **stop immediately when an error occurs**.

Example:

```text
Script starts
      ↓
Error occurs
      ↓
Script crashes
```

With proper error handling:

```text
Script starts
      ↓
Error occurs
      ↓
Error captured
      ↓
Script logs issue and continues
```

This makes automation systems **more stable and reliable**.

---

# Key Concepts

## Exceptions

In Python, errors are called **exceptions**.

Examples of common exceptions:

| Exception | Meaning |
|------|------|
| FileNotFoundError | File does not exist |
| ValueError | Invalid value |
| KeyError | Missing dictionary key |
| TypeError | Wrong data type |
| ConnectionError | Network or database issue |

---

## Try / Except

Python uses **try / except blocks** to catch errors.

Basic structure:

```python
try:
    code_that_might_fail()
except:
    handle_the_error()
```

This allows scripts to **recover from problems instead of crashing**.

---

## Controlled Failures

Sometimes automation should **fail gracefully**.

Example:

```text
Data missing
     ↓
Log error
     ↓
Send alert
     ↓
Stop pipeline safely
```

This is better than crashing unexpectedly.

---

# Decision Flow

Error handling should be added when:

```text
Does the script rely on external systems?
        |
        Yes
        |
Could those systems fail?
        |
        Yes
        |
Will the script run automatically?
        |
        Yes
        |
Add error handling
```

Examples:

- scheduled jobs
- ETL pipelines
- automated reporting systems
- API integrations

---

# Code Examples

## Example 1 — Basic Error Handling

```python
try:
    df = pd.read_csv("sales.csv")
except:
    print("File could not be loaded")
```

If the file does not exist, the script will not crash.

---

## Example 2 — Handling Specific Errors

It is better to catch **specific exceptions**.

```python
import pandas as pd

try:
    df = pd.read_csv("sales.csv")

except FileNotFoundError:

    print("The sales file is missing")

except Exception as e:

    print("Unexpected error:", e)
```

This script handles:

- missing files
- unexpected errors

---

## Example 3 — Error Handling with Logging

Automation pipelines usually **log errors**.

```python
import logging

logging.basicConfig(
    filename="pipeline.log",
    level=logging.INFO
)

try:

    df = pd.read_csv("sales.csv")

    logging.info("Data loaded successfully")

except FileNotFoundError:

    logging.error("Sales file not found")
```

This records failures in the log file.

---

## Example 4 — Protecting an Entire Pipeline

Automation pipelines often wrap the main process.

```python
def main():

    df = load_data()

    summary = process_data(df)

    generate_report(summary)

try:

    main()

except Exception as e:

    print("Pipeline failed:", e)
```

This ensures errors are captured at the **pipeline level**.

---

# SQL / Excel Comparison

### Manual Process

When errors occur manually:

```text
Excel file missing
     ↓
User notices
     ↓
Fix issue
```

Human intervention solves the problem.

---

### Automated Process

Without error handling:

```text
Script fails
     ↓
Process stops
     ↓
No report generated
```

With error handling:

```text
Error occurs
     ↓
Error logged
     ↓
Pipeline continues or alerts user
```

---

# Practice Exercises

## Exercise 1

Tags: Missing Data, File I/O, Scripts

Write a script that:

1. Attempts to read a CSV file
2. Prints a message if the file is missing.

---

## Exercise 2

Tags: Scripts, Automation

Modify the script to catch:

- FileNotFoundError
- ValueError

---

## Exercise 3

Tags: Logging, Automation

Add logging so errors are recorded in:

```text
error_log.txt
```

---

## Exercise 4 (Real-World)

Tags: Conditionals, Missing Data, Scripts, Notifications

Create a script that:

1. Loads data
2. Generates a report
3. Sends an email

Add error handling so the script logs failures if:

- data file is missing
- report generation fails
- email delivery fails

---

# Common Mistakes

## Mistake 1 — Catching All Errors Without Logging

Example:

```python
try:
    process_data()
except:
    pass
```

This hides the problem.

Better approach:

```python
except Exception as e:
    print(e)
```

---

## Mistake 2 — Overusing Try Blocks

Only wrap **risky operations**.

Bad:

```python
try:
    entire_script()
```

Better:

```python
try:
    load_data()
```

---

## Mistake 3 — Ignoring Errors

Automation systems should always:

- log errors
- alert users
- stop safely

---

# Real-World Use

Error handling is critical in professional data systems.

Examples include:

---

### Data Pipelines

Pipelines detect failures such as:

```text
Missing files
API failures
Database errors
```

Errors are logged and alerts are triggered.

---

### Reporting Systems

Automation scripts detect when:

- reports cannot be generated
- data is incomplete
- file exports fail

---

### Monitoring Systems

Error handling allows monitoring tools to detect:

- job failures
- abnormal execution

---

# Key Idea Cards

### Card 1

Exceptions are Python's way of representing **errors**.

---

### Card 2

Try / except blocks allow scripts to **recover from failures**.

---

### Card 3

Error handling makes automation systems **more reliable**.

---

# Lesson Recap

In this lesson you learned:

- what exceptions are
- how Python handles errors
- how try / except blocks prevent crashes
- how automation pipelines recover from failures

Error handling is essential for building **robust automation systems**.

---

# Next Lesson

Next you will learn:

**Module 15 — Lesson 9: Configuration Files for Automation Scripts**

You will learn how to:

- store settings in configuration files
- avoid hardcoding values
- build more flexible automation pipelines

This is an important practice for **production-quality Python automation**.