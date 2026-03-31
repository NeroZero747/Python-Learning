# Module 19 — Large Scale Data Processing  
## Lesson 5 — Columnar Storage

---

# Lesson Objective

By the end of this lesson you will understand:

- What **columnar storage** is
- Why columnar file formats are faster for analytics
- The difference between **row-based storage and column-based storage**
- Why modern data tools use **columnar formats like Parquet**

You will learn how columnar storage dramatically improves performance when working with large datasets.

---

# Overview

Many datasets are stored in **row-based formats**.

Examples include:

```text id="mi2tcw"
CSV
Excel
JSON
```

These formats store data row by row.

Example table:

```text id="spvel4"
order_id | customer | region | revenue
```

Stored in row format:

```text id="nzvyxj"
1, Alice, West, 120
2, Bob, East, 80
3, Maria, West, 200
```

Each row stores all column values together.

This format is simple but inefficient for large-scale analytics.

Modern analytics systems instead use **columnar storage**.

Columnar storage stores data **by column rather than by row**.

Example:

```text id="vuyepi"
order_id column
1
2
3

customer column
Alice
Bob
Maria

region column
West
East
West

revenue column
120
80
200
```

This storage format enables faster analytical queries.

---

# Key Idea Cards

### Card 1 — Row Storage vs Column Storage

Traditional files store rows together.  
Columnar systems store values from the same column together.

---

### Card 2 — Columnar Storage Improves Analytics

Columnar storage allows systems to read only the columns required for a query.

---

### Card 3 — Modern Data Systems Use Columnar Formats

Technologies like **Parquet, DuckDB, and Polars** rely on columnar storage for performance.

---

# Key Concepts

## Row-Based Storage

Most traditional data formats use row-based storage.

Example formats:

```text id="rr5tcx"
CSV
Excel
JSON
```

When reading a CSV file, Pandas must load every column.

Example:

```python id="zx36m7"
df = pd.read_csv("sales.csv")
```

Even if you only need one column.

Example query:

```python id="hzeebk"
df["revenue"].sum()
```

Pandas still loads the entire dataset.

---

## Column-Based Storage

Columnar formats store values by column.

Example:

```text id="iu7xth"
revenue column
120
80
200
```

If we calculate revenue totals:

```text id="31p0qb"
System reads only revenue column
```

Instead of reading the entire dataset.

This dramatically improves performance.

---

## Why Columnar Storage Is Faster

Columnar formats improve performance for several reasons.

### 1 — Reduced Disk Reads

If a dataset has:

```text id="waczeg"
50 columns
```

but we only need:

```text id="3y6z7n"
2 columns
```

columnar systems read only those columns.

---

### 2 — Better Compression

Columns often contain repeated values.

Example:

```text id="0g4heo"
region
West
West
West
West
```

Columnar formats compress repeated values efficiently.

---

### 3 — Faster Analytical Queries

Most analytical queries operate on columns.

Example:

```text id="sbqr6a"
SUM(revenue)
AVG(price)
GROUP BY region
```

Columnar storage is optimized for these operations.

---

# Decision Flow

Use columnar formats when working with large datasets.

```text id="4ivd5a"
Is dataset small (<1M rows)?
        │
       Yes
        │
CSV or Pandas works fine
```

If dataset becomes larger:

```text id="wtssoi"
Dataset > several million rows
        │
        ▼
Use columnar formats
```

Examples include:

```text id="352sx4"
Parquet
Arrow
```

These formats are optimized for analytics.

---

# Code Examples

## Example 1 — Reading CSV File

Standard workflow using CSV.

```python id="zfmy6a"
import pandas as pd

df = pd.read_csv("sales_data.csv")

print(df.head())
```

The entire dataset must be read.

---

## Example 2 — Selecting a Column

Even if we only need one column:

```python id="84d9ni"
df["revenue"].sum()
```

Pandas already loaded the entire dataset.

---

## Example 3 — Conceptual Columnar Access

In columnar systems:

```text id="d2sv5u"
Dataset
│
├ revenue column
├ price column
├ quantity column
└ region column
```

If we calculate:

```text id="gw9n39"
SUM(revenue)
```

Only the revenue column is accessed.

This dramatically improves efficiency.

---

# SQL / Excel Comparison

Understanding columnar storage is easier when compared with SQL and Excel.

---

## Excel

Excel stores rows sequentially.

Example:

```text id="skxy8l"
Row 1
Row 2
Row 3
```

Large Excel files slow down because every row must be loaded.

---

## SQL Databases

Traditional relational databases store rows together.

However, some modern data warehouses use columnar storage internally.

Examples:

```text id="eyx4hj"
Snowflake
BigQuery
Redshift
```

These systems are optimized for analytics.

---

## Pandas

Pandas works well with row-based files like CSV.

But when datasets grow, analysts often switch to **columnar formats**.

Example:

```text id="fbk9zn"
CSV → Parquet
```

This allows faster queries and smaller file sizes.

---

# Practice Exercises

## Exercise 1 — Identify Storage Type

Tags: Excel, Parquet

Determine whether the following formats are row-based or column-based.

```text id="ejp2n0"
CSV
Excel
Parquet
```

---

## Exercise 2 — Analyze Query Efficiency

Tags: Databases, Conditionals, Context Managers, SQL Queries

Imagine a dataset with:

```text id="xusnty"
100 columns
```

If we calculate:

```text id="1h8csv"
SUM(revenue)
```

How many columns must be read in:

- row-based storage
- columnar storage

---

## Exercise 3 — Research Columnar Databases

Tags: Databases, Big Data

Identify one database that uses columnar storage.

Examples include:

```text id="bkyu9n"
Snowflake
BigQuery
Redshift
```

---

# Common Mistakes

## Mistake 1 — Using CSV for Large Analytics Datasets

CSV files become inefficient as dataset size increases.

Columnar formats are more efficient.

---

## Mistake 2 — Assuming Storage Format Does Not Matter

File format dramatically affects performance.

---

## Mistake 3 — Ignoring Compression Benefits

Columnar formats compress repeated values much more efficiently.

---

# Real-World Use

Columnar storage is used in many modern analytics systems.

Examples include:

---

## Data Warehouses

Cloud data warehouses rely heavily on columnar storage.

---

## Analytics Platforms

Tools that process large datasets benefit from columnar formats.

---

## Data Pipelines

ETL pipelines often convert data from:

```text id="4xbenf"
CSV → Parquet
```

before performing analytics.

---

## Machine Learning Workflows

Large training datasets are often stored in columnar formats for efficient access.

---

# Lesson Recap

In this lesson you learned:

- the difference between row-based and column-based storage
- why columnar formats are faster for analytics
- how columnar storage reduces disk reads
- why modern analytics systems use columnar formats

Columnar storage is a key foundation for working with large datasets efficiently.

---

# Next Lesson

Module 19 — Lesson 6

**Parquet Files**

You will learn how to:

- read and write Parquet files
- use Parquet with Pandas
- dramatically improve performance compared to CSV files.

---

When you're ready, say:

```text id="10222d"
next lesson
```