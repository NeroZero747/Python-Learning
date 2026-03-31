# Module 16 — Automation with Python  
## Lesson 9 — Configuration Files for Automation Scripts

---

# Lesson Objective

By the end of this lesson you will understand:

- Why automation scripts should **avoid hardcoding values**
- How to store settings in **configuration files**
- How Python reads configuration files
- How configuration makes automation scripts **flexible and reusable**

Configuration files are widely used in **production automation systems and data pipelines**.

---

# Overview

Many beginner scripts contain **hardcoded values**.

Example:

```python
email = "team@example.com"
file_path = "C:/reports/sales.csv"
database = "analytics_db"
```

This approach creates problems:

- difficult to maintain
- hard to reuse scripts
- requires editing code for small changes

Instead, professional automation systems use **configuration files**.

Example:

```text
config file
      ↓
Python script reads config
      ↓
Script runs using configuration values
```

This separates **code** from **settings**.

---

# Key Concepts

## Hardcoded Values

Hardcoding means placing values directly inside code.

Example:

```python
report_file = "sales_report.xlsx"
email_recipient = "manager@example.com"
```

If the recipient changes, the script must be modified.

---

## Configuration Files

A configuration file stores settings outside the code.

Example:

```text
config.json
```

Example content:

```json
{
  "report_file": "sales_report.xlsx",
  "email_recipient": "manager@example.com"
}
```

The script reads these values when it runs.

---

## Benefits of Configuration

Using configuration files provides several advantages.

| Benefit | Description |
|------|------|
| Flexibility | Settings can change without editing code |
| Reusability | Scripts can run in different environments |
| Maintainability | Configuration is easier to manage |
| Collaboration | Teams can adjust settings safely |

---

# Decision Flow

Use configuration files when:

```text
Does the script have adjustable settings?
        |
        Yes
        |
Will the script run in multiple environments?
        |
        Yes
        |
Do settings change frequently?
        |
        Yes
        |
Use a configuration file
```

Examples:

- file paths
- database connections
- email recipients
- API keys
- report settings

---

# Code Examples

## Example 1 — JSON Configuration File

Create a file:

```text
config.json
```

Example contents:

```json
{
  "input_file": "sales_data.csv",
  "output_file": "sales_report.xlsx",
  "email_recipient": "team@example.com"
}
```

---

## Example 2 — Reading a Configuration File

Python can read JSON files easily.

```python
import json

with open("config.json") as f:
    config = json.load(f)

print(config["input_file"])
```

Output:

```text
sales_data.csv
```

---

## Example 3 — Using Configuration in a Script

```python
import json
import pandas as pd

with open("config.json") as f:
    config = json.load(f)

input_file = config["input_file"]
output_file = config["output_file"]

df = pd.read_csv(input_file)

summary = df.groupby("region")["sales"].sum()

summary.to_excel(output_file)

print("Report generated")
```

This script reads configuration values dynamically.

---

## Example 4 — Configuration for Email Automation

Example configuration file:

```json
{
  "smtp_server": "smtp.office365.com",
  "email_sender": "reports@example.com",
  "email_recipient": "team@example.com"
}
```

Python script:

```python
import json

with open("config.json") as f:
    config = json.load(f)

smtp_server = config["smtp_server"]
sender = config["email_sender"]
recipient = config["email_recipient"]

print("Sending report to:", recipient)
```

---

# SQL / Excel Comparison

### Manual Workflow

Users manually adjust:

- file locations
- email recipients
- report parameters

Example:

```text
Change Excel file path
Update email recipient
Modify SQL query
```

---

### Automated Workflow

Configuration files control script behavior.

```text
config.json
      ↓
Python script reads settings
      ↓
Script runs with new configuration
```

No code changes required.

---

# Practice Exercises

## Exercise 1

Tags: HTTP Methods, Notifications, Configuration

Create a configuration file that stores:

```text
input_file
output_file
email_recipient
```

---

## Exercise 2

Tags: File I/O, Scripts, Configuration

Write a Python script that:

1. Reads the configuration file
2. Prints the values.

---

## Exercise 3

Tags: Scripts, Configuration, Data I/O

Modify the script so it:

1. Loads a dataset
2. Generates a report
3. Uses configuration settings.

---

## Exercise 4 (Real-World)

Tags: Loops, UPDATE, Databases, CI/CD

Create a configuration file for a reporting pipeline that includes:

```text
database connection
report file name
email recipient
log file location
```

Then update the script to read these values.

---

# Common Mistakes

## Mistake 1 — Hardcoding Sensitive Data

Never store sensitive data directly in scripts.

Bad example:

```python
password = "mypassword123"
```

Better approach:

Use configuration or environment variables.

---

## Mistake 2 — Mixing Code and Configuration

Scripts should focus on **logic**, not settings.

Settings belong in configuration files.

---

## Mistake 3 — Poor Configuration Organization

Configuration files should be:

- structured
- readable
- documented

---

# Real-World Use

Configuration files are used extensively in professional data systems.

Examples include:

---

### Data Pipelines

Configuration controls:

```text
data sources
destination tables
pipeline schedules
```

---

### Reporting Systems

Configuration controls:

```text
report parameters
email recipients
output locations
```

---

### Application Deployment

Applications use configuration to define:

```text
environment settings
API endpoints
database credentials
```

---

# Key Idea Cards

### Card 1

Configuration files store **settings outside the code**.

---

### Card 2

JSON configuration files are easy for Python to read.

---

### Card 3

Separating configuration from code improves **flexibility and maintainability**.

---

# Lesson Recap

In this lesson you learned:

- why hardcoded values are problematic
- how configuration files store settings
- how Python reads configuration files
- how configuration improves automation scripts

Configuration files are essential for **production-ready automation systems**.

---

# Next Lesson

Next you will learn:

**Module 15 — Lesson 10: Packaging Automation Scripts for Reuse**

You will learn how to:

- organize automation scripts into reusable modules
- structure automation projects
- create maintainable automation systems.