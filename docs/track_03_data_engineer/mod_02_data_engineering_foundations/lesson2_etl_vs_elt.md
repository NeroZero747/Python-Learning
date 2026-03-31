# Module 7 — Data Engineering Foundations

# Lesson 2 — ETL vs ELT

---

# Lesson Objective

By the end of this lesson learners will understand:

• what **ETL** means  
• what **ELT** means  
• the differences between ETL and ELT architectures  
• when each approach should be used  
• how modern cloud data warehouses changed pipeline design  

Understanding ETL vs ELT is essential because **nearly every data pipeline follows one of these two patterns**.

---

# Overview

When organizations move data from operational systems into analytics systems, the data typically goes through three steps:

• Extract  
• Transform  
• Load  

These three steps form the basis of **ETL**.

ETL stands for:

```text
Extract
Transform
Load
```

Example workflow:

```text
Source System
      ↓
Extract Data
      ↓
Transform Data
      ↓
Load into Data Warehouse
```

In ETL, **data is transformed before it is loaded into the warehouse**.

However, modern cloud platforms introduced a different pattern called **ELT**.

ELT stands for:

```text
Extract
Load
Transform
```

Example workflow:

```text
Source System
      ↓
Extract Data
      ↓
Load Raw Data
      ↓
Transform Inside Warehouse
```

In ELT, raw data is loaded first, and transformations occur **inside the data warehouse**.

This approach became popular because modern warehouses like:

• Snowflake  
• BigQuery  
• Redshift  

are powerful enough to handle large transformations.

---

# Key Idea Cards (3 Cards)

## ETL Transforms Data Before Loading

In ETL pipelines, the data transformation happens before loading the data warehouse.

Example pipeline:

```text
Database
   ↓
Python Transformation
   ↓
Data Warehouse
```

This approach was common when warehouses had limited compute power.

---

## ELT Loads Raw Data First

In ELT pipelines, raw data is loaded first and transformed afterward.

Example pipeline:

```text
Database
   ↓
Data Warehouse
   ↓
SQL Transformations
```

This allows analysts to transform data using SQL directly in the warehouse.

---

## Modern Data Platforms Prefer ELT

Many modern organizations use ELT because:

• cloud warehouses scale automatically  
• transformations run faster inside the warehouse  
• raw data can be stored for auditing and reprocessing.

---

# Key Concepts

## Extract

Extraction is the process of retrieving data from a source system.

Examples:

• relational databases  
• APIs  
• CSV files  
• event streams  

Example extraction in Python:

```python
import pandas as pd

data = pd.read_csv("sales.csv")
```

---

## Transform

Transformation prepares data for analytics.

Common transformations include:

• cleaning values  
• joining datasets  
• creating calculated columns  
• filtering records.

Example:

```python
data["total"] = data["price"] * data["quantity"]
```

---

## Load

Loading stores the processed data in a system designed for analysis.

Common destinations include:

• data warehouses  
• analytics databases  
• data lakes.

Example:

```python
data.to_csv("clean_sales.csv", index=False)
```

---

# Decision Flow

Choosing between ETL and ELT typically follows this logic:

```text
Is warehouse compute powerful?
            ↓
          YES
            ↓
         Use ELT
            ↓
Transform inside warehouse

          NO
            ↓
          Use ETL
            ↓
Transform before loading
```

---

# Code Examples

## Example 1 — ETL Pipeline

```python
import pandas as pd

data = pd.read_csv("sales.csv")

data["total"] = data["price"] * data["quantity"]

data.to_csv("warehouse_sales.csv", index=False)
```

In this example:

• data is extracted  
• transformed in Python  
• then loaded.

---

## Example 2 — ELT Pipeline

```python
import pandas as pd

data = pd.read_csv("sales.csv")

data.to_csv("raw_sales.csv", index=False)
```

Then transformations occur in SQL.

---

## Example 3 — SQL Transformation

```sql
SELECT
    price * quantity AS total
FROM raw_sales
```

Here the transformation happens **inside the warehouse**.

---

## Example 4 — Hybrid Pipeline

Many organizations use a hybrid approach.

```text
API
 ↓
Python Extraction
 ↓
Load Raw Data
 ↓
SQL Transformations
 ↓
Analytics Tables
```

This allows flexibility in pipeline design.

---

# SQL / Excel Comparison

The ETL concept exists in familiar tools.

| Step | Python | SQL | Excel |
|-----|------|------|------|
| extract | pandas read_csv | SELECT | open workbook |
| transform | pandas operations | SQL transformations | formulas |
| load | write to warehouse | INSERT | save workbook |

Example Excel transformation:

```text
Total = Price * Quantity
```

This is equivalent to a transformation step in ETL.

---

# Practice Exercises

## Exercise 1

Tags: pandas, Imports, read_csv(), CSV

Load a dataset.

```python
import pandas as pd

data = pd.read_csv("orders.csv")
```

---

## Exercise 2

Tags: Lists, Arithmetic, ETL

Create a calculated column.

```python
data["total"] = data["price"] * data["quantity"]
```

---

## Exercise 3

Tags: Booleans, Tuples, Error Handling, to_csv()

Save the result.

```python
data.to_csv("clean_orders.csv", index=False)
```

Try modifying the pipeline to represent:

• ETL  
• ELT  

---

# Common Mistakes

## Transforming Too Much in ETL

If transformations are extremely heavy, performing them outside the warehouse may slow pipelines.

Modern platforms prefer **ELT when possible**.

---

## Not Keeping Raw Data

Some pipelines overwrite data after transformation.

Best practice:

```text
Store raw data
Store transformed data
```

This allows debugging and auditing.

---

## Mixing Pipeline Responsibilities

Pipelines should focus on **data preparation**, not analytics dashboards or reporting logic.

---

# Real-World Use

ETL and ELT pipelines power many real systems.

Examples include:

• healthcare claims pipelines  
• ecommerce transaction processing  
• financial reporting systems  
• marketing analytics pipelines.

Example healthcare pipeline:

```text
Claims Database
      ↓
Extract
      ↓
Load Raw Claims
      ↓
Transform for Analytics
      ↓
Provider Cost Dashboard
```

These systems ensure that analytics platforms always receive **clean, structured data**.

---

# Lesson Recap

In this lesson you learned:

• what ETL and ELT mean  
• how the two architectures differ  
• why modern warehouses favor ELT  
• how pipelines move data from sources to analytics systems  

Understanding ETL vs ELT is essential for designing **modern data platforms**.

---

# Next Lesson

Next we will learn:

# Lesson 3 — Working with Large Datasets

You will learn:

• why large datasets create challenges  
• how memory limitations affect processing  
• strategies for working with large data in Python  
• tools used in scalable data pipelines.
