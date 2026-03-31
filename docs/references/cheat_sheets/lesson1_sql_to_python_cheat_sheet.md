# Module 11 — Python Engineering Handbook

# Lesson 7 — SQL-to-Python Cheat Sheet

---

# Lesson Objective

By the end of this lesson learners will understand:

• how common **SQL operations translate into Python**  
• how **pandas DataFrame operations replicate SQL queries**  
• how analysts familiar with SQL can transition into Python data workflows  
• common patterns used when manipulating datasets in Python  

Many analysts and data engineers already know SQL. This lesson acts as a **reference guide** that shows how common SQL tasks map directly to Python.

---

# Overview

SQL is designed for querying structured data stored in databases.

Example SQL query:

```sql
SELECT customer_id, total_sales
FROM sales
WHERE region = 'West';
```

In Python, the same operation can be performed using a **pandas DataFrame**.

Example Python equivalent:

```python
filtered = df[df["region"] == "West"][["customer_id", "total_sales"]]
```

The logic is very similar:

| SQL | Python |
|----|----|
| SELECT | choose columns |
| WHERE | filter rows |
| GROUP BY | aggregate |
| JOIN | merge datasets |

Learning these equivalents allows SQL users to quickly become productive in Python.

---

# Key Idea Cards (3 Cards)

### Pandas DataFrames Behave Like Tables

A pandas DataFrame is conceptually similar to a database table.

Example:

```text
Rows → records
Columns → fields
```

You can filter, aggregate, and transform the data.

---

### SQL Logic Maps Closely to Python

Most SQL operations have direct equivalents in pandas.

Example:

```text
SELECT → column selection
WHERE → filtering
GROUP BY → groupby()
JOIN → merge()
```

This makes Python intuitive for SQL users.

---

### Python Allows More Flexible Data Processing

Unlike SQL, Python allows you to combine:

• data processing  
• automation  
• machine learning  
• visualization  

This makes Python extremely powerful for analytics workflows.

---

# Key Concepts

## Selecting Columns

SQL:

```sql
SELECT customer_id, sales
FROM transactions;
```

Python:

```python
df[["customer_id", "sales"]]
```

This selects specific columns from the dataset.

---

## Filtering Rows

SQL:

```sql
SELECT *
FROM sales
WHERE region = 'West';
```

Python:

```python
df[df["region"] == "West"]
```

Filtering works similarly to SQL WHERE clauses.

---

## Aggregations

SQL:

```sql
SELECT region, SUM(sales)
FROM sales
GROUP BY region;
```

Python:

```python
df.groupby("region")["sales"].sum()
```

Grouping operations behave similarly.

---

# Decision Flow

When translating SQL logic to Python:

```text
Need to filter rows?
      ↓
Use boolean filtering

Need aggregations?
      ↓
Use groupby()

Need to join datasets?
      ↓
Use merge()
```

Understanding these patterns makes translation easy.

---

# Code Examples

### Example 1 — SQL SELECT

SQL:

```sql
SELECT name, age
FROM customers;
```

Python:

```python
df[["name", "age"]]
```

---

### Example 2 — SQL WHERE

SQL:

```sql
SELECT *
FROM customers
WHERE age > 30;
```

Python:

```python
df[df["age"] > 30]
```

---

### Example 3 — SQL GROUP BY

SQL:

```sql
SELECT region, COUNT(*)
FROM sales
GROUP BY region;
```

Python:

```python
df.groupby("region").size()
```

---

### Example 4 — SQL JOIN

SQL:

```sql
SELECT *
FROM orders
JOIN customers
ON orders.customer_id = customers.customer_id;
```

Python:

```python
merged = orders.merge(customers, on="customer_id")
```

This merges two datasets using a common key.

---

# SQL / Excel Comparison

Many SQL operations also exist in Excel.

| Operation | SQL | Python | Excel |
|------|------|------|------|
| filtering | WHERE | boolean filtering | filters |
| aggregation | GROUP BY | groupby() | pivot tables |
| joins | JOIN | merge() | VLOOKUP/XLOOKUP |
| sorting | ORDER BY | sort_values() | sort |

Example Excel equivalent:

```text
Pivot Table → GROUP BY
```

This shows that many analytics tools share similar concepts.

---

# Practice Exercises

### Exercise 1

Tags: Missing Data, SELECT, WHERE, SQL Queries

Write Python code that replicates this SQL query:

```sql
SELECT name
FROM employees
WHERE department = 'Finance';
```

---

### Exercise 2

Tags: SELECT, GROUP BY, SQL Queries

Translate this SQL query into Python:

```sql
SELECT region, AVG(sales)
FROM sales
GROUP BY region;
```

---

### Exercise 3

Tags: JOIN, Data Engineering

Join two datasets in Python.

Example tables:

```text
orders
customers
```

Join on:

```text
customer_id
```

---

### Exercise 4

Tags: Lists, groupby(), Aggregations, GROUP BY

Create a pivot-style aggregation using pandas.

Example:

```python
df.groupby("category")["revenue"].sum()
```

---

# Common Mistakes

### Treating Pandas Exactly Like SQL

Although pandas resembles SQL, it is still Python.

Understanding Python syntax is important.

---

### Ignoring Index Behavior

Pandas DataFrames use indexes that may affect operations.

Always check the DataFrame index when filtering or merging.

---

### Inefficient Filtering

Chaining filters incorrectly may create inefficient code.

Example improvement:

```python
df[(df["region"] == "West") & (df["sales"] > 1000)]
```

Use combined conditions when possible.

---

# Real-World Use

Many analytics teams use Python together with SQL.

Example workflow:

```text
Extract data using SQL
        ↓
Load into pandas DataFrame
        ↓
Perform transformations
        ↓
Build dashboards or machine learning models
```

This hybrid workflow is common in:

• data engineering pipelines  
• analytics platforms  
• machine learning systems  
• business intelligence workflows.

Python complements SQL by enabling **advanced processing and automation**.

---

# Lesson Recap

In this lesson you learned:

• how SQL queries translate into Python operations  
• how pandas replicates common SQL patterns  
• how analysts can transition from SQL to Python  
• common operations used in analytics workflows.

This cheat sheet provides a quick reference when moving between **SQL and Python data processing**.

---

# Module 11 Complete

You have now completed the **Python Learning Hub** curriculum.

Throughout these modules you learned:

```text
Python fundamentals
Data analysis with pandas
Working with data sources
Clean code practices
Object-oriented programming
Data engineering foundations
Building data applications
Professional engineering practices
Automation and CI/CD
Python engineering standards
```

This training prepares learners to build **production-ready Python applications for data and analytics workflows**.
