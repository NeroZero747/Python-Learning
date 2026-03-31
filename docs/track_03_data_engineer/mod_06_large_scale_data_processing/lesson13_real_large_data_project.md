# Module 19 — Large Scale Data Processing  
## Lesson 14 — Real Large Data Project

---

# Lesson Objective

By the end of this lesson you will:

- Apply techniques for processing **large datasets**
- Use tools such as **Parquet, Polars, and DuckDB**
- Build a workflow capable of processing **millions of rows efficiently**
- Understand how real-world analytics pipelines handle large data

This lesson combines concepts from the entire module into a **realistic data processing workflow**.

---

# Overview

Throughout this module you learned several techniques for handling large datasets:

```text id="9cpi8n"
Chunk processing
Memory optimization
Columnar storage
Parquet files
PyArrow
Polars
DuckDB
Parallel processing
Dask
```

In real-world environments, these tools are often combined into a single workflow.

Typical large-data pipeline:

```text id="m2mhdg"
Raw data files
↓
Efficient storage format
↓
Fast processing engine
↓
Aggregation and analysis
↓
Results for reporting
```

In this project we will simulate processing a **large sales dataset**.

Example dataset:

```text id="ca9n99"
sales_transactions.parquet
```

Dataset characteristics:

```text id="r4k2n8"
10 million rows
multiple regions
multiple product categories
transaction-level data
```

The goal of the project is to answer analytical questions such as:

```text id="zzyzdl"
Total revenue
Revenue by region
Top selling products
Monthly sales trends
```

---

# Key Idea Cards

### Card 1 — Large Data Requires Efficient Tools

Large datasets should use modern tools such as Parquet, Polars, and DuckDB.

---

### Card 2 — Data Pipelines Combine Multiple Technologies

Real workflows combine storage formats, query engines, and processing libraries.

---

### Card 3 — Analytical Workflows Focus on Aggregations

Large datasets are often summarized into smaller analytical results.

---

# Key Concepts

## Step 1 — Efficient Storage Format

Large datasets should be stored using **columnar formats**.

Example:

```text id="h2ee9u"
CSV → inefficient
Parquet → optimized
```

Benefits:

```text id="mdt39s"
smaller file sizes
faster read speeds
column selection
```

---

## Step 2 — Efficient Query Engine

Instead of loading datasets entirely into Pandas, analytical engines can query files directly.

Examples:

```text id="yxbcv9"
DuckDB
Polars
```

These tools allow analysts to process millions of rows efficiently.

---

## Step 3 — Aggregation

Large datasets are often summarized.

Example metrics:

```text id="bpyav9"
total revenue
revenue by region
sales by product
```

Aggregation dramatically reduces dataset size.

Example:

```text id="2khzt0"
10 million rows
↓
10 summary rows
```

---

# Decision Flow

Large dataset workflows often follow this pattern.

```text id="3jtibo"
Raw dataset
      │
      ▼
Store in Parquet
      │
      ▼
Use analytical engine
      │
      ▼
Aggregate results
      │
      ▼
Produce analytics output
```

Tools used in each step:

```text id="xjqle4"
Storage → Parquet
Processing → Polars / DuckDB
Analysis → Python / SQL
```

---

# Code Examples

## Example 1 — Loading Dataset with Polars

```python id="y6ec8u"
import polars as pl

df = pl.read_parquet("sales_transactions.parquet")

print(df.head())
```

Polars reads Parquet efficiently.

---

## Example 2 — Calculating Revenue

Create a calculated column.

```python id="jn4yzs"
df = df.with_columns(
    (pl.col("price") * pl.col("quantity")).alias("revenue")
)
```

This calculates revenue for each transaction.

---

## Example 3 — Aggregating by Region

Calculate revenue by region.

```python id="ubxto4"
sales_by_region = df.groupby("region").agg(
    pl.col("revenue").sum()
)

print(sales_by_region)
```

---

## Example 4 — Running SQL with DuckDB

DuckDB allows SQL queries directly on Parquet files.

```python id="uuq4cg"
import duckdb

result = duckdb.query("""
SELECT region, SUM(price * quantity) AS revenue
FROM 'sales_transactions.parquet'
GROUP BY region
""")

print(result)
```

This query processes millions of rows efficiently.

---

## Example 5 — Finding Top Products

Using Polars:

```python id="ogqd0f"
top_products = df.groupby("product").agg(
    pl.col("revenue").sum()
).sort("revenue", descending=True)

print(top_products.head())
```

This identifies the highest revenue products.

---

# SQL / Excel Comparison

Understanding this workflow is easier when comparing tools.

---

## Excel

Excel struggles with large datasets.

Example limitations:

```text id="1b1oex"
1 million row limit
slow calculations
large file sizes
```

Excel is best suited for small datasets.

---

## SQL Databases

SQL databases process large datasets efficiently.

Example query:

```sql id="q3dgtj"
SELECT region, SUM(price * quantity)
FROM sales
GROUP BY region;
```

However, SQL databases require data to be loaded into the system.

---

## Python Analytics Workflow

Modern Python tools allow analytics directly on files.

Example workflow:

```text id="kmc5sc"
Parquet dataset
↓
Polars processing
↓
DuckDB SQL queries
↓
Aggregated results
```

This allows analysts to process large datasets locally.

---

# Practice Exercises

## Exercise 1 — Calculate Revenue

Tags: Arithmetic, Parquet, Polars, Data I/O

Load a Parquet dataset and calculate revenue.

```python id="p00ptj"
df = pl.read_parquet("sales.parquet")
```

Create a calculated column:

```python id="sqx1qp"
revenue = price * quantity
```

---

## Exercise 2 — Aggregate by Region

Tags: Aggregations, HTTP Methods, Arithmetic

Calculate total revenue by region.

Example output:

```text id="3matfw"
Region | Revenue
West   | 5,200,000
East   | 3,100,000
South  | 2,800,000
```

---

## Exercise 3 — Identify Top Products

Tags: Sorting, Big Data

Find the five products with the highest revenue.

Use grouping and sorting operations.

---

# Common Mistakes

## Mistake 1 — Loading Large Data into Pandas

Large datasets should use optimized tools.

---

## Mistake 2 — Using CSV Instead of Parquet

CSV files are inefficient for large datasets.

---

## Mistake 3 — Ignoring Aggregation

Large datasets should be summarized early to reduce complexity.

---

# Real-World Use

Large data workflows are common across industries.

Examples include:

---

## Retail Analytics

Analyzing millions of sales transactions.

---

## Marketing Analytics

Processing large customer interaction datasets.

---

## Financial Systems

Analyzing transaction histories.

---

## Healthcare Data

Processing large claims datasets.

---

Modern analytics workflows frequently combine:

```text id="gu6r4y"
Parquet
Polars
DuckDB
```

to build high-performance data pipelines.

---

# Lesson Recap

In this lesson you learned:

- how large datasets are processed in real analytics workflows
- how tools like Parquet, Polars, and DuckDB work together
- how to aggregate large datasets efficiently
- how to design scalable analytics pipelines

This project demonstrates how analysts can process **millions of rows efficiently** using modern Python data tools.

---

# Next Lesson

Module 19 — Lesson 15

**Performance Best Practices**

You will learn best practices for designing **efficient large-scale data workflows**.

---

When you're ready, say:

``` id="8sq5nh"
next lesson
```