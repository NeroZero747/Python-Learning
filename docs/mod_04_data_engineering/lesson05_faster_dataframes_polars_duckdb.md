# Lesson 05 — Faster DataFrames: Polars & DuckDB

**Track:** Data Engineering for Analysts  
**Module:** Module 2 — Modern Data Tools  
**Difficulty:** Intermediate | **Duration:** 12 min  
**Sources:** M1-L06 (Intro to Polars) · M5-L08 (Introduction to Polars — merged) · M5-L09 (Faster DataFrames with Polars) · M5-L10 (DuckDB for Analytics)

---

## Learning Objectives

1. **Understand pandas limitations** — Explain why pandas is single-threaded and what that means at scale.
2. **Polars basics** — Write basic Polars expressions using the lazy API and understand why it's faster.
3. **DuckDB basics** — Run SQL queries directly on CSV and Parquet files without loading them into a DataFrame.
4. **Choose the right tool** — Know when to reach for pandas, Polars, or DuckDB based on your task.

> By the end of this lesson you'll have two faster alternatives to pandas in your toolkit and know when each one is the right choice.

---

## Overview

### Hook
Pandas is the analyst's trusted workhorse — but it was designed for single-threaded operation on in-memory data. When datasets grow to tens of millions of rows, pandas gets slow. Polars and DuckDB were built from the ground up to use every core your machine has.

### Analogy: The Single Cashier vs the Self-Checkout Bank
Think of processing data like checking out at a supermarket. **Pandas** is like a single fast cashier — great for your regular shop, but one person scanning every item. **Polars** is like a bank of self-checkout machines running simultaneously — each item group moves through a different machine at the same time. **DuckDB** is like the store's back-office system that already knows every price — you hand it a query and it finds the answer in the indexed catalog without moving stock to the front first.

| Tool | Supermarket Analogy |
|------|-------------------|
| **Pandas** | One cashier — reliable, familiar, does the job |
| **Polars** | Bank of self-checkouts — parallel, fast, modern |
| **DuckDB** | Back-office lookup system — SQL on data where it sits |

> **Key takeaway:** You don't need to replace pandas everywhere. Use Polars when you process DataFrames with millions of rows. Use DuckDB when you want to query large files with SQL without loading them first.

---

## Key Takeaways

### 1. Polars Uses All Your CPU Cores by Default
Pandas operations run on a single thread. Polars operations run in parallel across all available CPU cores, and its lazy evaluation engine reorders and optimizes operations before executing any of them. On a 4-core laptop, a complex Polars query on 10 million rows often runs 5–20× faster than the equivalent pandas code.  
**Keywords:** Multi-threaded · Lazy evaluation · Query optimization

### 2. Polars Lazy Mode — Build First, Execute Once
In lazy mode, Polars builds a query plan without running anything. When you call `.collect()`, it executes the optimized plan. This is similar to how a database query optimizer works — dead columns are dropped, filters are pushed down, unnecessary steps are eliminated.  
**Keywords:** lf = pl.scan_csv() · .collect() · Query plan

### 3. DuckDB Is SQL on Files
DuckDB is an embedded database engine (no server needed — it runs in your Python process) that can query Parquet, CSV, and DataFrames using standard SQL. It reads files lazily, pushes predicates to the storage layer, and returns results as you need them. For analysts who think in SQL, DuckDB is often the fastest path to an answer on a large file.  
**Keywords:** Embedded DB · SQL on files · No server · Zero-copy pandas integration

---

## Key Concepts

### Pandas vs Polars Syntax Comparison
```python
import pandas as pd
import polars as pl

# Pandas — eager, single-threaded
df_pd = pd.read_csv("sales.csv")
result_pd = (
    df_pd[df_pd["amount"] > 100]
         .groupby("region")["amount"]
         .sum()
         .reset_index()
)

# Polars — lazy, multi-threaded (lf = LazyFrame)
result_pl = (
    pl.scan_csv("sales.csv")               # lazy read — nothing executed yet
      .filter(pl.col("amount") > 100)       # add filter to plan
      .group_by("region")                   # add groupby to plan
      .agg(pl.col("amount").sum())          # add aggregation to plan
      .collect()                             # NOW execute the optimized plan
)
```

### Polars Core Concepts
| Term | Meaning |
|------|---------|
| `DataFrame` | Eager dataframe — runs immediately, like pandas |
| `LazyFrame` | Lazy query plan — runs when `.collect()` is called |
| `pl.scan_csv()` | Lazy CSV reader — file is read lazily |
| `pl.scan_parquet()` | Lazy Parquet reader — column selection and filter pushed to file |
| `pl.col("name")` | Column expression — the main way to reference columns in Polars |
| `.collect()` | Execute the lazy query plan and return a DataFrame |

### DuckDB Basics
```python
import duckdb

# No server setup — just import and query
con = duckdb.connect()   # in-memory database

# Query a CSV file directly — no pandas needed
result = con.execute("""
    SELECT region, SUM(amount) AS total
    FROM 'sales.csv'
    WHERE amount > 100
    GROUP BY region
    ORDER BY total DESC
""").fetchdf()    # returns a pandas DataFrame

# Query a Parquet file — uses columnar skipping automatically
result = con.execute("""
    SELECT * FROM 'sales.parquet'
    WHERE year = 2024 AND region = 'EMEA'
""").fetchdf()
```

---

## Code Examples

### Example 1: Polars vs pandas — benchmark on 5 million rows
```python
import pandas as pd
import polars as pl
import time

# ── Pandas ────────────────────────────────────────────────
t0 = time.perf_counter()
df = pd.read_csv("sales_5m.csv")
result = (df[df["amount"] > 500]
            .groupby("region")["amount"]
            .agg(["sum", "mean", "count"]))
pd_time = time.perf_counter() - t0

# ── Polars lazy ───────────────────────────────────────────
t0 = time.perf_counter()
result = (
    pl.scan_csv("sales_5m.csv")
      .filter(pl.col("amount") > 500)
      .group_by("region")
      .agg([
          pl.col("amount").sum().alias("sum"),
          pl.col("amount").mean().alias("mean"),
          pl.col("amount").count().alias("count"),
      ])
      .collect()
)
pl_time = time.perf_counter() - t0

print(f"Pandas: {pd_time:.2f}s  |  Polars: {pl_time:.2f}s  |  Speedup: {pd_time/pl_time:.1f}x")
```
**Terminal output:**
```
Pandas: 18.4s  |  Polars: 1.9s  |  Speedup: 9.7x
```

### Example 2: Polars with multiple transformations
```python
import polars as pl

result = (
    pl.scan_parquet("orders.parquet")
      .filter(pl.col("status") == "completed")
      .with_columns([
          (pl.col("amount") * 1.1).alias("amount_with_tax"),      # new column
          pl.col("order_date").str.to_date().alias("order_date"),  # parse date
      ])
      .group_by(["region", pl.col("order_date").dt.year().alias("year")])
      .agg([
          pl.col("amount_with_tax").sum().alias("total_revenue"),
          pl.col("order_id").n_unique().alias("order_count"),
      ])
      .sort("total_revenue", descending=True)
      .collect()
)

print(result.head(10))
```

### Example 3: DuckDB querying multiple files
```python
import duckdb

con = duckdb.connect()

# DuckDB can read multiple Parquet files at once with a wildcard
result = con.execute("""
    SELECT
        year,
        region,
        SUM(amount) AS total_revenue,
        COUNT(*)    AS order_count,
        AVG(amount) AS avg_order_value
    FROM 'sales_partitioned/year=*/region=*/*.parquet'
    WHERE year >= 2023
    GROUP BY year, region
    ORDER BY year, total_revenue DESC
""").fetchdf()

print(result)
```

### Example 4: DuckDB with pandas zero-copy integration
```python
import pandas as pd
import duckdb

# You can query an existing pandas DataFrame with SQL — no copy needed
df = pd.read_csv("customers.csv")

result = duckdb.query("""
    SELECT
        region,
        COUNT(*) AS customer_count,
        AVG(lifetime_value) AS avg_ltv
    FROM df          -- references the 'df' variable directly
    GROUP BY region
    ORDER BY avg_ltv DESC
""").to_df()

print(result)
```

---

## Common Mistakes

### Mistake 1: Using Polars eager mode and losing the speed benefit
```python
# WRONG — pl.read_csv() is eager (executes immediately, like pandas)
df = pl.read_csv("huge.csv")           # loads entire file now
result = df.filter(pl.col("x") > 100)

# RIGHT — pl.scan_csv() is lazy (builds plan, executes at .collect())
result = (
    pl.scan_csv("huge.csv")            # nothing read yet
      .filter(pl.col("x") > 100)
      .collect()                         # reads only what passes the filter
)
```

### Mistake 2: Calling .collect() repeatedly instead of storing the result
```python
# WRONG — executes the query 3 times
lf = pl.scan_csv("data.csv").filter(pl.col("x") > 0)
print(lf.collect().shape)
print(lf.collect().head())
print(lf.collect()["x"].mean())

# RIGHT — collect once, use the result
df = lf.collect()
print(df.shape)
print(df.head())
print(df["x"].mean())
```

### Mistake 3: Installing DuckDB when you just need pandas for small data
```python
# Overkill for 10,000 rows — pandas is fine here
con = duckdb.connect()
result = con.execute("SELECT SUM(amount) FROM 'tiny.csv'").fetchdf()

# Right tool for small data
result = pd.read_csv("tiny.csv")["amount"].sum()
```
Use DuckDB and Polars when your data is large enough that the overhead of learning the API is less than the time pandas wastes.

---

## Practice Exercises

### Exercise 1 — Polars filter and aggregate
```python
import polars as pl

# TODO: Using lazy mode (scan_csv), on "orders.csv":
# 1. Filter to rows where status == "shipped"
# 2. Group by "product_category"
# 3. Aggregate: sum of "revenue" and count of "order_id"
# 4. Sort by sum of revenue descending
# 5. collect() and print the result
```

### Exercise 2 — DuckDB SQL on a file
```python
import duckdb

# TODO: Using DuckDB, query "sales.parquet" to find:
# - The top 5 regions by total revenue
# - Only include rows from 2024 onwards
# - Return a pandas DataFrame using .fetchdf()
```

### Exercise 3 — Speedup comparison
```python
# TODO: Write the same query in both pandas and Polars:
# - Read "large_data.csv"
# - Filter rows where "score" > 75
# - Calculate mean of "value" grouped by "category"
# Measure and print both execution times and the speedup ratio
```

---

## Lesson Recap

1. **Polars** is a multi-threaded DataFrame library with a lazy evaluation engine — it automatically optimizes and parallelizes operations, making it 5–20× faster than pandas on large datasets.
2. **Lazy mode** (`pl.scan_csv()`, `pl.scan_parquet()`) builds a query plan without executing it. Call `.collect()` once when you're ready to get the result.
3. **DuckDB** is an embedded SQL engine that queries Parquet, CSV, and pandas DataFrames directly with zero setup — ideal for analysts who think in SQL and need to query large files quickly.
4. **Choose your tool:** pandas for small-to-medium data and quick exploration; Polars for large DataFrame transformations; DuckDB for SQL-style queries on files.

---

## Knowledge Check

**Q1.** What is the key difference between `pl.read_csv()` and `pl.scan_csv()` in Polars?  
**Answer:** `pl.read_csv()` is eager — it reads the entire file immediately into memory. `pl.scan_csv()` is lazy — it returns a query plan and only reads the necessary data when `.collect()` is called.

**Q2.** True or False: DuckDB requires a running server process before you can connect to it.  
**Answer:** False. DuckDB is an embedded database — it runs entirely inside your Python process with no server setup required. Just `import duckdb` and start querying.

**Q3.** You have a 20-million-row Parquet file and need to perform a groupby aggregation with 5 transformations. Should you use pandas, Polars, or DuckDB?  
**Answer:** Either Polars (lazy mode for DataFrame-style transformations) or DuckDB (if you prefer SQL syntax). Both will use multiple CPU cores and outperform pandas significantly on this workload. Pandas would load the full file single-threaded and is likely to be much slower.

---

## Next Lesson
**Lesson 06 — NoSQL: When Tables Aren't Enough**  
You've mastered efficient tabular data handling. Now you'll explore the world beyond SQL tables — document databases, key-value stores, and graph databases — and learn when a DE reaches for NoSQL instead of a relational database.
