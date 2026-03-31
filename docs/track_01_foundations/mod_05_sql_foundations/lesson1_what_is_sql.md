# Module 12 — SQL Foundations

# Lesson 1 — What is SQL?

---

# Lesson Objective

By the end of this lesson learners will understand:

• what **SQL** stands for  
• why databases are used to store data  
• what **tables, rows, and columns** represent  
• how SQL compares to **Excel and Python**

SQL is one of the most important skills for anyone working with data because it allows you to **retrieve, filter, and analyze data stored in databases**.

---

# Overview

Many organizations store their data inside **databases** rather than spreadsheets.

Examples include:

```text
Customer data
Sales transactions
Healthcare claims
Product inventory
Website activity
```

These datasets can contain **millions or even billions of rows**, which makes spreadsheets impractical.

Databases solve this problem by storing data in **tables**.

Example table:

| customer_id | name | city |
|---|---|---|
| 101 | Maria | Los Angeles |
| 102 | James | Chicago |
| 103 | Sarah | New York |

Each table consists of:

```text
Columns → data attributes
Rows → records
```

To work with data in a database, we use **SQL**.

SQL stands for:

```text
Structured Query Language
```

SQL allows users to **query** data stored in tables.

Example SQL query:

```sql
SELECT *
FROM customers;
```

This query retrieves all records from the `customers` table.

---

# Key Idea Cards (3 Cards)

### SQL Is Used to Query Databases

SQL allows users to retrieve data stored inside database tables.

Example:

```sql
SELECT *
FROM customers;
```

This retrieves all rows and columns from a table.

---

### Databases Store Structured Data

Databases organize information into tables.

Example structure:

```text
Table
 ├── Rows (records)
 └── Columns (fields)
```

This structure allows databases to store large datasets efficiently.

---

### SQL Is One of the Most Important Data Skills

SQL is widely used in:

```text
Data analytics
Data engineering
Business intelligence
Software development
```

Almost every data platform supports SQL.

---

# Key Concepts

## Database

A **database** is a system that stores structured data.

Examples of database systems:

```text
PostgreSQL
MySQL
SQL Server
Oracle
Snowflake
BigQuery
```

Databases allow organizations to store and retrieve large datasets efficiently.

---

## Table

A **table** is a structured dataset stored in a database.

Example:

| order_id | customer_id | amount |
|---|---|---|
| 1 | 101 | 50 |
| 2 | 102 | 75 |

Each row represents a record.

Each column represents a field.

---

## Query

A **query** is a command used to retrieve or manipulate data.

Example:

```sql
SELECT name
FROM customers;
```

This retrieves the `name` column from the customers table.

---

# Decision Flow

When working with SQL, analysts typically follow this process:

```text
Need data?
     ↓
Write SQL query
     ↓
Database executes query
     ↓
Results returned
```

SQL acts as the **language used to communicate with the database**.

---

# Code Examples

### Example 1 — Selecting All Data

```sql
SELECT *
FROM customers;
```

`*` means **all columns**.

---

### Example 2 — Selecting Specific Columns

```sql
SELECT name, city
FROM customers;
```

This returns only the `name` and `city` columns.

---

### Example 3 — Viewing a Sales Table

Example table:

| order_id | product | price |
|---|---|---|
| 1 | Laptop | 1200 |
| 2 | Phone | 800 |

Query:

```sql
SELECT product, price
FROM sales;
```

---

### Example 4 — Simple Data Retrieval

```sql
SELECT customer_id
FROM customers;
```

This retrieves only the `customer_id` column.

---

# SQL / Excel Comparison

SQL concepts often resemble Excel concepts.

| SQL | Excel |
|---|---|
| Table | Worksheet |
| Row | Row |
| Column | Column |
| Query | Filter or formula |

Example Excel filter:

```text
Filter City = Los Angeles
```

Equivalent SQL query:

```sql
SELECT *
FROM customers
WHERE city = 'Los Angeles';
```

---

# Practice Exercises

### Exercise 1

Tags: SELECT, SQL Queries

Write a SQL query that retrieves all data from the table `employees`.

---

### Exercise 2

Tags: SELECT, SQL Queries

Write a query that returns only the `name` column from the `customers` table.

---

### Exercise 3

Tags: SELECT, SQL Queries

Write a query that returns the `product` and `price` columns from a table called `sales`.

---

### Exercise 4

Tags: SQL, Queries

Think about datasets your organization uses.

Examples might include:

```text
Customer records
Claims data
Product catalogs
```

Consider what information might be stored in a table.

---

# Common Mistakes

### Confusing Tables and Databases

A **database** can contain many tables.

Example:

```text
Database
 ├── customers
 ├── orders
 └── products
```

---

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

SQL needs to know **which table to query**.

---

### Using Incorrect Column Names

Column names must match the table structure exactly.

Example:

Incorrect:

```sql
SELECT customer
FROM customers;
```

Correct:

```sql
SELECT name
FROM customers;
```

---

# Real-World Use

SQL is used every day in data-driven organizations.

Example workflow:

```text
Data stored in database
        ↓
Analyst writes SQL query
        ↓
Query retrieves dataset
        ↓
Data used for analysis or reporting
```

Examples of SQL usage include:

```text
Business dashboards
Data pipelines
Financial reporting
Healthcare analytics
Machine learning datasets
```

SQL is one of the **core tools used by data professionals**.

---

# Lesson Recap

In this lesson you learned:

• what SQL stands for  
• how databases store structured data  
• what tables, rows, and columns represent  
• how SQL queries retrieve data from databases

SQL is the primary language used to **access and analyze data stored in databases**.

---

# Next Lesson

Next we will continue Module 12 with:

# Lesson 2 — Tables, Rows, and Columns

You will learn:

• how database tables are structured  
• how rows represent records  
• how columns represent attributes  
• how primary keys uniquely identify records.
