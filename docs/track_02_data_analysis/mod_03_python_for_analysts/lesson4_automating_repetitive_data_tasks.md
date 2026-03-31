# Module 15 — Python for Analysts

# Lesson 4 — Automating Repetitive Data Tasks

---

# Lesson Objective

By the end of this lesson learners will understand:

• how Python can automate repetitive analyst tasks  
• how to process **multiple files automatically**  
• how automation reduces manual reporting work  
• how to build simple **automation scripts**

Many analysts spend time performing the same tasks repeatedly. Python allows these tasks to be automated so they run **consistently and efficiently**.

---

# Overview

Analysts often perform repetitive workflows such as:

```text
Downloading reports
Cleaning datasets
Combining files
Updating spreadsheets
Generating summary reports
```

Example manual workflow:

```text
Download daily file
Open spreadsheet
Clean columns
Combine with previous data
Save new report
Send report to stakeholders
```

This process may take **30–60 minutes every day**.

Python can automate the same workflow.

Example automated pipeline:

```text
New Data Files → Python Script → Data Processing → Report Output
```

Instead of manually repeating steps, a script performs them automatically.

---

# Key Idea Cards (3 Cards)

### Automation Saves Time

Tasks that repeat frequently are ideal candidates for automation.

Examples:

```text
Daily reports
Weekly data consolidation
Monthly financial summaries
```

Python scripts can run these workflows automatically.

---

### Python Can Process Many Files

Python can scan folders and process many files at once.

Example scenario:

```text
100 CSV files
        ↓
Python script
        ↓
Combined dataset
```

This task would be difficult to perform manually.

---

### Automation Improves Consistency

Manual workflows may introduce errors.

Automation ensures that:

```text
Data is processed the same way every time
Reports follow the same structure
Steps are never skipped
```

This improves reliability.

---

# Key Concepts

## Identifying Automation Opportunities

Tasks that should be automated usually have these characteristics:

```text
Repeated frequently
Follow the same steps
Require processing multiple files
Require generating reports
```

Example:

```text
Daily sales report
```

Instead of manually updating the report, Python can automate it.

---

## Processing Files Automatically

Python can scan directories to identify files.

Example:

```python
import os

files = os.listdir("data")

print(files)
```

Output example:

```text
sales_jan.csv
sales_feb.csv
sales_mar.csv
```

Python can then process each file.

---

## Looping Through Files

Python loops allow scripts to process many files automatically.

Example:

```python
for file in files:
    print("Processing:", file)
```

This allows analysts to handle **large batches of files**.

---

## Combining Multiple Files

Python can combine datasets from multiple files.

Example:

```python
import pandas as pd

df1 = pd.read_csv("sales_jan.csv")
df2 = pd.read_csv("sales_feb.csv")

combined = pd.concat([df1, df2])

print(combined.head())
```

This creates a single dataset from multiple files.

---

# Decision Flow

When deciding whether to automate a task:

```text
Is the task repeated frequently?
        ↓
Automate with Python
```

```text
Does the task involve many files?
        ↓
Use Python loops
```

```text
Does the workflow follow predictable steps?
        ↓
Automation is ideal
```

Example automation workflow:

```text
Folder with daily reports
        ↓
Python script
        ↓
Clean dataset
        ↓
Combined reporting table
```

---

# Code Examples

### Example 1 — List Files in a Folder

```python
import os

files = os.listdir("data")

print(files)
```

---

### Example 2 — Loop Through Files

```python
for file in files:
    print("Processing:", file)
```

---

### Example 3 — Load Multiple CSV Files

```python
import pandas as pd

dataframes = []

for file in files:
    df = pd.read_csv("data/" + file)
    dataframes.append(df)
```

---

### Example 4 — Combine DataFrames

```python
combined = pd.concat(dataframes)

print(combined.head())
```

This creates a unified dataset.

---

# SQL / Excel Comparison

### Excel Example

Combining multiple files requires:

```text
Manual copy/paste
Power Query
```

---

### SQL Example

```sql
SELECT *
FROM sales_jan
UNION ALL
SELECT *
FROM sales_feb;
```

---

### Python Example

```python
combined = pd.concat([df1, df2])
```

Python provides flexibility for processing files.

---

# Practice Exercises

### Exercise 1

Tags: File I/O, Scripts, Automation

Write a script that lists all files in a folder.

---

### Exercise 2

Tags: Automation, Data Analysis

Loop through the files and print their names.

---

### Exercise 3

Tags: Automation, Data Analysis

Load two CSV files and combine them.

---

### Exercise 4

Tags: Automation, Data I/O

Export the combined dataset to a new CSV file.

---

# Common Mistakes

### Hardcoding File Names

Scripts should dynamically read files rather than relying on fixed filenames.

Example:

```python
files = os.listdir("data")
```

---

### Forgetting File Paths

Files must be referenced using the correct folder path.

Example:

```python
pd.read_csv("data/sales.csv")
```

---

### Ignoring File Formats

Ensure the correct file format is used:

```text
read_csv → CSV files
read_excel → Excel files
```

---

# Real-World Use

Automation is widely used in analytics teams.

Examples include:

```text
Automated financial reports
Daily sales summaries
Customer analytics reports
Inventory tracking reports
```

Example reporting pipeline:

```text
Daily CSV exports
      ↓
Python automation script
      ↓
Clean dataset
      ↓
Excel report
      ↓
Dashboard update
```

Automation allows analysts to focus on **analysis instead of manual data processing**.

---

# Lesson Recap

In this lesson you learned:

• how Python automates repetitive analyst tasks  
• how to process multiple files automatically  
• how loops enable batch data processing  
• how automation improves workflow efficiency

Automation is one of the **most valuable ways analysts use Python**.

---

# Next Lesson

Next we will continue Module 15 with:

# Lesson 5 — Building a Simple Reporting Script

You will learn:

• how to build a full reporting workflow in Python  
• how to extract data from a source  
• how to transform the data  
• how to generate a final report automatically.
