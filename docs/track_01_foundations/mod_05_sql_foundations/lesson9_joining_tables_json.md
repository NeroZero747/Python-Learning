# Module 12 — SQL Foundations

# Lesson 9 — Joining Tables (JOIN)

---

# Lesson Objective

By the end of this lesson learners will understand:

• why **relational databases store data across multiple tables**  
• how SQL **joins tables together**  
• how tables connect using **keys**  
• the most common join types used in analysis  

Joining tables is one of the most powerful capabilities in SQL because it allows analysts to **combine related datasets to answer complex questions**.

---

# Overview

In relational databases, data is often stored across **multiple tables** rather than one large table.

Example tables:

### Customers Table

| customer_id | name |
|---|---|
| 101 | Maria |
| 102 | James |
| 103 | Sarah |

### Orders Table

| order_id | customer_id | amount |
|---|---|---|
| 1 | 101 | 50 |
| 2 | 102 | 75 |
| 3 | 101 | 25 |

The **Orders table does not contain customer names**.

Instead it stores:

```text
customer_id
```

This value links to the Customers table.

To combine the two tables, we use a **JOIN**.

Example:

```sql
SELECT customers.name, orders.amount
FROM orders
JOIN customers
ON orders.customer_id = customers.customer_id;
```

Result:

| name | amount |
|---|---|
| Maria | 50 |
| James | 75 |
| Maria | 25 |

This query combines the two tables.

---

# Key Idea Cards (3 Cards)

### Relational Databases Use Multiple Tables

Databases separate data into related tables.

Example:

```text
customers
orders
products
payments
```

Tables connect using shared keys.

---

### Keys Connect Tables

A **key column** links tables together.

Example:

```text
customers.customer_id
orders.customer_id
```

This allows SQL to match related rows.

---

### JOIN Combines Data From Multiple Tables

JOIN retrieves related data across tables.

Example:

```sql
SELECT customers.name, orders.amount
FROM orders
JOIN customers
ON orders.customer_id = customers.customer_id;
```

This combines customer and order data.

---

# Key Concepts

## Primary Key

A **primary key** uniquely identifies each row in a table.

Example:

| customer_id | name |
|---|---|
| 101 | Maria |
| 102 | James |

Here:

```text
customer_id
```

is the primary key.

---

## Foreign Key

A **foreign key** references the primary key of another table.

Example:

Orders table:

| order_id | customer_id |
|---|---|
| 1 | 101 |

Here:

```text
customer_id
```

is a foreign key referencing the Customers table.

---

## INNER JOIN

The most common join type is **INNER JOIN**.

It returns rows where matching values exist in both tables.

Example:

```sql
SELECT customers.name, orders.amount
FROM orders
INNER JOIN customers
ON orders.customer_id = customers.customer_id;
```

This returns only matching records.

---

## Types of SQL Joins

SQL provides several different join types.  
Each join controls **which rows appear in the final result**.

The most common joins are:

```text
INNER JOIN
LEFT JOIN
RIGHT JOIN
FULL JOIN
```

Understanding these joins is important when combining datasets.

---

## INNER JOIN Detailed Example

An **INNER JOIN** returns only rows that have matching values in both tables.

### Customers

| customer_id | name |
|---|---|
| 101 | Maria |
| 102 | James |
| 103 | Sarah |

### Orders

| order_id | customer_id | amount |
|---|---|---|
| 1 | 101 | 50 |
| 2 | 102 | 75 |
| 3 | 101 | 25 |
| 4 | 104 | 60 |

Notice that **customer 104 does not exist in the customers table**.

Query:

```sql
SELECT customers.name, orders.amount
FROM orders
INNER JOIN customers
ON orders.customer_id = customers.customer_id;
```

Result:

| name | amount |
|---|---|
| Maria | 50 |
| James | 75 |
| Maria | 25 |

The order with `customer_id = 104` does **not appear** because it has no match in the customers table.

Key idea:

```text
INNER JOIN = only matching rows
```

---

## LEFT JOIN

A **LEFT JOIN** returns:

```text
All rows from the left table
+
Matching rows from the right table
```

If no match exists, SQL returns **NULL** values.

Query:

```sql
SELECT customers.name, orders.amount
FROM customers
LEFT JOIN orders
ON customers.customer_id = orders.customer_id;
```

Result:

| name | amount |
|---|---|
| Maria | 50 |
| Maria | 25 |
| James | 75 |
| Sarah | NULL |

Sarah appears even though she has **no orders**.

Key idea:

```text
LEFT JOIN = keep everything from the left table
```

This join is extremely common in analytics.

Example use cases:

```text
Customers without orders
Providers without claims
Products without sales
```

---

## RIGHT JOIN

A **RIGHT JOIN** returns:

```text
All rows from the right table
+
Matching rows from the left table
```

Query:

```sql
SELECT customers.name, orders.amount
FROM customers
RIGHT JOIN orders
ON customers.customer_id = orders.customer_id;
```

Result:

| name | amount |
|---|---|
| Maria | 50 |
| James | 75 |
| Maria | 25 |
| NULL | 60 |

The order with `customer_id = 104` appears even though the customer does not exist.

Key idea:

```text
RIGHT JOIN = keep everything from the right table
```

However, analysts often prefer **LEFT JOIN** because it reads more clearly.

---

## FULL JOIN

A **FULL JOIN** returns:

```text
All rows from both tables
```

If a row does not have a match, SQL fills the missing values with **NULL**.

Query:

```sql
SELECT customers.name, orders.amount
FROM customers
FULL JOIN orders
ON customers.customer_id = orders.customer_id;
```

Result:

| name | amount |
|---|---|
| Maria | 50 |
| Maria | 25 |
| James | 75 |
| Sarah | NULL |
| NULL | 60 |

This shows:

```text
Customers without orders
Orders without customers
```

---

## Join Type Summary

| Join Type | What It Returns |
|---|---|
| INNER JOIN | Only matching rows |
| LEFT JOIN | All rows from left table |
| RIGHT JOIN | All rows from right table |
| FULL JOIN | All rows from both tables |

---

# Decision Flow

When combining tables:

```text
Need data from multiple tables?
        ↓
Identify shared key column
        ↓
Use JOIN
        ↓
Define matching condition with ON
```

Example workflow:

```text
Orders table contains customer_id
Customers table contains name
       ↓
JOIN tables on customer_id
```

---

# Code Examples

### Example 1 — Basic INNER JOIN

```sql
SELECT customers.name, orders.amount
FROM orders
JOIN customers
ON orders.customer_id = customers.customer_id;
```

This returns order amounts with customer names.

---

### Example 2 — Join Products and Sales

Products table:

| product_id | product_name |
|---|---|
| 1 | Laptop |
| 2 | Phone |

Sales table:

| product_id | quantity |
|---|---|
| 1 | 5 |
| 2 | 3 |

Query:

```sql
SELECT products.product_name, sales.quantity
FROM sales
JOIN products
ON sales.product_id = products.product_id;
```

---

### Example 3 — Join With Multiple Columns

```sql
SELECT customers.name, orders.order_id, orders.amount
FROM orders
JOIN customers
ON orders.customer_id = customers.customer_id;
```

This retrieves multiple fields across both tables.

---

### Example 4 — Joining Three Tables

```sql
SELECT customers.name, products.product_name
FROM orders
JOIN customers
ON orders.customer_id = customers.customer_id
JOIN products
ON orders.product_id = products.product_id;
```

This combines three tables.

---

# SQL / Excel Comparison

Joins are similar to lookup operations in Excel.

| SQL | Excel | Python |
|---|---|---|
| JOIN | VLOOKUP / XLOOKUP | merge() |
| Key column | Lookup value | join key |
| Related tables | Lookup table | DataFrames |

Example Excel lookup:

```text
VLOOKUP(customer_id, customer_table, 2)
```

Equivalent SQL:

```sql
SELECT customers.name
FROM orders
JOIN customers
ON orders.customer_id = customers.customer_id;
```

Equivalent Python:

```python
orders.merge(customers, on="customer_id")
```

---

# Practice Exercises

### Exercise 1

Tags: JOIN, SQL

Join the `orders` table with the `customers` table using `customer_id`.

---

### Exercise 2

Tags: JOIN, SQL

Join the `sales` table with the `products` table using `product_id`.

---

### Exercise 3

Tags: JOIN, SQL

Return customer names and order amounts.

Tables:

```text
customers
orders
```

---

### Exercise 4

Tags: JOIN, SQL

Join three tables:

```text
orders
customers
products
```

---

# Common Mistakes

### Missing Join Condition

Incorrect:

```sql
SELECT *
FROM orders
JOIN customers;
```

Correct:

```sql
SELECT *
FROM orders
JOIN customers
ON orders.customer_id = customers.customer_id;
```

The ON clause defines how rows match.

---

### Joining Incorrect Columns

Ensure the columns represent the same relationship.

Incorrect:

```sql
ON orders.order_id = customers.customer_id
```

Correct:

```sql
ON orders.customer_id = customers.customer_id
```

---

### Duplicate Rows From Joins

Joins may produce multiple rows if a relationship is one-to-many.

Example:

```text
One customer → multiple orders
```

This is expected behavior.

---

# Real-World Use

Joining tables is essential in analytics workflows.

Examples:

```text
Orders + Customers
Sales + Products
Claims + Providers
Transactions + Accounts
```

Example business query:

```sql
SELECT providers.name, SUM(claims.amount)
FROM claims
JOIN providers
ON claims.provider_id = providers.provider_id
GROUP BY providers.name;
```

This calculates total claims by provider.

Joins allow analysts to **combine multiple datasets into meaningful insights**.

---

# Lesson Recap

In this lesson you learned:

• why relational databases store data across multiple tables  
• how primary and foreign keys connect tables  
• how SQL JOIN combines datasets  
• how different join types affect results

Joining tables allows SQL users to **analyze relationships across datasets**.

---

# Next Lesson

Next we will complete Module 12 with:

# Lesson 10 — SQL vs Python for Data Analysis

You will learn:

• how SQL compares with Python data analysis  
• when to use SQL vs Python  
• how analysts combine SQL and Python workflows  
• how SQL integrates into modern data pipelines.
