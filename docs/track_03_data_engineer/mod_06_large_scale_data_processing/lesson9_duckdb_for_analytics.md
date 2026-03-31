# Module 19 — Large Scale Data Processing  
## Lesson 10 — DuckDB for Analytics

---

# Lesson Objective

By the end of this lesson you will understand:

- What **DuckDB** is
- Why DuckDB is useful for **large analytical datasets**
- How DuckDB allows you to run **SQL directly on files**
- How DuckDB integrates with **Pandas, Parquet, and Polars**

You will learn how DuckDB allows analysts to process **millions of rows using SQL directly inside Python**.

---

# Overview

Most analysts are already familiar with **SQL databases**.

Typical workflow:

```text id="ufjzz0"
Database
↓
SQL Query
↓
Results
```

However, traditional databases require:

```text id="x8m874"
Database server
Data loading
Infrastructure
```

DuckDB is different.

DuckDB is an **embedded analytics database**.

This means it runs **directly inside your Python environment**.

Example workflow:

```text id="iz7q43"
CSV / Parquet File
↓
DuckDB SQL Query
↓
Results returned to Python
```

DuckDB is optimized for **analytical workloads** and works especially well with:

```text id="gi1is2"
Parquet files
large datasets
columnar data
```

Many analysts now use DuckDB as a lightweight analytics engine.

---

# Key Idea Cards

### Card 1 — DuckDB Is an Embedded Analytics Database

DuckDB runs directly inside Python without requiring a separate server.

---

### Card 2 — DuckDB Uses SQL for Large Datasets

DuckDB allows analysts to run SQL queries directly on files.

---

### Card 3 — DuckDB Works Well with Parquet and Arrow

DuckDB integrates with modern columnar data formats for fast analytics.

---

# Key Concepts

## Embedded Database

DuckDB is an **embedded database engine**.

This means the database runs inside the application instead of as a separate server.

Example comparison:

```text id="xzxhsm"
PostgreSQL
Requires database server
```

```text id="jm94lt"
DuckDB
Runs directly inside Python
```

This makes DuckDB extremely easy to use.

---

## Querying Files Directly

One of DuckDB’s most powerful features is the ability to run SQL directly on files.

Example:

```text id="0jb2v9"
sales.parquet
```

Instead of loading the dataset into Pandas first, DuckDB can query the file directly.

Example workflow:

```text id="lj6obo"
Parquet file
↓
DuckDB SQL query
↓
Results
```

This avoids loading large datasets into memory.

---

## Columnar Processing

DuckDB is optimized for columnar storage formats such as:

```text id="mi0qr1"
Parquet
Arrow
```

When executing a query like:

```text id="1okuui"
SUM(revenue)
```

DuckDB reads only the **revenue column**.

This dramatically improves performance.

---

# Decision Flow

Choose DuckDB when working with large analytical datasets.

```text id="z0akjl"
Dataset small (<1M rows)
        │
        ▼
Pandas may be sufficient
```

If dataset becomes larger:

```text id="c0eedj"
Dataset several million rows
        │
        ▼
Consider DuckDB
```

DuckDB is especially useful when:

```text id="teonfi"
Running SQL queries
Working with Parquet files
Processing large datasets
```

---

# Code Examples

## Example 1 — Installing DuckDB

Install DuckDB using pip.

```python id="dtxsud"
pip install duckdb
```

---

## Example 2 — Running SQL in Python

DuckDB allows SQL queries directly in Python.

```python id="m55q4d"
import duckdb

result = duckdb.query("""
SELECT 1 + 1
""")

print(result)
```

This demonstrates basic SQL execution.

---

## Example 3 — Querying a CSV File

DuckDB can query CSV files directly.

```python id="6fg8vd"
import duckdb

result = duckdb.query("""
SELECT *
FROM 'sales_data.csv'
LIMIT 5
""")

print(result)
```

DuckDB reads the file automatically.

---

## Example 4 — Querying a Parquet File

DuckDB works extremely well with Parquet.

```python id="n5y837"
import duckdb

result = duckdb.query("""
SELECT region, SUM(revenue)
FROM 'sales_data.parquet'
GROUP BY region
""")

print(result)
```

This processes the dataset without loading it into Pandas.

---

## Example 5 — Returning Results to Pandas

DuckDB queries can return results as Pandas DataFrames.

```python id="asp3vn"
import duckdb

df = duckdb.query("""
SELECT *
FROM 'sales_data.parquet'
LIMIT 10
""").to_df()

print(df.head())
```

This integrates DuckDB with Pandas workflows.

---

# SQL / Excel Comparison

Understanding DuckDB becomes easier when compared with SQL and Excel.

---

## Excel

Excel struggles with large datasets.

Large files can cause:

```text id="5t5zdb"
Slow calculations
Crashes
Memory issues
```

Excel is not designed for large-scale analytics.

---

## Traditional SQL Databases

SQL databases process queries efficiently.

Example:

```sql id="xqj0rh"
SELECT region, SUM(revenue)
FROM sales
GROUP BY region;
```

However, they require infrastructure and data loading.

---

## DuckDB

DuckDB combines SQL capabilities with Python flexibility.

Example workflow:

```text id="zx2rbb"
Parquet file
↓
DuckDB SQL query
↓
Results
```

This allows analysts to perform SQL analytics directly on files.

---

# Practice Exercises

## Exercise 1 — Install DuckDB

Tags: Installation, DuckDB, Databases, pip install

Install the DuckDB package.

```python id="9mhvf0"
pip install duckdb
```

---

## Exercise 2 — Query CSV File

Tags: File I/O, Databases, SELECT, SQL Queries

Run a SQL query on a CSV file.

```python id="mbafl7"
SELECT COUNT(*)
FROM 'sales_data.csv'
```

---

## Exercise 3 — Aggregate Parquet Dataset

Tags: Parquet, Aggregations, SELECT, GROUP BY

Calculate revenue by region using SQL.

```sql id="sya9cp"
SELECT region, SUM(revenue)
FROM 'sales_data.parquet'
GROUP BY region
```

---

# Common Mistakes

## Mistake 1 — Loading Large Files into Pandas First

DuckDB can query files directly without loading them into memory.

---

## Mistake 2 — Ignoring Parquet Performance Benefits

DuckDB works best with columnar formats such as Parquet.

---

## Mistake 3 — Treating DuckDB Like a Traditional Database

DuckDB is designed for analytical workloads rather than transactional systems.

---

# Real-World Use

DuckDB is widely used in modern analytics workflows.

Examples include:

---

## Data Analytics

Analysts use DuckDB to run SQL queries on large datasets locally.

---

## Data Science

DuckDB allows data scientists to explore large datasets efficiently.

---

## ETL Pipelines

Data engineers use DuckDB to process large Parquet datasets.

---

## Business Intelligence

DuckDB can power lightweight analytics workflows without requiring full database infrastructure.

---

Many modern data stacks combine:

```text id="q71u5a"
DuckDB
Polars
Parquet
```

to create fast and efficient analytics pipelines.

---

# Lesson Recap

In this lesson you learned:

- what DuckDB is
- how DuckDB runs SQL inside Python
- how DuckDB queries files directly
- how DuckDB integrates with modern data formats

DuckDB allows analysts to run powerful SQL queries on large datasets without needing a full database system.

---

# Next Lesson

Module 19 — Lesson 11

**Parallel Processing**

You will learn how parallel processing allows Python to use multiple CPU cores to speed up large data operations.

---

When you're ready, say:

```text id="zsyil2"
next lesson
```