# Module 4 — Working with Data Sources

# Lesson 3 — Connecting to Databases

---

# Lesson Objective

By the end of this lesson learners will understand:

• how Python connects to databases  
• how Pandas retrieves data using SQL queries  
• what database connection strings are  
• how database workflows compare to SQL tools and Excel  

Connecting to databases allows analysts to **pull data directly from production systems instead of working only with files**.

---

# Overview

In many organizations, data is not stored in files like CSV or Excel. Instead, it lives inside **databases**.

Examples of common databases:

• SQL Server  
• Oracle  
• PostgreSQL  
• MySQL  
• Snowflake  
• Databricks  

These databases store data in **tables** that can be queried using SQL.

Example SQL query:

```sql
SELECT Customer, City, Sales
FROM sales_table
```

Python can connect to a database, run a SQL query, and load the results into a **Pandas DataFrame**.

Example workflow:

```python
import pandas as pd
import sqlalchemy

engine = sqlalchemy.create_engine("connection_string")

df = pd.read_sql("SELECT * FROM sales_table", engine)

print(df.head())
```

Output:

```text
Customer   City        Sales
Alice      Los Angeles 120
Bob        Chicago     200
Maria      New York    150
```

This allows analysts to **combine SQL and Python in the same workflow**.

---

# Key Idea Cards (3 Cards)

## Databases Store Structured Data

Databases store information in structured tables.

Example table:

| Customer | City | Sales |
|------|------|------|
| Alice | LA | 120 |
| Bob | Chicago | 200 |

These tables can be queried using SQL.

---

## Python Can Query Databases

Python can connect to a database and execute SQL queries.

Example:

```python
df = pd.read_sql("SELECT * FROM sales_table", connection)
```

The result is automatically loaded into a DataFrame.

---

## SQL and Python Work Together

In many data workflows:

• SQL retrieves the data  
• Python analyzes the data  

Example workflow:

```text
Database → SQL query → Pandas DataFrame → Analysis
```

---

# Key Concepts

## Database Connection

Before querying data, Python must connect to the database.

Example:

```python
import sqlalchemy

engine = sqlalchemy.create_engine("database_connection_string")
```

This creates a connection to the database server.

---

## Running SQL Queries

Once connected, Python can run SQL queries.

Example:

```python
df = pd.read_sql("SELECT * FROM sales_table", engine)
```

This returns the query result as a DataFrame.

---

## Connection Strings

A **connection string** tells Python how to connect to the database.

Example:

```text
postgresql://username:password@server:5432/database
```

This contains:

• database type  
• username  
• password  
• server location  
• database name  

---

# Decision Flow

Retrieving data from a database usually follows this workflow:

```text
Connect to database
      ↓
Write SQL query
      ↓
Run query from Python
      ↓
Load results into DataFrame
      ↓
Analyze data
```

Example:

```python
engine = sqlalchemy.create_engine(connection_string)

df = pd.read_sql("SELECT * FROM sales_table", engine)
```

---

# Code Examples

## Example 1 — Connecting to a Database

```python
import sqlalchemy

engine = sqlalchemy.create_engine(
    "postgresql://user:password@localhost:5432/sales_db"
)
```

This creates a database connection.

---

## Example 2 — Running a SQL Query

```python
import pandas as pd

query = "SELECT * FROM sales_table"

df = pd.read_sql(query, engine)

print(df.head())
```

---

## Example 3 — Selecting Specific Columns

```python
query = """
SELECT Customer, Sales
FROM sales_table
"""

df = pd.read_sql(query, engine)
```

---

## Example 4 — Filtering with SQL

```python
query = """
SELECT *
FROM sales_table
WHERE Sales > 100
"""

df = pd.read_sql(query, engine)
```

This filters results before loading them into Python.

---

# SQL / Excel Comparison

Working with databases in Python resembles SQL workflows.

| Concept | Pandas | SQL Tool | Excel |
|------|------|------|------|
| connect to database | SQLAlchemy | DB connection | Power Query |
| run query | read_sql() | run query | data import |
| result | DataFrame | query result table | worksheet |

Example SQL tool workflow:

```sql
SELECT *
FROM sales_table
```

Equivalent Python workflow:

```python
df = pd.read_sql("SELECT * FROM sales_table", engine)
```

Excel equivalent:

Import data from database using **Power Query**.

---

# Practice Exercises

## Exercise 1

Tags: Strings, SQLAlchemy, Imports, Databases

Create a connection to a database.

```python
import sqlalchemy

engine = sqlalchemy.create_engine("connection_string")
```

---

## Exercise 2

Tags: Tuples, SELECT, SQL Queries, Databases

Run a SQL query.

```python
df = pd.read_sql("SELECT * FROM sales_table", engine)
```

---

## Exercise 3

Tags: SELECT, WHERE, Databases

Filter results using SQL.

```python
df = pd.read_sql(
    "SELECT * FROM sales_table WHERE Sales > 100",
    engine
)
```

---

# Common Mistakes

## Hardcoding Credentials

Example:

```python
engine = sqlalchemy.create_engine(
"postgresql://user:password@server/db"
)
```

This can expose sensitive credentials.

It is better to store credentials in **environment variables**.

---

## Pulling Too Much Data

Example:

```python
SELECT * FROM huge_table
```

This may load millions of rows.

Better approach:

```text
SELECT needed_columns
FROM table
WHERE conditions
```

---

## Database Driver Missing

Some database connections require additional drivers.

Examples:

• `psycopg2` for PostgreSQL  
• `pyodbc` for SQL Server  
• `cx_Oracle` for Oracle  

---

# Real-World Use

Database connections are extremely common in analytics.

Examples include:

• querying data warehouses  
• pulling healthcare claims data  
• retrieving sales data for dashboards  
• integrating operational databases  

Example workflow:

```python
query = """
SELECT provider_id, total_claims
FROM claims_table
"""

df = pd.read_sql(query, engine)
```

This loads claims data into a DataFrame for analysis.

---

# Lesson Recap

In this lesson you learned:

• how Python connects to databases  
• how to run SQL queries using Pandas  
• how query results become DataFrames  
• how Python integrates with database workflows  

Database connections allow analysts to work with **live production data instead of static files**.

---

# Next Lesson

Next we will learn:

# Lesson 4 — Running SQL in Python

You will learn:

• how to write SQL queries inside Python scripts  
• how SQL and Python complement each other  
• best practices for combining SQL and Pandas  

This is a key skill for **data analysts and data engineers**.
