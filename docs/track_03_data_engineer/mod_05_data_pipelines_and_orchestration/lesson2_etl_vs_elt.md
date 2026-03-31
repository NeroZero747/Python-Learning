# Module 18 — Data Pipelines & Orchestration  
## Lesson 2 — ETL vs ELT

---

# Lesson Objective

By the end of this lesson you will understand:

- What **ETL** means  
- What **ELT** means  
- The differences between ETL and ELT pipelines  
- When each architecture is used in modern data systems

Understanding ETL vs ELT is essential for designing **efficient data pipelines**.

---

# Overview

In the previous lesson you learned that most pipelines follow a structure like:

```text
Extract → Transform → Load
```

This model is called:

```text
ETL
```

However, modern data systems often use a different architecture called:

```text
ELT
```

Which means:

```text
Extract → Load → Transform
```

Both approaches move and process data, but they do it **in different orders**.

---

# ETL Architecture

ETL stands for:

```text
Extract
Transform
Load
```

The pipeline works like this:

```text
Data Source
      ↓
Extract Data
      ↓
Transform Data
      ↓
Load Clean Data into Database
```

This means the **data is cleaned before it is stored**.

---

# ETL Example

Example pipeline:

```text
Sales CSV
      ↓
Python script cleans data
      ↓
Clean data inserted into database
```

Example Python transformation:

```python
import pandas as pd

df = pd.read_csv("sales.csv")

df = df.dropna()

df["revenue"] = df["price"] * df["quantity"]
```

After transformation:

```python
df.to_sql("sales_clean")
```

Only **clean data** enters the database.

---

# ELT Architecture

ELT stands for:

```text
Extract
Load
Transform
```

The pipeline works like this:

```text
Data Source
      ↓
Extract Data
      ↓
Load Raw Data into Database
      ↓
Transform Inside Database
```

This means the **database performs the transformation work**.

---

# ELT Example

Example pipeline:

```text
Sales CSV
      ↓
Load raw data into database
      ↓
Transform using SQL
```

Example SQL transformation:

```sql
SELECT
    price,
    quantity,
    price * quantity AS revenue
FROM sales_raw
```

The transformation happens **inside the database**.

---

# Visual Comparison

### ETL

```text
Source
  ↓
Transform
  ↓
Database
```

### ELT

```text
Source
  ↓
Database
  ↓
Transform
```

The difference is **where the transformation happens**.

---

# Why ETL Was Popular

Historically, databases were not powerful enough to process large datasets efficiently.

So pipelines processed data **before loading it into databases**.

Example:

```text
Data source
      ↓
ETL tool
      ↓
Clean database tables
```

Tools commonly used for ETL included:

```text
Informatica
Talend
SSIS
```

---

# Why ELT Became Popular

Modern data platforms are extremely powerful.

Examples include:

```text
Snowflake
BigQuery
Redshift
Databricks
```

These systems can process massive datasets quickly.

This allows pipelines to:

```text
Load first
Transform later
```

Which simplifies pipeline design.

---

# Decision Flow

When designing pipelines:

```text
Is your database very powerful?
        |
       Yes
        |
Use ELT
```

If the database has limited processing capability:

```text
Use ETL
```

---

# Code Example — ETL Pipeline

```python
import pandas as pd

df = pd.read_csv("sales.csv")

df["revenue"] = df["price"] * df["quantity"]

df.to_sql("sales_clean")
```

Pipeline:

```text
CSV → Python Transform → Database
```

---

# Code Example — ELT Pipeline

Step 1 — Load raw data:

```python
df.to_sql("sales_raw")
```

Step 2 — Transform with SQL:

```sql
SELECT
    price,
    quantity,
    price * quantity AS revenue
FROM sales_raw
```

Pipeline:

```text
CSV → Database → SQL Transform
```

---

# SQL / Excel Comparison

Excel workflow often resembles ETL:

```text
Download data
Clean spreadsheet
Save cleaned version
```

Modern analytics workflows resemble ELT:

```text
Load raw data
Transform with SQL
```

---

# Practice Exercises

### Exercise 1

Tags: Databases, APIs, CI/CD, ETL

Identify whether the following pipeline is ETL or ELT.

```text
API
 ↓
Python cleans data
 ↓
Database
```

Answer: **ETL**

---

### Exercise 2

Tags: Databases, CI/CD, ETL, Data I/O

Identify whether this pipeline is ETL or ELT.

```text
CSV
 ↓
Load into database
 ↓
SQL transformations
```

Answer: **ELT**

---

### Exercise 3

Tags: pandas, Imports, read_csv(), CSV

Write a Python script that loads raw data into a database.

```python
import pandas as pd

df = pd.read_csv("sales.csv")

df.to_sql("sales_raw")
```

---

# Common Mistakes

### Mistake 1 — Transforming Too Early

Some pipelines transform data unnecessarily before loading.

Sometimes it's better to **load raw data first**.

---

### Mistake 2 — Losing Raw Data

Always keep a copy of the **original raw dataset**.

This allows pipelines to be rerun safely.

---

### Mistake 3 — Ignoring Database Capabilities

Modern databases can perform transformations extremely efficiently.

Use them when possible.

---

# Real-World Use

ETL and ELT are used across modern data systems.

Examples include:

---

### ETL Systems

```text
Python pipelines
Data integration tools
Legacy enterprise systems
```

---

### ELT Systems

```text
Snowflake pipelines
BigQuery analytics
Modern data warehouses
```

---

### Hybrid Systems

Many organizations use a combination:

```text
Extract → Load → Transform → Additional Python Processing
```

---

# Key Idea Cards

### Card 1

ETL means **Extract → Transform → Load**.

---

### Card 2

ELT means **Extract → Load → Transform**.

---

### Card 3

Modern data platforms often favor **ELT architectures**.

---

# Lesson Recap

In this lesson you learned:

- what ETL means  
- what ELT means  
- how ETL and ELT pipelines differ  
- when each architecture is used

Understanding these architectures helps you design **efficient data pipelines**.

---

# Next Lesson

Next you will learn:

**Module 18 — Lesson 3: Pipeline Design Patterns**

You will learn:

- common pipeline architectures  
- batch pipelines vs streaming pipelines  
- how to design maintainable pipelines.