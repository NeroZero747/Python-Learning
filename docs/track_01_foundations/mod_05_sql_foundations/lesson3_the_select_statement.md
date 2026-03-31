# Module 12 — SQL Foundations

# Lesson 3 — The SELECT Statement

---

# Lesson Objective

By the end of this lesson learners will understand:

• how the **SELECT statement retrieves data** from tables  
• how to **select specific columns**  
• how to retrieve **all columns using \***  
• how to **rename columns using aliases**

The `SELECT` statement is the most fundamental command in SQL because it allows you to **retrieve data stored in database tables**.

---

# Overview

In SQL, the most common task is retrieving data from a table.

This is done using the **SELECT statement**.

Basic structure:

```sql
SELECT column_name
FROM table_name;
```

Example table:

| customer_id | name | city |
|---|---|---|
| 101 | Maria | Los Angeles |
| 102 | James | Chicago |
| 103 | Sarah | New York |

Query:

```sql
SELECT name
FROM customers;
```

Result:

| name |
|---|
| Maria |
| James |
| Sarah |

The query tells the database:

```text
Retrieve the "name" column
from the "customers" table
```

The SELECT statement is used in almost **every SQL query**.

---

# Key Idea Cards (3 Cards)

### SELECT Retrieves Data

The SELECT statement retrieves data from database tables.

Example:

```sql
SELECT name
FROM customers;
```

This returns the `name` column from the table.

---

### FROM Specifies the Table

SQL must know which table to retrieve data from.

Example:

```sql
SELECT name
FROM customers;
```

`customers` is the table being queried.

---

### SELECT Can Retrieve Multiple Columns

You can retrieve several columns in one query.

Example:

```sql
SELECT name, city
FROM customers;
```

This returns both columns.

---

# Key Concepts

## SELECT *

The `*` symbol means **all columns**.

Example:

```sql
SELECT *
FROM customers;
```

Result:

| customer_id | name | city |
|---|---|---|
| 101 | Maria | Los Angeles |
| 102 | James | Chicago |
| 103 | Sarah | New York |

This retrieves the entire table.

---

## Selecting Specific Columns

Instead of retrieving everything, you can choose specific columns.

Example:

```sql
SELECT name, city
FROM customers;
```

Result:

| name | city |
|---|---|
| Maria | Los Angeles |
| James | Chicago |
| Sarah | New York |

Selecting specific columns improves query efficiency.

---

## Column Aliases

Aliases allow you to rename columns in the result.

Example:

```sql
SELECT name AS customer_name
FROM customers;
```

Result:

| customer_name |
|---|
| Maria |
| James |
| Sarah |

Aliases improve readability.

---

# Decision Flow

When writing a SQL query:

```text
What data do you need?
       ↓
Select columns
       ↓
Identify table
       ↓
Write SELECT statement
```

Example workflow:

```text
Need customer names
       ↓
SELECT name
FROM customers
```

---

# Code Examples

### Example 1 — Selecting One Column

```sql
SELECT name
FROM customers;
```

Result:

| name |
|---|
| Maria |
| James |
| Sarah |

---

### Example 2 — Selecting Multiple Columns

```sql
SELECT name, city
FROM customers;
```

Result:

| name | city |
|---|---|
| Maria | Los Angeles |
| James | Chicago |

---

### Example 3 — Selecting All Columns

```sql
SELECT *
FROM customers;
```

This returns the entire table.

---

### Example 4 — Using Column Aliases

```sql
SELECT name AS customer_name
FROM customers;
```

Output column will appear as:

```text
customer_name
```

---

# SQL / Excel Comparison

SQL SELECT behaves similarly to selecting columns in Excel.

| SQL | Excel | Python |
|---|---|---|
| SELECT column | choose column | df["column"] |
| SELECT * | entire sheet | df |
| alias | rename header | df.rename() |

Example Excel operation:

```text
Selecting columns A and B
```

Equivalent SQL:

```sql
SELECT name, city
FROM customers;
```

Equivalent Python:

```python
df[["name", "city"]]
```

---

# Practice Exercises

### Exercise 1

Tags: SELECT, SQL Queries

Write a query that retrieves all columns from the `employees` table.

---

### Exercise 2

Tags: SELECT, SQL Queries

Write a query that returns only the `name` column from the `customers` table.

---

### Exercise 3

Tags: SELECT, SQL Queries

Write a query that retrieves the `product_name` and `price` columns from the `products` table.

---

### Exercise 4

Tags: SELECT, SQL

Rename the column `name` as `customer_name`.

Example table:

```text
customers
```

---

# Common Mistakes

### Forgetting the FROM Clause

Incorrect:

```sql
SELECT name;
```

Correct:

```sql
SELECT name
FROM customers;
```

---

### Selecting Too Many Columns

Using `SELECT *` retrieves all columns, which may include unnecessary data.

Better approach:

```sql
SELECT name, city
FROM customers;
```

---

### Incorrect Table Names

SQL queries must reference the correct table.

Incorrect:

```sql
SELECT name
FROM customer;
```

Correct:

```sql
SELECT name
FROM customers;
```

---

# Real-World Use

The SELECT statement is used constantly in data analysis.

Example use cases:

```text
Retrieve sales data
View customer records
Analyze website traffic
Generate reports
```

Example analyst workflow:

```text
Database stores data
       ↓
Analyst writes SELECT query
       ↓
Query returns dataset
       ↓
Data used for analysis
```

Nearly every SQL query begins with **SELECT**.

---

# Lesson Recap

In this lesson you learned:

• how the SELECT statement retrieves data  
• how to select specific columns  
• how to retrieve all columns using `*`  
• how to rename columns using aliases

The SELECT statement is the **foundation of all SQL queries**.

---

# Next Lesson

Next we will continue Module 12 with:

# Lesson 4 — Filtering Data with WHERE

You will learn:

• how to filter rows in a SQL query  
• comparison operators  
• AND / OR logic  
• how analysts isolate specific records.
