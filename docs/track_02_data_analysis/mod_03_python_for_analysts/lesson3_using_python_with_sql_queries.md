# Module 15 — Python for Analysts

# Lesson 3 — Using Python with SQL Queries

---

# Lesson Objective

By the end of this lesson learners will understand:

• how Python connects to relational databases  
• how to execute **SQL queries from Python**  
• how query results can be loaded into **Pandas DataFrames**  
• how Python and SQL work together for **data analysis and reporting**

Python allows analysts to combine the strengths of **SQL (data extraction)** and **Python (data transformation and automation)**.

---

# Overview

Many analysts already use SQL to retrieve data from databases.

Example SQL query:

```sql
SELECT customer_id, sales
FROM transactions
WHERE year = 2024;
```

Normally this query is run inside:

```text
SQL Server
Snowflake
Oracle
PostgreSQL
MySQL
```

However, Python can execute the same query and store the results in a **DataFrame**.

Example workflow:

```text
Database → SQL Query → Python DataFrame → Data Processing → Report
```

This allows analysts to:

• run SQL queries  
• transform the results  
• combine data with other sources  
• automate reporting workflows

---

# Key Idea Cards (3 Cards)

### Python Can Run SQL Queries

Python can connect to many database systems using database drivers.

Common libraries include:

```text
sqlalchemy
pyodbc
psycopg2
pymysql
```

These libraries allow Python to communicate with databases.

---

### SQL Results Become DataFrames

When Python runs a SQL query, the results can be loaded into a **Pandas DataFrame**.

Example:

```python
df = pd.read_sql(query, connection)
```

This makes SQL results easy to analyze in Python.

---

### SQL + Python Is a Powerful Combination

A common workflow is:

```text
SQL → extract data
Python → transform data
Python → generate report
```

This allows complex reporting pipelines.

---

# Key Concepts

## Database Connections

Before running SQL queries, Python must establish a connection to the database.

Example:

```python
import pyodbc

connection = pyodbc.connect(
    "DRIVER={SQL Server};"
    "SERVER=server_name;"
    "DATABASE=database_name;"
    "Trusted_Connection=yes;"
)
```

This creates a connection between Python and the database.

---

## Running SQL Queries

Once connected, Python can execute SQL queries.

Example:

```python
query = """
SELECT customer_id, sales
FROM transactions
WHERE year = 2024
"""
```

---

## Loading Query Results into Pandas

Pandas provides a function that automatically converts SQL results into a DataFrame.

Example:

```python
import pandas as pd

df = pd.read_sql(query, connection)

print(df.head())
```

Output example:

| customer_id | sales |
|---|---|
| 101 | 200 |
| 102 | 150 |
| 103 | 300 |

---

## Combining SQL and Python Transformations

After loading the data, Python can perform additional transformations.

Example:

```python
df["sales_tax"] = df["sales"] * 0.08
```

Python can also perform aggregations.

Example:

```python
total_sales = df["sales"].sum()
```

---

# Decision Flow

When deciding where logic should live:

```text
Large dataset filtering needed?
        ↓
Use SQL
```

```text
Complex transformations required?
        ↓
Use Python
```

```text
Repeated reporting workflow?
        ↓
Combine SQL + Python automation
```

Example pipeline:

```text
SQL Database
      ↓
Python Query
      ↓
Python Transformations
      ↓
Excel / Dashboard Output
```

---

# Code Examples

### Example 1 — Connect to Database

```python
import pyodbc

connection = pyodbc.connect(
    "DRIVER={SQL Server};"
    "SERVER=my_server;"
    "DATABASE=sales_db;"
    "Trusted_Connection=yes;"
)
```

---

### Example 2 — Execute SQL Query

```python
query = """
SELECT customer_id, sales
FROM transactions
WHERE year = 2024
"""
```

---

### Example 3 — Load Results into DataFrame

```python
import pandas as pd

df = pd.read_sql(query, connection)

print(df.head())
```

---

### Example 4 — Perform Calculations

```python
df["tax"] = df["sales"] * 0.08

print(df.head())
```

---

# SQL / Excel Comparison

### SQL Example

```sql
SELECT SUM(sales)
FROM transactions;
```

---

### Excel Example

```text
=SUM(B2:B100)
```

---

### Python Example

```python
df["sales"].sum()
```

All three approaches produce the same result, but Python allows automation.

---

# Practice Exercises

### Exercise 1

Tags: SELECT, SQL Queries

Write a SQL query that retrieves customer sales data.

---

### Exercise 2

Tags: DataFrames, SQL Queries, Data I/O

Load the SQL query results into a Pandas DataFrame.

---

### Exercise 3

Tags: Arithmetic, Data Analysis

Create a new column that calculates a tax value.

---

### Exercise 4

Tags: Arithmetic, Data Analysis

Calculate total sales using Python.

---

# Common Mistakes

### Loading Too Much Data

Large datasets should be filtered using SQL before loading into Python.

Example:

```sql
WHERE year = 2024
```

---

### Storing Credentials in Scripts

Database credentials should not be hardcoded.

Instead use:

```text
environment variables
.env files
```

---

### Forgetting to Close Connections

Connections should be closed after use.

Example:

```python
connection.close()
```

---

# Real-World Use

Many organizations use Python + SQL together for reporting.

Examples include:

```text
Automated sales reports
Financial reporting pipelines
Data warehouse transformations
Dashboard data preparation
```

Example workflow:

```text
SQL Data Warehouse
        ↓
Python Data Processing
        ↓
Clean Reporting Dataset
        ↓
Dashboard or Excel Output
```

Python acts as the **automation layer for analytics workflows**.

---

# Lesson Recap

In this lesson you learned:

• how Python connects to databases  
• how Python executes SQL queries  
• how query results become DataFrames  
• how Python and SQL work together in reporting pipelines

This combination is one of the **most common workflows used by data professionals**.

---

# Next Lesson

Next we will continue Module 15 with:

# Lesson 4 — Automating Repetitive Data Tasks

You will learn:

• how Python automates repetitive analyst work  
• how to process multiple files automatically  
• how automation reduces manual reporting tasks  
• how to build simple automation scripts.
