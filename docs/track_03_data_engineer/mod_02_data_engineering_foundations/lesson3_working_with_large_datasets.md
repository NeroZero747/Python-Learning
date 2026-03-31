# Module 7 — Data Engineering Foundations

# Lesson 3 — Handling Large Datasets

---

# Lesson Objective

By the end of this lesson learners will understand:

• why large datasets create technical challenges  
• how memory limitations affect Python programs  
• strategies for processing large datasets efficiently  
• techniques for reducing memory usage (data types, column selection)  
• tools used in scalable data pipelines  

Working with large datasets is one of the most common challenges in data engineering. As data grows to millions or billions of records, traditional approaches can become slow or fail entirely.

---

# Overview

When working with small datasets, loading data into memory is simple.

Example:

```python
import pandas as pd

data = pd.read_csv("sales.csv")
```

For small files this works perfectly.

However, when files become very large (for example **millions of rows or multiple gigabytes**), loading everything into memory can cause problems.

Typical issues include:

• slow processing  
• high memory usage  
• system crashes  

Example scenario:

```text
CSV file size = 8 GB
Laptop memory = 16 GB
```

If Python attempts to load the entire dataset into memory, the system may become unstable.

This is why data engineers use specialized techniques to process large datasets efficiently.

---

# Key Idea Cards (3 Cards)

## Large Data Requires Efficient Processing

When datasets grow large, traditional processing methods may fail.

Example:

```text
Small dataset → pandas works easily
Large dataset → memory issues occur
```

Efficient processing strategies are required.

---

## Memory Is Often the Limiting Factor

Most data processing tools store data in RAM.

Example:

```text
Dataset size = 12 GB
Available RAM = 8 GB
```

The dataset cannot fit in memory, which causes failures.

Data engineers must design pipelines that handle these limitations.

---

## Data Engineers Use Scalable Tools

Large-scale processing often uses tools designed for big data.

Examples include:

• distributed processing systems  
• optimized storage formats  
• chunked data processing  

These techniques allow pipelines to process very large datasets.

---

# Key Concepts

## Memory Constraints

RAM limits how much data a program can process at once.

Example:

```text
Laptop RAM = 16 GB
Dataset = 20 GB
```

The dataset cannot be fully loaded into memory.

---

## Chunk Processing

Chunking processes data in smaller pieces instead of loading everything at once.

Example:

```python
for chunk in pd.read_csv("sales.csv", chunksize=10000):
    print(chunk.head())
```

Each chunk is processed independently.

---

## Distributed Processing

Large datasets can also be processed across multiple machines.

Example frameworks:

• Spark  
• Dask  
• distributed databases.

These systems divide work across clusters.

---

# Decision Flow

Handling large datasets often follows this process:

```text
Is dataset small enough for memory?
           ↓
         YES
           ↓
      Load with pandas
           ↓
         Process

           NO
           ↓
  Use chunk processing or distributed tools
```

This helps determine the appropriate processing method.

---

# Code Examples

## Example 1 — Loading a Dataset

```python
import pandas as pd

data = pd.read_csv("orders.csv")
```

This works for moderate datasets.

---

## Example 2 — Chunk Processing

```python
import pandas as pd

for chunk in pd.read_csv("orders.csv", chunksize=5000):
    print(len(chunk))
```

This reads the file in smaller sections.

---

## Example 3 — Processing Each Chunk

```python
import pandas as pd

for chunk in pd.read_csv("orders.csv", chunksize=5000):
    chunk["total"] = chunk["price"] * chunk["quantity"]
```

Each chunk is transformed independently.

---

## Example 4 — Combining Results

```python
results = []

for chunk in pd.read_csv("orders.csv", chunksize=5000):
    results.append(chunk)

final_data = pd.concat(results)
```

This rebuilds the dataset after chunk processing.

---

# SQL / Excel Comparison

Handling large datasets also appears in SQL and Excel workflows.

| Concept | Python | SQL | Excel |
|------|------|------|------|
| load data | pandas | SELECT | open workbook |
| chunking | pandas chunks | pagination | filtering |
| large dataset tools | Dask / Spark | distributed databases | Power Query |

Example SQL limit query:

```sql
SELECT *
FROM orders
LIMIT 10000
```

This retrieves a portion of the dataset.

---

# Practice Exercises

## Exercise 1

Tags: print(), Tuples, Loops, Iteration

Load a dataset in chunks.

```python
import pandas as pd

for chunk in pd.read_csv("sales.csv", chunksize=1000):
    print(chunk.head())
```

---

## Exercise 2

Tags: Lists, Tuples, Loops, Iteration

Calculate totals for each chunk.

```python
for chunk in pd.read_csv("sales.csv", chunksize=1000):
    chunk["total"] = chunk["price"] * chunk["quantity"]
```

---

## Exercise 3

Tags: print(), len(), Tuples, Loops

Count the number of records processed.

```python
count = 0

for chunk in pd.read_csv("sales.csv", chunksize=1000):
    count += len(chunk)

print(count)
```

---

# Common Mistakes

## Loading Extremely Large Files at Once

Incorrect approach:

```python
data = pd.read_csv("large_file.csv")
```

Better approach:

```python
pd.read_csv("large_file.csv", chunksize=5000)
```

---

## Ignoring Memory Usage

Large datasets require monitoring memory consumption.

Developers should track:

• RAM usage  
• file sizes  
• processing speed.

---

## Rebuilding the Entire Dataset

Some pipelines reassemble large datasets unnecessarily.

Often it is better to **process and write results incrementally**.

---

# Real-World Use

Large dataset processing appears in many real systems.

Examples include:

• healthcare claims processing  
• ecommerce transaction logs  
• financial market data  
• website analytics.

Example healthcare scenario:

```text
Claims records = 300 million
File size = 80 GB
```

A pipeline may process this data in **smaller chunks** and load results into a warehouse.

Example pipeline:

```text
Claims Source
     ↓
Chunk Processing
     ↓
Transform Data
     ↓
Load into Warehouse
```

These techniques allow systems to handle data far larger than system memory.

---

# Lesson Recap

In this lesson you learned:

• why large datasets create challenges  
• how memory limitations affect Python programs  
• how chunk processing helps manage large data  
• how to reduce memory usage with data type optimization and column selection  
• how distributed tools enable scalable processing  

These techniques form the foundation of **large-scale data engineering pipelines**.

---

# Memory Optimization Techniques

When datasets approach or exceed available RAM, data engineers use these techniques:

## Checking Memory Usage

```python
import pandas as pd

data = pd.read_csv("sales.csv")

print(data.memory_usage())
```

This displays memory usage for each column.

## Reducing Data Types

```python
data["quantity"] = data["quantity"].astype("int32")
```

Using smaller data types reduces memory consumption. For example, `int64` uses 8 bytes per value while `int32` uses only 4 bytes.

## Selecting Only Required Columns

```python
data = pd.read_csv("sales.csv", usecols=["price", "quantity"])
```

This prevents unnecessary data from being loaded.

## Combining Techniques

```python
data = pd.read_csv(
    "sales.csv",
    usecols=["price", "quantity"],
    dtype={"quantity": "int32"}
)
```

This reduces memory usage during loading. These memory optimization techniques combined with chunk processing ensure pipelines remain **efficient and stable**.

---

# Next Lesson

Next we will learn:

# Lesson 4 — Parquet & Efficient Storage

You will learn:

• why file formats matter for data pipelines  
• how Parquet improves storage and performance  
• how columnar storage benefits analytics systems  
• how Python reads and writes Parquet files.
