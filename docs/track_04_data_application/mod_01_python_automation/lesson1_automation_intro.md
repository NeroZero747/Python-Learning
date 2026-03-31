# Module 16 — Automation with Python  
## Lesson 1 — Automating Repetitive Work with Python

---

# Lesson Objective
By the end of this lesson you will understand:

- What **automation** means in Python
- How Python can replace **manual Excel tasks**
- How to write a **simple automation script**
- How to schedule or reuse automation scripts

This lesson introduces one of the **most valuable uses of Python in the workplace**: removing repetitive work.

---

# Overview

Many people first learn Python because they are tired of doing the same task repeatedly.

Examples include:

- Downloading reports
- Cleaning Excel data
- Combining multiple files
- Sending daily emails
- Updating dashboards
- Running the same SQL queries every day

These tasks often take **10–60 minutes per day**.

With Python, they can be reduced to **seconds**.

Automation allows Python to:

1. Load data
2. Process it
3. Export results
4. Repeat the process automatically

Instead of manually doing the same work every day, Python can do it for you.

---

# Key Concepts

## Automation
Automation means **using code to perform tasks automatically instead of manually**.

Example:

Manual Process:
1. Open Excel
2. Load a CSV file
3. Filter rows
4. Calculate totals
5. Save the file

Automated Process:

```python
python run_report.py
```

Everything happens automatically.

---

## Scripts

Automation is typically written in **Python scripts**.

Example file:

```text
daily_report.py
```

A script is simply a Python file that runs from start to finish.

---

## Repeatable Workflows

Automation works best for **repeatable tasks**.

Examples:

| Task | Manual Time | Python Time |
|-----|-----|-----|
| Combine 20 Excel files | 20 minutes | 5 seconds |
| Run SQL queries | 10 minutes | 2 seconds |
| Clean messy data | 30 minutes | 5 seconds |
| Send report emails | 10 minutes | 1 second |

---

# Decision Flow

When deciding if something should be automated, ask:

```text
Do I do this task repeatedly?
        |
        Yes
        |
Does the task follow clear steps?
        |
        Yes
        |
Can those steps be written in code?
        |
        Yes
        |
AUTOMATE IT
```

Good automation candidates:

- Daily reports
- Data cleaning
- File merging
- Scheduled exports

---

# Code Examples

## Example 1 — Simple Automation Script

Imagine you download a CSV report every day.

Python can load and summarize it automatically.

```python
import pandas as pd

# Load the report
df = pd.read_csv("sales_report.csv")

# Calculate total sales
total_sales = df["sales"].sum()

print("Total Sales:", total_sales)
```

Instead of opening Excel and calculating totals manually, Python does it instantly.

---

## Example 2 — Cleaning Data Automatically

Imagine a dataset with missing values.

```python
import pandas as pd

df = pd.read_csv("customers.csv")

# Remove missing values
df_clean = df.dropna()

# Save cleaned data
df_clean.to_csv("clean_customers.csv", index=False)

print("Data cleaned successfully")
```

This script:

1. Loads data
2. Cleans it
3. Saves a new file

All automatically.

---

## Example 3 — Automating Multiple Files

Python can combine many files automatically.

```python
import pandas as pd
import glob

files = glob.glob("data/*.csv")

dfs = []

for file in files:
    df = pd.read_csv(file)
    dfs.append(df)

combined = pd.concat(dfs)

combined.to_csv("combined_data.csv", index=False)
```

This script:

- Reads all CSV files in a folder
- Combines them
- Saves one final dataset

---

# SQL / Excel Comparison

### Excel Workflow

1. Open multiple files
2. Copy data
3. Paste into master sheet
4. Remove duplicates
5. Save file

Time: **20–30 minutes**

---

### Python Workflow

```python
import pandas as pd
import glob

files = glob.glob("data/*.csv")

df = pd.concat(pd.read_csv(f) for f in files)

df.to_csv("master_file.csv", index=False)
```

Time: **3 seconds**

---

# Practice Exercises

## Exercise 1

Tags: CSV, HTTP Methods, Scripts, Arithmetic

Create a Python script that:

1. Loads a CSV file
2. Calculates the average of a column
3. Prints the result

Example dataset:

```text
sales.csv
```

Columns:

```text
date, sales
```

Expected output:

```text
Average Sales: 2450
```

---

## Exercise 2

Tags: Missing Data, Scripts, Automation, Data I/O

Write a script that:

1. Loads a CSV file
2. Removes rows with missing values
3. Saves the cleaned dataset

---

## Exercise 3 (Real-World)

Tags: Scripts, Arithmetic, Automation

You receive **daily sales reports**.

Write a script that:

1. Loads the file
2. Calculates total sales
3. Saves a summary file.

---

# Common Mistakes

## Mistake 1 — Hardcoding File Paths

Bad:

```python
df = pd.read_csv("C:/Users/name/Desktop/data.csv")
```

Better:

```python
df = pd.read_csv("data/data.csv")
```

---

## Mistake 2 — Not Handling Errors

If a file is missing, the script will crash.

Better approach:

```python
try:
    df = pd.read_csv("data.csv")
except FileNotFoundError:
    print("File not found")
```

---

## Mistake 3 — Writing One-Time Code

Automation scripts should be **reusable**, not written for a single run.

---

# Real-World Use

Automation is used everywhere in data work.

Examples:

### Reporting Automation

Python automatically:

- Runs SQL queries
- Processes data
- Sends Excel reports

---

### Data Engineering

Python pipelines:

- Extract data
- Transform it
- Load it into databases

(ETL pipelines)

---

### File Processing

Python scripts:

- Clean messy files
- Standardize formats
- Merge datasets

---

# Key Idea Cards

### Card 1

Automation saves **hours of manual work**.

---

### Card 2

Python scripts can replace **repetitive Excel workflows**.

---

### Card 3

The best automation targets **tasks you repeat often**.

---

# Lesson Recap

In this lesson you learned:

- What automation means
- Why Python is ideal for automation
- How scripts automate tasks
- How Python replaces manual Excel work

Automation is one of the **most practical uses of Python in business environments**.

---

# Next Lesson

In the next lesson you will learn:

**Scheduling Python Jobs (Running Scripts Automatically)**

You will learn how to:

- Run Python scripts on a schedule
- Automate daily reports
- Set up automated workflows.