# Module 7 — Data Engineering Foundations

# Lesson 7 — Pipeline Design Concepts

---

# Lesson Objective

By the end of this lesson learners will understand:

• how data pipelines are structured  
• common architecture patterns used in data engineering  
• how pipelines move data through multiple processing stages  
• best practices for designing reliable and scalable pipelines  

Pipeline design is important because poorly designed pipelines can cause:

• slow processing  
• unreliable data  
• difficult maintenance  

Good pipeline design ensures that data systems remain **scalable, reliable, and easy to maintain**.

---

# Overview

A **data pipeline** is a system that moves and processes data through multiple stages.

Example pipeline:

```text
Source System
      ↓
Data Extraction
      ↓
Data Transformation
      ↓
Data Storage
      ↓
Analytics / Reporting
```

Each stage performs a specific task in the data workflow.

For example:

| Stage | Purpose |
|------|------|
| Extract | retrieve data from source systems |
| Transform | clean and prepare the data |
| Load | store data in analytics systems |
| Serve | provide data for dashboards or applications |

Well-designed pipelines divide processing into **clear stages**, which improves reliability and maintainability.

---

# Key Idea Cards (3 Cards)

## Pipelines Break Work Into Stages

Data pipelines separate processing into logical steps.

Example:

```text
Extract → Transform → Load
```

Breaking tasks into stages simplifies pipeline design.

---

## Pipelines Should Be Reproducible

A pipeline should produce the same results every time it runs.

Example:

```text
Same input data
      ↓
Same transformation
      ↓
Same output dataset
```

Reproducibility ensures consistent analytics.

---

## Pipelines Must Be Reliable

Production pipelines must handle:

• failures  
• missing data  
• unexpected input formats  

Robust pipelines include validation and error handling.

---

# Key Concepts

## Pipeline Stages

Data pipelines typically include multiple stages.

Example structure:

```text
Extract
Transform
Load
Serve
```

Each stage performs a specific operation.

---

## Batch Pipelines

Batch pipelines process data at scheduled intervals.

Example schedule:

```text
Run every hour
Run daily
Run weekly
```

Batch pipelines are common in analytics systems.

---

## Streaming Pipelines

Streaming pipelines process data continuously as it arrives.

Example:

```text
Event → Process → Store → Serve
```

Streaming pipelines are used for real-time analytics.

---

# Decision Flow

Designing a pipeline usually follows this planning process:

```text
Identify data source
        ↓
Determine processing steps
        ↓
Design pipeline stages
        ↓
Implement transformations
        ↓
Store processed data
```

This structured approach helps ensure reliable pipeline design.

---

# Code Examples

## Example 1 — Simple Pipeline Script

```python
import pandas as pd

data = pd.read_csv("orders.csv")

data["total"] = data["price"] * data["quantity"]

data.to_csv("processed_orders.csv", index=False)
```

This script performs a basic ETL process.

---

## Example 2 — Pipeline with Functions

```python
import pandas as pd

def extract():
    return pd.read_csv("orders.csv")

def transform(data):
    data["total"] = data["price"] * data["quantity"]
    return data

def load(data):
    data.to_csv("processed_orders.csv", index=False)

data = extract()
data = transform(data)
load(data)
```

Breaking the pipeline into functions improves readability.

---

## Example 3 — Pipeline Using Classes

```python
class DataPipeline:

    def extract(self):
        pass

    def transform(self):
        pass

    def load(self):
        pass
```

Classes help organize complex pipelines.

---

## Example 4 — Scheduled Pipeline Concept

```text
Daily ETL Job
       ↓
Load Data Warehouse
       ↓
Update Dashboards
```

Many pipelines run on scheduled jobs.

---

# SQL / Excel Comparison

Pipeline concepts exist in other tools.

| Concept | Python | SQL | Excel |
|------|------|------|------|
| pipeline stage | function | stored procedure step | macro step |
| transformation | pandas operations | SQL queries | formulas |
| scheduling | cron job | scheduled job | workbook automation |

Example SQL pipeline step:

```sql
INSERT INTO analytics_table
SELECT *
FROM staging_table
```

This represents a transformation and load stage.

---

# Practice Exercises

## Exercise 1

Tags: Functions, CI/CD

Create simple pipeline functions.

```python
def extract():
    pass

def transform():
    pass

def load():
    pass
```

---

## Exercise 2

Tags: CI/CD, Scripts, Data I/O

Create a script that calls the functions in order.

```python
data = extract()
data = transform(data)
load(data)
```

---

## Exercise 3

Tags: Functions, CI/CD, Validation, Data Quality

Modify the pipeline to include a validation step.

Example:

```python
def validate(data):
    pass
```

This checks data quality before loading.

---

# Common Mistakes

## Creating Monolithic Pipelines

Large scripts that perform all operations in one block become difficult to maintain.

Better practice:

```text
Divide pipeline into stages
```

---

## Lack of Error Handling

Pipelines should detect and handle errors.

Example issues:

• missing files  
• corrupted data  
• connection failures.

---

## No Logging or Monitoring

Production pipelines should record events.

Logging allows engineers to detect pipeline failures quickly.

---

# Real-World Use

Pipeline design is critical in real-world data platforms.

Examples include:

• healthcare analytics pipelines  
• financial reporting pipelines  
• marketing data platforms  
• ecommerce transaction systems.

Example healthcare pipeline:

```text
Claims System
     ↓
Daily Extraction
     ↓
Data Cleaning
     ↓
Load Analytics Warehouse
     ↓
Provider Dashboard
```

This design ensures that data is processed consistently and reliably.

---

# Lesson Recap

In this lesson you learned:

• how data pipelines are structured  
• the stages of a pipeline  
• batch vs streaming pipelines  
• best practices for pipeline design  

Good pipeline design ensures that data systems remain **reliable, scalable, and maintainable**.

---

# Next Module

You have now completed:

# Module 7 — Data Engineering Foundations

You learned:

• what data engineering is  
• ETL vs ELT architectures  
• handling large datasets  
• memory optimization techniques  
• efficient storage formats like Parquet  
• high-performance tools like Polars  
• how to design reliable data pipelines  

These concepts form the **foundation of modern data engineering systems**.

---

# Next Module

Next we will begin:

# Module 8 — Building Data Applications

First lesson:

**Why Build Data Apps?**

You will learn how Python tools like:

• **Streamlit**  
• **Shiny for Python**

allow analysts and engineers to build **interactive data applications and dashboards**.
