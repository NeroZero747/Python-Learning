# Module 7 — Data Engineering Foundations

# Lesson 5 — Parquet & Efficient Storage

---

# Lesson Objective

By the end of this lesson learners will understand:

• why file formats matter in data pipelines  
• what **Parquet** is and why it is widely used in data engineering  
• how columnar storage improves analytics performance  
• how to read and write Parquet files using Python  

Efficient storage formats are critical because **data pipelines often process extremely large datasets**, and inefficient formats can significantly slow down systems.

---

# Overview

Many beginners store data in formats such as:

• CSV  
• Excel  
• JSON  

Example CSV file:

```text
order_id,price,quantity
1,10,2
2,20,1
```

These formats are easy to understand, but they are **not optimized for large-scale data systems**.

Problems with CSV:

• large file sizes  
• slow read speeds  
• no compression  
• inefficient for analytics queries  

To solve these issues, data engineers use **columnar storage formats**.

One of the most common formats is **Apache Parquet**.

Parquet is designed for:

• large-scale analytics  
• efficient compression  
• fast query performance  

Example workflow:

```text
Raw CSV Data
      ↓
Transform
      ↓
Save as Parquet
      ↓
Load into Data Warehouse
```

Using Parquet can reduce file sizes dramatically and improve processing speed.

---

# Key Idea Cards (3 Cards)

## Parquet Is a Columnar Storage Format

Traditional formats store data **row by row**.

Example row-based format:

```text
Row1: order_id, price, quantity
Row2: order_id, price, quantity
```

Parquet stores data **column by column**, which improves query performance.

---

## Parquet Files Are Highly Compressed

Parquet supports efficient compression algorithms.

Benefits include:

• smaller file sizes  
• faster storage operations  
• lower storage costs.

Large datasets can shrink significantly when converted from CSV to Parquet.

---

## Columnar Storage Improves Analytics

Analytics queries often access only a few columns.

Example query:

```text
SELECT price, quantity
FROM sales
```

With columnar storage, only the required columns are read, which speeds up queries.

---

# Key Concepts

## Row-Based Storage

Row-based formats store entire records together.

Example CSV row:

```text
1,10,2
```

This approach is good for transactional systems but inefficient for analytics queries.

---

## Columnar Storage

Columnar storage organizes data by columns instead of rows.

Example structure:

```text
order_id: 1,2,3,4
price: 10,20,15,12
quantity: 2,1,3,1
```

This allows queries to scan only the necessary columns.

---

## Compression

Parquet supports compression techniques that reduce file size.

Benefits include:

• faster reads  
• lower storage costs  
• improved pipeline performance.

---

# Decision Flow

Choosing a storage format often follows this logic:

```text
Is dataset small and simple?
         ↓
       YES
         ↓
       CSV

         NO
         ↓
Large analytics dataset?
         ↓
       YES
         ↓
       Use Parquet
```

Most modern data pipelines store data in **Parquet format**.

---

# Code Examples

## Example 1 — Reading a CSV File

```python
import pandas as pd

data = pd.read_csv("sales.csv")
```

This loads data from a CSV file.

---

## Example 2 — Writing a Parquet File

```python
data.to_parquet("sales.parquet")
```

This converts the dataset into Parquet format.

---

## Example 3 — Reading a Parquet File

```python
data = pd.read_parquet("sales.parquet")
```

Parquet files load faster than CSV for large datasets.

---

## Example 4 — Compression Example

```python
data.to_parquet("sales.parquet", compression="snappy")
```

Compression reduces file size while maintaining fast read speeds.

---

# SQL / Excel Comparison

Storage formats also exist in other tools.

| Concept | Python | SQL | Excel |
|------|------|------|------|
| raw data | CSV | table dump | workbook |
| analytics storage | Parquet | data warehouse tables | Power Query models |
| columnar storage | Parquet | columnstore indexes | data model |

Example SQL analytics query:

```sql
SELECT price, quantity
FROM sales
```

Columnar storage speeds up queries like this.

---

# Practice Exercises

## Exercise 1

Tags: pandas, Imports, read_csv(), CSV

Load a CSV dataset.

```python
import pandas as pd

data = pd.read_csv("orders.csv")
```

---

## Exercise 2

Tags: Parquet, Data I/O

Save the dataset as Parquet.

```python
data.to_parquet("orders.parquet")
```

---

## Exercise 3

Tags: Parquet, Performance

Load the Parquet file.

```python
data = pd.read_parquet("orders.parquet")
```

Compare performance with the CSV version.

---

# Common Mistakes

## Using CSV for Large Analytics Pipelines

CSV is easy to use but inefficient for large-scale analytics.

Parquet should be used for:

• large datasets  
• frequent queries  
• distributed processing systems.

---

## Ignoring Compression

Uncompressed files waste storage space.

Parquet compression helps reduce storage costs.

---

## Converting Files Repeatedly

Repeated conversions between formats can slow pipelines.

Best practice:

```text
Extract → Transform → Store as Parquet
```

---

# Real-World Use

Parquet is widely used in modern data platforms.

Examples include:

• Snowflake data pipelines  
• Spark processing jobs  
• data lakes  
• analytics warehouses.

Example pipeline:

```text
Application Database
        ↓
Extract Data
        ↓
Transform Data
        ↓
Store as Parquet
        ↓
Load into Data Warehouse
```

This structure enables fast analytics and efficient storage.

---

# Lesson Recap

In this lesson you learned:

• why file formats matter in data pipelines  
• how Parquet improves storage efficiency  
• how columnar storage speeds up analytics queries  
• how Python reads and writes Parquet files  

Efficient storage formats are a core part of **modern data engineering systems**.

---

# Next Lesson

Next we will learn:

# Lesson 6 — Intro to Polars (Optional)

You will learn:

• what Polars is  
• why Polars can be faster than pandas  
• when Polars is useful for large datasets  
• how to perform basic operations using Polars.
