# Module 16 — Automation with Python  
## Lesson 10 — Packaging Automation Scripts for Reuse

---

# Lesson Objective

By the end of this lesson you will understand:

- Why automation scripts should be **organized into reusable modules**
- How to structure Python automation projects
- How to break large scripts into **maintainable components**
- How teams build **scalable automation systems**

This lesson focuses on transforming small scripts into **well-organized automation projects**.

---

# Overview

When people first automate tasks with Python, they often write a **single large script**.

Example:

```text
automation_script.py
```

This script may contain:

- data loading
- data processing
- report generation
- email sending
- logging
- configuration

While this works initially, it becomes difficult to maintain.

Problems with large scripts:

- hard to debug
- difficult to reuse
- difficult for teams to collaborate on
- hard to scale automation

Professional automation systems organize code into **modules and packages**.

---

# Key Concepts

## Modular Design

Instead of one large script, automation systems are divided into **modules**.

Example structure:

```text
automation_project/

    main.py
    config.py

    data/
        load_data.py
        process_data.py

    reporting/
        generate_report.py

    notifications/
        send_email.py

    utils/
        logging_setup.py
```

Each module handles **one responsibility**.

---

## Separation of Responsibilities

Well-designed automation scripts separate tasks.

| Module | Responsibility |
|------|------|
| Data module | Load and clean data |
| Processing module | Transform data |
| Reporting module | Generate reports |
| Notification module | Send alerts |
| Utility module | Logging and helpers |

This design is easier to maintain and expand.

---

## Main Script

The **main script** controls the pipeline.

Example:

```text
main.py
```

It orchestrates the automation workflow.

Example workflow:

```text
Load Data
   ↓
Process Data
   ↓
Generate Report
   ↓
Send Email
```

---

# Decision Flow

You should organize automation code when:

```text
Is the script growing large?
        |
        Yes
        |
Does it contain multiple tasks?
        |
        Yes
        |
Will others use the script?
        |
        Yes
        |
Organize it into modules
```

This improves maintainability and collaboration.

---

# Code Examples

## Example 1 — A Single Script (Beginner Approach)

```python
import pandas as pd

df = pd.read_csv("sales.csv")

summary = df.groupby("region")["sales"].sum()

summary.to_excel("sales_report.xlsx")

print("Report generated")
```

This works but becomes messy as features are added.

---

## Example 2 — Modular Project Structure

Project structure:

```text
automation_project/

    main.py
    load_data.py
    process_data.py
    generate_report.py
```

---

### load_data.py

```python
import pandas as pd

def load_data():

    df = pd.read_csv("sales.csv")

    return df
```

---

### process_data.py

```python
def process_data(df):

    summary = df.groupby("region")["sales"].sum()

    return summary
```

---

### generate_report.py

```python
def generate_report(summary):

    summary.to_excel("sales_report.xlsx")

    print("Report generated")
```

---

### main.py

```python
from load_data import load_data
from process_data import process_data
from generate_report import generate_report

def main():

    df = load_data()

    summary = process_data(df)

    generate_report(summary)

main()
```

This structure is much easier to maintain.

---

# SQL / Excel Comparison

### Manual Workflow

Many Excel workflows become messy over time:

- multiple sheets
- duplicated formulas
- manual steps

Eventually the workbook becomes difficult to manage.

---

### Python Modular Workflow

Python automation organizes tasks into **separate modules**.

Example:

```text
data module
report module
email module
config module
```

This makes automation easier to maintain.

---

# Practice Exercises

## Exercise 1

Tags: Scripts, Automation, Data I/O

Create a project structure:

```text
automation_project/

main.py
load_data.py
process_data.py
```

---

## Exercise 2

Tags: Data I/O, Automation

Move the following logic into modules:

```text
Load data
Process data
Generate report
```

---

## Exercise 3

Tags: UPDATE, Scripts

Update `main.py` to call the functions in sequence.

---

## Exercise 4 (Real-World)

Tags: Logging, Automation, Notifications

Design an automation project structure that includes:

```text
data ingestion
report generation
email automation
logging
configuration
```

---

# Common Mistakes

## Mistake 1 — Keeping Everything in One File

Large scripts become difficult to maintain.

Better approach:

Break scripts into **modules**.

---

## Mistake 2 — Mixing Responsibilities

Avoid combining unrelated tasks.

Example problem:

```text
Database code + Email code + File management in one module
```

Each module should focus on **one responsibility**.

---

## Mistake 3 — Poor Project Organization

A messy folder structure makes automation projects difficult to navigate.

Good structure improves maintainability.

---

# Real-World Use

Professional data teams structure automation projects carefully.

Examples include:

---

### Data Engineering Pipelines

Large pipelines often contain modules for:

```text
data extraction
data transformation
data loading
monitoring
```

---

### Reporting Systems

Reporting pipelines include modules for:

```text
data collection
metric calculation
report generation
distribution
```

---

### Automation Frameworks

Large automation systems often resemble:

```text
automation/

    pipelines/
    config/
    logging/
    notifications/
    utils/
```

---

# Key Idea Cards

### Card 1

Large automation scripts should be **broken into modules**.

---

### Card 2

Each module should focus on **one responsibility**.

---

### Card 3

Well-organized automation projects are **easier to maintain and scale**.

---

# Lesson Recap

In this lesson you learned:

- why large scripts become difficult to maintain
- how to organize automation code into modules
- how Python projects are structured
- how modular design improves automation systems

You now understand how to turn simple scripts into **maintainable automation projects**.

---

# Next Lesson

Next you will learn:

**Module 15 — Lesson 11: Version Control for Automation Projects**

You will learn how to:

- track changes to automation scripts
- collaborate with teams
- manage versions of automation pipelines

using **Git and Git repositories**.