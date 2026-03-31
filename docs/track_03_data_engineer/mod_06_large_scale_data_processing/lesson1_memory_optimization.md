# Module 19 — Large Scale Data Processing  
## Lesson 2 — Memory Optimization

---

# Lesson Objective

By the end of this lesson you will understand:

- Why **DataFrames often use more memory than expected**
- How to **inspect memory usage in Pandas**
- How to **optimize column data types**
- How to significantly **reduce memory consumption**

You will learn techniques that allow Python to process **larger datasets using less memory**.

---

# Overview

When working with large datasets, **memory usage becomes a critical factor**.

Even datasets that appear small can consume large amounts of memory once loaded into Pandas.

Example dataset:

```text id="v2a0pm"
sales_data.csv
1,000,000 rows
8 columns
```

After loading:

```python id="jddtlf"
import pandas as pd

df = pd.read_csv("sales_data.csv")
```

The DataFrame might consume:

```text id="r8rqts"
300–600 MB of RAM
```

But why?

Because Pandas must store:

- column values
- column metadata
- index information
- object references

In addition, many datasets contain **inefficient data types**.

Example:

```text id="m7p33u"
Customer IDs stored as strings
Integer columns stored as 64-bit values
Categorical values stored as objects
```

These inefficiencies cause memory usage to increase dramatically.

Memory optimization techniques allow analysts to:

```text id="9s7xhl"
process larger datasets
improve performance
avoid memory crashes
```

---

# Key Idea Cards

### Card 1 — Data Types Impact Memory Usage

Choosing the correct data type can significantly reduce memory consumption.

---

### Card 2 — Object Columns Are Expensive

Columns stored as **object types** consume more memory than numeric or categorical types.

---

### Card 3 — Memory Optimization Improves Performance

Reducing memory usage often results in **faster processing and more scalable workflows**.

---

# Key Concepts

## Inspecting Memory Usage

Before optimizing a dataset, it is important to understand how much memory it consumes.

Pandas provides tools to inspect memory usage.

Example:

```python id="a9slg3"
df.info(memory_usage="deep")
```

Example output:

```text id="9k8mkh"
RangeIndex: 1000000 entries
Data columns: 8 columns
memory usage: 420.5 MB
```

This shows how much memory the DataFrame requires.

---

## Data Types in Pandas

Common Pandas data types include:

```text id="l6r3li"
int64
float64
object
bool
datetime
category
```

Many datasets default to large data types such as:

```text id="j8s9f2"
int64
float64
```

These types use more memory than necessary.

---

## Numeric Type Optimization

Example dataset:

```text id="azks2y"
age column
values between 0–120
```

If stored as:

```text id="js6uaz"
int64
```

It uses **8 bytes per value**.

Instead we can store it as:

```text id="p7m2kp"
int8
```

Which uses **1 byte per value**.

---

## Category Data Type

Columns containing repeated values can be stored as **category** types.

Example column:

```text id="4v72ab"
country
USA
USA
USA
Canada
Canada
Mexico
```

Instead of storing repeated strings, Pandas stores:

```text id="r5v3o0"
unique values list
+
integer references
```

This significantly reduces memory usage.

---

# Decision Flow

Use memory optimization when working with medium or large datasets.

```text id="ogj0y2"
Dataset loaded in Pandas
        │
        ▼
Check memory usage
```

If memory is high:

```text id="z1xv28"
Optimize data types
```

Steps:

```text id="30ccs7"
convert object → category
convert large integers → smaller types
convert strings → categorical values
```

This allows Pandas to handle larger datasets.

---

# Code Examples

## Example 1 — Checking Memory Usage

First inspect memory usage.

```python id="v4pljl"
import pandas as pd

df = pd.read_csv("sales_data.csv")

df.info(memory_usage="deep")
```

This displays memory consumption.

---

## Example 2 — Converting Column Data Types

Example numeric column optimization.

```python id="q4z7rr"
df["quantity"] = df["quantity"].astype("int32")
```

This reduces memory compared to `int64`.

---

## Example 3 — Converting to Category Type

If a column contains repeated values:

```python id="pfh6q4"
df["country"] = df["country"].astype("category")
```

This significantly reduces memory usage.

---

## Example 4 — Downcasting Numeric Data

Pandas can automatically reduce numeric sizes.

```python id="1fmxvr"
df["sales"] = pd.to_numeric(df["sales"], downcast="float")
```

Downcasting selects the smallest possible type.

---

## Example 5 — Measuring Memory Reduction

After optimization:

```python id="l3bpxq"
df.info(memory_usage="deep")
```

Compare the before and after memory usage.

---

# SQL / Excel Comparison

Understanding memory optimization becomes clearer when comparing systems.

---

## Excel

Excel stores data in memory.

Large files slow down quickly because Excel must manage:

```text id="93e4mh"
cells
formulas
formatting
```

This leads to slow calculations.

---

## SQL Databases

SQL databases optimize storage automatically.

Example:

```sql id="4t93st"
CREATE TABLE sales (
  quantity SMALLINT,
  country VARCHAR(50)
)
```

Databases choose efficient storage formats.

---

## Pandas

Pandas gives analysts control over data types.

Example:

```python id="2u6x3e"
df["country"].astype("category")
```

This manual optimization is similar to defining data types in SQL.

---

# Practice Exercises

## Exercise 1 — Inspect Memory Usage

Tags: Memory Optimization, Data I/O, Performance

Load a dataset and inspect its memory usage.

```python id="1ugy8s"
df.info(memory_usage="deep")
```

Identify which columns consume the most memory.

---

## Exercise 2 — Convert Columns to Category

Tags: Strings, Lists, Memory Optimization, Performance

Convert a repeated string column to category.

Example:

```python id="rc1z9x"
df["region"] = df["region"].astype("category")
```

Check memory usage again.

---

## Exercise 3 — Downcast Numeric Columns

Tags: Integers, Lists, Tuples, Memory Optimization

Use numeric downcasting to reduce memory.

Example:

```python id="j1e2m1"
df["sales"] = pd.to_numeric(df["sales"], downcast="integer")
```

Compare memory usage before and after.

---

# Common Mistakes

## Mistake 1 — Ignoring Data Types

Many beginners rely on default Pandas types.

These defaults may not be memory efficient.

---

## Mistake 2 — Overusing Object Columns

Object columns consume large amounts of memory.

Convert repeated values to categorical types.

---

## Mistake 3 — Optimizing Before Inspecting

Always inspect memory usage before attempting optimizations.

---

# Real-World Use

Memory optimization is common in many industries.

Examples include:

---

## Financial Analytics

Processing millions of transaction records.

---

## Healthcare Data

Analyzing patient records and claim histories.

---

## Marketing Analytics

Working with large customer event datasets.

---

## E-commerce

Analyzing product orders and clickstream data.

---

In each case, reducing memory usage allows analysts to work with larger datasets using standard tools.

---

# Lesson Recap

In this lesson you learned:

- how to inspect DataFrame memory usage
- how data types impact memory consumption
- how to convert columns to more efficient types
- how to reduce memory usage in large datasets

Memory optimization allows Pandas to handle **larger datasets efficiently**.

---

# Next Lesson

Module 19 — Lesson 3

**Chunk Processing**

You will learn how to:

- process large datasets in smaller segments
- avoid loading entire files into memory
- analyze datasets with millions of rows.

---

When you're ready, say:

```text id="nsqv6d"
next lesson
```