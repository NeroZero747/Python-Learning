# Lesson 08 — Data Quality & Validation

**Track:** Data Engineering for Analysts  
**Module:** Module 3 — Data Collection  
**Difficulty:** Intermediate | **Duration:** 12 min  
**Sources:** M4-L05 (Data Validation in Pipelines) · M4-L12 (Pipeline Project: Data Quality Checks) · Parts of M3-L14 (defensive error handling)

---

## Learning Objectives

1. **Define data quality dimensions** — Name the 5 key dimensions of data quality and explain what violates each one.
2. **Write validation assertions** — Use Python assertions and pandas methods to check schema, nulls, ranges, and row counts.
3. **Handle validation failures** — Route bad records to a quarantine table rather than crashing the whole pipeline.
4. **Schema drift detection** — Detect when an API or source file adds, removes, or renames columns unexpectedly.

> By the end of this lesson you'll have a reusable validation layer you can plug into any pipeline to catch data problems before they reach dashboards.

---

## Overview

### Hook
Bad data that reaches a dashboard is worse than no pipeline at all — it creates false confidence. A chart showing "£0 revenue last week" because the pipeline silently loaded 0 clean rows is the data engineer's most embarrassing failure. Data quality checks are the discipline that prevents it.

### Analogy: The Airport Security Checkpoint
Think of a data validation layer like airport security screening. Every passenger (data record) goes through a checkpoint before reaching the departure lounge (your warehouse/dashboard). The checkpoint has specific rules — valid ID, no prohibited items, boarding pass matches the flight. Records that fail a check are quarantined for manual review. Records that pass continue. You don't cancel the whole flight because one passenger left their keys in their pocket — you pull them aside and process the rest.

| Validation Step | Airport Security Equivalent |
|-----------------|---------------------------|
| **Schema check** | Does the passenger have a valid ID format? |
| **Null check** | Is the boarding pass blank? |
| **Range check** | Is the declared bag weight within the allowed limit? |
| **Uniqueness check** | Is this passenger already on the flight? (duplicate row) |
| **Quarantine** | Secondary screening — separate that record for investigation |

> **Key takeaway:** The goal is not zero bad records — it's knowing about every bad record so you can decide what to do with it. A pipeline that quarantines 3 rows and loads 99,997 clean ones is far better than one that either crashes or silently loads all 100,000 including the 3 corrupted ones.

---

## Key Takeaways

### 1. The 5 Dimensions of Data Quality
**Completeness** (are all expected rows and columns present?), **Validity** (are values in the expected format and range?), **Consistency** (do related fields agree with each other?), **Uniqueness** (are there duplicate records where there shouldn't be?), and **Timeliness** (did the data arrive on schedule?). A validation layer should check all five dimensions.  
**Keywords:** Completeness · Validity · Consistency · Uniqueness · Timeliness

### 2. Assert Early and Log Everything
Write validation checks immediately after the extract step — before transformation. If data fails validation, log exactly which check failed, how many rows were affected, and a sample of the bad records. Silent failures (loading 0 rows with no error) are far more dangerous than loud ones.  
**Keywords:** Early validation · Logging · Alerting · Fail-fast

### 3. Quarantine Don't Crash
When 3 out of 10,000 rows fail validation, crashing the pipeline stops all 9,997 good rows from loading. Instead, split records into "clean" and "quarantine" sets, load the clean set normally, and write the quarantine set to a separate table for investigation. The pipeline continues; you get alerted; you fix it later.  
**Keywords:** Quarantine table · Partial load · Alert threshold

---

## Key Concepts

### Data Quality Dimensions
```python
# COMPLETENESS — all expected rows arrived
assert len(df) > 0, "DataFrame is empty — source may have failed to extract"
assert len(df) >= expected_minimum_rows, f"Expected ≥{expected_minimum_rows} rows, got {len(df)}"

# VALIDITY — values are in the right format
assert df["amount"].between(0, 1_000_000).all(), "Amount column has out-of-range values"
assert df["status"].isin(["pending","completed","cancelled"]).all(), "Unexpected status values"
assert df["email"].str.contains("@").all(), "Invalid email addresses found"

# UNIQUENESS — no duplicates where there shouldn't be
assert df["order_id"].is_unique, "Duplicate order IDs detected"
assert df.duplicated().sum() == 0, "Duplicate rows found"

# CONSISTENCY — related fields agree
assert (df["end_date"] >= df["start_date"]).all(), "end_date is before start_date"
assert (df["total"] == (df["amount"] * df["quantity"]).round(2)).all(), "total doesn't match amount * quantity"

# TIMELINESS — data isn't too old
from datetime import datetime, timedelta
latest_record = df["created_at"].max()
assert latest_record >= datetime.now() - timedelta(hours=25), f"Latest record is from {latest_record} — pipeline may be stale"
```

### Schema Validation
```python
def validate_schema(df: pd.DataFrame, expected_columns: list) -> bool:
    """Check that all expected columns are present."""
    actual = set(df.columns)
    expected = set(expected_columns)
    
    missing = expected - actual
    extra   = actual - expected

    if missing:
        raise ValueError(f"Missing columns: {missing}")
    if extra:
        print(f"Warning: unexpected extra columns: {extra}")  # log but don't crash

    return True
```

### Quarantine Pattern
```python
def split_clean_quarantine(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Separate valid rows from invalid rows."""
    is_valid = (
        df["amount"].notna() &
        df["amount"].between(0, 1_000_000) &
        df["order_id"].notna() &
        df["status"].isin(["pending", "completed", "cancelled"])
    )
    clean     = df[is_valid].copy()
    quarantine = df[~is_valid].copy()
    return clean, quarantine
```

---

## Code Examples

### Example 1: A complete validation function
```python
import pandas as pd
import logging
from datetime import datetime, timedelta

log = logging.getLogger(__name__)

EXPECTED_COLUMNS = ["order_id", "customer_id", "amount", "status", "created_at"]
VALID_STATUSES   = {"pending", "completed", "cancelled", "refunded"}

def validate_orders(df: pd.DataFrame) -> dict:
    """
    Run all quality checks on the orders DataFrame.
    Returns a dict with 'passed' (bool) and 'issues' (list of strings).
    """
    issues = []

    # 1. Schema
    missing_cols = set(EXPECTED_COLUMNS) - set(df.columns)
    if missing_cols:
        issues.append(f"Missing columns: {missing_cols}")

    # 2. Completeness
    if len(df) == 0:
        issues.append("DataFrame is empty")
        return {"passed": False, "issues": issues}  # can't continue

    null_counts = df[EXPECTED_COLUMNS].isnull().sum()
    for col, count in null_counts[null_counts > 0].items():
        pct = count / len(df) * 100
        issues.append(f"Column '{col}' has {count} nulls ({pct:.1f}%)")

    # 3. Validity
    if "amount" in df.columns:
        invalid_amounts = (~df["amount"].between(0, 1_000_000)).sum()
        if invalid_amounts:
            issues.append(f"{invalid_amounts} rows have out-of-range amounts")

    if "status" in df.columns:
        bad_statuses = (~df["status"].isin(VALID_STATUSES)).sum()
        if bad_statuses:
            issues.append(f"{bad_statuses} rows have unrecognized status values")

    # 4. Uniqueness
    dupes = df["order_id"].duplicated().sum()
    if dupes:
        issues.append(f"{dupes} duplicate order_id values")

    # 5. Timeliness
    if "created_at" in df.columns:
        latest = pd.to_datetime(df["created_at"]).max()
        if latest < datetime.now() - timedelta(hours=25):
            issues.append(f"Latest record is {latest} — data may be stale")

    passed = len(issues) == 0
    log.info(f"Validation {'PASSED' if passed else 'FAILED'}: {len(issues)} issues found")
    for issue in issues:
        log.warning(f"  ✗ {issue}")

    return {"passed": passed, "issues": issues, "row_count": len(df)}
```

### Example 2: Quarantine bad rows instead of crashing
```python
import pandas as pd
import sqlalchemy

def load_with_quarantine(df: pd.DataFrame, engine, table: str) -> None:
    """Load clean rows to target table; quarantine bad rows separately."""

    # Identify bad rows
    is_bad = (
        df["amount"].isna() |
        df["amount"].lt(0)  |
        df["order_id"].isna() |
        df["status"].isna()
    )

    clean      = df[~is_bad]
    quarantine  = df[is_bad].assign(
        quarantine_reason="null or negative amount/order_id/status",
        quarantined_at=pd.Timestamp.now()
    )

    # Load clean rows
    clean.to_sql(table, engine, if_exists="replace", index=False)
    log.info(f"Loaded {len(clean):,} clean rows into '{table}'")

    # Write quarantine rows for investigation
    if len(quarantine) > 0:
        quarantine.to_sql(f"{table}_quarantine", engine, if_exists="append", index=False)
        log.warning(f"Quarantined {len(quarantine):,} rows into '{table}_quarantine'")

    # Alert if quarantine ratio is too high
    quarantine_pct = len(quarantine) / len(df) * 100
    if quarantine_pct > 5:   # more than 5% bad is a serious problem
        raise ValueError(
            f"Quarantine rate {quarantine_pct:.1f}% exceeds threshold. "
            f"Check source data quality before proceeding."
        )
```

### Example 3: Schema drift detection
```python
import json, os

SCHEMA_FILE = "expected_schema.json"

def save_schema(df: pd.DataFrame) -> None:
    """Save the current schema as the expected baseline."""
    schema = {col: str(dtype) for col, dtype in df.dtypes.items()}
    with open(SCHEMA_FILE, "w") as f:
        json.dump(schema, f, indent=2)
    print(f"Schema saved: {list(schema.keys())}")

def detect_schema_drift(df: pd.DataFrame) -> list:
    """Compare current DataFrame columns against the saved baseline."""
    if not os.path.exists(SCHEMA_FILE):
        save_schema(df)
        return []

    with open(SCHEMA_FILE) as f:
        expected = json.load(f)

    actual   = {col: str(dtype) for col, dtype in df.dtypes.items()}
    drifts   = []

    for col in expected:
        if col not in actual:
            drifts.append(f"REMOVED: column '{col}' is missing from source")
        elif actual[col] != expected[col]:
            drifts.append(f"TYPE CHANGE: '{col}' changed from {expected[col]} to {actual[col]}")

    for col in actual:
        if col not in expected:
            drifts.append(f"ADDED: new column '{col}' ({actual[col]}) appeared in source")

    return drifts
```

### Example 4: Row-count assertion with alerting
```python
def assert_row_count(df: pd.DataFrame, min_rows: int, context: str = "") -> None:
    """Fail loudly if row count is suspiciously low."""
    count = len(df)
    if count < min_rows:
        msg = (
            f"Row count check FAILED{f' ({context})' if context else ''}: "
            f"expected ≥{min_rows:,}, got {count:,}. "
            f"Source data may be missing or pipeline extraction failed."
        )
        log.error(msg)
        raise AssertionError(msg)
    log.info(f"Row count OK: {count:,} ≥ {min_rows:,}")
```

---

## Common Mistakes

### Mistake 1: Validating after transformation instead of before
```python
# WRONG — transform might hide the original problem
clean = transform(raw)
validate(clean)    # you're validating your own output, not the source

# RIGHT — validate the raw data immediately after extract
raw = extract()
validate(raw)      # catch source problems early
clean = transform(raw)
```

### Mistake 2: Using assert statements in production pipelines
```python
# WRONG — Python's assert can be disabled with the -O flag
assert len(df) > 0

# RIGHT — use explicit exceptions
if len(df) == 0:
    raise ValueError("Source returned empty dataset")
```

### Mistake 3: Crashing on any validation failure
```python
# WRONG — crashes the whole pipeline for 3 bad rows out of 10,000
df.to_sql("orders", engine, if_exists="replace")   # only if ALL rows pass

# RIGHT — quarantine bad rows, load the rest, then alert
clean, quarantine = split_clean_quarantine(df)
load_with_quarantine(clean, quarantine, engine, "orders")
```

---

## Practice Exercises

### Exercise 1 — Write a validator
```python
import pandas as pd

df = pd.DataFrame({
    "product_id": [1, 2, None, 4, 2],        # has null, has duplicate
    "price":      [9.99, -5.00, 14.99, 0, 7.50],  # has negative
    "category":   ["A", "B", "C", "D", "X"]  # "X" is not a valid category
})

VALID_CATEGORIES = {"A", "B", "C", "D"}

# TODO: Write a validate() function that checks:
# 1. product_id has no nulls
# 2. product_id has no duplicates
# 3. price >= 0 for all rows
# 4. category is in VALID_CATEGORIES
# Return a list of issue strings (empty list = all passed)
```

### Exercise 2 — Quarantine bad rows
```python
# Using the DataFrame from Exercise 1:
# TODO: Split df into clean_df (passes all checks) and quarantine_df (fails any)
# TODO: Print the row counts for each
# TODO: Print which rows are in the quarantine set and why
```

### Exercise 3 — Schema drift
```python
import pandas as pd
from io import StringIO

# Simulate two versions of a source API response
v1 = pd.read_csv(StringIO("id,amount,region\n1,100,EMEA\n2,200,APAC"))
v2 = pd.read_csv(StringIO("id,revenue,region,currency\n1,100,EMEA,GBP"))

# TODO: Write a function that compares two DataFrames' columns and dtypes
# and returns a list describing any added, removed, or renamed columns
```

---

## Lesson Recap

1. **5 quality dimensions** — Completeness, Validity, Consistency, Uniqueness, and Timeliness. A robust validation layer checks all five on every pipeline run.
2. **Validate early** — immediately after extract, before any transformation, so you catch source problems rather than problems your own code introduced.
3. **Quarantine don't crash** — separate bad rows from clean ones and load both to different tables. The pipeline continues; you investigate quarantined rows at a convenient time.
4. **Schema drift detection** — save the expected schema on the first run and compare against it on every subsequent run to catch added, removed, or renamed columns before they corrupt downstream data.

---

## Knowledge Check

**Q1.** Your pipeline loads 0 rows into the warehouse but exits with no error. Which quality dimension did it fail, and how would you prevent this?  
**Answer:** Completeness. Add a row count assertion immediately after extraction: `if len(df) == 0: raise ValueError("Source returned empty dataset")`. Never let a 0-row load pass silently.

**Q2.** Out of 50,000 records, 120 have a negative `amount`. Should you crash the pipeline or load what you can?  
**Answer:** Quarantine the 120 bad rows into a separate table and load the 49,880 clean rows normally. Alert on the quarantine and investigate the root cause. Crashing stops all the good data from loading.

**Q3.** What is schema drift and why is it dangerous for data pipelines?  
**Answer:** Schema drift is when the structure of your source data changes — columns are added, removed, or renamed — without warning. It's dangerous because downstream transformations and dashboards built on the old schema will silently break or produce incorrect results. Detecting it early (by saving and comparing expected column schemas) lets you adapt before users notice.

---

## Next Lesson
**Lesson 09 — Pipeline Automation & Deployment**  
Your pipeline extracts, validates, transforms, and loads. Now you'll learn to run it automatically on a schedule, deploy it to a managed environment, and set up the monitoring that tells you when something goes wrong at 3 AM.
