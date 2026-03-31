# Module 18 — Data Pipelines & Orchestration  
## Lesson 13 — Pipeline Project: Database Loading

---

# Lesson Objective

By the end of this lesson you will:

- Load **validated data into analytics tables**
- Separate **raw data from processed data**
- Build a **multi-stage pipeline architecture**
- Prepare data for reporting and analytics

This lesson expands the pipeline to include **database loading and structured data layers**.

---

# Overview

In the previous lessons you built a pipeline that:

```text
Extracts data
Validates files
Performs data quality checks
Stores raw data
```

However, raw datasets are not ideal for analytics.

Example raw dataset:

```text
transaction_id,customer_id,price,quantity
1001,2001,10,2
1002,2002,15,1
```

Analytics systems often require **clean and structured tables**.

This lesson adds a stage that loads **cleaned data into analytics tables**.

---

# Layered Data Architecture

Modern pipelines often organize data into layers.

Example layered architecture:

```text
Raw Layer
     ↓
Clean Layer
     ↓
Analytics Layer
```

Each layer serves a different purpose.

---

# Raw Data Layer

The raw layer stores **data exactly as it was received**.

Example:

```text
transactions_raw
```

Benefits of storing raw data:

```text
Historical record of data
Ability to reprocess pipelines
Audit trail for debugging
```

---

# Clean Data Layer

The clean layer stores **validated and standardized data**.

Example table:

```text
transactions_clean
```

In this layer the dataset may be:

```text
Validated
Deduplicated
Standardized
```

Clean datasets are easier to analyze.

---

# Analytics Layer

The analytics layer contains **aggregated or business-ready datasets**.

Example:

```text
daily_sales_summary
customer_revenue_totals
product_performance_metrics
```

These tables power dashboards and reports.

---

# Pipeline Architecture

The updated pipeline structure:

```text
Extract Data
      ↓
Validate File
      ↓
Quality Checks
      ↓
Load Raw Data
      ↓
Transform Data
      ↓
Load Clean Data
```

The pipeline now has **two database stages**.

---

# Transforming Raw Data

Example transformation:

```text
Calculate revenue
Remove duplicates
Standardize column names
```

Example Python transformation:

```python
def transform_data(df):

    df["revenue"] = df["price"] * df["quantity"]

    df = df.drop_duplicates()

    return df
```

---

# Loading Clean Data

After transformation, the clean dataset is loaded into a separate table.

Example:

```python
from sqlalchemy import create_engine

def load_clean_data(df):

    engine = create_engine("sqlite:///pipeline.db")

    df.to_sql("transactions_clean", engine, if_exists="replace", index=False)
```

This creates a clean analytics dataset.

---

# Updated Pipeline Script

Below is the updated pipeline with raw and clean layers.

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


def transform_data(df):

    df["revenue"] = df["price"] * df["quantity"]

    df = df.drop_duplicates()

    return df


def load_clean_data(df):

    engine = create_engine("sqlite:///pipeline.db")

    df.to_sql("transactions_clean", engine, if_exists="replace", index=False)


def run_pipeline():

    df = extract_data()

    df = validate_file(df)

    df = data_quality_checks(df)

    load_raw_data(df)

    clean_df = transform_data(df)

    load_clean_data(clean_df)


if __name__ == "__main__":

    run_pipeline()
```

This script now supports **multi-layer data processing**.

---

# Visual Pipeline Flow

The complete pipeline now looks like this:

```text
transactions.csv
      ↓
Extract Data
      ↓
Validate File
      ↓
Quality Checks
      ↓
transactions_raw
      ↓
Transform Data
      ↓
transactions_clean
```

This structure is widely used in production systems.

---

# SQL / Excel Comparison

Manual workflow:

```text
Open spreadsheet
Clean data
Save new file
Upload results
```

Pipeline workflow:

```text
Raw data stored
      ↓
Automated transformation
      ↓
Clean analytics tables
```

Automation improves reliability.

---

# Practice Exercises

### Exercise 1

Tags: Lists, Databases, CI/CD, Arithmetic

Modify the pipeline to calculate a **total revenue column**.

Example:

```python
df["revenue"] = df["price"] * df["quantity"]
```

---

### Exercise 2

Tags: Lists, groupby(), Aggregations, CREATE TABLE

Create an analytics table that aggregates sales by customer.

Example:

```python
df.groupby("customer_id")["revenue"].sum()
```

---

### Exercise 3

Tags: to_csv(), CSV, Databases, CI/CD

Modify the pipeline to load clean data into a **CSV file instead of a database**.

Example:

```python
df.to_csv("clean_transactions.csv")
```

---

# Common Mistakes

### Mistake 1 — Mixing Raw and Clean Data

Raw and transformed datasets should be stored in separate tables.

---

### Mistake 2 — Overwriting Raw Data

Raw data tables should usually append records instead of replacing them.

---

### Mistake 3 — Skipping Transformation

Clean data layers improve analytics and reporting.

---

# Real-World Use

Layered pipelines are used in most modern data systems.

Examples include:

---

### Analytics Systems

```text
Raw marketing events
      ↓
Clean event data
      ↓
Campaign analytics
```

---

### Financial Systems

```text
Trade data
      ↓
Validated transactions
      ↓
Portfolio analytics
```

---

### Healthcare Systems

```text
Claims ingestion
      ↓
Validated claims
      ↓
Cost analytics
```

Layered pipelines ensure systems remain **organized and scalable**.

---

# Key Idea Cards

### Card 1

Raw data layers preserve original datasets.

---

### Card 2

Clean data layers contain validated and transformed data.

---

### Card 3

Layered pipelines improve reliability and maintainability.

---

# Lesson Recap

In this lesson you expanded the pipeline to include:

- raw data storage  
- transformation steps  
- clean analytics tables

This layered architecture is widely used in **modern data pipelines**.

---

# Next Lesson

Next you will learn:

**Module 18 — Lesson 14: Production Pipeline Architecture**

You will learn:

- how production pipelines are designed
- how systems scale data processing
- how engineers manage complex pipeline workflows.