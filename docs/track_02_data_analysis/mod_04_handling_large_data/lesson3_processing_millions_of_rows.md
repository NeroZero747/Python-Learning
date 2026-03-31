# Module 19 — Large Scale Data Processing  
## Lesson 4 — Processing Millions of Rows

---

# Lesson Objective

By the end of this lesson you will understand:

- What changes when working with **millions of rows**
- How to design workflows that scale to **very large datasets**
- How to avoid common performance bottlenecks
- How to structure large-data processing pipelines

You will learn strategies that allow analysts to work with **datasets containing millions of records** without overwhelming system resources.

---

# Overview

In earlier lessons, we discussed:

- Pandas memory limits  
- chunk processing  
- memory optimization  

These techniques help analysts work with larger datasets.

However, when datasets grow to **millions of rows**, additional challenges appear.

Example dataset:

```text
sales_transactions.csv
```

Dataset size:

```text
25,000,000 rows
12 columns
```

Common operations include:

```text
Filtering rows
Aggregating data
Joining datasets
Creating calculated columns
```

When these operations are applied to millions of rows, performance becomes critical.

Example operation:

```python
df["revenue"] = df["price"] * df["quantity"]
```

This operation must run **25 million times**.

Even simple operations can become expensive.

Processing large datasets efficiently requires **good workflow design**.

---

# Key Idea Cards

### Card 1 — Scale Changes Performance

Operations that run instantly on small datasets may become slow on millions of rows.

---

### Card 2 — Efficient Workflows Matter

Reducing unnecessary computations dramatically improves performance.

---

### Card 3 — Large Data Requires Planning

Large dataset processing requires careful design of:

- memory usage  
- data formats  
- processing strategies  

---

# Key Concepts

## Row-Based Scaling

Many operations scale based on row count.

Example:

```text
1,000 rows → very fast
1,000,000 rows → slower
25,000,000 rows → significantly slower
```

Operations that must iterate through rows can become performance bottlenecks.

---

## Vectorized Operations

One of Pandas’ strengths is **vectorization**.

Vectorized operations apply calculations across entire columns efficiently.

Example:

```python
df["revenue"] = df["price"] * df["quantity"]
```

This operation runs much faster than looping through rows.

Avoid code like this:

```python
for index, row in df.iterrows():
    df.loc[index, "revenue"] = row["price"] * row["quantity"]
```

Row iteration is extremely slow.

---

## Filtering Early

When working with large datasets, filtering early reduces workload.

Example dataset:

```text
20 million rows
```

If we only need data from 2024:

```python
df = df[df["year"] == 2024]
```

Reducing the dataset early improves performance for all later operations.

---

## Avoiding Duplicate Work

Large datasets should be processed **as few times as possible**.

Example inefficient workflow:

```text
Load dataset
Filter dataset
Reload dataset
Aggregate dataset
Reload dataset again
```

Better workflow:

```text
Load dataset once
Perform all operations
Store results
```

---

# Decision Flow

When processing large datasets, follow this workflow.

```text
Dataset loaded
      │
      ▼
Check dataset size
```

If dataset is manageable:

```text
Use optimized Pandas operations
```

If dataset becomes very large:

```text
Apply strategies:
- Filter early
- Use vectorized operations
- Avoid loops
- Process data in chunks
```

If dataset grows further:

```text
Consider specialized tools
Polars
DuckDB
Dask
```

---

# Code Examples

## Example 1 — Vectorized Calculation

Vectorized calculations are efficient.

```python
import pandas as pd

df = pd.read_csv("sales_data.csv")

df["revenue"] = df["price"] * df["quantity"]
```

This processes millions of rows quickly.

---

## Example 2 — Filtering Large Dataset

Filtering reduces dataset size.

```python
df_2024 = df[df["year"] == 2024]
```

Now later operations run faster.

---

## Example 3 — Aggregating Millions of Rows

Aggregations are common with large datasets.

```python
total_revenue = df["revenue"].sum()

print(total_revenue)
```

Grouping operations are also common.

```python
sales_by_region = df.groupby("region")["revenue"].sum()
```

These operations remain efficient when vectorized.

---

## Example 4 — Combining Chunk Processing

If the dataset is extremely large:

```python
import pandas as pd

chunks = pd.read_csv("sales_data.csv", chunksize=100000)

total_revenue = 0

for chunk in chunks:
    total_revenue += (chunk["price"] * chunk["quantity"]).sum()

print(total_revenue)
```

This processes millions of rows incrementally.

---

# SQL / Excel Comparison

Understanding large-scale processing becomes easier when compared to SQL and Excel.

---

## Excel

Excel struggles with large datasets.

Limit:

```text
1,048,576 rows
```

Even approaching this limit causes performance issues.

---

## SQL Databases

SQL engines are designed for large datasets.

Example query:

```sql
SELECT SUM(price * quantity)
FROM sales;
```

The database processes data efficiently using optimized storage.

---

## Pandas

Pandas is powerful but requires efficient workflows.

Example workflow:

```text
Load dataset
Apply vectorized operations
Filter early
Aggregate results
```

This allows Pandas to process millions of rows effectively.

---

# Practice Exercises

## Exercise 1 — Create Calculated Column

Tags: Lists, Arithmetic, Data I/O, Performance

Load a dataset and calculate revenue.

```python
df["revenue"] = df["price"] * df["quantity"]
```

Check performance with large datasets.

---

## Exercise 2 — Filter Dataset

Tags: Filtering, Aggregations, WHERE

Extract only rows where:

```text
country = "USA"
```

Use filtering before performing aggregations.

---

## Exercise 3 — Aggregate by Category

Tags: Aggregations, Lists, groupby(), GROUP BY

Calculate total revenue per region.

```python
df.groupby("region")["revenue"].sum()
```

---

# Common Mistakes

## Mistake 1 — Iterating Through Rows

Using loops such as `iterrows()` dramatically slows performance.

Always prefer vectorized operations.

---

## Mistake 2 — Filtering Too Late

Filtering after expensive operations wastes processing time.

Filter early when possible.

---

## Mistake 3 — Reprocessing Data Multiple Times

Loading and processing the dataset repeatedly increases runtime.

Perform multiple operations within the same workflow.

---

# Real-World Use

Large-scale datasets are common in modern analytics.

Examples include:

---

## Financial Systems

Millions of daily transactions.

---

## Marketing Analytics

Tracking user interactions across websites and campaigns.

---

## Healthcare Data

Analyzing millions of claim records.

---

## E-commerce Platforms

Processing large order and inventory datasets.

---

In these environments, efficient workflows allow analysts to process millions of rows successfully.

---

# Lesson Recap

In this lesson you learned:

- how large datasets affect performance
- why vectorized operations are essential
- how filtering early improves performance
- how chunk processing can scale workflows

These techniques allow analysts to process **millions of rows efficiently**.

---

# Next Lesson

Module 19 — Lesson 5

**Columnar Storage**

You will learn how columnar file formats such as **Parquet** dramatically improve performance when working with large datasets.

---

When you're ready, say:

```
next lesson
```