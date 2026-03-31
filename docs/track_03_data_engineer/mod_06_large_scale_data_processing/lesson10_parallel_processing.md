# Module 19 — Large Scale Data Processing  
## Lesson 11 — Parallel Processing

---

# Lesson Objective

By the end of this lesson you will understand:

- What **parallel processing** is
- Why parallel processing improves performance
- How modern data tools use **multiple CPU cores**
- How parallel processing helps process **large datasets faster**

You will learn how parallel processing allows data workflows to **scale to millions of records efficiently**.

---

# Overview

Most beginner Python programs run in a **single-threaded mode**.

This means the program executes tasks **one step at a time**.

Example:

```text id="8o7g4b"
Read file
Process data
Calculate totals
Write results
```

Each step must complete before the next begins.

This is called **sequential processing**.

Sequential processing works well for small datasets.

However, when datasets grow larger, sequential workflows become slow.

Example:

```text id="8usvh5"
Processing 10 million rows
```

If every operation runs on a single CPU core, processing may take a long time.

Modern computers contain **multiple CPU cores**.

Example laptop:

```text id="un2ewn"
4 cores
8 cores
16 cores
```

Parallel processing allows software to use **multiple cores at the same time**.

Example workflow:

```text id="1supks"
Dataset
│
├ Core 1 → Process part of dataset
├ Core 2 → Process part of dataset
├ Core 3 → Process part of dataset
└ Core 4 → Process part of dataset
```

This dramatically improves performance for large workloads.

---

# Key Idea Cards

### Card 1 — Sequential vs Parallel Processing

Sequential processing uses one CPU core, while parallel processing uses multiple cores simultaneously.

---

### Card 2 — Large Datasets Benefit from Parallelism

Processing large datasets becomes much faster when work is divided across multiple processors.

---

### Card 3 — Modern Data Tools Use Parallel Execution

Libraries such as **Polars, DuckDB, and Dask** automatically use parallel processing.

---

# Key Concepts

## Sequential Processing

Traditional Python scripts execute sequentially.

Example:

```python id="9x7kzp"
for value in data:
    process(value)
```

Each iteration runs one after another.

This approach works but may be slow for large datasets.

---

## Parallel Processing

Parallel processing divides a task into multiple pieces.

Each piece is processed by a different CPU core.

Example concept:

```text id="wpoiyp"
Large dataset
↓
Split into segments
↓
Process segments simultaneously
```

This reduces total processing time.

---

## CPU Cores

Modern processors contain multiple cores.

Example system:

```text id="b70ghz"
CPU
│
├ Core 1
├ Core 2
├ Core 3
└ Core 4
```

Parallel programs assign tasks to each core.

---

## Parallelism in Data Tools

Many modern analytics tools use parallel processing automatically.

Examples:

```text id="41b4gh"
Polars
DuckDB
Spark
Dask
```

These tools distribute work across multiple CPU cores.

Example operation:

```text id="u098ej"
GROUP BY region
```

Instead of processing sequentially, the workload can be distributed across cores.

---

# Decision Flow

Determine when parallel processing is useful.

```text id="34jvzv"
Small dataset
      │
      ▼
Sequential processing acceptable
```

If datasets grow larger:

```text id="pqyl6d"
Large dataset
      │
      ▼
Parallel processing recommended
```

Parallel tools help when:

```text id="byqafi"
processing millions of rows
running heavy aggregations
processing large files
```

---

# Code Examples

## Example 1 — Sequential Processing

Basic sequential workflow.

```python id="avseix"
data = [1,2,3,4,5]

results = []

for value in data:
    results.append(value * 2)

print(results)
```

Each element is processed one at a time.

---

## Example 2 — Parallel Processing Concept

Parallel processing divides the workload.

Example conceptual workflow:

```text id="fu2fiz"
Dataset
↓
Split into chunks
↓
Process chunks in parallel
```

This approach reduces runtime.

---

## Example 3 — Polars Parallel Execution

Polars uses parallel processing automatically.

```python id="jqqblw"
import polars as pl

df = pl.read_csv("sales_data.csv")

result = df.groupby("region").agg(
    pl.col("revenue").sum()
)

print(result)
```

Polars distributes work across CPU cores automatically.

---

## Example 4 — DuckDB Parallel Queries

DuckDB also performs parallel processing.

```python id="8aneyd"
import duckdb

result = duckdb.query("""
SELECT region, SUM(revenue)
FROM 'sales_data.parquet'
GROUP BY region
""")

print(result)
```

DuckDB uses multiple cores for query execution.

---

# SQL / Excel Comparison

Understanding parallel processing becomes easier when comparing tools.

---

## Excel

Excel performs calculations mostly sequentially.

Large calculations can become slow.

---

## SQL Databases

Modern database engines perform many operations in parallel.

Example:

```sql id="kvxlri"
SELECT region, SUM(revenue)
FROM sales
GROUP BY region;
```

The database engine distributes work across CPU cores.

---

## Python Data Tools

Modern Python libraries increasingly use parallel processing.

Examples include:

```text id="lqonzc"
Polars
DuckDB
Dask
```

These tools allow Python workflows to scale to large datasets.

---

# Practice Exercises

## Exercise 1 — Identify Parallel Tools

Tags: Concurrency, Databases, Big Data, Polars

Which tools from this module support parallel processing?

```text id="oizwrw"
Pandas
Polars
DuckDB
Dask
```

---

## Exercise 2 — Analyze Workflow

Tags: Context Managers, Filtering, Aggregations, Sorting

Consider a dataset with:

```text id="wpr0nv"
20 million rows
```

Identify which operations would benefit from parallel processing.

Examples:

```text id="a9yhep"
Aggregation
Filtering
Sorting
```

---

## Exercise 3 — Compare Tools

Tags: Databases, Concurrency, Automation, Polars

Research which tool in this module performs parallel processing automatically.

Examples include:

```text id="l353kc"
Polars
DuckDB
```

---

# Common Mistakes

## Mistake 1 — Assuming Python Is Always Slow

Many Python tools achieve high performance through parallel processing.

---

## Mistake 2 — Writing Manual Loops

Loops often prevent parallel optimization.

Vectorized or library-based operations are usually faster.

---

## Mistake 3 — Ignoring Hardware Capabilities

Modern CPUs have multiple cores that can accelerate data processing.

---

# Real-World Use

Parallel processing is widely used in modern analytics systems.

Examples include:

---

## Financial Systems

Processing millions of transactions quickly.

---

## Web Analytics

Analyzing large event logs.

---

## Marketing Analytics

Aggregating customer interaction data.

---

## Machine Learning

Preparing large training datasets.

---

Parallel processing enables modern data workflows to scale efficiently.

---

# Lesson Recap

In this lesson you learned:

- what parallel processing is
- how multiple CPU cores improve performance
- how modern data tools distribute workloads
- why parallel execution is important for large datasets

Parallel processing is a critical component of modern large-scale analytics.

---

# Next Lesson

Module 19 — Lesson 12

**Dask Basics**

You will learn how Dask enables Python to process **datasets that exceed memory limits** and scale across multiple machines.

---

When you're ready, say:

``` id="xygx97"
next lesson
```