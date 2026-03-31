# Module 19 — Large Scale Data Processing  
## Lesson 6 — Parquet Files

---

# Lesson Objective

By the end of this lesson you will understand:

- What **Parquet files** are
- Why Parquet is widely used in modern data systems
- How Parquet improves performance compared to CSV
- How to read and write Parquet files using Python

You will learn how Parquet allows analysts to work with **large datasets more efficiently**.

---

# Overview

In the previous lesson you learned about **columnar storage**.

Parquet is one of the most widely used **columnar file formats**.

Many modern data systems use Parquet because it is optimized for:

```text id="c7p2az"
Analytics
Large datasets
Efficient storage
Fast query performance
```

Unlike CSV files, which store rows sequentially, Parquet stores data **by column**.

Example table:

```text id="yr8h8q"
order_id | region | revenue
```

CSV storage:

```text id="1a4qyx"
1,West,100
2,East,80
3,West,120
```

Parquet storage:

```text id="3xqjlg"
order_id column
1
2
3

region column
West
East
West

revenue column
100
80
120
```

This design makes Parquet extremely efficient for analytical workloads.

---

# Key Idea Cards

### Card 1 — Parquet Is a Columnar Format

Parquet stores values by column rather than by row.

---

### Card 2 — Parquet Files Are Highly Compressed

Parquet uses advanced compression techniques to reduce file size.

---

### Card 3 — Parquet Is Optimized for Analytics

Analytical queries often read only a few columns, making Parquet much faster than CSV.

---

# Key Concepts

## Why CSV Becomes Inefficient

CSV files are simple but inefficient for large datasets.

Example issues:

```text id="t7xw5h"
Large file sizes
Slow read performance
No compression
All columns must be read
```

Example file size comparison:

```text id="36hoy3"
sales.csv      3.5 GB
sales.parquet  600 MB
```

Parquet dramatically reduces storage size.

---

## Columnar Storage in Parquet

Parquet organizes datasets by column.

Example dataset:

```text id="2rj4f3"
customer_id
region
price
quantity
```

When running this calculation:

```text id="j5pl4x"
SUM(price)
```

Parquet reads only the **price column**.

This dramatically reduces disk reads.

---

## Compression

Parquet compresses repeated values effectively.

Example column:

```text id="8gjbbp"
region
West
West
West
West
West
```

Parquet stores this efficiently using compression techniques.

This reduces file size and speeds up reading.

---

# Decision Flow

Use Parquet when working with medium or large datasets.

```text id="m5i7vy"
Dataset small (<100k rows)
        │
       Yes
        │
CSV acceptable
```

If dataset grows larger:

```text id="2r9vo2"
Dataset >1 million rows
        │
        ▼
Use Parquet format
```

Parquet is especially useful when:

```text id="ly9c0o"
Running analytics
Processing large datasets
Building data pipelines
```

---

# Code Examples

## Example 1 — Writing Parquet Files

First install the required library.

```python id="zv0vnt"
pip install pyarrow
```

Now write a Parquet file.

```python id="o7e3g4"
import pandas as pd

df = pd.read_csv("sales_data.csv")

df.to_parquet("sales_data.parquet")
```

This converts a CSV dataset into Parquet format.

---

## Example 2 — Reading Parquet Files

Reading Parquet files is simple.

```python id="xf5n9y"
import pandas as pd

df = pd.read_parquet("sales_data.parquet")

print(df.head())
```

Parquet files often load faster than CSV files.

---

## Example 3 — Selecting Columns

Because Parquet is columnar, we can load only specific columns.

```python id="3v4q8o"
df = pd.read_parquet("sales_data.parquet", columns=["revenue"])
```

This reads only the **revenue column**.

This improves performance.

---

## Example 4 — Comparing File Sizes

Save datasets in both formats.

```python id="ytp9ko"
df.to_csv("sales.csv")
df.to_parquet("sales.parquet")
```

Compare file sizes on disk.

Parquet is often significantly smaller.

---

# SQL / Excel Comparison

Understanding Parquet becomes clearer when compared to familiar tools.

---

## Excel

Excel files store data row by row.

Large Excel files become slow and difficult to open.

---

## SQL Databases

Many modern cloud data warehouses use columnar storage internally.

Examples include:

```text id="in2yxm"
Snowflake
BigQuery
Redshift
```

These systems use columnar storage to accelerate analytical queries.

---

## Pandas

Pandas works well with CSV files.

However, Parquet allows Pandas to handle larger datasets more efficiently.

Typical workflow:

```text id="4y1pxo"
CSV → Parquet → Analytics
```

This improves both performance and storage efficiency.

---

# Practice Exercises

## Exercise 1 — Convert CSV to Parquet

Tags: CSV, Parquet, read_csv()

Load a CSV file and convert it to Parquet.

```python id="9d6r4p"
df = pd.read_csv("data.csv")

df.to_parquet("data.parquet")
```

Compare file sizes.

---

## Exercise 2 — Read Specific Columns

Tags: File I/O, Lists, Tuples, Parquet

Load only two columns from a Parquet file.

```python id="i4y9y2"
df = pd.read_parquet("data.parquet", columns=["price", "quantity"])
```

Observe how quickly the file loads.

---

## Exercise 3 — Performance Comparison

Tags: Performance, Parquet

Time how long it takes to read:

```text id="sk4hzt"
CSV file
Parquet file
```

You will often see faster load times with Parquet.

---

# Common Mistakes

## Mistake 1 — Continuing to Use CSV for Large Data

CSV is convenient but inefficient for analytics.

---

## Mistake 2 — Ignoring Column Selection

When reading Parquet files, load only the columns needed.

---

## Mistake 3 — Not Installing the Required Engine

Parquet requires a backend library such as:

```text id="42o45b"
PyArrow
Fastparquet
```

---

# Real-World Use

Parquet is used extensively in modern data systems.

Examples include:

---

## Data Warehouses

Cloud data warehouses commonly store data in Parquet format.

---

## Data Lakes

Large data lakes use Parquet because it scales well for big datasets.

---

## Machine Learning Pipelines

Training datasets are often stored in Parquet to enable efficient access.

---

## ETL Pipelines

Many pipelines convert raw CSV data into Parquet before processing.

---

# Lesson Recap

In this lesson you learned:

- what Parquet files are
- why Parquet is more efficient than CSV
- how columnar storage improves analytics
- how to read and write Parquet files using Python

Parquet is one of the most important formats for large-scale analytics.

---

# Next Lesson

Module 19 — Lesson 7

**PyArrow Basics**

You will learn how **PyArrow powers many modern data systems**, including Parquet, and how it enables efficient data processing.

---

When you're ready, say:

```text id="6csa52"
next lesson
```