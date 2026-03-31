# Module 18 — Data Pipelines & Orchestration  
## Lesson 11 — Pipeline Project: Automating Data Ingestion

---

# Lesson Objective

By the end of this lesson you will:

- Build a **data ingestion pipeline**
- Automatically retrieve a dataset
- Load the dataset into a processing system
- Prepare the data for transformation and analytics

This lesson introduces the **first stage of a real pipeline project**.

---

# Overview

Data pipelines often begin with **data ingestion**.

Data ingestion means **collecting data from external sources and bringing it into a system** for processing.

Example ingestion pipeline:

```text
External Data Source
        ↓
Python Pipeline
        ↓
Raw Data Storage
```

This stage ensures data enters the pipeline **automatically and reliably**.

---

# Project Scenario

Imagine your analytics team receives daily transaction data.

Currently the workflow is:

```text
Download data file
      ↓
Open spreadsheet
      ↓
Clean data
      ↓
Upload to database
```

This manual process is inefficient.

Instead, you will build a pipeline that automatically ingests the data.

Example automated workflow:

```text
Data file appears in directory
        ↓
Python pipeline runs
        ↓
Data loaded into raw database table
```

---

# Pipeline Architecture

The ingestion pipeline will follow this structure:

```text
Source Data
      ↓
Extract File
      ↓
Validate File
      ↓
Load Raw Data
```

This stage focuses on **reliably collecting raw data**.

---

# Example Source Data

Assume the system receives a CSV file:

```text
transactions.csv
```

Example dataset:

```text
transaction_id,customer_id,price,quantity
1001,2001,10,2
1002,2002,15,1
1003,2003,20,3
```

The ingestion pipeline will load this file into the system.

---

# Step 1 — Extract Data

First the pipeline retrieves the source file.

Example:

```python
import pandas as pd

def extract_data():

    df = pd.read_csv("transactions.csv")

    return df
```

This stage reads the file into a DataFrame.

---

# Step 2 — Validate the File

Before loading the dataset, the pipeline validates the file.

Example validation rules:

```text
File exists
Dataset is not empty
Expected columns are present
```

Example validation code:

```python
def validate_file(df):

    if df.empty:
        raise Exception("Dataset is empty")

    required_columns = ["transaction_id", "customer_id", "price", "quantity"]

    for col in required_columns:
        if col not in df.columns:
            raise Exception(f"Missing column: {col}")

    return df
```

This prevents invalid files from entering the system.

---

# Step 3 — Load Raw Data

After validation, the dataset is loaded into a **raw data table**.

Example:

```python
from sqlalchemy import create_engine

def load_raw_data(df):

    engine = create_engine("sqlite:///pipeline.db")

    df.to_sql("transactions_raw", engine, if_exists="append", index=False)
```

The raw table stores the dataset exactly as received.

---

# Full Ingestion Pipeline Script

Below is the full ingestion pipeline.

```python
import pandas as pd
from sqlalchemy import create_engine


def extract_data():

    df = pd.read_csv("transactions.csv")

    return df


def validate_file(df):

    if df.empty:
        raise Exception("Dataset is empty")

    required_columns = ["transaction_id", "customer_id", "price", "quantity"]

    for col in required_columns:
        if col not in df.columns:
            raise Exception(f"Missing column: {col}")

    return df


def load_raw_data(df):

    engine = create_engine("sqlite:///pipeline.db")

    df.to_sql("transactions_raw", engine, if_exists="append", index=False)


def run_pipeline():

    df = extract_data()

    df = validate_file(df)

    load_raw_data(df)


if __name__ == "__main__":

    run_pipeline()
```

This script automatically ingests the dataset.

---

# Visual Pipeline Flow

The pipeline workflow:

```text
transactions.csv
      ↓
Extract Data
      ↓
Validate File
      ↓
Raw Database Table
```

This raw dataset will be used by later pipeline stages.

---

# Why Raw Data Is Stored

Most production pipelines store **raw data first**.

Example layered pipeline:

```text
Raw Data Layer
      ↓
Clean Data Layer
      ↓
Analytics Layer
```

Keeping raw data allows pipelines to:

```text
Reprocess data
Fix pipeline errors
Audit historical records
```

---

# SQL / Excel Comparison

Manual workflow:

```text
Download file
Open Excel
Clean data
Upload results
```

Automated ingestion:

```text
New data file
      ↓
Pipeline ingests automatically
```

Automation removes repetitive tasks.

---

# Practice Exercises

### Exercise 1

Tags: File I/O, Databases, CI/CD, Automation

Create a pipeline that reads a CSV file and loads it into a database.

---

### Exercise 2

Tags: Lists, CI/CD, Validation, Automation

Modify the validation stage to check that **price values are positive**.

Example:

```python
(df["price"] > 0).all()
```

---

### Exercise 3

Tags: CI/CD, Automation

Modify the pipeline to log a message when ingestion completes.

---

# Common Mistakes

### Mistake 1 — Skipping File Validation

Pipelines should always validate incoming files.

---

### Mistake 2 — Overwriting Raw Data

Raw ingestion tables should typically **append records** instead of replacing them.

---

### Mistake 3 — Not Preserving Raw Data

Raw datasets are important for debugging and auditing.

---

# Real-World Use

Data ingestion pipelines are used in many systems.

Examples include:

---

### Marketing Analytics

```text
Ad campaign reports
Website activity logs
Customer event data
```

---

### Financial Systems

```text
Market data feeds
Transaction records
Payment processing logs
```

---

### Healthcare Systems

```text
Claims records
Provider rosters
Patient encounters
```

Data ingestion pipelines ensure new data enters systems **automatically and reliably**.

---

# Key Idea Cards

### Card 1

Data ingestion pipelines retrieve external data and load it into the system.

---

### Card 2

Raw data is often stored before transformation occurs.

---

### Card 3

Validation ensures incoming data files meet expected structure requirements.

---

# Lesson Recap

In this lesson you built a pipeline that:

- ingests a dataset automatically  
- validates incoming files  
- stores raw data in a database

This represents the **first stage of a real-world data pipeline**.

---

# Next Lesson

Next you will learn:

**Module 18 — Lesson 12: Pipeline Project — Data Quality Checks**

You will expand the pipeline to include:

- automated **data validation rules**
- detection of **invalid records**
- improved data quality controls.