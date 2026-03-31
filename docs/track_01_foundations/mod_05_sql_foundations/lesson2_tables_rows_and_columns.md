# Module 12 — SQL Foundations

# Lesson 2 — Tables, Rows, and Columns

---

# Lesson Objective

By the end of this lesson learners will understand:

• how **database tables are structured**  
• the difference between **rows and columns**  
• how **primary keys uniquely identify records**  
• how table structure relates to **Excel and Python DataFrames**

Understanding table structure is critical because **all SQL queries operate on tables**.

---

# Overview

A **database table** stores structured data in a format similar to a spreadsheet.

Example table:

| customer_id | name | city | age |
|---|---|---|---|
| 101 | Maria | Los Angeles | 32 |
| 102 | James | Chicago | 41 |
| 103 | Sarah | New York | 28 |

This table contains:

```text
Columns → attributes of the data
Rows → individual records
```

Each **row represents one entity**.

Example:

```text
Row → one customer
```

Each **column represents a field describing that entity**.

Example:

```text
Column → customer name
Column → city
Column → age
```

Tables are the fundamental building block of relational databases.

---

# Key Idea Cards (3 Cards)

### Tables Store Structured Data

Tables organize information into rows and columns.

Example structure:

```text
Table
 ├── Rows → records
 └── Columns → attributes
```

This structure allows databases to store large datasets efficiently.

---

### Rows Represent Records

Each row represents a single item in the dataset.

Example:

| customer_id | name |
|---|---|
| 101 | Maria |

This row represents one customer.

---

### Columns Represent Attributes

Columns describe characteristics of the data.

Example columns:

```text
customer_id
name
city
age
```

Each column stores a specific type of information.

---

# Key Concepts

## Columns

A **column** represents a specific attribute of the data.

Example table:

| product_id | product_name | price |
|---|---|---|
| 1 | Laptop | 1200 |

Column meanings:

```text
product_id → unique identifier
product_name → product description
price → cost of the product
```

Each column typically has a **data type**.

Examples:

```text
integer
text
date
decimal
```

---

## Rows

A **row** represents one complete record in the table.

Example:

| product_id | product_name | price |
|---|---|---|
| 1 | Laptop | 1200 |

This row represents one product.

Large tables may contain:

```text
Thousands of rows
Millions of rows
Billions of rows
```

---

## Primary Key

A **primary key** uniquely identifies each row in a table.

Example:

| customer_id | name |
|---|---|
| 101 | Maria |
| 102 | James |

`customer_id` is the primary key.

Primary keys ensure that:

```text
Each record is unique
No duplicate identifiers exist
```

Primary keys are important when **joining tables together**.

---

# Decision Flow

When designing or analyzing a database table:

```text
What entities are stored?
        ↓
Define rows (records)
        ↓
Define columns (attributes)
        ↓
Choose a primary key
```

This ensures tables remain organized and relational.

---

# Code Examples

### Example 1 — Viewing All Data

```sql
SELECT *
FROM customers;
```

This retrieves every row and column in the table.

---

### Example 2 — Selecting Specific Columns

```sql
SELECT name, city
FROM customers;
```

This returns only the `name` and `city` columns.

---

### Example 3 — Example Orders Table

| order_id | customer_id | amount |
|---|---|---|
| 1 | 101 | 50 |
| 2 | 102 | 75 |

Query:

```sql
SELECT order_id, amount
FROM orders;
```

---

### Example 4 — Product Table

| product_id | product_name | price |
|---|---|---|
| 1 | Laptop | 1200 |
| 2 | Phone | 800 |

Query:

```sql
SELECT product_name, price
FROM products;
```

---

# SQL / Excel Comparison

Tables behave similarly to spreadsheets.

| SQL | Excel | Python |
|---|---|---|
| Table | Worksheet | DataFrame |
| Row | Row | Row |
| Column | Column | Column |
| Primary Key | Unique ID column | Index |

Example Excel table:

| ID | Name | City |
|---|---|---|
| 101 | Maria | LA |

Equivalent SQL table:

```text
customers
```

SQL simply stores this data in a **database system instead of a spreadsheet file**.

---

# Practice Exercises

### Exercise 1

Tags: Missing Data, SQL

Look at the following table:

| employee_id | name | department |
|---|---|---|
| 1 | Alex | Finance |
| 2 | Priya | HR |

Identify:

```text
Rows
Columns
Primary key
```

---

### Exercise 2

Tags: SELECT, SQL Queries

Write a SQL query that returns all columns from the `employees` table.

---

### Exercise 3

Tags: SQL Queries, SQL

Write a query that returns only the `name` column.

---

### Exercise 4

Tags: SQL, Queries

Imagine a **products table**.

What columns might it include?

Example ideas:

```text
product_id
product_name
price
category
```

---

# Common Mistakes

### Confusing Rows and Columns

Rows represent **records**, not attributes.

Columns represent **attributes of the data**.

---

### Missing Primary Keys

Tables should usually have a primary key.

Without one:

```text
Duplicate rows may exist
Joins become difficult
```

---

### Too Many Columns

Tables should only contain relevant fields.

Excess columns can make tables difficult to manage.

---

# Real-World Use

Tables are used to store nearly every type of structured data.

Examples include:

```text
Customer records
Healthcare claims
Sales transactions
Inventory data
Website activity
```

Example database structure:

```text
Database
 ├── customers
 ├── orders
 ├── products
 └── payments
```

Each table stores a specific type of data.

Analysts use SQL queries to **retrieve and analyze information from these tables**.

---

# Lesson Recap

In this lesson you learned:

• how database tables are structured  
• the difference between rows and columns  
• how primary keys uniquely identify records  
• how tables compare to Excel sheets and Python DataFrames.

Understanding table structure is the foundation of working with SQL.

---

# Next Lesson

Next we will continue Module 12 with:

# Lesson 3 — The SELECT Statement

You will learn:

• how SQL retrieves data from tables  
• how to select specific columns  
• how to rename columns using aliases  
• how to structure basic SQL queries.
