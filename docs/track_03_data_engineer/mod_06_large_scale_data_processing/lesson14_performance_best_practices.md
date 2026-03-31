# Module 19 — Large Scale Data Processing  
## Lesson 15 — Performance Best Practices

---

# Lesson Objective

By the end of this lesson you will understand:

- Best practices for working with **large datasets**
- How to design **efficient data workflows**
- How to choose the right tool for different data sizes
- How to avoid common performance problems

You will learn practical strategies used by analysts and engineers to ensure data systems remain **fast and scalable**.

---

# Overview

Throughout this module you learned several tools and techniques for processing large datasets.

Examples include:

```text id="g9633r"
Chunk processing
Memory optimization
Columnar storage
Parquet
PyArrow
Polars
DuckDB
Parallel processing
Dask
```

Each of these tools helps improve performance in different situations.

However, knowing **when and how to use them** is just as important as understanding how they work.

Large-scale data processing requires thoughtful design.

Poorly designed workflows can cause:

```text id="4tifs0"
slow processing
memory errors
long runtimes
inefficient resource usage
```

Efficient workflows follow a set of **performance best practices**.

These practices help analysts process datasets containing **millions or even billions of rows**.

---

# Key Idea Cards

### Card 1 — Choose the Right Tool for the Job

Different tools are optimized for different dataset sizes and workloads.

---

### Card 2 — Reduce Data Early

Filtering and aggregating early reduces the amount of data that must be processed.

---

### Card 3 — Efficient Storage Improves Performance

Using columnar storage formats dramatically improves large-data workflows.

---

# Key Concepts

## Selecting the Right Tool

Different tools perform better depending on dataset size.

Example guideline:

```text id="2vcyu2"
Small datasets (<1 million rows)
Pandas
```

```text id="xcingi"
Medium datasets (1–10 million rows)
Polars
DuckDB
```

```text id="bqf99g"
Very large datasets (10+ million rows)
Dask
distributed systems
```

Choosing the correct tool improves both performance and reliability.

---

## Use Columnar File Formats

Columnar formats improve performance for analytical queries.

Example formats:

```text id="59zzhx"
Parquet
Arrow
```

Benefits include:

```text id="s22k1w"
smaller file sizes
faster data loading
efficient column selection
```

Many modern data pipelines convert raw CSV files into Parquet.

Example workflow:

```text id="dfd7d4"
CSV → Parquet → Analytics
```

---

## Filter Early

Filtering early reduces the amount of data processed later.

Example dataset:

```text id="l9sdj8"
10 million rows
```

If only one region is needed:

```python id="ba2q51"
df = df[df["region"] == "West"]
```

The dataset may shrink significantly.

Later operations become faster.

---

## Avoid Row-Based Loops

Loops are inefficient when processing large datasets.

Example inefficient workflow:

```python id="u8qg4j"
for index, row in df.iterrows():
    process(row)
```

Instead, use vectorized operations.

Example:

```python id="3lwoch"
df["revenue"] = df["price"] * df["quantity"]
```

Vectorized operations process entire columns efficiently.

---

## Use Efficient Data Types

Memory usage affects performance.

Example improvements:

```text id="z2jx8d"
Convert strings → category
Reduce numeric precision
Use efficient data types
```

These changes reduce memory consumption.

---

## Use Parallel Processing

Parallel processing allows multiple CPU cores to work simultaneously.

Many modern libraries support parallel processing automatically.

Examples include:

```text id="q1wlhj"
Polars
DuckDB
Dask
```

These tools distribute workloads across CPU cores.

---

# Decision Flow

When designing data workflows, follow this general strategy.

```text id="cnyiak"
Start with Pandas
      │
      ▼
Dataset grows
      │
      ▼
Switch to Parquet storage
      │
      ▼
Use faster processing tools
Polars or DuckDB
      │
      ▼
Dataset exceeds memory
      │
      ▼
Use Dask or distributed computing
```

This progression helps workflows scale as datasets grow.

---

# Code Examples

## Example 1 — Efficient Column Calculation

Use vectorized operations instead of loops.

```python id="9cfzlg"
import pandas as pd

df = pd.read_parquet("sales_data.parquet")

df["revenue"] = df["price"] * df["quantity"]
```

This calculation processes entire columns efficiently.

---

## Example 2 — Filtering Early

Filter datasets before performing expensive operations.

```python id="heclnz"
df = df[df["region"] == "West"]

sales_by_product = df.groupby("product")["revenue"].sum()
```

This reduces the number of rows processed.

---

## Example 3 — Querying Large Files with DuckDB

Instead of loading the dataset into Pandas:

```python id="wu1gnw"
import duckdb

result = duckdb.query("""
SELECT region, SUM(price * quantity) AS revenue
FROM 'sales_data.parquet'
GROUP BY region
""")
```

DuckDB processes the dataset directly.

---

## Example 4 — Processing with Polars

Polars provides efficient processing for large datasets.

```python id="m2qmjp"
import polars as pl

df = pl.read_parquet("sales_data.parquet")

result = df.groupby("region").agg(
    pl.col("revenue").sum()
)

print(result)
```

Polars automatically uses parallel processing.

---

# SQL / Excel Comparison

Understanding performance best practices becomes easier when comparing tools.

---

## Excel

Excel is designed for smaller datasets.

Limitations include:

```text id="pblhcg"
1 million row limit
slow calculations
large file sizes
```

Large datasets often require other tools.

---

## SQL Databases

SQL databases are optimized for large datasets.

Example query:

```sql id="2wgm5x"
SELECT region, SUM(revenue)
FROM sales
GROUP BY region;
```

The database engine automatically optimizes query execution.

---

## Python Analytics Stack

Modern Python analytics workflows combine multiple tools.

Example architecture:

```text id="7s3i2w"
Raw Data
↓
Parquet Storage
↓
Processing Engine
Polars / DuckDB
↓
Aggregation
↓
Results
```

This architecture supports large-scale analytics.

---

# Practice Exercises

## Exercise 1 — Identify Best Tool

Tags: Databases, Big Data, Polars, DuckDB

For each dataset size, identify the best tool.

```text id="1yrrta"
100k rows
5 million rows
50 million rows
```

Possible tools:

```text id="zo1s5z"
Pandas
Polars
DuckDB
Dask
```

---

## Exercise 2 — Optimize Workflow

Tags: Performance, Filtering, Aggregations, CI/CD

Given this workflow:

```text id="u0bauq"
Load dataset
Aggregate data
Filter region
```

Rewrite the workflow so filtering happens earlier.

---

## Exercise 3 — Convert CSV to Parquet

Tags: CSV, Parquet, read_csv(), Performance

Convert a CSV dataset to Parquet.

```python id="xzd8ds"
df = pd.read_csv("data.csv")

df.to_parquet("data.parquet")
```

Observe file size differences.

---

# Common Mistakes

## Mistake 1 — Using Pandas for Extremely Large Datasets

Pandas may struggle with very large datasets.

Other tools may be more appropriate.

---

## Mistake 2 — Ignoring File Formats

File format selection can dramatically impact performance.

---

## Mistake 3 — Processing More Data Than Needed

Always reduce datasets early when possible.

---

# Real-World Use

Performance best practices are used in many analytics systems.

Examples include:

---

## Retail Analytics

Analyzing large sales datasets.

---

## Financial Systems

Processing millions of transactions.

---

## Marketing Analytics

Analyzing customer interaction data.

---

## Healthcare Analytics

Processing large claims datasets.

---

Efficient data workflows allow analysts to process large datasets without requiring massive infrastructure.

---

# Lesson Recap

In this lesson you learned:

- best practices for large-scale data processing
- how to select the right tools for different dataset sizes
- why columnar storage improves performance
- how to design efficient analytics workflows

These practices help analysts build **scalable and reliable data workflows**.

---

# Next Lesson

Module 19 is now complete.

In the next module you will begin:

**Module 17 — Automation with Python**

You will learn how to automate data workflows, reporting tasks, and scheduled processes.

---

When you are ready to export this module, you can request the **FINAL EXPORT**.