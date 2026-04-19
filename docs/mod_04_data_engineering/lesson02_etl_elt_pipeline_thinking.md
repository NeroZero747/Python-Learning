# Lesson 02 — ETL, ELT & Pipeline Thinking

**Track:** Data Engineering for Analysts  
**Module:** Module 1 — Data Engineering Foundations  
**Difficulty:** Beginner | **Duration:** 12 min  
**Sources:** M1-L02 (ETL vs ELT) · M1-L07 (Pipeline Design Concepts) · M4-L01 (What Is a Data Pipeline?) · M4-L02 (ETL vs ELT — merged) · M4-L03 (Pipeline Design Patterns)

---

## Learning Objectives

1. **Contrast ETL and ELT** — Explain the difference and identify when each pattern is appropriate.
2. **Pipeline design principles** — Describe what makes a pipeline reliable, idempotent, and debuggable.
3. **Common patterns** — Recognize batch vs streaming and fan-out/merge architectures.
4. **Write modular code** — Structure an ETL pipeline as separate, testable functions.

> By the end of this lesson you will be able to design a data pipeline on paper and explain your choices to a colleague.

---

## Overview

### Hook
A data pipeline is the automated replacement for the copy-paste-clean routine that every analyst does manually — except it runs on a schedule, handles any data volume, and never forgets a step.

### Analogy: The Assembly Line
Think of an ETL pipeline like a car assembly line. Each station performs one specific job in a fixed sequence: the frame arrives, then the engine is fitted, then the bodywork, then the inspection. No station skips ahead, and every car that exits has gone through every step. A **data pipeline** works the same way — raw data arrives, passes through each defined stage, and emerges as a clean, structured result ready to use.

| Pipeline Stage | Assembly Line Equivalent |
|---------------|------------------------|
| **Extract** | Raw materials delivered to the factory floor |
| **Transform** | Each station shapes the part to specification |
| **Load** | Finished car exits onto the delivery lot |
| **Validation** | Quality control inspector checks each vehicle |

> **Key takeaway:** Whether you choose ETL or ELT depends on one question: is it cheaper to clean data before or after you store it? Modern cloud warehouses have made "after" increasingly practical.

---

## Key Takeaways

### 1. ETL: Clean Before You Store
In ETL (Extract → Transform → Load), you clean and reshape data before it ever reaches the destination. This approach is best when your destination has strict schemas, limited storage, or when you want to keep raw data out of the warehouse entirely.  
**Keywords:** Strict schema · Pre-processing · Privacy

### 2. ELT: Store First, Transform Later
In ELT (Extract → Load → Transform), you store raw data as-is first, then run transformations inside the warehouse using SQL or tools like dbt. Modern warehouses (BigQuery, Snowflake) make this fast and cheap. Analysts can then run their own transformations without waiting for engineering.  
**Keywords:** Raw storage · dbt · Warehouse-native · Flexibility

### 3. Good Pipelines Are Idempotent
An **idempotent** pipeline produces the same result no matter how many times you run it with the same input. This is critical: if your pipeline crashes at 2 AM and re-runs at 3 AM, the output should be identical. Avoid appending rows without deduplication, and avoid side effects that accumulate.  
**Keywords:** Idempotency · Rerunnable · Reliability

---

## Key Concepts

### ETL (Extract, Transform, Load)
Transform data before loading it to the destination.

```
Source → [Extract] → [Transform] → [Load] → Warehouse
         (Python)     (Python)      (SQL insert)
```

**Use ETL when:**
- Your destination has a rigid schema and can't store messy raw data
- You need to anonymize or mask PII before it touches the warehouse
- Your transformations are complex and must happen in Python (not SQL)

### ELT (Extract, Load, Transform)
Load raw data first, then transform it inside the warehouse.

```
Source → [Extract] → [Load raw] → [Transform in warehouse] → Clean table
         (Python)     (Python)     (SQL / dbt)
```

**Use ELT when:**
- Your warehouse is powerful enough to transform large data cheaply (BigQuery, Snowflake)
- You want analysts to define their own transformation logic
- You want to preserve the raw data for future re-processing

### Pipeline Design Principles

| Principle | What it means | Why it matters |
|-----------|--------------|----------------|
| **Idempotency** | Same input → same output, every time | Safe to re-run after a failure |
| **Modularity** | Each function does one thing | Easy to test individually |
| **Observability** | Log what happened at each step | Know *where* a failure occurred |
| **Fail-fast** | Assert expectations early | Catch bad data before it propagates |
| **Backfill-ready** | Can re-process historical data | Useful when source data arrives late |

### Batch vs Streaming

| | Batch | Streaming |
|--|--|--|
| **When it runs** | On a schedule (e.g. nightly at 2 AM) | Continuously, as events arrive |
| **Latency** | Hours to a day | Seconds to minutes |
| **Complexity** | Low — easier to build and debug | High — requires message queues (Kafka, Pub/Sub) |
| **Best for** | Daily reports, warehouse refreshes | Fraud detection, live dashboards |

For most analysts transitioning to DE, batch pipelines are the starting point.

---

## Code Examples

### Example 1: A complete ETL pipeline with separate functions
```python
# etl_pipeline.py
import pandas as pd
import sqlalchemy

# ── EXTRACT ──────────────────────────────────────────────
def extract(filepath: str) -> pd.DataFrame:
    """Read raw sales data from a CSV file."""
    return pd.read_csv(filepath)

# ── TRANSFORM ─────────────────────────────────────────────
def transform(df: pd.DataFrame) -> pd.DataFrame:
    """Clean and reshape the raw sales data."""
    df = df.dropna(subset=["sale_date", "amount"])       # drop incomplete rows
    df["sale_date"] = pd.to_datetime(df["sale_date"])    # parse dates
    df["amount"] = df["amount"].abs()                     # amounts must be positive
    df = df[df["amount"] > 0]                             # filter zero-value rows
    df["year_month"] = df["sale_date"].dt.to_period("M") # add derived column
    return df

# ── LOAD ──────────────────────────────────────────────────
def load(df: pd.DataFrame, table: str, engine) -> None:
    """Write clean data to the warehouse.  Replaces the table each run (idempotent)."""
    df.to_sql(table, con=engine, if_exists="replace", index=False)
    print(f"Loaded {len(df):,} rows into '{table}'.")

# ── ORCHESTRATE ───────────────────────────────────────────
def run():
    engine = sqlalchemy.create_engine("sqlite:///warehouse.db")
    raw    = extract("sales_raw.csv")
    clean  = transform(raw)
    load(clean, "clean_sales", engine)

if __name__ == "__main__":
    run()
```
**Terminal output:**
```
Loaded 14,832 rows into 'clean_sales'.
```

### Example 2: Making a pipeline idempotent with UPSERT logic
```python
# Instead of blindly appending, upsert by primary key so re-runs are safe
from sqlalchemy.dialects.postgresql import insert

def load_idempotent(df, table_name, engine, unique_key="order_id"):
    """Insert rows; update them if the key already exists."""
    with engine.connect() as conn:
        for _, row in df.iterrows():
            stmt = insert(table_name).values(**row)
            stmt = stmt.on_conflict_do_update(
                index_elements=[unique_key],
                set_=row.to_dict()            # overwrite all columns on conflict
            )
            conn.execute(stmt)
```

### Example 3: ELT pattern — raw load then SQL transform
```python
# Step 1 (Python): load raw data as-is, preserving everything
raw_df.to_sql("raw_orders", con=engine, if_exists="replace", index=False)

# Step 2 (SQL inside warehouse): the transformation runs in the database
TRANSFORM_SQL = """
CREATE OR REPLACE TABLE clean_orders AS
SELECT
    order_id,
    CAST(order_date AS DATE)     AS order_date,
    ABS(amount)                   AS amount,
    UPPER(TRIM(region))           AS region
FROM raw_orders
WHERE amount IS NOT NULL
  AND order_id IS NOT NULL
"""
with engine.connect() as conn:
    conn.execute(TRANSFORM_SQL)
```

### Example 4: Logging pipeline progress
```python
import logging, time

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
log = logging.getLogger(__name__)

def run():
    log.info("Pipeline started")
    t0 = time.perf_counter()

    raw = extract("sales_raw.csv")
    log.info(f"Extracted {len(raw):,} rows")

    clean = transform(raw)
    log.info(f"Transformed: {len(clean):,} rows retained")

    load(clean, "clean_sales", engine)
    log.info(f"Pipeline complete in {time.perf_counter()-t0:.1f}s")
```

---

## Common Mistakes

### Mistake 1: Appending without deduplication (breaks idempotency)
```python
# WRONG — Running this twice will double every row
df.to_sql("sales", con=engine, if_exists="append")

# RIGHT — Use replace (full refresh) or upsert (incremental + safe)
df.to_sql("sales", con=engine, if_exists="replace")
```

### Mistake 2: Putting all logic in one giant function
```python
# WRONG — impossible to test or debug
def run_everything():
    df = pd.read_csv("data.csv")
    df = df.dropna()
    df["date"] = pd.to_datetime(df["date"])
    df.to_sql("table", engine, if_exists="replace")

# RIGHT — each step is separately testable
raw   = extract("data.csv")
clean = transform(raw)
load(clean, "table", engine)
```

### Mistake 3: Choosing ETL vs ELT without considering your warehouse
If you're working with SQLite or a small Postgres instance, ETL in Python is appropriate. If you're working with BigQuery or Snowflake, ELT is almost always faster and cheaper — the warehouse is purpose-built to run transformations at scale.

---

## Practice Exercises

### Exercise 1 — Complete the transform
```python
import pandas as pd

def transform(df):
    # TODO: drop rows where 'customer_id' or 'total' is null
    # TODO: convert 'order_date' to datetime
    # TODO: filter out rows where total < 0
    # TODO: add a column 'tax' = total * 0.1
    return df

raw = pd.read_csv("orders.csv")
clean = transform(raw)
print(clean.head())
```

### Exercise 2 — Classify the pattern
For each scenario below, decide: ETL or ELT?
1. You work with sensitive health records and must anonymize before storing.
2. You pull raw event logs into BigQuery and let analysts write dbt models.
3. Your destination is an Excel file that must have exactly 5 columns.
4. You load tweets into Snowflake and parse hashtags with SQL later.

**Answers:** 1. ETL, 2. ELT, 3. ETL, 4. ELT

### Exercise 3 — Make it idempotent
```python
# This pipeline appends rows every run — fix it to be idempotent
def load(df, engine):
    df.to_sql("events", engine, if_exists="append", index=False)
    # HINT: What if_exists value makes this safe to re-run?
    # HINT: What check could you add first to avoid duplicates?
```

---

## Lesson Recap

1. **ETL** transforms data before loading it — ideal when your destination has a rigid schema or data must be cleaned before storage.
2. **ELT** loads raw data first and transforms inside the warehouse — ideal for modern cloud platforms where SQL transformations are fast and analysts can own their own logic.
3. **Idempotency** means running the pipeline multiple times produces the same result — essential for overnight jobs that might need to re-run after a failure.
4. **Modularity** — splitting extract, transform, and load into separate functions — makes every step independently testable and debuggable.

---

## Knowledge Check

**Q1.** You work at a company that uses BigQuery and wants analysts to write their own SQL transformations on top of raw loaded data. Which pattern fits best?  
**Answer:** ELT — load raw data into BigQuery first, then let analysts (or dbt) run transformations inside the warehouse.

**Q2.** What does "idempotent" mean for a data pipeline?  
**Answer:** Running the pipeline multiple times with the same input produces the same output — no duplicate rows, no accumulating side effects.

**Q3.** True or False: ETL always requires more Python code than ELT.  
**Answer:** False. ELT can require just as much code — the transformation logic moves from Python into SQL, but the total complexity is similar. The difference is *where* the transformation happens, not how much work it is.

---

## Next Lesson
**Lesson 03 — Working with Large Datasets**  
You've mastered the pipeline pattern. Now you'll tackle the first challenge every DE faces: data that's too big to fit in memory. You'll learn chunked reading, dtype optimization, and vectorized operations.
