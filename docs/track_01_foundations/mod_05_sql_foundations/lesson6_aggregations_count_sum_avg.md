# Module 12 — SQL Foundations

# Lesson 6 — Aggregations (COUNT, SUM, AVG)

---

# Lesson Objective

By the end of this lesson learners will understand:

• how SQL **summarizes data using aggregation functions**  
• how the functions **COUNT, SUM, and AVG** work  
• how analysts calculate totals, averages, and record counts  
• how aggregation helps transform raw data into **summary insights**

Aggregation is essential because analysts rarely analyze **individual rows**; they typically analyze **summaries of data**.

---

# Overview

In real-world datasets, tables may contain **thousands or millions of rows**.

Example table:

| order_id | product | revenue |
|---|---|---|
| 1 | Laptop | 1200 |
| 2 | Phone | 800 |
| 3 | Laptop | 1200 |
| 4 | Tablet | 600 |

If we retrieve the data:

```sql
SELECT *
FROM sales;
```

We see individual records.

However, analysts often want to answer questions such as:

```text
How many orders exist?
What is the total revenue?
What is the average order value?
```

SQL provides **aggregation functions** to answer these questions.

Example:

```sql
SELECT SUM(revenue)
FROM sales;
```

This calculates the total revenue.

Aggregation functions summarize data across **multiple rows**.

---

# Key Idea Cards (3 Cards)

### Aggregations Summarize Data

Aggregation functions convert multiple rows into a single summary value.

Example:

```sql
SELECT SUM(revenue)
FROM sales;
```

This returns the total revenue.

---

### COUNT Calculates Row Totals

The `COUNT` function returns the number of rows.

Example:

```sql
SELECT COUNT(*)
FROM customers;
```

This counts all records in the table.

---

### Aggregations Are Common in Data Analysis

Analysts frequently use aggregation functions to calculate:

```text
Totals
Averages
Counts
Maximum values
Minimum values
```

These summaries help identify trends in data.

---

# Key Concepts

## COUNT

The `COUNT` function calculates how many rows exist.

Example table:

| order_id | product |
|---|---|
| 1 | Laptop |
| 2 | Phone |
| 3 | Tablet |

Query:

```sql
SELECT COUNT(*)
FROM sales;
```

Result:

```text
3
```

`COUNT(*)` counts all rows.

---

## SUM

The `SUM` function calculates the total of a numeric column.

Example:

| revenue |
|---|
| 1200 |
| 800 |
| 600 |

Query:

```sql
SELECT SUM(revenue)
FROM sales;
```

Result:

```text
2600
```

This returns the total revenue.

---

## AVG

The `AVG` function calculates the average value of a column.

Example:

| revenue |
|---|
| 1200 |
| 800 |
| 600 |

Query:

```sql
SELECT AVG(revenue)
FROM sales;
```

Result:

```text
866.67
```

This returns the average revenue.

---

# Decision Flow

When summarizing data:

```text
Need row count?
       ↓
Use COUNT()

Need total value?
       ↓
Use SUM()

Need average value?
       ↓
Use AVG()
```

Aggregation functions help answer high-level questions about datasets.

---

# Code Examples

### Example 1 — Counting Rows

```sql
SELECT COUNT(*)
FROM customers;
```

This returns the number of customers.

---

### Example 2 — Total Revenue

```sql
SELECT SUM(revenue)
FROM sales;
```

This calculates the total revenue.

---

### Example 3 — Average Price

```sql
SELECT AVG(price)
FROM products;
```

This calculates the average product price.

---

### Example 4 — Counting Specific Column Values

```sql
SELECT COUNT(customer_id)
FROM customers;
```

This counts rows that contain a customer ID.

---

# SQL / Excel Comparison

Aggregation functions in SQL are similar to formulas used in Excel.

| SQL | Excel | Python |
|---|---|---|
| COUNT() | COUNT() | df.count() |
| SUM() | SUM() | df.sum() |
| AVG() | AVERAGE() | df.mean() |

Example Excel formula:

```text
=SUM(B2:B10)
```

Equivalent SQL query:

```sql
SELECT SUM(revenue)
FROM sales;
```

Equivalent Python:

```python
df["revenue"].sum()
```

These operations summarize data across multiple rows.

---

# Practice Exercises

### Exercise 1

Tags: Aggregations, SQL

Count how many rows exist in the `employees` table.

---

### Exercise 2

Tags: Aggregations, Arithmetic

Calculate the total sales revenue from the `sales` table.

---

### Exercise 3

Tags: Aggregations, Arithmetic

Calculate the average price of products in the `products` table.

---

### Exercise 4

Tags: Aggregations, Arithmetic

Calculate the total number of customers in the `customers` table.

---

# Common Mistakes

### Using Aggregation on Non-Numeric Data

Functions like `SUM` and `AVG` require numeric columns.

Incorrect:

```sql
SELECT SUM(name)
FROM customers;
```

Correct:

```sql
SELECT SUM(sales)
FROM transactions;
```

---

### Confusing COUNT(*) with COUNT(column)

`COUNT(*)` counts all rows.

`COUNT(column)` counts rows where the column is not NULL.

---

### Forgetting Aggregation Intent

Aggregation summarizes the dataset.

If row-level data is required, aggregation may not be appropriate.

---

# Real-World Use

Aggregation functions are used in nearly every analytics workflow.

Examples include:

```text
Total company revenue
Average order value
Number of active customers
Total claims submitted
```

Example business query:

```sql
SELECT SUM(claim_amount)
FROM claims;
```

This calculates the total value of healthcare claims.

Analysts rely on aggregation functions to **summarize large datasets into meaningful metrics**.

---

# Lesson Recap

In this lesson you learned:

• how SQL summarizes data using aggregation functions  
• how COUNT calculates the number of rows  
• how SUM calculates totals  
• how AVG calculates averages

Aggregation allows analysts to transform raw data into **summary insights**.

---

# Next Lesson

Next we will continue Module 12 with:

# Lesson 7 — GROUP BY

You will learn:

• how SQL groups rows into categories  
• how aggregation works with grouped data  
• how analysts summarize metrics by category  
• how GROUP BY is similar to Excel pivot tables.
