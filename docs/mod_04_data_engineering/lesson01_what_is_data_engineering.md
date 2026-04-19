# Lesson 01 — What Is Data Engineering?

**Track:** Data Engineering for Analysts  
**Module:** Module 1 — Data Engineering Foundations  
**Difficulty:** Beginner | **Duration:** 10 min  
**Source:** M1-L01 (pages/track_04_data_engineering/mod_01_data_engineering_foundations/lesson01_what_is_data_engineering.html)

---

## Learning Objectives

1. **Define data engineering** — Explain what data engineering is and how it supports analytics and machine learning workflows.
2. **Distinguish related roles** — Describe how data engineering differs from data analysis and data science in daily work.
3. **Core responsibilities** — Identify the main tasks a data engineer handles, from pipelines to infrastructure.
4. **Why it matters** — Understand why reliable data engineering is essential before any analysis can begin.

> This lesson introduces data engineering as a discipline so you can see where pipeline-building fits in the broader data landscape.

---

## Overview

### Hook
Data engineering is the work of collecting raw data from many sources, cleaning it, and delivering it in a form that analysts and scientists can trust.

### Analogy: The Water Treatment Plant
Think of data engineering like running a water treatment plant. Raw water flows in from rivers and wells. The plant filters it, tests it, and pumps clean water to every tap in the city. A **data engineer** builds and maintains that plant — and Python is one of the main tools for the job.

| Concept | Water Plant Equivalent |
|---------|----------------------|
| **Data Sources** | The intake pipes — where raw water arrives (rivers, wells, reservoirs) |
| **Data Pipelines** | The treatment stages — filters running in sequence |
| **Data Storage** | The reservoir — holds clean water ready to distribute |
| **Data Quality** | The testing lab — checks every batch at each stage |

> **Key takeaway:** If you've ever tidied a spreadsheet — removing blanks, fixing dates, merging columns — you've already done mini data engineering.

---

## Key Takeaways

### 1. Pipelines Power Every Dashboard
Every chart or report you see relies on a pipeline that moved raw data from its source, cleaned it, and delivered it to the right place. Without that pipeline running overnight, the dashboard would show yesterday's data — or nothing at all.  
**Keywords:** Automation · Reliability · Delivery

### 2. Analysts Depend on Engineers
Without a data engineer maintaining pipelines, an analyst's SQL query would return stale or broken results — like opening a spreadsheet that was never updated. The analyst focuses on "what does the data mean?" while the engineer focuses on "is the data there and correct?"  
**Keywords:** Trust · Freshness · Accuracy

### 3. Scale Changes Everything
A CSV with 500 rows opens instantly in Excel, but a dataset with 50 million rows needs specialized tools and a plan for memory, storage, and speed. Data engineering is, at its core, the discipline of handling data at the scale where manual tools stop working.  
**Keywords:** Volume · Memory · Throughput

---

## Key Concepts

### Data Pipeline
A data pipeline is a sequence of automated steps that moves data from one or more sources to a destination — usually a database or data warehouse. Each step performs a specific task: extract from source, transform to the right shape, load into the target system.

```python
# Conceptual pipeline structure
def run_pipeline():
    raw_data = extract(source="sales_api")       # Step 1: Get the data
    clean_data = transform(raw_data)              # Step 2: Clean and reshape
    load(clean_data, destination="warehouse")     # Step 3: Write to storage
```

### Data Engineering vs Data Analysis
| | Data Analyst | Data Engineer |
|--|--|--|
| **Question** | "What happened?" | "Is the data ready?" |
| **Primary skill** | SQL, Excel, visualization | Python, SQL, infrastructure |
| **Output** | Charts, reports, insights | Pipelines, databases, APIs |
| **Tooling** | Tableau, Power BI, pandas | Airflow, Spark, dbt, Docker |
| **Values** | Interpretation | Reliability, scale |

A data analyst *consumes* data. A data engineer *produces* it in a usable form.

### Data Warehouse
A data warehouse is a centralized database designed specifically for analytics. Unlike an operational database (which is optimized for fast insert/update), a warehouse is optimized for fast reads across large historical datasets. Examples: Google BigQuery, Snowflake, Amazon Redshift, PostgreSQL (smaller scale).

### ETL (Extract, Transform, Load)
The classic three-step pipeline pattern:
- **Extract** — Read data from sources (APIs, databases, files)
- **Transform** — Clean, reshape, join, aggregate
- **Load** — Write the result to a target system

(Covered in depth in Lesson 02.)

---

## Code Examples

### Example 1: Reading data from multiple sources
```python
import pandas as pd

# A data engineer often pulls in data from several places
sales = pd.read_csv("sales_data.csv")           # flat file
customers = pd.read_sql("SELECT * FROM customers", conn)  # database
api_response = requests.get("https://api.example.com/orders").json()  # API
orders = pd.DataFrame(api_response["orders"])

# Then joins them into one clean dataset
combined = sales.merge(customers, on="customer_id")
```

### Example 2: A simple transformation
```python
def transform(df: pd.DataFrame) -> pd.DataFrame:
    """Clean a raw sales DataFrame."""
    df = df.dropna(subset=["sale_date", "amount"])     # remove incomplete rows
    df["sale_date"] = pd.to_datetime(df["sale_date"])  # fix date type
    df["amount"] = df["amount"].abs()                   # amounts must be positive
    df = df.rename(columns={"amt": "amount"})           # standardize column names
    return df
```

### Example 3: Writing a clean result to a database
```python
import sqlalchemy

engine = sqlalchemy.create_engine("postgresql://user:pass@host/db")

clean_df.to_sql(
    name="clean_sales",
    con=engine,
    if_exists="replace",   # overwrite table each run
    index=False
)
print(f"Loaded {len(clean_df):,} rows into warehouse.")
```

---

## Common Mistakes

### Mistake 1: Confusing the roles
**Wrong view:** "Data analysts and data engineers do the same thing."  
**Reality:** Analysts *interpret* clean data; engineers *produce* clean data. When an analyst gets a broken report, they should ask: did the pipeline fail, or is the logic wrong? Those are two very different problems with two very different fixes.

### Mistake 2: Skipping data validation
**Wrong approach:** Run the pipeline and trust the output.  
**Right approach:** Always verify row counts, check for nulls, and assert expected ranges. A pipeline that silently loads 0 rows is worse than one that crashes — at least you know the crash happened.

```python
# Add a basic sanity check
assert len(clean_df) > 0, "Pipeline produced no rows — check the source!"
assert clean_df["amount"].isna().sum() == 0, "Unexpected nulls in amount column"
```

### Mistake 3: Hard-coding credentials in scripts
**Wrong:**
```python
conn = pg.connect(password="mypassword123")  # NEVER do this
```
**Right:**
```python
import os
conn = pg.connect(password=os.environ["DB_PASSWORD"])
```

---

## Practice Exercises

### Exercise 1 — Role mapping
List 3 tasks your current job involves. For each one, decide: is this a data analyst task (interpreting data) or a data engineer task (moving/preparing data)?

### Exercise 2 — Spot the pipeline
Think of a dashboard or report you use at work. Trace back: where does that data come from? How does it get there? How often is it refreshed? You've just sketched a pipeline.

### Exercise 3 — Write a mini pipeline
```python
# Complete this pipeline skeleton:
import pandas as pd

def extract():
    return pd.read_csv("sample_sales.csv")

def transform(df):
    # TODO: drop rows where 'revenue' is null
    # TODO: convert 'date' column to datetime
    # TODO: add a new column 'revenue_rounded' = revenue rounded to 2 decimals
    return df

def load(df):
    df.to_csv("clean_sales.csv", index=False)
    print(f"Done. {len(df)} rows saved.")

load(transform(extract()))
```

---

## Real-World Application
At a retail company, data engineers build pipelines that:
- Pull daily transaction records from point-of-sale systems (extract)
- Join them with inventory data and clean price/discount fields (transform)
- Load the merged dataset into a warehouse every night at 2 AM (load)

By 8 AM when analysts arrive, the data is fresh and reliable. The analysts never touch the pipeline — they write SQL on top of the warehouse knowing the DE has already done the preparation work.

---

## Lesson Recap

1. **Data engineering** is the practice of building automated systems that move, clean, and deliver data reliably.
2. **Data engineers** build infrastructure so that **data analysts** can focus on insights rather than data preparation.
3. The core pattern is **ETL** (Extract, Transform, Load) — pull data, clean it, put it somewhere useful.
4. **Scale** is what separates data engineering from spreadsheet work — when data is too large, too fast, or too irregular for manual tools, a pipeline is needed.

---

## Knowledge Check

**Q1.** True or False: A data engineer's primary job is to create charts and dashboards.  
**Answer:** False. Data engineers build pipelines that deliver clean, reliable data. Creating charts and dashboards is the data analyst's role.

**Q2.** In the ETL pattern, what does the "T" stand for?  
**Answer:** Transform — the step where raw data is cleaned, reshaped, joined, or aggregated into a useful form.

**Q3.** Which of these is a data engineering task?  
(a) Interpreting a sales trend in a dashboard  
(b) Writing a Python script that pulls data from an API nightly and loads it into a database  
(c) Building a Tableau visualization  
**Answer:** (b) — Writing the automated pipeline that moves and loads data.

---

## Next Lesson
**Lesson 02 — ETL, ELT & Pipeline Thinking**  
Now that you know what data engineering is, you'll learn the two dominant patterns for moving data (ETL and ELT), how to design a pipeline that is reliable and repeatable, and the core principles that make pipelines easy to debug at 3 AM.
