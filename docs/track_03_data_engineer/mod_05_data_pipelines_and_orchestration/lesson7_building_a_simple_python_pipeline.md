# Module 18 — Data Pipelines & Orchestration  
## Lesson 10 — Building a Simple Python Pipeline

---

# Lesson Objective

By the end of this lesson you will understand:

- How to build a **complete Python data pipeline**
- How pipeline stages work together
- How to structure pipeline code for readability
- How to automate common data processing tasks

In this lesson you will combine concepts from earlier lessons to create a **fully functioning pipeline**.

---

# Overview

A typical pipeline consists of several stages:

```text
Extract Data
      ↓
Validate Data
      ↓
Transform Data
      ↓
Load Data
```

Each stage performs a specific task in the data workflow.

Instead of performing these steps manually, Python can automate the entire process.

---

# Example Pipeline Scenario

Imagine your organization receives a daily sales file.

Example workflow:

```text
Sales CSV File
      ↓
Pipeline reads the file
      ↓
Data is validated
      ↓
Data is transformed
      ↓
Clean data stored in database
```

This pipeline runs automatically every day.

---

# Pipeline Structure

A well-structured pipeline separates each stage into functions.

Example structure:

```text
extract_data()
validate_data()
transform_data()
load_data()
```

This improves code readability and maintainability.

---

# Step 1 — Extract Data

The extraction step retrieves the source data.

Example:

```python
import pandas as pd

def extract_data():

    df = pd.read_csv("sales.csv")

    return df
```

This function loads the dataset into a DataFrame.

---

# Step 2 — Validate Data

Next, the pipeline validates the dataset.

Example:

```python
def validate_data(df):

    if df.empty:
        raise Exception("Dataset is empty")

    if df["price"].isnull().any():
        raise Exception("Missing price values")

    return df
```

Validation prevents invalid data from entering the pipeline.

---

# Step 3 — Transform Data

The transformation stage cleans and prepares the dataset.

Example:

```python
def transform_data(df):

    df["revenue"] = df["price"] * df["quantity"]

    df = df.drop_duplicates()

    return df
```

This step prepares the dataset for analytics.

---

# Step 4 — Load Data

The final stage stores the processed data.

Example:

```python
from sqlalchemy import create_engine

def load_data(df):

    engine = create_engine("sqlite:///sales.db")

    df.to_sql("sales_data", engine, if_exists="replace", index=False)
```

This loads the cleaned data into a database.

---

# Complete Pipeline Script

Below is a full pipeline combining all stages.

```python
import pandas as pd
from sqlalchemy import create_engine


def extract_data():

    df = pd.read_csv("sales.csv")

    return df


def validate_data(df):

    if df.empty:
        raise Exception("Dataset is empty")

    if df["price"].isnull().any():
        raise Exception("Missing price values")

    return df


def transform_data(df):

    df["revenue"] = df["price"] * df["quantity"]

    df = df.drop_duplicates()

    return df


def load_data(df):

    engine = create_engine("sqlite:///sales.db")

    df.to_sql("sales_data", engine, if_exists="replace", index=False)


def run_pipeline():

    df = extract_data()

    df = validate_data(df)

    df = transform_data(df)

    load_data(df)


if __name__ == "__main__":

    run_pipeline()
```

This script represents a **complete ETL pipeline**.

---

# Visual Pipeline Flow

The script follows this workflow:

```text
CSV File
  ↓
Extract Data
  ↓
Validate Data
  ↓
Transform Data
  ↓
Database
```

Each stage performs a specific function.

---

# Benefits of Structured Pipelines

Separating pipeline stages into functions provides several advantages.

```text
Improved readability
Easier debugging
Reusable code
Clear pipeline structure
```

Structured pipelines are easier to maintain in production environments.

---

# SQL / Excel Comparison

Manual workflow:

```text
Download spreadsheet
Clean data
Calculate columns
Upload results
```

Pipeline workflow:

```text
Automated Python script
      ↓
Data processed automatically
```

Automation saves time and reduces errors.

---

# Practice Exercises

### Exercise 1

Tags: Lists, File I/O, CI/CD, Arithmetic

Create a pipeline that reads a CSV file and adds a calculated column.

Example:

```python
df["total"] = df["price"] * df["quantity"]
```

---

### Exercise 2

Tags: UPDATE, DELETE, CI/CD

Modify the pipeline to remove duplicate records.

Example:

```python
df.drop_duplicates()
```

---

### Exercise 3

Tags: to_csv(), CSV, File I/O, Databases

Modify the pipeline to write results to a CSV file instead of a database.

Example:

```python
df.to_csv("clean_sales.csv")
```

---

# Common Mistakes

### Mistake 1 — Writing Pipelines as One Large Script

Large scripts become difficult to maintain.

Always break pipelines into stages.

---

### Mistake 2 — Skipping Validation

Validation ensures pipeline output remains reliable.

---

### Mistake 3 — Hardcoding Values

Pipeline settings should be stored in configuration files when possible.

---

# Real-World Use

Simple pipelines like this are used in many real-world systems.

Examples include:

---

### Reporting Pipelines

```text
Daily sales data
      ↓
Pipeline processing
      ↓
Analytics database
```

---

### API Ingestion Pipelines

```text
API data
      ↓
Python pipeline
      ↓
Database storage
```

---

### Data Cleaning Pipelines

```text
Raw dataset
      ↓
Transformation pipeline
      ↓
Clean analytics dataset
```

These pipelines automate repetitive data tasks.

---

# Key Idea Cards

### Card 1

A data pipeline automates extraction, transformation, and loading of data.

---

### Card 2

Structured pipelines separate stages into reusable functions.

---

### Card 3

Python pipelines automate repetitive data processing tasks.

---

# Lesson Recap

In this lesson you learned:

- how to build a complete Python pipeline  
- how extraction, validation, transformation, and loading work together  
- how structured pipelines improve maintainability  
- how automation replaces manual workflows

This lesson demonstrates how Python can automate **real-world data processing pipelines**.

---

# Next Lesson

Next you will learn:

**Module 18 — Lesson 11: Pipeline Project — Automating Data Ingestion**

You will build a project that:

- retrieves data automatically  
- processes the dataset  
- stores the results in a database.