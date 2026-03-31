# Module 19 — Large Scale Data Processing  
## Lesson 3 — Chunk Processing

---

# Lesson Objective

By the end of this lesson you will understand:

- What **chunk processing** is
- How to process very large datasets **without loading them fully into memory**
- How to perform **calculations across chunks**
- When chunk processing is appropriate compared to other large-data tools

Chunk processing is one of the most important techniques analysts use when datasets begin to exceed the limits of normal Pandas workflows.

---

# Overview

Earlier in this module you learned that Pandas loads data **entirely into memory**.

Example:

```python id="g2dz35"
import pandas as pd

df = pd.read_csv("sales_data.csv")
```

Behind the scenes:

```text id="4vkzam"
CSV File
↓
Entire dataset loaded into RAM
↓
DataFrame created
```

This works perfectly for small datasets.

However, problems occur when files become very large.

Example dataset sizes:

```text id="t7hkp4"
5 million rows
20 million rows
100+ million rows
```

These datasets may exceed available memory.

To solve this problem, we use **chunk processing**.

Chunk processing means reading the dataset **in smaller pieces** instead of loading everything at once.

Example:

```text id="obur58"
Large CSV File
↓
Chunk 1 (10,000 rows)
Chunk 2 (10,000 rows)
Chunk 3 (10,000 rows)
...
```

Each chunk is processed independently.

This allows Python to analyze datasets **far larger than system memory**.

---

# Key Idea Cards

### Card 1 — Chunk Processing Reads Data in Pieces

Instead of loading a dataset entirely, Python reads smaller subsets sequentially.

---

### Card 2 — Chunk Processing Reduces Memory Usage

Only one portion of the dataset exists in memory at a time.

---

### Card 3 — Chunk Processing Enables Large Data Analysis

Datasets with tens of millions of rows can be analyzed on standard laptops.

---

# Key Concepts

## What Is a Chunk?

A chunk is simply a **subset of rows from the dataset**.

Example:

```text id="j1gz5q"
Dataset size: 5,000,000 rows
Chunk size: 10,000 rows
```

Python will process:

```text id="3ll0sv"
500 chunks
```

Each chunk behaves like a **normal Pandas DataFrame**.

---

## Chunk Iterators

When using chunk processing, Pandas returns an **iterator**.

An iterator allows Python to read one portion of the dataset at a time.

Example:

```python id="qzb0il"
chunks = pd.read_csv("sales_data.csv", chunksize=10000)
```

Here, `chunks` is not a DataFrame.

It is a sequence of DataFrames that can be processed one by one.

---

## Why Chunk Processing Is Useful

Chunk processing solves several common problems:

```text id="ghjk6v"
Large CSV files
Memory limitations
Streaming data analysis
Incremental calculations
```

This technique is widely used in ETL pipelines.

---

# Decision Flow

Use chunk processing when working with large CSV files.

```text id="htspg2"
Dataset small (<1M rows)
        │
       Yes
        │
Use standard Pandas
```

If dataset becomes large:

```text id="o8z4h4"
Dataset too large for memory
        │
        ▼
Use chunk processing
```

For extremely large datasets:

```text id="iyztpt"
Consider:
Parquet
DuckDB
Polars
Dask
```

These tools are introduced later in this module.

---

# Code Examples

## Example 1 — Reading a CSV File in Chunks

Pandas allows chunk processing using the `chunksize` parameter.

```python id="1822np"
import pandas as pd

chunks = pd.read_csv("sales_data.csv", chunksize=10000)

for chunk in chunks:
    print(chunk.head())
```

Explanation:

```text id="nvbj84"
chunksize = 10000
```

Each iteration loads 10,000 rows.

---

## Example 2 — Counting Total Rows

Suppose we want to count rows in a large dataset.

```python id="uy4x8u"
import pandas as pd

total_rows = 0

chunks = pd.read_csv("sales_data.csv", chunksize=10000)

for chunk in chunks:
    total_rows += len(chunk)

print(total_rows)
```

This method avoids loading the entire dataset.

---

## Example 3 — Aggregating Data Across Chunks

Suppose we want total revenue.

```python id="i4r0h5"
import pandas as pd

total_revenue = 0

chunks = pd.read_csv("sales_data.csv", chunksize=10000)

for chunk in chunks:
    total_revenue += chunk["revenue"].sum()

print(total_revenue)
```

Each chunk contributes to the total result.

---

## Example 4 — Filtering Rows

Suppose we only want rows where:

```text id="uxly5y"
country = USA
```

```python id="s3vqdg"
import pandas as pd

chunks = pd.read_csv("sales_data.csv", chunksize=10000)

filtered_data = []

for chunk in chunks:
    filtered = chunk[chunk["country"] == "USA"]
    filtered_data.append(filtered)

result = pd.concat(filtered_data)

print(result.head())
```

This extracts relevant records from a large dataset.

---

# SQL / Excel Comparison

Understanding chunk processing becomes easier when compared with SQL and Excel.

---

## Excel

Excel loads the entire dataset into memory.

Maximum rows:

```text id="zgaktp"
1,048,576 rows
```

Large datasets cannot be opened.

---

## SQL

SQL databases read data **directly from disk**.

Example query:

```sql id="nj31w0"
SELECT SUM(revenue)
FROM sales
```

The database processes only necessary data.

---

## Pandas with Chunk Processing

Chunk processing behaves somewhat like SQL.

Instead of loading the full dataset:

```text id="4btmty"
Read chunk
Process chunk
Read next chunk
Process next chunk
```

This approach mimics **streaming data processing**.

---

# Practice Exercises

## Exercise 1 — Print Chunk Sizes

Tags: Memory Optimization, Tuples, read_csv(), CSV

Load a CSV file with chunk processing.

```python id="ty4x3n"
chunks = pd.read_csv("sales_data.csv", chunksize=5000)
```

Print the number of rows in each chunk.

---

## Exercise 2 — Compute Average Value

Tags: len(), Lists, Aggregations, HTTP Methods

Calculate the average of a numeric column across chunks.

Hint:

```python id="ep28p5"
total_sum += chunk["sales"].sum()
total_count += len(chunk)
```

Then compute:

```python id="7ellu5"
average = total_sum / total_count
```

---

## Exercise 3 — Extract Rows

Tags: String Formatting, WHERE, Chunk Processing

Use chunk processing to extract rows where:

```text id="5zcu2f"
region = "West"
```

Combine results using `pd.concat`.

---

# Common Mistakes

## Mistake 1 — Using Large Chunk Sizes

Very large chunks defeat the purpose.

Example mistake:

```text id="qe5ytr"
chunksize = 5,000,000
```

---

## Mistake 2 — Forgetting to Aggregate Results

When computing totals across chunks, results must be accumulated manually.

---

## Mistake 3 — Assuming Chunk Processing Is Always Fast

Chunk processing prevents memory errors but may still be slower than optimized storage formats.

Later lessons introduce faster solutions.

---

# Real-World Use

Chunk processing is commonly used in data pipelines.

Examples include:

---

## Financial Data

Analyzing millions of stock trades.

---

## Marketing Analytics

Processing event logs from advertising platforms.

---

## Web Analytics

Analyzing website traffic logs.

---

## Healthcare Systems

Processing claims records from multiple years.

---

In many real-world environments, datasets exceed memory limits and must be processed incrementally.

---

# Lesson Recap

In this lesson you learned:

- what chunk processing is
- how Pandas processes large files in smaller segments
- how to perform aggregations across chunks
- how chunk processing enables large dataset analysis

Chunk processing is one of the first techniques analysts use when data begins to scale beyond memory limits.

---

# Next Lesson

Module 19 — Lesson 4

**Processing Millions of Rows**

You will learn how to design workflows that process extremely large datasets efficiently.

---

When you're ready, say:

```text id="493jfv"
next lesson
```