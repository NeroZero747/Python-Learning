# Module 18 — Data Pipelines & Orchestration  
## Lesson 4 — Working with Large Data Files

---

# Lesson Objective

By the end of this lesson you will understand:

- Why **large datasets create challenges for pipelines**
- Techniques for processing **large files efficiently**
- How Python handles large datasets
- Strategies for processing **millions of records without crashing systems**

Real-world pipelines often process **gigabytes or terabytes of data**, so efficiency becomes extremely important.

---

# Overview

Small datasets are easy to process.

Example:

```python
df = pd.read_csv("sales.csv")
```

But real-world data pipelines often deal with files that are:

```text
Millions of rows
Multiple gigabytes
Hundreds of columns
```

Trying to load extremely large files into memory can cause problems such as:

```text
Slow performance
Memory errors
System crashes
```

Efficient pipelines must process data **incrementally or in optimized formats**.

---

# Why Large Files Are Difficult

Most computers have limited memory.

Example system memory:

```text
8 GB RAM
16 GB RAM
32 GB RAM
```

If a dataset is larger than available memory, a standard approach like:

```python
pd.read_csv("large_file.csv")
```

may fail.

This is why pipelines use techniques designed for **large-scale processing**.

---

# Common Strategies for Large Data

Several techniques are commonly used in production pipelines.

```text
Chunk Processing
Efficient File Formats
Parallel Processing
Database Processing
```

Each method helps pipelines process data more efficiently.

---

# Chunk Processing

Instead of loading the entire file at once, the file can be processed in **smaller pieces**.

Example:

```text
Large File
   ↓
Chunk 1
Chunk 2
Chunk 3
Chunk 4
```

Each chunk is processed individually.

---

# Python Chunk Example

Pandas allows reading files in chunks.

```python
import pandas as pd

chunks = pd.read_csv("large_file.csv", chunksize=10000)

for chunk in chunks:

    process(chunk)
```

This processes the dataset **10,000 rows at a time**.

Advantages:

```text
Lower memory usage
Better stability
Scalable processing
```

---

# Efficient File Formats

CSV files are common but not always efficient.

Better formats include:

```text
Parquet
Feather
Arrow
```

These formats are designed for **fast data processing**.

Example:

```python
df.to_parquet("data.parquet")
```

Benefits:

```text
Smaller file sizes
Faster read speeds
Better compression
```

---

# Example — Reading Parquet

```python
import pandas as pd

df = pd.read_parquet("data.parquet")
```

This is often **much faster than CSV**.

---

# Database Processing

Sometimes large datasets should not be processed in Python.

Instead, pipelines can push processing into databases.

Example:

```sql
SELECT
    customer_id,
    SUM(sales)
FROM transactions
GROUP BY customer_id
```

Databases are optimized for large-scale queries.

---

# Parallel Processing

Some pipelines divide work across multiple processes.

Example:

```text
File
 ↓
Process 1
Process 2
Process 3
Process 4
```

Each processor handles a portion of the data.

Libraries that support parallel processing include:

```text
Dask
Ray
Spark
```

These tools allow pipelines to scale across multiple CPUs or machines.

---

# Decision Flow

When processing large datasets:

```text
Is the dataset larger than memory?
        |
       Yes
        |
Use chunk processing
```

If the dataset is extremely large:

```text
Use distributed processing
```

Or move the processing to a **database system**.

---

# Code Example — Chunk Pipeline

Example pipeline processing a large file.

```python
import pandas as pd

chunks = pd.read_csv("large_file.csv", chunksize=50000)

for chunk in chunks:

    chunk["revenue"] = chunk["price"] * chunk["quantity"]

    chunk.to_csv("processed_data.csv", mode="a", header=False, index=False)
```

This pipeline processes the file **incrementally**.

---

# SQL / Excel Comparison

Excel often struggles with large datasets.

Example limitations:

```text
Excel row limit
Memory constraints
Slow calculations
```

Python pipelines can process much larger datasets.

Example workflow:

```text
Large file
 ↓
Python chunk processing
 ↓
Database storage
```

---

# Practice Exercises

### Exercise 1

Tags: Tuples, read_csv(), CSV, File I/O

Write a Python script that processes a file in chunks.

Example:

```python
pd.read_csv("file.csv", chunksize=10000)
```

---

### Exercise 2

Tags: Parquet, Pipelines

Convert a CSV dataset into a Parquet file.

Example:

```python
df.to_parquet("dataset.parquet")
```

---

### Exercise 3

Tags: Chunk Processing, Pipelines

Identify which processing approach should be used:

```text
Small dataset → standard Pandas
Large dataset → chunk processing
Huge dataset → distributed processing
```

---

# Common Mistakes

### Mistake 1 — Loading Entire Files Into Memory

Large files should often be processed in chunks.

---

### Mistake 2 — Using Inefficient File Formats

CSV files are slower than optimized formats such as Parquet.

---

### Mistake 3 — Ignoring Database Capabilities

Large transformations can often be performed faster using SQL.

---

# Real-World Use

Handling large datasets is common in many industries.

Examples include:

---

### Financial Systems

```text
Transaction records
Market data
Trade history
```

These datasets may contain **millions of rows per day**.

---

### Marketing Analytics

```text
Customer events
Ad impressions
Campaign metrics
```

Large-scale marketing pipelines often process **billions of records**.

---

### Healthcare Systems

```text
Claims records
Patient encounters
Provider transactions
```

Healthcare data pipelines frequently process **massive datasets**.

---

# Key Idea Cards

### Card 1

Large datasets require efficient processing strategies.

---

### Card 2

Chunk processing allows large files to be processed incrementally.

---

### Card 3

Efficient file formats such as **Parquet** improve pipeline performance.

---

# Lesson Recap

In this lesson you learned:

- challenges of working with large datasets  
- how chunk processing works  
- how efficient file formats improve performance  
- when to use distributed processing tools

These techniques allow pipelines to process **millions of records efficiently**.

---

# Next Lesson

Next you will learn:

**Module 18 — Lesson 5: Data Validation in Pipelines**

You will learn:

- why data quality checks are critical
- how pipelines detect bad data
- how to build validation rules inside pipelines.