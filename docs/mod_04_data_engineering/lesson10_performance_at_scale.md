# Lesson 10 — Performance at Scale

**Track:** Data Engineering for Analysts  
**Module:** Module 4 — Production Engineering  
**Difficulty:** Intermediate | **Duration:** 12 min  
**Sources:** M5-L11 (Parallel Processing) · M5-L12 (Dask Basics — trimmed to awareness) · M5-L13 (Performance Profiling) · M5-L14 (Real Large Data Project) · M5-L15 (Performance Best Practices)

---

## Learning Objectives

1. **Profile a pipeline** — Use timing and memory profiling tools to identify where a pipeline spends its time.
2. **Parallel processing** — Use `concurrent.futures` to process multiple files or partitions simultaneously.
3. **Dask awareness** — Understand what Dask is and when to reach for it (without needing to master it).
4. **Best practices checklist** — Apply the 10-point performance checklist to any large-data pipeline.

> By the end of this lesson you'll be able to measure a pipeline's performance accurately and apply the most impactful optimizations first.

---

## Overview

### Hook
Optimizing a pipeline without profiling it first is guesswork. Data engineers who profile before optimizing consistently find that 80% of a pipeline's time is spent in one or two steps — and those steps are almost never what they expected. Measure first. Optimize second.

### Analogy: The Race Car Pit Stop Analysis
Think of performance optimization like a Formula 1 team analyzing a pit stop. Before improving anything, they review telemetry data to see exactly where time was lost — was it the wheel change, the refueling, the driver reaction, or time getting into the pit lane? Without the telemetry, they'd be guessing. **Profiling** is your telemetry. Once you know where the time goes, you fix the exact bottleneck — not your second best guess.

| Performance Concept | Pit Stop Analogy |
|-------------------|-----------------|
| **Profiling** | Reviewing lap telemetry data |
| **Identifying bottlenecks** | Finding which wheel change was slowest |
| **Parallel processing** | Multiple mechanics working different wheels simultaneously |
| **Dask** | A second team car — extra capacity for extremely large jobs |
| **Best practices** | The standard operating procedures that keep every pit stop under 3 seconds |

> **Key takeaway:** A 10× speedup from profiling and targeting the real bottleneck beats a 2× speedup from blindly parallelizing code that wasn't the problem.

---

## Key Takeaways

### 1. Profile Before You Optimize
The fastest code to write is code that doesn't need to be optimized — because you measured and found the slow step is actually the network call, not your transform function. `%timeit`, `time.perf_counter()`, and `memory_profiler` are your three essential tools.  
**Keywords:** %timeit · time.perf_counter · memory_profiler · Bottleneck identification

### 2. `concurrent.futures` Is the Right Parallelism Tool for Most DE Work
`multiprocessing` is complex. `threading` is limited by Python's GIL for CPU-bound work. `concurrent.futures.ProcessPoolExecutor` gives you multi-core parallelism with a clean, simple API — submit a function and a list of inputs, get back a list of results.  
**Keywords:** ProcessPoolExecutor · map() · CPU-bound · GIL

### 3. Dask Exists for When Data Truly Doesn't Fit in RAM
Dask extends pandas DataFrames to work on data distributed across many machines or too large for a single machine's RAM. It uses the same API as pandas. You're unlikely to need it as an analyst exploring DE — but knowing it exists prevents you from manually reinventing distributed processing with loops.  
**Keywords:** Dask DataFrame · Delayed execution · Distributed · Out-of-core

---

## Key Concepts

### Three Profiling Tools

```python
# Tool 1: time.perf_counter — time any block of code
import time
t0 = time.perf_counter()
result = some_function()
elapsed = time.perf_counter() - t0
print(f"{elapsed:.3f}s")

# Tool 2: %timeit in Jupyter — accurate micro-benchmarks
%timeit df["amount"].sum()                    # runs 1000 times, reports average

# Tool 3: memory_profiler — see memory per line
from memory_profiler import memory_usage
mem = memory_usage((my_function, (df,)))      # peak MB used
print(f"Peak memory: {max(mem):.1f} MB")
```

### concurrent.futures — parallel file processing
```python
from concurrent.futures import ProcessPoolExecutor

def process_file(filepath: str) -> pd.DataFrame:
    """Process one file — called in parallel."""
    df = pd.read_parquet(filepath)
    # ... transform ...
    return df

files = ["data/jan.parquet", "data/feb.parquet", "data/mar.parquet"]

# Sequential — one file at a time
results = [process_file(f) for f in files]

# Parallel — all files at once (across all CPU cores)
with ProcessPoolExecutor() as executor:
    results = list(executor.map(process_file, files))

combined = pd.concat(results)
```

### Dask in Brief
```python
import dask.dataframe as dd

# Same API as pandas but works on data larger than RAM
ddf = dd.read_parquet("data/*.parquet")        # lazy — nothing read yet

result = (
    ddf[ddf["amount"] > 100]
       .groupby("region")["amount"]
       .sum()
       .compute()                                # compute() = Dask's .collect()
)
# Dask splits the work across all files and CPU cores automatically
```

---

## Code Examples

### Example 1: Profile a pipeline step-by-step
```python
import time, pandas as pd
import sqlalchemy

def run_pipeline_with_timing():
    timings = {}

    # Extract
    t = time.perf_counter()
    raw = pd.read_csv("orders.csv")
    timings["extract"] = time.perf_counter() - t

    # Optimize dtypes
    t = time.perf_counter()
    for col in raw.select_dtypes("int64"):
        raw[col] = pd.to_numeric(raw[col], downcast="integer")
    for col in raw.select_dtypes("float64"):
        raw[col] = pd.to_numeric(raw[col], downcast="float")
    for col in raw.select_dtypes("object"):
        if raw[col].nunique() / len(raw) < 0.05:
            raw[col] = raw[col].astype("category")
    timings["optimize_dtypes"] = time.perf_counter() - t

    # Transform
    t = time.perf_counter()
    clean = transform(raw)
    timings["transform"] = time.perf_counter() - t

    # Load
    t = time.perf_counter()
    engine = sqlalchemy.create_engine("sqlite:///warehouse.db")
    clean.to_sql("orders", engine, if_exists="replace", index=False)
    timings["load"] = time.perf_counter() - t

    # Report
    total = sum(timings.values())
    print(f"\n{'Step':<20} {'Time':>8} {'% of Total':>12}")
    print("-" * 42)
    for step, t in sorted(timings.items(), key=lambda x: -x[1]):
        print(f"{step:<20} {t:>7.2f}s {(t/total*100):>11.1f}%")
    print(f"\n{'TOTAL':<20} {total:>7.2f}s")
```
**Terminal output:**
```
Step                   Time  % of Total
------------------------------------------
load                  8.21s       67.3%
extract               2.04s       16.7%
transform             1.42s       11.6%
optimize_dtypes       0.55s        4.5%

TOTAL                12.22s
```
The load step is the bottleneck — worth investigating bulk load options before optimizing the transform.

### Example 2: ProcessPoolExecutor for parallel file processing
```python
from concurrent.futures import ProcessPoolExecutor, as_completed
import pandas as pd
import glob, time

def process_monthly_file(filepath: str) -> dict:
    """Process one month of sales data. Returns summary dict."""
    df = pd.read_parquet(filepath)
    return {
        "file":    filepath,
        "rows":    len(df),
        "revenue": df["amount"].sum(),
        "orders":  df["order_id"].nunique()
    }

files = sorted(glob.glob("data/sales_*.parquet"))

# Sequential baseline
t0 = time.perf_counter()
sequential = [process_monthly_file(f) for f in files]
seq_time = time.perf_counter() - t0

# Parallel — uses all CPU cores
t0 = time.perf_counter()
with ProcessPoolExecutor() as executor:
    parallel = list(executor.map(process_monthly_file, files))
par_time = time.perf_counter() - t0

print(f"Sequential: {seq_time:.1f}s  Parallel: {par_time:.1f}s  Speedup: {seq_time/par_time:.1f}x")

# Combine results
summary = pd.DataFrame(parallel).sort_values("file")
print(summary)
```

### Example 3: Memory profiling a DataFrame operation
```python
from memory_profiler import profile

@profile   # decorator — adds line-by-line memory tracking
def load_and_process(filepath: str) -> pd.DataFrame:
    df = pd.read_csv(filepath)                             # Line 1: peak load
    df = df.dropna()                                       # Line 2: small drop
    df["amount"] = df["amount"].astype("float32")          # Line 3: downcast
    df["region"] = df["region"].astype("category")         # Line 4: categorize
    result = df.groupby("region")["amount"].sum()          # Line 5: aggregate
    del df                                                  # Line 6: free memory
    return result

result = load_and_process("large_sales.csv")
```
**Sample output:**
```
Line #    Mem usage   Increment   Line Contents
==============================================
     1    245.3 MiB  +412.1 MiB  df = pd.read_csv(filepath)
     2    221.8 MiB   -23.5 MiB  df = df.dropna()
     3    184.2 MiB   -37.6 MiB  df["amount"] = df["amount"].astype("float32")
     4    134.1 MiB   -50.1 MiB  df["region"] = df["region"].astype("category")
     5    135.0 MiB    +0.9 MiB  result = df.groupby(...)["amount"].sum()
     6     89.3 MiB   -45.7 MiB  del df
```

### Example 4: Performance best practices applied
```python
import pandas as pd, pyarrow.parquet as pq

# ✓ Practice 1: Use Parquet instead of CSV for repeated reads
pq.write_table(pa.Table.from_pandas(df), "clean.parquet")

# ✓ Practice 2: Select only the columns you need
df = pd.read_parquet("clean.parquet", columns=["id", "amount", "region"])

# ✓ Practice 3: Downcast dtypes immediately after reading
df["amount"] = df["amount"].astype("float32")
df["region"] = df["region"].astype("category")

# ✓ Practice 4: Avoid chained indexing — creates hidden copies
# WRONG: df["region"][df["amount"] > 100]
# RIGHT:
mask = df["amount"] > 100
result = df.loc[mask, "region"]

# ✓ Practice 5: Delete large objects you no longer need
raw_df = pd.read_csv("huge.csv")
clean_df = transform(raw_df)
del raw_df    # frees ~400 MB before the load step

# ✓ Practice 6: Use vectorized operations — never iterrows for computations
df["tax"] = df["amount"] * 0.1          # NOT iterrows()

# ✓ Practice 7: Batch database loads (not row-by-row inserts)
df.to_sql("table", engine, method="multi", chunksize=10_000)

# ✓ Practice 8: Profile before optimizing — find the real bottleneck
```

---

## Common Mistakes

### Mistake 1: Optimizing the wrong thing without profiling
```python
# Spent 2 hours optimizing the transform step (saves 0.3s)
# ...but the load step takes 12 seconds and could be 2s with bulk insert
# → Always profile first to find the real bottleneck
```

### Mistake 2: Using threading for CPU-bound work
```python
# WRONG for CPU-bound tasks — Python's GIL limits threads to one at a time
from concurrent.futures import ThreadPoolExecutor
with ThreadPoolExecutor(max_workers=8) as ex:
    results = list(ex.map(cpu_heavy_transform, chunks))   # still runs serially

# RIGHT for CPU-bound tasks — processes have separate GILs
from concurrent.futures import ProcessPoolExecutor
with ProcessPoolExecutor(max_workers=8) as ex:
    results = list(ex.map(cpu_heavy_transform, chunks))   # truly parallel
```

### Mistake 3: Parallelizing I/O-bound work with processes instead of threads
```python
# I/O-bound work (API calls, DB queries) — threads are fine and lighter
from concurrent.futures import ThreadPoolExecutor
with ThreadPoolExecutor(max_workers=20) as ex:
    results = list(ex.map(fetch_from_api, user_ids))   # 20 concurrent requests
```

---

## Performance Best Practices Checklist

| # | Practice | Impact |
|---|----------|--------|
| 1 | Profile before optimizing | Ensures you fix the real bottleneck |
| 2 | Use Parquet instead of CSV for repeated reads | 5–15× faster reads |
| 3 | Select only needed columns (`usecols`, `columns=`) | Reduces I/O by 50–90% |
| 4 | Downcast dtypes immediately after reading | 50–80% memory reduction |
| 5 | Convert low-cardinality strings to `category` | 70–95% memory reduction |
| 6 | Use vectorized operations, never iterrows() | 10–100× faster |
| 7 | Delete large objects when finished with them | Prevents out-of-memory |
| 8 | Batch database loads (method="multi") | 5–20× faster DB writes |
| 9 | Parallelize independent file/partition processing | Up to N× speedup (N = cores) |
| 10 | Schedule profiling as a regular pipeline step | Catches regressions early |

---

## Practice Exercises

### Exercise 1 — Find and measure the bottleneck
```python
import time, pandas as pd

# TODO: Add timing instrumentation to each step of this pipeline
# and print a table showing which step takes the longest percentage of time.

def run():
    df = pd.read_csv("large_orders.csv")
    df = df.dropna(subset=["amount", "order_id"])
    df["amount"] = df["amount"].astype("float32")
    df["region"] = df["region"].astype("category")
    result = df.groupby("region")["amount"].agg(["sum", "mean", "count"])
    result.to_csv("region_summary.csv")
    return result
```

### Exercise 2 — Parallelize file processing
```python
import glob, pandas as pd

files = glob.glob("monthly_data/*.parquet")

# TODO: Write a function that processes one file (filter, aggregate)
# TODO: Run it sequentially and time it
# TODO: Run it in parallel with ProcessPoolExecutor and time it
# TODO: Confirm both produce identical results
```

### Exercise 3 — Apply the checklist
```python
# This pipeline loads a 10-million-row CSV and is slow.
# TODO: Apply as many items from the performance checklist as possible.
# TODO: Measure the before and after times.

def slow_pipeline():
    df = pd.read_csv("big_data.csv")
    total = 0
    for i, row in df.iterrows():
        if row["status"] == "completed":
            total += row["amount"]
    print(f"Total: {total}")
```

---

## Lesson Recap

1. **Profile first** — use `time.perf_counter()` and `memory_profiler` to find the actual bottleneck before writing a single line of optimization.
2. **`concurrent.futures.ProcessPoolExecutor`** is the simplest way to run CPU-bound pipeline steps in parallel across all CPU cores — processing 8 files at once on an 8-core machine is an 8× speedup.
3. **Dask** extends the pandas API to data larger than RAM or distributed across many machines — know it exists and use it when your data genuinely exceeds a single machine's capacity.
4. **The 10-point performance checklist** — Parquet, column selection, dtype downcasting, categoricals, vectorization, batched I/O, parallel processing, and profiling — applied together can turn a 30-minute pipeline into a 3-minute one.

---

## Knowledge Check

**Q1.** You profile your pipeline and find that the transformation step takes 2 seconds but the database load step takes 45 seconds. Where should you focus your optimization effort?  
**Answer:** The database load step — it accounts for 95%+ of the runtime. Optimizing the transform step would have almost no impact on the total. Use bulk loading (`method="multi"`, `COPY` commands, or SQLAlchemy's bulk insert) to speed up the load.

**Q2.** When should you use `ThreadPoolExecutor` versus `ProcessPoolExecutor`?  
**Answer:** Use `ThreadPoolExecutor` for I/O-bound tasks (API calls, file reads, network requests) where Python's GIL isn't a bottleneck. Use `ProcessPoolExecutor` for CPU-bound tasks (data transformations, calculations) where you need true parallel execution across multiple CPU cores.

**Q3.** What is Dask and in what scenario would an analyst-turned-engineer actually need it?  
**Answer:** Dask is a library that extends pandas DataFrames to work on data distributed across many machines or larger than RAM. An analyst-turned-DE would need it when processing a dataset too large to fit in a single machine's memory (e.g. 200 GB of logs) and when Polars + chunked processing are not sufficient.

---

## Track Complete 🎉
You've completed all 10 lessons of **Data Engineering for Analysts**. You can now build production-grade ETL pipelines, handle large-scale data efficiently, collect data from APIs, validate quality, deploy to CI/CD, and optimize for performance. These are the core skills of a junior data engineer — and a uniquely valuable extension of your analytics background.
