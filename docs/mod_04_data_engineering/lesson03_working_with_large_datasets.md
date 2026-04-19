# Lesson 03 — Working with Large Datasets

**Track:** Data Engineering for Analysts  
**Module:** Module 1 — Data Engineering Foundations  
**Difficulty:** Beginner → Intermediate | **Duration:** 12 min  
**Sources:** M1-L03 (Handling Large Datasets) · M5-L02 (Memory Optimization) · M5-L03 (Chunk Processing) · M5-L04 (Processing Millions of Rows)

---

## Learning Objectives

1. **Diagnose memory issues** — Explain why pandas runs out of memory on large files and identify the root causes.
2. **Chunked reading** — Use `chunksize` to process files that are larger than available RAM.
3. **Dtype optimization** — Downcast numeric columns and convert string columns to categoricals to cut memory usage by 50–80%.
4. **Vectorized operations** — Replace Python loops with pandas vectorized methods for dramatic speed gains.

> By the end of this lesson you'll be able to process a 5-million-row CSV on a laptop that only has 8 GB of RAM.

---

## Overview

### Hook
When a dataset outgrows your laptop's memory, pandas throws a `MemoryError` and your pipeline dies. Data engineers solve this not by buying more RAM, but by working smarter with the data they already have.

### Analogy: The Moving Truck
Think of loading large data like moving house with a small truck. You can't fit every box in one trip — so instead of trying to hire a bigger truck, you make multiple smaller trips. Each trip loads only what fits, processes it at the destination, and returns for the next load. **Chunk processing** works exactly the same way: read a manageable slice of the file, process it, save the result, then read the next slice.

| Technique | Moving Analogy |
|-----------|---------------|
| **Chunked reading** | Making multiple smaller trips instead of one giant one |
| **Dtype downcasting** | Using smaller boxes — why use a wardrobe box for just one shirt? |
| **Categorical columns** | Labeling boxes by room — one label covers hundreds of identical items |
| **Vectorized operations** | Using a dolly instead of carrying each box by hand |

> **Key takeaway:** The average analyst uses 5–10× more memory than needed because pandas defaults to the largest possible dtype for every column. Fixing this is free — it just requires knowing where to look.

---

## Key Takeaways

### 1. Pandas Defaults Are Memory-Hungry
By default, pandas loads every integer column as `int64` (8 bytes per value) and every text column as `object` (a Python string pointer — 50+ bytes per value). A column with values 0–100 doesn't need 8 bytes — it fits in `int8` (1 byte). Downcasting alone often halves the memory footprint.  
**Keywords:** Dtype · int8/int16 · float32 · Memory footprint

### 2. Chunk Processing Fits Any File Size Into Any RAM
`pd.read_csv("file.csv", chunksize=100_000)` returns an iterator. Each iteration gives you 100,000 rows — enough to process without filling memory. Aggregate the results across chunks and you can handle files of any size on any machine.  
**Keywords:** chunksize · Iterator · Aggregation

### 3. Categoricals Eliminate String Duplication
When a text column has low cardinality (e.g. a "region" column with 5 unique values across 10 million rows), pandas stores 10 million strings by default. Converting to `category` dtype stores only 5 unique strings plus a mapping of integers — reducing memory use by 90%+ in that column.  
**Keywords:** category dtype · Low cardinality · String deduplication

---

## Key Concepts

### memory_usage() — Understand what you're working with
```python
import pandas as pd

df = pd.read_csv("large_sales.csv")

# See memory used by each column
print(df.memory_usage(deep=True))

# Total in megabytes
total_mb = df.memory_usage(deep=True).sum() / 1024**2
print(f"DataFrame uses {total_mb:.1f} MB")
```

### Dtype Downcasting Rules
| Current dtype | Max value | Can downcast to | Memory saving |
|---------------|-----------|-----------------|---------------|
| `int64` | up to 127 | `int8` | 87.5% |
| `int64` | up to 32,767 | `int16` | 75% |
| `int64` | up to 2.1B | `int32` | 50% |
| `float64` | most floats | `float32` | 50% |
| `object` (low cardinality) | — | `category` | 70–95% |

### Chunked Reading Pattern
```python
# Process a large CSV in chunks without loading it all at once
results = []

for chunk in pd.read_csv("sales.csv", chunksize=100_000):
    # Do your processing on this chunk
    summary = chunk.groupby("region")["amount"].sum()
    results.append(summary)

# Combine all chunk results
final = pd.concat(results).groupby(level=0).sum()
```

### Vectorized Operations vs Loops
```python
# SLOW: Python loop (100× slower on large DataFrames)
df["tax"] = [row["amount"] * 0.1 for _, row in df.iterrows()]

# FAST: Vectorized operation (operates on whole column at once)
df["tax"] = df["amount"] * 0.1
```

---

## Code Examples

### Example 1: Reading a CSV with optimized dtypes upfront
```python
import pandas as pd

# Define dtypes before reading — pandas won't need to infer them
dtypes = {
    "order_id":    "int32",
    "customer_id": "int32",
    "amount":      "float32",
    "region":      "category",
    "status":      "category",
}

df = pd.read_csv(
    "orders.csv",
    dtype=dtypes,
    usecols=["order_id", "customer_id", "amount", "region", "status"],
    parse_dates=["order_date"]  # parse date columns directly
)

print(df.memory_usage(deep=True).sum() / 1024**2, "MB")
```
**Terminal output:**
```
Before optimization:  412 MB
After optimization:    54 MB
```

### Example 2: Auto-downcast an existing DataFrame
```python
def optimize_dtypes(df: pd.DataFrame) -> pd.DataFrame:
    """Downcast numeric columns and categorize low-cardinality strings."""
    # Downcast integers and floats
    for col in df.select_dtypes(include=["int64", "int32"]).columns:
        df[col] = pd.to_numeric(df[col], downcast="integer")
    for col in df.select_dtypes(include=["float64"]).columns:
        df[col] = pd.to_numeric(df[col], downcast="float")

    # Convert low-cardinality object columns to category
    for col in df.select_dtypes(include=["object"]).columns:
        if df[col].nunique() / len(df) < 0.05:  # less than 5% unique values
            df[col] = df[col].astype("category")

    return df

df = optimize_dtypes(df)
```

### Example 3: Chunked aggregation — sum sales by region across a huge file
```python
import pandas as pd

totals = {}

for i, chunk in enumerate(pd.read_csv("sales_10m.csv", chunksize=250_000)):
    # Optimize each chunk before processing
    chunk["amount"] = chunk["amount"].astype("float32")
    chunk["region"] = chunk["region"].astype("category")

    # Aggregate this chunk
    for region, total in chunk.groupby("region")["amount"].sum().items():
        totals[region] = totals.get(region, 0) + total

    print(f"Chunk {i+1} processed ({(i+1)*250_000:,} rows)")

# Final results
for region, total in sorted(totals.items()):
    print(f"{region}: £{total:,.2f}")
```
**Terminal output:**
```
Chunk 1 processed (250,000 rows)
Chunk 2 processed (500,000 rows)
...
Chunk 40 processed (10,000,000 rows)
EMEA: £3,218,492.75
APAC: £2,891,003.00
AMER: £4,105,228.50
```

### Example 4: Reading only the columns you need
```python
# Loading all 50 columns when you only need 4 wastes 92% of the memory
df = pd.read_csv(
    "big_report.csv",
    usecols=["order_id", "date", "amount", "region"]  # only the 4 you need
)
```

---

## Common Mistakes

### Mistake 1: Loading then filtering (loads everything first)
```python
# WRONG — loads 10 million rows, then discards 9.9 million
df = pd.read_csv("huge.csv")
df = df[df["region"] == "EMEA"]

# RIGHT — use nrows or chunked filter
chunks = []
for chunk in pd.read_csv("huge.csv", chunksize=100_000):
    chunks.append(chunk[chunk["region"] == "EMEA"])
df = pd.concat(chunks)
```

### Mistake 2: Using iterrows() on large DataFrames
```python
# WRONG — iterrows creates a new Python object for each row
for idx, row in df.iterrows():
    df.at[idx, "tax"] = row["amount"] * 0.1   # extremely slow at 1M+ rows

# RIGHT — vectorized operation runs in C, not Python
df["tax"] = df["amount"] * 0.1                  # ~100× faster
```

### Mistake 3: Forgetting that category dtype breaks some operations
```python
# Category columns don't always work like strings
df["region"] = df["region"].astype("category")

# This will fail if "New Region" isn't in the existing categories
df["region"] = df["region"].cat.add_categories("New Region")   # must add first
df.loc[0, "region"] = "New Region"
```

---

## Practice Exercises

### Exercise 1 — Measure the impact
```python
import pandas as pd

df = pd.read_csv("sample_data.csv")
before = df.memory_usage(deep=True).sum() / 1024**2

# TODO: downcast all int64 columns to int32
# TODO: downcast all float64 columns to float32
# TODO: convert any object columns with < 10% unique values to category

after = df.memory_usage(deep=True).sum() / 1024**2
print(f"Before: {before:.1f} MB  |  After: {after:.1f} MB  |  Saved: {before-after:.1f} MB")
```

### Exercise 2 — Fix the loop
```python
import pandas as pd
import numpy as np

df = pd.DataFrame({"score": np.random.randint(0, 100, 1_000_000)})

# TODO: Replace this loop with a vectorized operation
for i, row in df.iterrows():
    if row["score"] >= 60:
        df.at[i, "grade"] = "Pass"
    else:
        df.at[i, "grade"] = "Fail"

# HINT: use np.where() or pd.cut()
```

### Exercise 3 — Count rows without loading the full file
```python
# TODO: Use chunked reading to count the number of rows
# where amount > 1000 in "large_sales.csv"
# Do NOT load the entire file into memory at once
```

---

## Lesson Recap

1. **Pandas defaults** allocate more memory than necessary — `int64`, `float64`, and `object` dtypes are the main culprits.
2. **Dtype optimization** (downcasting integers, floats, and converting strings to `category`) typically reduces DataFrame size by 50–80% for free.
3. **Chunk processing** with `chunksize` turns memory-bound problems into time-bound ones — any file can be processed in any amount of RAM given enough chunks.
4. **Vectorized operations** replace Python loops and run 10–100× faster because they execute in compiled C rather than interpreted Python.

---

## Knowledge Check

**Q1.** A column contains the values "Pass", "Fail", "Pending" repeated 2 million times. Which dtype change would save the most memory?  
**Answer:** Convert from `object` to `category`. There are only 3 unique values, so instead of storing 2 million Python strings, pandas stores 3 strings and 2 million integers (the category codes).

**Q2.** Your script crashes with `MemoryError` when reading a 15 GB CSV on a machine with 8 GB RAM. What is the correct approach?  
**Answer:** Use chunked reading with `pd.read_csv("file.csv", chunksize=N)` to process the file in batches that fit in memory.

**Q3.** True or False: `df.iterrows()` is the recommended way to update values in a large DataFrame.  
**Answer:** False. `iterrows()` is extremely slow on large DataFrames because it creates a Python object for every row. Vectorized operations or `df.apply()` are the correct approach.

---

## Next Lesson
**Lesson 04 — Efficient Storage: Parquet & Columnar Formats**  
Now that you know how to handle large data in memory, you'll learn how to store it efficiently on disk. Parquet files load faster, compress better, and are the standard format in modern data platforms — here's why and how.
