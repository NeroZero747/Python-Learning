# Module 13 — Advanced SQL for Data Analysis

# Lesson 1 — Subqueries

---

# Lesson Objective

By the end of this lesson learners will understand:

• what **subqueries** are in SQL  
• how to write **queries inside other queries**  
• how subqueries work in **WHERE, SELECT, and FROM clauses**  
• when analysts use subqueries in real-world data analysis  

Subqueries allow analysts to **build more complex logic inside SQL queries** by using the results of one query as input to another.

---

# Overview

In SQL, a **subquery** is a query nested inside another query.

Example:

```sql
SELECT name
FROM customers
WHERE customer_id IN (
    SELECT customer_id
    FROM orders
);
```

The inner query:

```sql
SELECT customer_id
FROM orders
```

runs first and returns a list of customer IDs.

The outer query then retrieves the **names of customers who placed orders**.

Subqueries allow SQL users to **break complex logic into smaller steps**.

---

# Key Idea Cards (3 Cards)

### Subqueries Are Queries Inside Queries

A subquery is simply a **query nested inside another SQL query**.

Example structure:

```text
Main Query
    ↓
Subquery
    ↓
Results returned to main query
```

---

### Subqueries Run First

SQL executes the **subquery first**, then uses the results in the outer query.

Example flow:

```text
Run subquery
Return results
Apply results to main query
```

---

### Subqueries Help Solve Complex Problems

Subqueries allow analysts to answer questions such as:

```text
Customers who placed orders
Products with above-average sales
Employees earning more than the department average
```

---

# Key Concepts

## Subqueries in the WHERE Clause

The most common use of subqueries is inside a **WHERE clause**.

Example:

```sql
SELECT name
FROM customers
WHERE customer_id IN (
    SELECT customer_id
    FROM orders
);
```

This retrieves customers who appear in the **orders table**.

Steps:

```text
Subquery returns customer IDs
Main query filters customers
```

---

## Subqueries Using Comparison Operators

Subqueries can be used with comparison operators.

Example:

```sql
SELECT name
FROM employees
WHERE salary > (
    SELECT AVG(salary)
    FROM employees
);
```

This retrieves employees who earn **more than the company average salary**.

---

## Subqueries in the FROM Clause

Subqueries can also act as **temporary tables**.

Example:

```sql
SELECT region, total_sales
FROM (
    SELECT region, SUM(sales) AS total_sales
    FROM sales
    GROUP BY region
) AS regional_sales;
```

The subquery creates a **temporary result set**.

---

## Subqueries in the SELECT Clause

Subqueries can appear inside SELECT statements.

Example:

```sql
SELECT
    name,
    (SELECT AVG(salary) FROM employees) AS avg_salary
FROM employees;
```

This adds the company average salary to each row.

---

# Decision Flow

When deciding whether to use a subquery:

```text
Do you need the result of another query?
        ↓
Use a subquery
```

Example scenario:

```text
Find employees earning above average salary
```

Steps:

```text
Calculate average salary
Filter employees above that value
```

---

# Code Examples

### Example 1 — Customers Who Placed Orders

```sql
SELECT name
FROM customers
WHERE customer_id IN (
    SELECT customer_id
    FROM orders
);
```

This identifies customers who placed orders.

---

### Example 2 — Products with Above Average Price

```sql
SELECT product_name
FROM products
WHERE price > (
    SELECT AVG(price)
    FROM products
);
```

This finds products priced above the average.

---

### Example 3 — Regions with High Sales

```sql
SELECT region
FROM sales
GROUP BY region
HAVING SUM(revenue) > (
    SELECT AVG(revenue)
    FROM sales
);
```

This identifies regions performing above average.

---

### Example 4 — Subquery in FROM

```sql
SELECT *
FROM (
    SELECT department, AVG(salary) AS avg_salary
    FROM employees
    GROUP BY department
) AS dept_salary;
```

This creates a **temporary summary table**.

---

# SQL / Excel / Python Comparison

Subqueries behave similarly to nested logic in other tools.

| Concept | SQL | Python | Excel |
|---|---|---|---|
| nested logic | subquery | nested function | nested formula |
| intermediate results | subquery result | variable | helper column |

Example Python equivalent:

```python
avg_salary = df["salary"].mean()

df[df["salary"] > avg_salary]
```

Equivalent SQL:

```sql
SELECT *
FROM employees
WHERE salary > (
    SELECT AVG(salary)
    FROM employees
);
```

---

# Practice Exercises

### Exercise 1

Tags: Subqueries, SQL

Find customers who placed orders.

Tables:

```text
customers
orders
```

---

### Exercise 2

Tags: Subqueries, SQL

Find employees earning more than the average salary.

Table:

```text
employees
```

---

### Exercise 3

Tags: Subqueries, SQL

Find products priced above the average product price.

Table:

```text
products
```

---

### Exercise 4

Tags: WHERE, Subqueries, SQL Queries

Write a query that returns departments where the average salary exceeds the company average.

---

# Common Mistakes

### Forgetting Parentheses

Incorrect:

```sql
WHERE salary > SELECT AVG(salary)
```

Correct:

```sql
WHERE salary > (
    SELECT AVG(salary)
)
```

---

### Returning Multiple Values with Single Comparison

Incorrect:

```sql
WHERE salary > (
    SELECT salary
    FROM employees
)
```

This may return multiple rows.

Use:

```text
IN
ANY
ALL
```

when necessary.

---

### Using Subqueries When Joins Are Better

Sometimes joins are more efficient.

Example:

```sql
JOIN customers
ON orders.customer_id = customers.customer_id
```

Understanding when to use **joins vs subqueries** is important.

---

# Real-World Use

Subqueries are commonly used in analytics.

Examples:

```text
Customers with recent purchases
Employees earning above department average
Providers with high claim totals
Products above average revenue
```

Example healthcare query:

```sql
SELECT provider_id
FROM claims
GROUP BY provider_id
HAVING SUM(claim_amount) > (
    SELECT AVG(claim_amount)
    FROM claims
);
```

This identifies providers with **above-average claim totals**.

---

# Lesson Recap

In this lesson you learned:

• what subqueries are  
• how queries can be nested inside other queries  
• how subqueries work in WHERE, SELECT, and FROM clauses  
• when analysts use subqueries in real-world analysis  

Subqueries allow SQL users to **build complex logic by combining multiple queries**.

---

# Next Lesson

Next we will continue Module 13 with:

# Lesson 2 — Common Table Expressions (CTEs)

You will learn:

• how CTEs simplify complex queries  
• how to write step-by-step SQL queries  
• why analysts prefer CTEs over nested subqueries  
• how CTEs improve readability and debugging.
