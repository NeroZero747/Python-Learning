# Lesson 04 — Efficient Storage: Parquet & Columnar Formats

**Track:** Data Engineering for Analysts  
**Module:** Module 1 — Data Engineering Foundations  
**Difficulty:** Beginner | **Duration:** 10 min  
**Sources:** M1-L05 (Parquet & Efficient Storage) · M5-L05 (Columnar Storage — concepts trim) · M5-L06 (Parquet Files — merged) · M5-L07 (PyArrow Basics)

---

## Learning Objectives

1. **Explain columnar storage** — Describe why column-oriented files are faster for analytics than row-oriented files like CSV.
2. **Read and write Parquet** — Use pandas and PyArrow to convert CSVs to Parquet and query them efficiently.
3. **Column selection & predicate pushdown** — Load only the columns and rows you need, skipping data at the file level.
4. **Know when to convert** — Identify when replacing CSV with Parquet in your workflow gives the biggest benefit.

> By the end of this lesson you'll know why every modern data platform defaults to Parquet — and how to use it in your own pipelines.

---

## Overview

### Hook
A CSV stores data the way a spreadsheet does — one row at a time, left to right. Parquet stores it the way an analytics engine thinks — one column at a time, compressed per column. That single difference makes Parquet 5–20× faster to query and 3–10× smaller on disk.

### Analogy: The Filing Cabinet vs the Spreadsheet Binder
Think of row vs column storage like two ways of organizing employee records. A **row store** (CSV) is like a binder where each page holds one employee's complete record — name, salary, department, start date, all on one page. Useful when you need everything about one person. A **column store** (Parquet) is like a set of indexed folders — one folder for all names, one for all salaries, one for all departments. Useful when you ask "what is the average salary?" — you only open the salary folder, not every page.

| Storage Type | Analogy | Best For |
|-------------|---------|---------|
| **CSV (row store)** | One page per employee | Exporting a full record |
| **Parquet (column store)** | Indexed folders by field | Aggregating one field across all records |

> **Key takeaway:** For analytics workloads — aggregations, filters, selecting specific columns — columnar storage is almost always faster and smaller than CSV.

---

## Key Takeaways

### 1. Parquet Is the Standard for Data Engineering
Every major data platform — BigQuery, Snowflake, Databricks, AWS Athena — uses columnar storage internally or accepts Parquet as the native import format. If you work in DE, you will work with Parquet constantly.  
**Keywords:** Parquet · Columnar · Industry standard

### 2. Column Selection Happens at the File Level
Unlike CSV (where you must read the full row to access any column), Parquet lets you request specific columns and the file reader skips everything else. On a 200-column dataset where you only need 4 columns, Parquet reads 98% less data than CSV.  
**Keywords:** Column pruning · Predicate pushdown · Selective reads

### 3. PyArrow Is the Engine Underneath
When you call `pd.read_parquet()`, pandas delegates the work to PyArrow — a Python binding for the Apache Arrow in-memory columnar format. PyArrow handles compression, encoding, and zero-copy reads. You usually don't need to call PyArrow directly, but it's good to know what powers the operation.  
**Keywords:** PyArrow · Apache Arrow · Zero-copy · In-memory format

---

## Key Concepts

### Row Store vs Column Store — Reading Pattern
```
CSV (row store) — reading "average salary":
Row 1: [Alice, Engineering, 85000, 2019]  ← read all 4 fields
Row 2: [Bob,   Marketing,   72000, 2021]  ← read all 4 fields
Row 3: [Carol, Engineering, 91000, 2020]  ← read all 4 fields
→ Must scan entire file to get just the salary column

Parquet (column store) — reading "average salary":
salary column: [85000, 72000, 91000, ...]  ← read this column only
→ Skips name, department, start_date entirely
```

### Parquet File Structure
- **Row groups** — data is split into horizontal chunks (e.g. 128 MB per group)
- **Column chunks** — within each row group, each column is stored contiguously
- **Metadata footer** — stores column statistics (min, max, null count) used for predicate pushdown
- **Compression** — each column chunk is compressed independently (Snappy by default)

### Writing Parquet with pandas
```python
import pandas as pd

df = pd.read_csv("sales.csv")

# Write to Parquet — default compression is snappy
df.to_parquet("sales.parquet", index=False)

# Read back
df_back = pd.read_parquet("sales.parquet")
```

### Reading with column selection (the big win)
```python
# Load only the columns you need — Parquet skips the rest at the file level
df = pd.read_parquet(
    "sales.parquet",
    columns=["order_id", "amount", "region"]  # 3 of maybe 50 columns
)
```

---

## Code Examples

### Example 1: CSV vs Parquet — size and speed comparison
```python
import pandas as pd
import time, os

# Write CSV
df.to_csv("sales.csv", index=False)

# Write Parquet
df.to_parquet("sales.parquet", index=False)

# Compare file sizes
csv_mb  = os.path.getsize("sales.csv")    / 1024**2
pq_mb   = os.path.getsize("sales.parquet")/ 1024**2
print(f"CSV:     {csv_mb:.1f} MB")
print(f"Parquet: {pq_mb:.1f} MB  ({csv_mb/pq_mb:.1f}x smaller)")

# Compare read speed for a single column
t0 = time.perf_counter()
pd.read_csv("sales.csv")["amount"].sum()
csv_time = time.perf_counter() - t0

t0 = time.perf_counter()
pd.read_parquet("sales.parquet", columns=["amount"])["amount"].sum()
pq_time = time.perf_counter() - t0

print(f"CSV read:     {csv_time:.2f}s")
print(f"Parquet read: {pq_time:.2f}s  ({csv_time/pq_time:.1f}x faster)")
```
**Terminal output:**
```
CSV:     412.3 MB
Parquet:  58.7 MB  (7.0x smaller)
CSV read:     8.41s
Parquet read: 0.73s  (11.5x faster)
```

### Example 2: Writing Parquet with partitioning
```python
# Partition by year and region — creates a folder hierarchy
# Useful when pipelines only need to read one partition
df.to_parquet(
    "sales_partitioned/",
    partition_cols=["year", "region"],
    index=False
)

# Folder structure created:
# sales_partitioned/year=2024/region=EMEA/part-0.parquet
# sales_partitioned/year=2024/region=APAC/part-0.parquet
# sales_partitioned/year=2025/region=EMEA/part-0.parquet
# ...

# Reading only 2025 EMEA data — skips all other partitions entirely
df_emea_2025 = pd.read_parquet(
    "sales_partitioned/",
    filters=[("year", "==", 2025), ("region", "==", "EMEA")]
)
```

### Example 3: PyArrow for finer control
```python
import pyarrow as pa
import pyarrow.parquet as pq

# Convert DataFrame to Arrow table (in-memory columnar format)
table = pa.Table.from_pandas(df)

# Write with explicit compression
pq.write_table(
    table,
    "sales.parquet",
    compression="snappy",     # also: "gzip", "brotli", "zstd"
    row_group_size=100_000    # tune for your read patterns
)

# Read with predicate pushdown — skips row groups where max < filter
dataset = pq.read_table(
    "sales.parquet",
    columns=["order_id", "amount"],
    filters=[("amount", ">", 1000)]   # server-side filter
)
df = dataset.to_pandas()
```

### Example 4: Best-practice pipeline — CSV in, Parquet out
```python
import pandas as pd, os

RAW_DIR = "raw/"
CLEAN_DIR = "clean/"

def csv_to_parquet(filename: str) -> None:
    """Read a raw CSV, optimize dtypes, and save as Parquet."""
    df = pd.read_csv(os.path.join(RAW_DIR, filename))

    # Optimize dtypes before saving
    for col in df.select_dtypes("int64"):
        df[col] = pd.to_numeric(df[col], downcast="integer")
    for col in df.select_dtypes("float64"):
        df[col] = pd.to_numeric(df[col], downcast="float")
    for col in df.select_dtypes("object"):
        if df[col].nunique() / len(df) < 0.1:
            df[col] = df[col].astype("category")

    out = os.path.join(CLEAN_DIR, filename.replace(".csv", ".parquet"))
    df.to_parquet(out, index=False)
    print(f"Saved {filename} → {out}  ({len(df):,} rows)")

csv_to_parquet("orders.csv")
```

---

## Common Mistakes

### Mistake 1: Saving Parquet with the index included
```python
# WRONG — creates a useless integer index column in the file
df.to_parquet("data.parquet")

# RIGHT — exclude the index unless you specifically need it
df.to_parquet("data.parquet", index=False)
```

### Mistake 2: Loading all columns when you need only a few
```python
# WRONG — loads entire file including 40 columns you don't need
df = pd.read_parquet("wide_table.parquet")
result = df["amount"].sum()

# RIGHT — column selection at the file level (skips everything else)
result = pd.read_parquet("wide_table.parquet", columns=["amount"])["amount"].sum()
```

### Mistake 3: Partitioning by a high-cardinality column
```python
# WRONG — creates thousands of tiny files (one per unique order_id)
df.to_parquet("data/", partition_cols=["order_id"])

# RIGHT — partition by a low-cardinality column (date, region, category)
df.to_parquet("data/", partition_cols=["year", "region"])
```

---

## Practice Exercises

### Exercise 1 — Convert your first CSV to Parquet
```python
import pandas as pd, os

# TODO: Read sample_data.csv
# TODO: Write it to sample_data.parquet with index=False
# TODO: Print the file size difference in MB
```

### Exercise 2 — Selective column read
```python
import pandas as pd

# Given a wide Parquet file with 30 columns,
# TODO: Read ONLY the columns: customer_id, order_date, total
# TODO: Calculate the mean total by month
# HINT: pd.read_parquet supports a 'columns' parameter
```

### Exercise 3 — Benchmark it
```python
import pandas as pd, time

# TODO: Read a CSV file and time it
# TODO: Convert it to Parquet
# TODO: Read the Parquet file (same columns) and time it
# TODO: Print the speedup ratio
```

---

## Lesson Recap

1. **Columnar storage** (Parquet) is faster for analytics than row storage (CSV) because reading one column doesn't require reading any other column.
2. **Parquet files** are typically 5–10× smaller than equivalent CSVs and 5–15× faster to read for analytical queries due to compression and columnar layout.
3. **Column selection** (`columns=["a","b"]`) and **predicate pushdown** (server-side filters) let you skip data at the file level — a major advantage over CSV.
4. **PyArrow** powers pandas' Parquet support and provides finer control over compression, row groups, and partitioning when you need it.

---

## Knowledge Check

**Q1.** Why is Parquet faster than CSV when calculating the sum of one column on a 50-column dataset?  
**Answer:** Parquet stores each column contiguously and allows column-level skipping. Reading the sum column only touches that column's data — it skips the other 49 columns entirely. CSV must read every byte of every row to reach any column.

**Q2.** What does "predicate pushdown" mean in the context of Parquet?  
**Answer:** The file reader evaluates filter conditions (like `amount > 1000`) against the row group metadata (min/max statistics) before reading the actual data, skipping entire row groups that can't satisfy the filter. This reduces I/O significantly.

**Q3.** You have a Parquet file partitioned by `year` and `region`. How do you read only 2024 data from the APAC region?  
**Answer:** Use the `filters` parameter: `pd.read_parquet("data/", filters=[("year", "==", 2024), ("region", "==", "APAC")])`. Pandas/PyArrow will skip all other partitions entirely.

---

## Next Lesson
**Lesson 05 — Faster DataFrames: Polars & DuckDB**  
Parquet solves storage efficiency. Now you'll meet the tools that solve compute efficiency — Polars for multi-threaded DataFrames and DuckDB for running SQL directly on files.
