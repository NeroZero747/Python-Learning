# Module 18 — Data Pipelines & Orchestration  
## Lesson 1 — What is a Data Pipeline

---

# Lesson Objective

By the end of this lesson you will understand:

- What a **data pipeline** is  
- Why organizations build pipelines  
- The basic structure of a pipeline  
- How Python is commonly used to build pipelines

Data pipelines are the foundation of **modern data systems**.

---

# Overview

A **data pipeline** is a system that automatically moves data from one place to another.

Example:

```text
Source Data
      ↓
Python Script
      ↓
Cleaned Data
      ↓
Database
      ↓
Dashboard
```

Instead of manually moving data between systems, pipelines **automate the entire process**.

---

# Simple Real-World Example

Imagine a sales reporting system.

Every day:

```text
Sales System
      ↓
Python Pipeline
      ↓
Clean Data Table
      ↓
PowerBI / Tableau Dashboard
```

Without pipelines someone would need to:

```text
Download data
Clean it
Upload it
Refresh dashboards
```

Pipelines automate this.

---

# Pipeline Example (Conceptual)

A typical pipeline might look like this:

```text
API
 ↓
Python script retrieves data
 ↓
Clean and transform the data
 ↓
Store the data in a database
 ↓
Dashboard reads the data
```

This happens automatically.

---

# Key Components of a Pipeline

Most pipelines contain several stages.

### 1 — Data Source

Where the data originates.

Examples:

```text
API
Database
CSV files
Excel files
Cloud storage
```

---

### 2 — Extraction

Retrieving the data.

Example:

```python
requests.get(api_url)
```

or

```python
pd.read_csv("sales.csv")
```

---

### 3 — Transformation

Cleaning and preparing the data.

Examples:

```python
df.drop_duplicates()
df.fillna(0)
df["total"] = df["price"] * df["quantity"]
```

---

### 4 — Loading

Saving the processed data.

Examples:

```python
df.to_sql()
df.to_parquet()
df.to_csv()
```

---

# The ETL Model

Pipelines often follow a structure called:

```text
ETL
```

Which stands for:

```text
Extract
Transform
Load
```

Example:

```text
Extract → Retrieve API data
Transform → Clean dataset
Load → Store in database
```

You will explore this model in the next lesson.

---

# Decision Flow

When deciding to build a pipeline:

```text
Is data being moved repeatedly?
        |
       Yes
        |
Should the process be automated?
        |
       Yes
        |
Build a pipeline
```

Pipelines eliminate repetitive manual work.

---

# Code Example (Simple Pipeline)

```python
import pandas as pd

df = pd.read_csv("sales.csv")

df["revenue"] = df["price"] * df["quantity"]

df.to_csv("sales_clean.csv", index=False)
```

This small script acts as a pipeline:

```text
Raw CSV → Process → Clean CSV
```

---

# SQL / Excel Comparison

Manual workflow:

```text
Download file
Open Excel
Clean data
Create report
```

Pipeline workflow:

```text
Python pipeline
      ↓
Automated data processing
```

Automation removes repetitive work.

---

# Practice Exercises

### Exercise 1

Tags: CI/CD, Dashboards

Think of a task you perform repeatedly.

Examples:

```text
Downloading reports
Cleaning spreadsheets
Updating dashboards
```

Could this task become a pipeline?

---

### Exercise 2

Tags: pandas, Imports, read_csv(), to_csv()

Write a small Python pipeline.

```python
import pandas as pd

df = pd.read_csv("data.csv")

df = df.dropna()

df.to_csv("clean_data.csv")
```

---

### Exercise 3

Tags: HTTP Methods, CI/CD

Draw a pipeline diagram for a dataset you use.

Example:

```text
Data source
     ↓
Processing
     ↓
Output
```

---

# Common Mistakes

### Mistake 1 — Overcomplicating Pipelines

Many pipelines start as simple scripts.

Start simple.

---

### Mistake 2 — Manual Processes

If a process runs every day, it should likely be automated.

---

### Mistake 3 — Ignoring Data Validation

Always check data quality during transformation.

---

# Real-World Use

Data pipelines are used everywhere.

Examples include:

---

### Analytics Systems

Example:

```text
Marketing Data
      ↓
Python Pipeline
      ↓
Data Warehouse
      ↓
Dashboards
```

---

### Financial Systems

Example:

```text
Market Data API
      ↓
Data Pipeline
      ↓
Trading Analytics
```

---

### Healthcare Systems

Example:

```text
Claims Data
      ↓
Processing Pipeline
      ↓
Reporting Systems
```

---

# Key Idea Cards

### Card 1

A data pipeline automates the movement and processing of data.

---

### Card 2

Most pipelines follow the structure:

```text
Extract → Transform → Load
```

---

### Card 3

Pipelines eliminate repetitive manual data work.

---

# Lesson Recap

In this lesson you learned:

- what data pipelines are  
- why organizations build pipelines  
- the main stages of a pipeline  
- how Python scripts act as pipelines

Data pipelines are the **foundation of modern data engineering and analytics systems**.

---

# Next Lesson

Next you will learn:

**Module 18 — Lesson 2: ETL vs ELT**

You will learn:

- the difference between ETL and ELT
- when each model is used
- how modern data systems process large datasets.