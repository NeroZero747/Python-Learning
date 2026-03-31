# Module 15 — Python for Analysts

# Lesson 1 — Why Analysts Use Python

---

# Lesson Objective

By the end of this lesson learners will understand:

• why analysts increasingly use Python  
• how Python complements **SQL and Excel workflows**  
• common analyst tasks that Python can automate  
• when Python is a better tool than Excel or SQL

Python allows analysts to **automate repetitive work, process large datasets, and build data workflows**.

---

# Overview

Many analysts start their work using tools like:

```text
Excel
SQL
BI tools (Power BI / Tableau)
```

These tools are excellent, but they can become difficult to manage when workflows grow larger.

Common problems analysts encounter include:

```text
Large Excel files
Manual repetitive steps
Complex nested formulas
Manual report generation
Combining multiple data sources
```

Python solves these problems by allowing analysts to create **repeatable data workflows**.

Example workflow:

```text
Database → Python Script → Clean Data → Excel Report → Email
```

Instead of manually performing these steps each day, Python can **automate the entire process**.

---

# Key Idea Cards (3 Cards)

### Python Automates Repetitive Work

Many analyst tasks repeat every day or week.

Examples:

```text
Downloading data
Cleaning datasets
Generating reports
Updating dashboards
```

Python scripts allow these tasks to run automatically.

---

### Python Works With Many Data Sources

Python can connect to many different data systems.

Examples:

```text
Databases
CSV files
Excel files
APIs
Cloud storage
```

This makes Python a powerful tool for combining data.

---

### Python Complements SQL and Excel

Python does not replace SQL or Excel.

Instead it enhances them.

Example workflow:

```text
SQL → extract data
Python → transform data
Excel → final reporting
```

Each tool performs the task it does best.

---

# Key Concepts

## Why Analysts Learn Python

Python helps analysts solve several common problems.

### Problem 1 — Manual Workflows

Example:

```text
Download file
Clean data
Build pivot tables
Create report
Email results
```

Python can automate this workflow.

---

### Problem 2 — Large Data

Excel becomes slow when datasets grow large.

Python tools like **Pandas** can process millions of rows efficiently.

---

### Problem 3 — Complex Logic

Nested Excel formulas can become difficult to manage.

Example Excel formula:

```text
=IF(A2>100,IF(B2="Yes","High","Medium"),"Low")
```

Python logic is easier to read.

Example:

```python
if value > 100 and approved:
    category = "High"
elif value > 100:
    category = "Medium"
else:
    category = "Low"
```

---

### Problem 4 — Combining Data Sources

Python can combine:

```text
SQL data
Excel data
API data
CSV files
```

into one dataset.

---

# Decision Flow

When deciding whether to use Python:

```text
Is the task repetitive?
        ↓
Use Python automation
```

```text
Is the dataset very large?
        ↓
Python may be more efficient
```

```text
Are multiple data sources required?
        ↓
Python simplifies integration
```

Example:

```text
Excel workflow too complex
        ↓
Move transformation logic into Python
```

---

# Code Examples

### Example 1 — Simple Python Script

```python
print("Hello Analysts")
```

This is the simplest Python program.

---

### Example 2 — Basic Data Processing

```python
import pandas as pd

data = {
    "sales": [100, 200, 150]
}

df = pd.DataFrame(data)

print(df)
```

Output:

```text
   sales
0   100
1   200
2   150
```

---

### Example 3 — Calculating Totals

```python
total_sales = df["sales"].sum()

print(total_sales)
```

Output:

```text
450
```

---

### Example 4 — Simple Conditional Logic

```python
value = 120

if value > 100:
    print("High value")
else:
    print("Normal value")
```

Output:

```text
High value
```

---

# SQL / Excel Comparison

### SQL Example

```sql
SELECT SUM(sales)
FROM transactions
```

---

### Excel Example

```text
=SUM(A1:A100)
```

---

### Python Example

```python
df["sales"].sum()
```

All three tools perform the same calculation.

---

# Practice Exercises

### Exercise 1

Tags: Lists, Automation

List three analyst tasks that could be automated using Python.

---

### Exercise 2

Tags: Excel, Data Analysis

Explain why Python is better than Excel for large datasets.

---

### Exercise 3

Tags: WHERE, Excel, HTTP Methods, CI/CD

Describe a workflow where SQL, Python, and Excel could be used together.

---

# Common Mistakes

### Expecting Python to Replace All Tools

Python works best when used **alongside SQL and Excel**, not instead of them.

---

### Overcomplicating Simple Tasks

Small calculations may still be easier in Excel.

Python becomes more valuable as workflows grow more complex.

---

### Ignoring Automation Opportunities

If a task is repeated frequently, it is often a good candidate for automation.

---

# Real-World Use

Many organizations now use Python to support analytics teams.

Examples include:

```text
Automating financial reports
Cleaning data before dashboards
Combining multiple data sources
Generating daily metrics reports
```

Example reporting pipeline:

```text
SQL Database
      ↓
Python Data Processing
      ↓
Excel / Dashboard Output
```

Python reduces manual work and improves reliability.

---

# Lesson Recap

In this lesson you learned:

• why analysts increasingly use Python  
• how Python complements SQL and Excel  
• common workflows Python can automate  
• when Python is the right tool for data tasks

Python allows analysts to build **automated, repeatable data workflows**.

---

# Next Lesson

Next we will continue Module 15 with:

# Lesson 2 — Replacing Excel Workflows with Python

You will learn:

• how Python reads Excel files  
• how Python transforms spreadsheet data  
• how Python writes results back to Excel  
• how Python automates Excel-based reports.
