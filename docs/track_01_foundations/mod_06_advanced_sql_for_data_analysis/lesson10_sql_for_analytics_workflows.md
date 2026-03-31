# Module 13 — Advanced SQL for Data Analysis

# Lesson 10 — SQL for Analytics Workflows

---

# Lesson Objective

By the end of this lesson learners will understand:

• how SQL fits into **modern data workflows**  
• how analysts combine **SQL with Python and analytics tools**  
• how SQL supports **data pipelines and reporting systems**  
• how SQL is used in real-world **analytics environments**

SQL is not just a querying language—it is a **core component of the entire analytics ecosystem**.

---

# Overview

In most analytics environments, SQL is used to retrieve and transform data before it is analyzed or visualized.

A typical analytics workflow looks like this:

```text
Database
   ↓
SQL Query
   ↓
Python / Pandas
   ↓
Visualization / Dashboard
```

For example:

```text
Healthcare database → SQL query → Python analysis → dashboard
```

SQL retrieves the necessary data from databases, while tools like Python and BI platforms perform additional analysis and visualization.

---

# Key Idea Cards (3 Cards)

### SQL Is the Foundation of Data Analysis

Most data in organizations is stored in **databases**.

SQL is used to:

```text
Retrieve data
Filter records
Aggregate metrics
Prepare datasets
```

Without SQL, analysts cannot access structured data effectively.

---

### SQL Works with Many Data Tools

SQL is commonly used alongside tools such as:

```text
Python
Power BI
Tableau
Excel
Data pipelines
```

These tools often rely on SQL queries to retrieve data.

---

### SQL Enables Data Pipelines

Many automated systems depend on SQL queries.

Examples:

```text
ETL pipelines
Data warehouse transformations
Scheduled reports
Analytics dashboards
```

SQL plays a central role in these workflows.

---

# Key Concepts

## SQL as the Data Retrieval Layer

In most analytics environments, SQL is responsible for retrieving data from databases.

Example:

```sql
SELECT
    customer_id,
    order_date,
    revenue
FROM orders
WHERE order_date >= '2024-01-01';
```

This query retrieves relevant data for further analysis.

---

## SQL + Python Workflow

SQL is often used to load data into Python.

Example workflow:

```text
Database → SQL → Python → Visualization
```

Example Python code:

```python
query = """
SELECT order_date, revenue
FROM sales
WHERE order_date >= '2024-01-01'
"""

df = pd.read_sql(query, connection)
```

Python then performs analysis on the dataset.

---

## SQL for Dashboard Data

Business intelligence dashboards rely heavily on SQL queries.

Example:

```sql
SELECT
    region,
    SUM(revenue) AS total_revenue
FROM sales
GROUP BY region;
```

This query produces summarized data used in dashboards.

---

## SQL in Data Pipelines

SQL is frequently used in automated workflows.

Example pipeline:

```text
Raw Data
   ↓
SQL transformation
   ↓
Clean dataset
   ↓
Analytics or reporting
```

SQL transformations often include:

```text
Filtering
Aggregations
Joins
Data classification
```

---

# Decision Flow

When building analytics workflows:

```text
Need data from a database?
        ↓
Write SQL query
```

If further analysis is required:

```text
Load SQL results into Python or BI tools
```

If automation is needed:

```text
Use SQL in data pipelines
```

SQL often serves as the **first step in data processing**.

---

# Code Examples

### Example 1 — Data Extraction

```sql
SELECT
    order_id,
    customer_id,
    revenue
FROM orders
WHERE order_date >= '2024-01-01';
```

This query retrieves recent order data.

---

### Example 2 — Dashboard Dataset

```sql
SELECT
    region,
    SUM(revenue) AS total_revenue
FROM sales
GROUP BY region;
```

This prepares aggregated data for visualization.

---

### Example 3 — Customer Analysis Dataset

```sql
SELECT
    customer_id,
    COUNT(order_id) AS total_orders,
    SUM(revenue) AS total_spent
FROM orders
GROUP BY customer_id;
```

This creates a dataset used for customer segmentation.

---

### Example 4 — Healthcare Claims Analysis

Healthcare example:

```sql
SELECT
    provider_id,
    SUM(claim_amount) AS total_claims
FROM claims
WHERE claim_date >= '2024-01-01'
GROUP BY provider_id;
```

This query identifies provider claim totals.

---

# SQL / Excel / Python Comparison

SQL is frequently combined with other tools.

| Tool | Purpose |
|---|---|
| SQL | retrieve and transform data |
| Python | advanced analysis |
| Excel | quick reporting |
| BI tools | visualization |

Example workflow:

Python example:

```python
df = pd.read_sql(query, connection)
df.groupby("region")["revenue"].sum()
```

SQL retrieves the dataset; Python performs additional analysis.

---

# Practice Exercises

### Exercise 1

Tags: SELECT, SQL Queries, CI/CD, Arithmetic

Write a SQL query that retrieves orders placed in **2024**.

Table:

```text
orders
```

---

### Exercise 2

Tags: CI/CD, SQL

Create a dataset showing **total revenue by region**.

Table:

```text
sales
```

---

### Exercise 3

Tags: SQL Queries, CI/CD

Create a query showing **total orders per customer**.

Table:

```text
orders
```

---

### Exercise 4

Tags: SQL Queries, CI/CD

Create a query showing **total claim amounts per provider**.

Table:

```text
claims
```

---

# Common Mistakes

### Retrieving Too Much Data

Queries that return too many rows can slow down analysis.

Example:

```sql
SELECT *
FROM transactions;
```

Better approach:

```sql
SELECT transaction_id, amount
FROM transactions
WHERE transaction_date >= '2024-01-01';
```

---

### Mixing SQL and Python Logic Inefficiently

Some transformations are better done in SQL.

Example tasks suited for SQL:

```text
Filtering
Aggregations
Joining tables
```

Python is better suited for:

```text
Machine learning
Statistical analysis
Advanced transformations
```

---

# Real-World Use

SQL workflows are common in many industries.

Examples include:

```text
Sales reporting
Healthcare analytics
Customer behavior analysis
Financial reporting
```

Example healthcare pipeline:

```text
Claims database
   ↓
SQL query
   ↓
Python analysis
   ↓
Dashboard reporting
```

SQL enables organizations to **access and prepare large datasets for analysis**.

---

# Lesson Recap

In this lesson you learned:

• how SQL fits into analytics workflows  
• how SQL interacts with Python and BI tools  
• how SQL supports dashboards and pipelines  
• how SQL enables data-driven analysis

SQL serves as the **foundation of most modern data analysis systems**.

---

# Module 13 Complete

You have now learned advanced SQL concepts including:

```text
Subqueries
CTEs
Window functions
Ranking functions
Running totals
Advanced joins
CASE statements
NULL handling
Query optimization
Analytics workflows
```

These skills allow analysts to **write powerful SQL queries used in real analytics environments**.
