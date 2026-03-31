# Module 13 — Advanced SQL for Data Analysis

# Lesson 2 — Common Table Expressions (CTEs)

---

# Lesson Objective

By the end of this lesson learners will understand:

• what **Common Table Expressions (CTEs)** are  
• how CTEs simplify complex SQL queries  
• how CTEs compare to **subqueries**  
• how analysts use CTEs to build **step-by-step queries**

CTEs are one of the most important SQL techniques because they allow queries to be written in a **clear and modular structure**.

---

# Overview

A **Common Table Expression (CTE)** is a temporary result set that can be referenced within a SQL query.

CTEs begin with the keyword:

```sql
WITH
```

Example:

```sql
WITH regional_sales AS (
    SELECT region, SUM(revenue) AS total_revenue
    FROM sales
    GROUP BY region
)
SELECT *
FROM regional_sales;
```

This query performs two steps:

```text
Step 1: Calculate revenue by region
Step 2: Retrieve results from the temporary table
```

The CTE acts like a **temporary table that exists only during the query execution**.

---

# Key Idea Cards (3 Cards)

### CTEs Create Temporary Tables

A CTE defines a temporary dataset that exists only during the query.

Example:

```sql
WITH summary_table AS (
    SELECT region, SUM(sales)
    FROM sales
    GROUP BY region
)
SELECT *
FROM summary_table;
```

---

### CTEs Improve Query Readability

Instead of writing deeply nested subqueries, analysts can organize queries into **logical steps**.

Example workflow:

```text
Step 1 → calculate revenue
Step 2 → filter results
Step 3 → rank results
```

---

### CTEs Are Common in Analytics

CTEs are frequently used for:

```text
Data transformations
Multi-step analysis
Ranking and window functions
Data pipeline queries
```

---

# Key Concepts

## Basic CTE Structure

A CTE always follows this pattern:

```sql
WITH cte_name AS (
    SELECT columns
    FROM table
)
SELECT *
FROM cte_name;
```

The first query defines the temporary dataset.

The second query uses it.

---

## Multiple CTEs

SQL allows multiple CTEs in the same query.

Example:

```sql
WITH sales_by_region AS (
    SELECT region, SUM(revenue) AS revenue
    FROM sales
    GROUP BY region
),
high_performing_regions AS (
    SELECT *
    FROM sales_by_region
    WHERE revenue > 10000
)
SELECT *
FROM high_performing_regions;
```

Steps:

```text
Step 1: Calculate revenue by region
Step 2: Filter high performing regions
Step 3: Return final results
```

---

## CTE vs Subquery

Subqueries and CTEs can often accomplish the same result.

Subquery example:

```sql
SELECT *
FROM (
    SELECT region, SUM(revenue) AS revenue
    FROM sales
    GROUP BY region
) AS regional_sales;
```

CTE version:

```sql
WITH regional_sales AS (
    SELECT region, SUM(revenue) AS revenue
    FROM sales
    GROUP BY region
)
SELECT *
FROM regional_sales;
```

CTEs are usually **easier to read and maintain**.

---

# Decision Flow

When writing SQL queries:

```text
Is the query becoming complex?
        ↓
Break logic into steps
        ↓
Use CTEs
```

Example:

```text
Calculate revenue
Filter regions
Rank performance
```

Each step can become its own CTE.

---

# Code Examples

### Example 1 — Sales by Region

```sql
WITH sales_summary AS (
    SELECT region, SUM(revenue) AS total_revenue
    FROM sales
    GROUP BY region
)
SELECT *
FROM sales_summary;
```

This calculates total revenue by region.

---

### Example 2 — Filtering Results

```sql
WITH sales_summary AS (
    SELECT region, SUM(revenue) AS total_revenue
    FROM sales
    GROUP BY region
)
SELECT *
FROM sales_summary
WHERE total_revenue > 10000;
```

This returns only high-performing regions.

---

### Example 3 — Multi-Step Analysis

```sql
WITH sales_summary AS (
    SELECT region, SUM(revenue) AS total_revenue
    FROM sales
    GROUP BY region
),
ranked_sales AS (
    SELECT region, total_revenue,
           RANK() OVER(ORDER BY total_revenue DESC) AS rank
    FROM sales_summary
)
SELECT *
FROM ranked_sales;
```

This query:

```text
Step 1: Calculates revenue
Step 2: Ranks regions
```

---

### Example 4 — Using CTE with Joins

```sql
WITH order_totals AS (
    SELECT customer_id, SUM(amount) AS total_spent
    FROM orders
    GROUP BY customer_id
)
SELECT customers.name, order_totals.total_spent
FROM customers
JOIN order_totals
ON customers.customer_id = order_totals.customer_id;
```

This joins the CTE to another table.

---

# SQL / Excel / Python Comparison

CTEs resemble intermediate variables in other tools.

| Concept | SQL | Python | Excel |
|---|---|---|---|
| intermediate step | CTE | variable | helper table |
| multi-step logic | multiple CTEs | functions | formulas |

Python equivalent:

```python
sales_summary = df.groupby("region")["revenue"].sum()

sales_summary[sales_summary > 10000]
```

CTEs provide the same **step-by-step logic inside SQL**.

---

# Practice Exercises

### Exercise 1

Tags: CTEs, Arithmetic

Write a CTE that calculates **total sales by region**.

Table:

```text
sales
```

---

### Exercise 2

Tags: CTEs, Arithmetic

Use a CTE to calculate **average salary by department**.

Table:

```text
employees
```

---

### Exercise 3

Tags: CTEs, Arithmetic

Create a CTE that calculates **total revenue by product**, then return products with revenue greater than **5000**.

---

### Exercise 4

Tags: CTEs, Arithmetic

Use two CTEs:

```text
CTE 1 → calculate total orders per customer
CTE 2 → filter customers with more than 5 orders
```

---

# Common Mistakes

### Forgetting the WITH Keyword

Incorrect:

```sql
sales_summary AS (
    SELECT region, SUM(revenue)
)
```

Correct:

```sql
WITH sales_summary AS (
    SELECT region, SUM(revenue)
)
```

---

### Missing Parentheses

CTEs must contain the query inside parentheses.

Incorrect:

```sql
WITH sales_summary AS
SELECT region, SUM(revenue)
FROM sales
```

Correct:

```sql
WITH sales_summary AS (
    SELECT region, SUM(revenue)
    FROM sales
)
```

---

### Overusing CTEs

CTEs improve readability but should not be used unnecessarily.

Sometimes a simple query is sufficient.

---

# Real-World Use

CTEs are widely used in analytics and data engineering.

Examples include:

```text
Revenue calculations
Customer segmentation
Provider performance analysis
Sales ranking
Fraud detection
```

Example healthcare analysis:

```sql
WITH provider_claims AS (
    SELECT provider_id, SUM(claim_amount) AS total_claims
    FROM claims
    GROUP BY provider_id
)
SELECT *
FROM provider_claims
WHERE total_claims > 500000;
```

This identifies providers with **high claim totals**.

---

# Lesson Recap

In this lesson you learned:

• what Common Table Expressions are  
• how CTEs simplify complex SQL queries  
• how CTEs compare to subqueries  
• how analysts structure multi-step SQL queries

CTEs allow analysts to write **clean, modular SQL queries**.

---

# Next Lesson

Next we will continue Module 13 with:

# Lesson 3 — Window Functions (PARTITION BY)

You will learn:

• how window functions work  
• how `PARTITION BY` divides data into groups  
• how analysts calculate metrics across rows  
• how window functions differ from `GROUP BY`.
