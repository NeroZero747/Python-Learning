# Module 7 — Data Engineering Foundations

# Lesson 6 — Intro to Polars (Optional)

---

# Lesson Objective

By the end of this lesson learners will understand:

• what **Polars** is  
• why Polars can be faster than pandas  
• how Polars processes data differently from pandas  
• when Polars is useful for large datasets  

Polars is becoming popular in data engineering because it is designed for **high-performance data processing and large-scale analytics**.

---

# Overview

Many Python data workflows use **pandas** for data manipulation.

Example pandas workflow:

```python
import pandas as pd

data = pd.read_csv("sales.csv")

data["total"] = data["price"] * data["quantity"]
```

Pandas works well for many tasks, but it has limitations when working with **very large datasets**.

Some common challenges include:

• slower performance on large datasets  
• high memory usage  
• limited parallel processing  

To solve these issues, new libraries have been developed.

One of the most popular alternatives is **Polars**.

Polars is a **high-performance DataFrame library written in Rust** and designed for:

• faster computation  
• efficient memory usage  
• parallel processing.

Polars uses a **columnar execution engine**, similar to modern analytics systems.

Example Polars workflow:

```python
import polars as pl

data = pl.read_csv("sales.csv")

data = data.with_columns(
    (pl.col("price") * pl.col("quantity")).alias("total")
)
```

Polars performs operations very efficiently, especially for large datasets.

---

# Key Idea Cards (3 Cards)

## Polars Is Built for Performance

Polars is designed to process large datasets quickly.

It achieves this through:

• a Rust-based engine  
• efficient memory usage  
• multi-threaded execution.

These features allow Polars to process data faster than pandas in many scenarios.

---

## Polars Uses Columnar Execution

Polars processes data column by column rather than row by row.

Example structure:

```text
price column → processed together
quantity column → processed together
```

This improves performance for analytics operations.

---

## Polars Supports Parallel Processing

Polars automatically uses multiple CPU cores.

Example:

```text
CPU Core 1 → process data chunk
CPU Core 2 → process data chunk
CPU Core 3 → process data chunk
```

This allows large datasets to be processed more efficiently.

---

# Key Concepts

## DataFrame Libraries

Both pandas and Polars provide **DataFrame structures**.

A DataFrame is a table-like structure used to store and manipulate data.

Example structure:

```text
order_id | price | quantity
```

---

## Lazy Execution

Polars supports **lazy execution**, which means operations are optimized before execution.

Example concept:

```text
Define transformations
        ↓
Polars optimizes execution
        ↓
Execute efficiently
```

This allows Polars to run complex transformations efficiently.

---

## Arrow-Based Memory

Polars uses the **Apache Arrow memory format**.

Arrow provides:

• efficient columnar storage  
• fast data transfers  
• compatibility with analytics tools.

---

# Decision Flow

Choosing between pandas and Polars often follows this logic:

```text
Dataset small to medium?
        ↓
      YES
        ↓
     Use pandas

Dataset very large?
        ↓
      YES
        ↓
     Consider Polars
```

Polars becomes especially useful when processing **millions or hundreds of millions of rows**.

---

# Code Examples

## Example 1 — Reading Data with Polars

```python
import polars as pl

data = pl.read_csv("orders.csv")
```

This loads a dataset into a Polars DataFrame.

---

## Example 2 — Creating a Calculated Column

```python
data = data.with_columns(
    (pl.col("price") * pl.col("quantity")).alias("total")
)
```

This creates a new column called `total`.

---

## Example 3 — Filtering Data

```python
filtered = data.filter(
    pl.col("price") > 50
)
```

This returns rows where price is greater than 50.

---

## Example 4 — Aggregation

```python
summary = data.group_by("product").agg(
    pl.col("total").sum()
)
```

This calculates totals by product.

---

# SQL / Excel Comparison

Polars operations resemble familiar data operations.

| Concept | Polars | SQL | Excel |
|------|------|------|------|
| filtering | filter() | WHERE | filter |
| aggregation | group_by().agg() | GROUP BY | pivot table |
| calculated column | with_columns() | SELECT expression | formula |

Example SQL equivalent:

```sql
SELECT product,
       SUM(price * quantity)
FROM sales
GROUP BY product
```

Polars performs similar operations programmatically.

---

# Practice Exercises

## Exercise 1

Tags: Imports, read_csv(), CSV, Polars

Load a dataset using Polars.

```python
import polars as pl

data = pl.read_csv("orders.csv")
```

---

## Exercise 2

Tags: Arithmetic, Polars

Create a calculated column.

```python
data = data.with_columns(
    (pl.col("price") * pl.col("quantity")).alias("total")
)
```

---

## Exercise 3

Tags: Aggregations, GROUP BY, Polars

Aggregate totals by product.

```python
data.group_by("product").agg(
    pl.col("total").sum()
)
```

---

# Common Mistakes

## Mixing pandas and Polars Syntax

Pandas:

```python
data["total"] = data["price"] * data["quantity"]
```

Polars:

```python
data = data.with_columns(
    (pl.col("price") * pl.col("quantity")).alias("total")
)
```

The syntax is different.

---

## Converting Too Frequently Between Libraries

Repeated conversions between pandas and Polars can reduce performance.

Best practice:

```text
Choose one library per pipeline
```

---

## Using Polars for Very Small Datasets

For small datasets, pandas may be simpler and easier.

Polars provides the most benefit with **large datasets**.

---

# Real-World Use

Polars is increasingly used in modern data engineering pipelines.

Examples include:

• large-scale ETL processing  
• analytics pipelines  
• machine learning preprocessing  
• high-performance data transformations.

Example pipeline:

```text
Raw CSV Data
      ↓
Polars Transformation
      ↓
Parquet Storage
      ↓
Data Warehouse
```

This approach allows pipelines to process large datasets efficiently.

---

# Lesson Recap

In this lesson you learned:

• what Polars is  
• how Polars differs from pandas  
• why Polars is useful for large datasets  
• how to perform basic operations using Polars  

Polars is a powerful tool for **high-performance data processing in modern Python pipelines**.

---

# Next Lesson

Next we will learn:

# Lesson 7 — Pipeline Design Concepts

You will learn:

• how data pipelines are structured  
• common pipeline architecture patterns  
• best practices for reliable data workflows.
