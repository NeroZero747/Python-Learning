# Module 17 — APIs & Data Integration  
## Lesson 11 — Saving API Data to Databases

---

# Lesson Objective

By the end of this lesson you will understand:

- How to **store API data in databases**
- How APIs integrate with **SQL-based workflows**
- How Python writes data from APIs into tables
- How to build automated **data ingestion pipelines**

Many real-world systems retrieve data from APIs and **store it in databases for analysis and reporting**.

---

# Overview

When data is retrieved from an API, it is often stored in a database so that it can be:

- queried with SQL  
- used in dashboards  
- integrated with other datasets  

Example workflow:

```text
API Request
      ↓
JSON Response
      ↓
Convert to DataFrame
      ↓
Store in Database Table
```

This allows organizations to maintain **historical records and structured datasets**.

---

# Key Concepts

## API Data Ingestion

API ingestion refers to retrieving data from APIs and storing it in a data system.

Typical pipeline:

```text
API
 ↓
Python Script
 ↓
DataFrame
 ↓
Database
```

This pattern is widely used in data engineering.

---

## Databases as Storage Layers

Once API data is stored in a database, it can be used by:

- analysts
- reporting systems
- dashboards
- machine learning models

Example database systems:

```text
PostgreSQL
MySQL
SQL Server
Snowflake
```

---

## Database Tables

API data is typically stored in tables.

Example table:

```text
sales_data
```

| city | sales |
|------|------|
| Los Angeles | 100 |
| New York | 200 |

This table structure allows SQL queries to analyze the data.

---

# Decision Flow

When retrieving API data:

```text
Retrieve API data
        ↓
Convert JSON to DataFrame
        ↓
Does the data need long-term storage?
        |
       Yes
        ↓
Write DataFrame to database
```

Storing data enables **historical analysis and reporting**.

---

# Code Examples

## Example 1 — Converting API Data into a DataFrame

```python
import requests
import pandas as pd

url = "https://api.example.com/data"

response = requests.get(url)

data = response.json()

records = data["results"]

df = pd.DataFrame(records)

print(df.head())
```

---

## Example 2 — Writing Data to a SQL Database

Pandas provides the `to_sql()` function.

```python
from sqlalchemy import create_engine

engine = create_engine("sqlite:///example.db")

df.to_sql("sales_data", engine, if_exists="replace", index=False)
```

This creates a table in the database.

---

## Example 3 — Appending Data to Existing Tables

```python
df.to_sql("sales_data", engine, if_exists="append", index=False)
```

This adds new records without replacing existing data.

---

## Example 4 — Querying Stored Data

Once data is stored, it can be queried with SQL.

Example:

```sql
SELECT city, SUM(sales)
FROM sales_data
GROUP BY city;
```

This enables analysis using SQL tools.

---

# SQL / Excel Comparison

Traditional workflow:

```text
Download CSV
Import into Excel
Analyze data manually
```

Automated workflow:

```text
API Request
      ↓
DataFrame
      ↓
Database Table
      ↓
SQL Analysis
```

This enables scalable analytics systems.

---

# Practice Exercises

## Exercise 1

Tags: DataFrames, Databases, APIs

Convert API JSON data into a DataFrame.

Example:

```python
df = pd.DataFrame(records)
```

---

## Exercise 2

Tags: Databases, APIs

Create a SQLite database connection.

Example:

```python
engine = create_engine("sqlite:///example.db")
```

---

## Exercise 3

Tags: Tuples, DataFrames, Databases, APIs

Write the DataFrame to a database table.

Example:

```python
df.to_sql("api_data", engine)
```

---

# Common Mistakes

## Mistake 1 — Replacing Tables Accidentally

Using:

```python
if_exists="replace"
```

will overwrite existing data.

Use `"append"` when adding new records.

---

## Mistake 2 — Ignoring Data Types

Database columns should match the data types of the API data.

Incorrect types may cause errors.

---

## Mistake 3 — Storing Unclean Data

Always inspect API data before inserting it into databases.

Example:

```python
df.head()
```

---

# Real-World Use

Saving API data to databases is common in many systems.

Examples include:

---

### Financial Data Systems

APIs retrieve:

```text
stock prices
market indicators
currency exchange rates
```

These datasets are stored for historical analysis.

---

### Marketing Analytics

Marketing platforms provide APIs for retrieving campaign metrics.

Example pipeline:

```text
Marketing API → Database → Dashboard
```

---

### Data Warehouses

Organizations often load API data into warehouses such as:

```text
Snowflake
BigQuery
Redshift
```

This enables large-scale analytics.

---

# Key Idea Cards

### Card 1

API data is often stored in databases for long-term analysis.

---

### Card 2

Pandas can write DataFrames to SQL tables using `to_sql()`.

---

### Card 3

Storing API data enables SQL queries and analytics workflows.

---

# Lesson Recap

In this lesson you learned:

- how API data can be stored in databases  
- how Python writes DataFrames to SQL tables  
- how API ingestion pipelines work  
- how stored data supports analytics and reporting

Saving API data to databases is a key step in **modern data pipelines**.

---

# Next Lesson

Next you will learn:

**Module 17 — Lesson 12: Building an API Data Pipeline**

You will learn how to:

- combine API requests, data processing, and storage  
- build automated API ingestion workflows  
- structure production-ready API pipelines.