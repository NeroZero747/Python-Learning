# Module 4 — Working with Data Sources

# Lesson 4 — Running SQL in Python

---

# Lesson Objective

By the end of this lesson learners will understand:

• how to write SQL queries inside Python scripts  
• how to execute SQL queries using Pandas  
• how SQL and Python work together in data workflows  
• how analysts use SQL to retrieve and filter data before analysis  

Running SQL in Python allows analysts to **combine the strengths of SQL databases with Python analytics tools**.

---

# Overview

In many analytics environments, data is stored inside **databases**, and SQL is used to retrieve it.

Instead of running SQL in a database tool, analysts can run SQL directly from Python.

Example SQL query:

```sql
SELECT Customer, Sales
FROM sales_table
WHERE Sales > 100
```

Using Python and Pandas, we can execute the same query and load the results into a DataFrame.

Example:

```python
import pandas as pd

query = """
SELECT Customer, Sales
FROM sales_table
WHERE Sales > 100
"""

df = pd.read_sql(query, engine)

print(df)
```

Output:

```text
Customer   Sales
Alice      120
Bob        200
Maria      150
```

This approach allows analysts to:

• use SQL for data retrieval  
• use Python for analysis and transformation  

This combination is common in **data engineering and analytics workflows**.

---

# Key Idea Cards (3 Cards)

## SQL Retrieves Data Efficiently

Databases are optimized to retrieve and filter data quickly.

Example:

```sql
SELECT *
FROM sales_table
WHERE Sales > 100
```

Filtering data in SQL reduces the amount of data sent to Python.

---

## Python Analyzes the Data

Once SQL retrieves the data, Python can perform advanced analysis.

Example tasks:

• aggregations  
• visualizations  
• machine learning  
• automation  

---

## SQL + Python Is a Powerful Combination

A common workflow is:

```text
Database → SQL query → Pandas DataFrame → Analysis
```

SQL extracts the data, and Python processes it.

---

# Key Concepts

## SQL Query Strings

SQL queries are usually written as strings inside Python.

Example:

```python
query = "SELECT * FROM sales_table"
```

For longer queries, triple quotes are often used.

Example:

```python
query = """
SELECT Customer, Sales
FROM sales_table
WHERE Sales > 100
"""
```

---

## Running SQL Queries

Pandas can execute SQL queries using `read_sql()`.

Example:

```python
df = pd.read_sql(query, engine)
```

This returns the query results as a DataFrame.

---

## Query Optimization

It is best practice to retrieve only the data you need.

Example:

Bad query:

```sql
SELECT *
FROM large_table
```

Better query:

```sql
SELECT Customer, Sales
FROM large_table
WHERE Sales > 100
```

This reduces processing time and memory usage.

---

# Decision Flow

Running SQL in Python typically follows this process:

```text
Connect to database
      ↓
Write SQL query
      ↓
Execute query using Pandas
      ↓
Load results into DataFrame
      ↓
Perform analysis
```

Example:

```python
df = pd.read_sql(query, engine)
```

---

# Code Examples

## Example 1 — Running a Simple SQL Query

```python
import pandas as pd

query = "SELECT * FROM sales_table"

df = pd.read_sql(query, engine)

print(df.head())
```

---

## Example 2 — Filtering with SQL

```python
query = """
SELECT Customer, Sales
FROM sales_table
WHERE Sales > 100
"""

df = pd.read_sql(query, engine)
```

---

## Example 3 — Aggregating with SQL

```python
query = """
SELECT City, SUM(Sales) AS Total_Sales
FROM sales_table
GROUP BY City
"""

df = pd.read_sql(query, engine)
```

---

## Example 4 — Ordering Results

```python
query = """
SELECT *
FROM sales_table
ORDER BY Sales DESC
"""

df = pd.read_sql(query, engine)
```

---

# SQL / Excel Comparison

Running SQL in Python resembles SQL tools and Excel data imports.

| Concept | Pandas | SQL Tool | Excel |
|------|------|------|------|
| run SQL query | read_sql() | run query | Power Query |
| result | DataFrame | result table | worksheet |
| filtering | WHERE | WHERE | filter |
| aggregation | GROUP BY | GROUP BY | pivot table |

Example SQL tool workflow:

```sql
SELECT City, SUM(Sales)
FROM sales_table
GROUP BY City
```

Equivalent Python workflow:

```python
df = pd.read_sql(query, engine)
```

Excel equivalent:

Use **Pivot Table** after importing data.

---

# Practice Exercises

## Exercise 1

Tags: Tuples, SELECT, SQL Queries

Run a simple query.

```python
df = pd.read_sql("SELECT * FROM sales_table", engine)
```

---

## Exercise 2

Tags: SELECT, WHERE

Filter records with SQL.

```python
df = pd.read_sql(
"SELECT * FROM sales_table WHERE Sales > 100",
engine
)
```

---

## Exercise 3

Tags: SELECT, GROUP BY, Arithmetic

Calculate totals by city.

```python
df = pd.read_sql(
"""
SELECT City, SUM(Sales)
FROM sales_table
GROUP BY City
""",
engine
)
```

---

# Common Mistakes

## Loading Too Much Data

Example:

```sql
SELECT *
FROM huge_table
```

Large queries may overload Python memory.

Always filter data when possible.

---

## SQL Syntax Errors

Example:

```sql
SELECT FROM sales_table
```

SQL syntax errors will cause the query to fail.

---

## Mixing Python and SQL Syntax

Incorrect:

```python
SELECT * FROM sales_table
```

SQL must be inside a **Python string**.

Correct:

```python
query = "SELECT * FROM sales_table"
```

---

# Real-World Use

Running SQL inside Python is extremely common.

Examples include:

• pulling data for dashboards  
• retrieving healthcare claims data  
• extracting warehouse data for analysis  
• building automated data pipelines  

Example workflow:

```python
query = """
SELECT provider_id, COUNT(*) AS total_claims
FROM claims
GROUP BY provider_id
"""

df = pd.read_sql(query, engine)
```

This retrieves summarized claims data for analysis.

---

# Lesson Recap

In this lesson you learned:

• how to write SQL queries inside Python  
• how to execute SQL using Pandas  
• how SQL and Python work together in analytics workflows  
• best practices for retrieving data efficiently  

Combining SQL with Python allows analysts to **retrieve, process, and analyze data within a single workflow**.

---

# Next Lesson

Next we will learn:

# Lesson 5 — Writing Data Back to a Database

You will learn:

• how to insert data into a database from Python  
• how Pandas exports DataFrames to database tables  
• how data pipelines load processed data back into databases  

This is an important step for **data pipelines and automated workflows**.
