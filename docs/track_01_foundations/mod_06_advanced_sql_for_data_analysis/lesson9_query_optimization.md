# Module 13 — Advanced SQL for Data Analysis

# Lesson 9 — Query Optimization

---

# Lesson Objective

By the end of this lesson learners will understand:

• why **SQL query performance matters**  
• how **query design affects database speed**  
• how to write **efficient SQL queries**  
• how analysts avoid common **performance issues**

As datasets grow larger, poorly written queries can become **very slow and expensive to run**. Query optimization helps ensure that SQL queries run **efficiently and scale to large datasets**.

---

# Overview

In real-world environments, databases often contain **millions or billions of rows**.

A poorly written query might:

```text
Scan an entire table
Join too many rows
Return unnecessary columns
Run for minutes or hours
```

An optimized query:

```text
Filters early
Uses indexes
Retrieves only required columns
Minimizes unnecessary joins
```

Example of an inefficient query:

```sql
SELECT *
FROM orders;
```

This retrieves **every column and every row**.

A better query would be:

```sql
SELECT order_id, order_date, revenue
FROM orders
WHERE order_date >= '2024-01-01';
```

This returns only the **necessary data**.

---

# Key Idea Cards (3 Cards)

### Query Design Impacts Performance

How a query is written affects how quickly it runs.

Examples of poor design:

```text
SELECT *
Unnecessary joins
No filtering conditions
```

Efficient queries minimize unnecessary processing.

---

### Indexes Improve Query Speed

Indexes allow the database to find rows **much faster**.

Example:

```text
Search using indexed column
```

Instead of scanning the entire table, the database can jump directly to the correct rows.

---

### Filtering Early Reduces Work

Applying filters early reduces the number of rows processed.

Example:

```sql
WHERE order_date >= '2024-01-01'
```

This avoids scanning unnecessary data.

---

# Key Concepts

## Avoid SELECT *

Using `SELECT *` retrieves every column.

Example:

```sql
SELECT *
FROM customers;
```

Problems:

```text
Slower queries
More data transferred
Harder to read queries
```

Better approach:

```sql
SELECT customer_id, name
FROM customers;
```

Only retrieve columns that are needed.

---

## Filtering with WHERE

Filtering reduces the number of rows returned.

Example:

```sql
SELECT order_id, revenue
FROM orders
WHERE order_date >= '2024-01-01';
```

This ensures the database processes only relevant records.

---

## Using Indexes

Indexes help databases locate rows quickly.

Example index column:

```text
customer_id
order_id
transaction_date
```

Query example:

```sql
SELECT *
FROM orders
WHERE customer_id = 123;
```

If `customer_id` is indexed, the query will run much faster.

---

## Reducing Joins

Each join adds complexity to the query.

Example:

```text
JOIN customers
JOIN products
JOIN regions
```

Large joins can significantly increase query time.

Analysts should ensure joins are **necessary and efficient**.

---

## Limiting Returned Rows

When exploring data, it is helpful to limit results.

Example:

```sql
SELECT *
FROM orders
LIMIT 100;
```

This prevents retrieving millions of rows unnecessarily.

---

# Decision Flow

When writing SQL queries:

```text
Are you retrieving too many rows?
        ↓
Add WHERE filters
```

If queries run slowly:

```text
Check indexes
Reduce joins
Avoid SELECT *
```

Efficient queries minimize unnecessary processing.

---

# Code Examples

### Example 1 — Inefficient Query

```sql
SELECT *
FROM orders;
```

Problems:

```text
Scans entire table
Returns unnecessary columns
```

---

### Example 2 — Optimized Query

```sql
SELECT order_id, order_date, revenue
FROM orders
WHERE order_date >= '2024-01-01';
```

Benefits:

```text
Smaller dataset
Faster execution
Less memory usage
```

---

### Example 3 — Filtering Early

```sql
SELECT customer_id, revenue
FROM orders
WHERE revenue > 1000;
```

Filtering early reduces rows processed.

---

### Example 4 — Healthcare Claims Example

Healthcare example:

```sql
SELECT
    provider_id,
    claim_amount
FROM claims
WHERE claim_date >= '2024-01-01';
```

This limits results to **recent claims**.

---

# SQL / Excel / Python Comparison

Query optimization concepts appear in other tools.

| SQL | Python | Excel |
|---|---|---|
| WHERE | filtering | filters |
| SELECT columns | selecting columns | selecting fields |
| LIMIT | head() | preview rows |

Python example:

```python
df[["order_id", "revenue"]].head(100)
```

Equivalent SQL:

```sql
SELECT order_id, revenue
FROM orders
LIMIT 100;
```

Optimizing queries improves performance in **any data tool**.

---

# Practice Exercises

### Exercise 1

Tags: SELECT, SQL Queries, Performance

Rewrite this inefficient query:

```sql
SELECT *
FROM sales;
```

Return only:

```text
sale_id
sale_date
revenue
```

---

### Exercise 2

Tags: SELECT, SQL Queries, Arithmetic, Performance

Retrieve orders from **2023 onward**.

Table:

```text
orders
```

---

### Exercise 3

Tags: SELECT, SQL Queries, Arithmetic, Performance

Retrieve customers who spent more than **5000**.

Table:

```text
customers
```

---

### Exercise 4

Tags: SQL Queries, Arithmetic, Performance

Limit query results to the first **50 rows**.

Table:

```text
orders
```

---

# Common Mistakes

### Using SELECT * in Production Queries

This retrieves unnecessary data.

Always select only the required columns.

---

### Missing Filters

Queries without filters can scan entire tables.

Example problem:

```sql
SELECT *
FROM transactions;
```

Large tables may contain millions of rows.

---

### Joining Too Many Tables

Unnecessary joins increase query complexity.

Always ensure joins are required for the analysis.

---

# Real-World Use

Query optimization is essential when working with large datasets.

Examples include:

```text
Healthcare claims datasets
Customer transaction records
Financial reporting systems
Product sales databases
```

Healthcare example:

```sql
SELECT
    provider_id,
    SUM(claim_amount)
FROM claims
WHERE claim_date >= '2024-01-01'
GROUP BY provider_id;
```

This query focuses only on **recent claims**, improving performance.

Optimized queries ensure analysts can work efficiently with **large-scale data environments**.

---

# Lesson Recap

In this lesson you learned:

• why SQL performance matters  
• how query design affects speed  
• how indexes and filters improve performance  
• how analysts write efficient queries

Efficient SQL queries ensure databases can handle **large datasets quickly and reliably**.

---

# Next Lesson

Next we will complete Module 13 with:

# Lesson 10 — SQL for Analytics Workflows

You will learn:

• how SQL fits into modern **data workflows**  
• how analysts combine **SQL with Python and dashboards**  
• how SQL supports **data pipelines and analytics systems**.
