# Module 18 — Data Pipelines & Orchestration  
## Lesson 12 — Pipeline Project: Data Quality Checks

---

# Lesson Objective

By the end of this lesson you will:

- Add **data quality checks** to the pipeline
- Detect **invalid or corrupted records**
- Separate **valid and invalid data**
- Improve the reliability of the ingestion pipeline

This lesson expands the ingestion pipeline by adding **data validation and quality control**.

---

# Overview

In the previous lesson you built a pipeline that:

```text
Extracts a dataset
Validates file structure
Loads raw data into a database
```

However, real-world datasets often contain errors.

Examples:

```text
Negative prices
Missing values
Duplicate transactions
Invalid customer IDs
```

If pipelines ignore these problems, incorrect data may propagate through the system.

To prevent this, pipelines perform **data quality checks**.

---

# Pipeline Architecture Update

The updated pipeline will include a validation stage.

```text
Extract Data
      ↓
Validate File
      ↓
Data Quality Checks
      ↓
Load Valid Data
```

Invalid records can be separated or flagged.

---

# Example Dataset

Example transaction dataset:

```text
transaction_id,customer_id,price,quantity
1001,2001,10,2
1002,2002,-5,1
1003,2003,20,3
```

In this dataset:

```text
Row 2 contains an invalid negative price
```

The pipeline must detect this issue.

---

# Common Data Quality Checks

Pipelines commonly validate:

```text
Missing values
Negative numbers
Duplicate records
Invalid formats
```

Each rule protects data quality.

---

# Check 1 — Missing Values

Example dataset with missing values:

```text
transaction_id,customer_id,price,quantity
1001,2001,10,2
1002,,15,1
```

Missing customer IDs could break analytics systems.

---

# Python Missing Value Check

Example rule:

```python
if df["customer_id"].isnull().any():
    raise Exception("Missing customer IDs detected")
```

The pipeline stops if invalid records are detected.

---

# Check 2 — Negative Values

Certain fields should never contain negative numbers.

Example:

```text
Price
Quantity
Revenue
```

Negative values may indicate:

```text
Data entry errors
Corrupted files
Incorrect system exports
```

---

# Python Negative Value Check

Example validation rule:

```python
if (df["price"] < 0).any():
    raise Exception("Negative price detected")
```

---

# Check 3 — Duplicate Records

Duplicate records can distort analytics results.

Example dataset:

```text
transaction_id,customer_id,price
1001,2001,10
1001,2001,10
```

The pipeline should detect duplicates.

---

# Python Duplicate Check

Example rule:

```python
duplicates = df.duplicated()

if duplicates.any():
    print("Duplicate records detected")
```

Duplicates can either be removed or flagged.

---

# Separating Invalid Records

Instead of stopping the pipeline, some systems separate invalid records.

Example workflow:

```text
Raw data
   ↓
Validation rules
   ↓
Valid records → pipeline continues
Invalid records → error table
```

This allows the pipeline to continue processing good data.

---

# Example Data Quality Pipeline

Example validation function:

```python
def data_quality_checks(df):

    if df["customer_id"].isnull().any():
        raise Exception("Missing customer IDs")

    if (df["price"] < 0).any():
        raise Exception("Negative prices detected")

    return df
```

This function ensures the dataset meets quality requirements.

---

# Updated Pipeline Script

Below is the updated pipeline including quality checks.

```python
import pandas as pd
from sqlalchemy import create_engine


def extract_data():

    df = pd.read_csv("transactions.csv")

    return df


def validate_file(df):

    if df.empty:
        raise Exception("Dataset is empty")

    return df


def data_quality_checks(df):

    if df["customer_id"].isnull().any():
        raise Exception("Missing customer IDs")

    if (df["price"] < 0).any():
        raise Exception("Negative prices detected")

    return df


def load_raw_data(df):

    engine = create_engine("sqlite:///pipeline.db")

    df.to_sql("transactions_raw", engine, if_exists="append", index=False)


def run_pipeline():

    df = extract_data()

    df = validate_file(df)

    df = data_quality_checks(df)

    load_raw_data(df)


if __name__ == "__main__":

    run_pipeline()
```

This pipeline ensures only **valid data is loaded**.

---

# Visual Pipeline Flow

Updated pipeline:

```text
transactions.csv
      ↓
Extract Data
      ↓
Validate File
      ↓
Quality Checks
      ↓
Raw Database Table
```

This improves pipeline reliability.

---

# SQL / Excel Comparison

Manual validation workflow:

```text
Open spreadsheet
Search for missing values
Check negative numbers
Remove duplicates
```

Pipeline workflow:

```text
Automated validation rules
      ↓
Clean dataset
```

Automation ensures **consistent data quality**.

---

# Practice Exercises

### Exercise 1

Tags: Lists, CI/CD, Data Quality

Write a rule detecting negative values in the quantity column.

Example:

```python
(df["quantity"] < 0).any()
```

---

### Exercise 2

Tags: Lists, Transactions, CI/CD, Data Quality

Write a rule detecting duplicate transaction IDs.

Example:

```python
df["transaction_id"].duplicated()
```

---

### Exercise 3

Tags: CI/CD, Data Quality

Modify the pipeline to remove duplicate rows.

Example:

```python
df = df.drop_duplicates()
```

---

# Common Mistakes

### Mistake 1 — Ignoring Data Quality

Pipelines without validation may introduce corrupted data.

---

### Mistake 2 — Overly Strict Validation

Validation rules should detect real errors without rejecting valid records.

---

### Mistake 3 — Not Logging Quality Failures

Quality check failures should always be logged.

---

# Real-World Use

Data quality checks are essential in many systems.

Examples include:

---

### Financial Systems

```text
Transaction validation
Fraud detection
Accounting accuracy
```

---

### Marketing Analytics

```text
Campaign metrics validation
Customer data verification
Event tracking integrity
```

---

### Healthcare Systems

```text
Claims validation
Provider ID verification
Patient data quality checks
```

Data quality checks ensure analytics systems rely on **accurate data**.

---

# Key Idea Cards

### Card 1

Data quality checks detect invalid records in datasets.

---

### Card 2

Common validation rules include missing values, negative numbers, and duplicates.

---

### Card 3

Pipelines should detect and handle invalid records automatically.

---

# Lesson Recap

In this lesson you added data quality checks to the pipeline.

You learned:

- how to detect invalid records  
- how pipelines enforce data quality rules  
- how validation protects downstream analytics systems

Data quality checks are essential for **trustworthy data pipelines**.

---

# Next Lesson

Next you will learn:

**Module 18 — Lesson 13: Pipeline Project — Database Loading**

You will expand the pipeline to:

- load **clean data into analytics tables**
- separate **raw data and processed data**
- build a multi-stage pipeline architecture.