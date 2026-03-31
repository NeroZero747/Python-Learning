# Module 13 — Advanced SQL for Data Analysis

# Lesson 6 — Advanced Joins

---

# Lesson Objective

By the end of this lesson learners will understand:

• how **advanced joins** work in SQL  
• how to perform **self joins**  
• how to join **multiple tables together**  
• how analysts combine **aggregated data with detail data**

Joins are one of the most important SQL concepts because real-world datasets are often **spread across multiple tables**.

---

# Overview

In SQL Foundations you learned the most common joins:

```text
INNER JOIN
LEFT JOIN
RIGHT JOIN
FULL JOIN
```

Example:

```sql
SELECT
    customers.name,
    orders.order_id
FROM customers
JOIN orders
ON customers.customer_id = orders.customer_id;
```

However, analysts frequently need more advanced join patterns such as:

```text
Self joins
Joining aggregated tables
Joining multiple datasets
Combining summary and detail data
```

These techniques allow analysts to **build more complex relationships between datasets**.

---

# Key Idea Cards (3 Cards)

### Joins Combine Data from Multiple Tables

A join connects rows between tables using a shared column.

Example:

```sql
customers.customer_id = orders.customer_id
```

This relationship allows SQL to merge the two datasets.

---

### Self Joins Connect a Table to Itself

A self join occurs when a table joins to itself.

Example:

```sql
employees → managers
```

Both records exist in the **same table**.

---

### Joins Are Essential for Analytics

Most analytics queries require combining data from multiple tables.

Examples:

```text
Orders + Customers
Claims + Providers
Sales + Products
Employees + Departments
```

---

# Key Concepts

## Self Joins

A self join occurs when a table joins to itself.

Example dataset:

| employee_id | employee | manager_id |
|---|---|---|
| 1 | Alice | 3 |
| 2 | Bob | 3 |
| 3 | Maria | NULL |

We can find employee managers with a self join.

```sql
SELECT
    e.employee AS employee_name,
    m.employee AS manager_name
FROM employees e
JOIN employees m
ON e.manager_id = m.employee_id;
```

Result:

| employee_name | manager_name |
|---|---|
| Alice | Maria |
| Bob | Maria |

---

## Joining Aggregated Data

Sometimes analysts need to join **summary data with detail records**.

Example:

```sql
SELECT
    employees.name,
    employees.salary,
    dept_avg.avg_salary
FROM employees
JOIN (
    SELECT department, AVG(salary) AS avg_salary
    FROM employees
    GROUP BY department
) dept_avg
ON employees.department = dept_avg.department;
```

This joins employee records with department averages.

---

## Joining Multiple Tables

Real-world datasets often require joining several tables.

Example:

```sql
SELECT
    orders.order_id,
    customers.name,
    products.product_name
FROM orders
JOIN customers
ON orders.customer_id = customers.customer_id
JOIN products
ON orders.product_id = products.product_id;
```

This connects three datasets:

```text
Orders
Customers
Products
```

---

# Decision Flow

When combining datasets:

```text
Need to combine rows from two tables?
        ↓
Use JOIN
```

If the relationship exists within the same table:

```text
Use SELF JOIN
```

If joining summary data:

```text
Use aggregated subquery or CTE
```

---

# Code Examples

### Example 1 — Customer Orders

```sql
SELECT
    customers.name,
    orders.order_date
FROM customers
JOIN orders
ON customers.customer_id = orders.customer_id;
```

This shows which customers placed orders.

---

### Example 2 — Employee Manager Relationship

```sql
SELECT
    e.employee,
    m.employee AS manager
FROM employees e
JOIN employees m
ON e.manager_id = m.employee_id;
```

This identifies each employee’s manager.

---

### Example 3 — Sales with Product Information

```sql
SELECT
    sales.sale_id,
    products.product_name,
    sales.revenue
FROM sales
JOIN products
ON sales.product_id = products.product_id;
```

This connects product names with sales data.

---

### Example 4 — Joining Aggregated Results

```sql
SELECT
    employees.name,
    employees.salary,
    dept_summary.avg_salary
FROM employees
JOIN (
    SELECT department, AVG(salary) AS avg_salary
    FROM employees
    GROUP BY department
) dept_summary
ON employees.department = dept_summary.department;
```

This compares employee salary with department average.

---

### Example 5 — Healthcare Claims Example

```sql
SELECT
    claims.claim_id,
    providers.provider_name,
    claims.claim_amount
FROM claims
JOIN providers
ON claims.provider_id = providers.provider_id;
```

This links healthcare claims to provider information.

---

# SQL / Excel / Python Comparison

Joining data is similar across many tools.

| SQL | Python | Excel |
|---|---|---|
| JOIN | merge() | VLOOKUP / XLOOKUP |
| ON clause | key column | lookup column |

Python equivalent:

```python
df = orders.merge(customers, on="customer_id")
```

Excel equivalent:

```text
XLOOKUP(customer_id, customers_table, name_column)
```

---

# Practice Exercises

### Exercise 1

Tags: JOIN, SQL

Join **customers** with **orders** to show customer names and order IDs.

Tables:

```text
customers
orders
```

---

### Exercise 2

Tags: JOIN, SQL

Create a self join that shows employees and their managers.

Table:

```text
employees
```

---

### Exercise 3

Tags: JOIN, SQL

Join **sales** with **products** to show product names.

Tables:

```text
sales
products
```

---

### Exercise 4

Tags: JOIN, SQL

Join employee records with department averages.

Table:

```text
employees
```

---

# Common Mistakes

### Forgetting the Join Condition

Incorrect:

```sql
SELECT *
FROM customers
JOIN orders;
```

This produces a **Cartesian product**.

Correct:

```sql
JOIN orders
ON customers.customer_id = orders.customer_id
```

---

### Using the Wrong Join Type

Using `INNER JOIN` removes unmatched rows.

If all records are needed:

```sql
LEFT JOIN
```

---

### Confusing Self Join Aliases

Self joins require aliases.

Example:

```sql
employees e
employees m
```

Aliases help distinguish each table reference.

---

# Real-World Use

Joins are used in almost every analytics workflow.

Examples include:

```text
Customer purchase analysis
Sales reporting
Healthcare claims analysis
Provider performance tracking
```

Healthcare example:

```sql
SELECT
    providers.provider_name,
    SUM(claims.claim_amount) AS total_claims
FROM claims
JOIN providers
ON claims.provider_id = providers.provider_id
GROUP BY providers.provider_name;
```

This calculates total claims by provider.

Joins allow analysts to **combine multiple datasets into meaningful insights**.

---

# Lesson Recap

In this lesson you learned:

• how advanced joins combine multiple tables  
• how self joins work  
• how to join aggregated datasets  
• how analysts combine data from multiple sources

Joins are essential for **building complex analytical queries**.

---

# Next Lesson

Next we will continue Module 13 with:

# Lesson 7 — CASE Statements

You will learn:

• how SQL performs **conditional logic**  
• how the **CASE statement works**  
• how analysts categorize data  
• how SQL conditions compare to **Python if statements**.
