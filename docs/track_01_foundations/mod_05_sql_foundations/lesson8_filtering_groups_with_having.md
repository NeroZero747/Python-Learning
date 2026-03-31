# Module 12 — SQL Foundations

# Lesson 8 — Filtering Groups with HAVING

---

# Lesson Objective

By the end of this lesson learners will understand:

• how to **filter aggregated results using HAVING**  
• the difference between **WHERE and HAVING**  
• how analysts isolate **specific grouped results**  
• how HAVING works together with **GROUP BY and aggregation functions**

The HAVING clause allows analysts to filter **summary results**, which is essential when working with grouped data.

---

# Overview

In previous lessons you learned:

• `WHERE` filters individual rows  
• `GROUP BY` summarizes rows into categories

Example table:

| region | revenue |
|---|---|
| West | 1200 |
| West | 900 |
| East | 800 |
| East | 500 |
| North | 200 |

Query using GROUP BY:

```sql
SELECT region, SUM(revenue)
FROM sales
GROUP BY region;
```

Result:

| region | total_revenue |
|---|---|
| West | 2100 |
| East | 1300 |
| North | 200 |

But suppose we only want regions with **revenue greater than 1000**.

We cannot use WHERE because the revenue totals are calculated **after grouping**.

Instead we use **HAVING**.

Example:

```sql
SELECT region, SUM(revenue)
FROM sales
GROUP BY region
HAVING SUM(revenue) > 1000;
```

Result:

| region | total_revenue |
|---|---|
| West | 2100 |
| East | 1300 |

HAVING filters the grouped results.

---

# Key Idea Cards (3 Cards)

### HAVING Filters Aggregated Results

The HAVING clause filters results **after aggregation occurs**.

Example:

```sql
HAVING SUM(sales) > 10000
```

Only groups meeting this condition appear in the results.

---

### WHERE Filters Rows Before Grouping

WHERE filters rows before grouping occurs.

Example:

```sql
WHERE region = 'West'
```

This limits the rows included in the grouping.

---

### HAVING Works With Aggregation Functions

HAVING usually appears with functions like:

```text
SUM()
COUNT()
AVG()
MAX()
MIN()
```

Example:

```sql
HAVING COUNT(*) > 100
```

---

# Key Concepts

## WHERE vs HAVING

The most important difference:

| Clause | Filters |
|---|---|
| WHERE | individual rows |
| HAVING | grouped results |

Example workflow:

```text
Rows filtered → WHERE
Groups created → GROUP BY
Groups filtered → HAVING
```

---

## HAVING with SUM

Example table:

| product | revenue |
|---|---|
| Laptop | 1200 |
| Laptop | 800 |
| Phone | 600 |

Query:

```sql
SELECT product, SUM(revenue)
FROM sales
GROUP BY product
HAVING SUM(revenue) > 1000;
```

Result:

| product | total_revenue |
|---|---|
| Laptop | 2000 |

---

## HAVING with COUNT

Example:

```sql
SELECT city, COUNT(*)
FROM customers
GROUP BY city
HAVING COUNT(*) > 10;
```

This returns cities with **more than 10 customers**.

---

# Decision Flow

When filtering grouped results:

```text
Need to filter individual rows?
        ↓
Use WHERE

Need to filter aggregated groups?
        ↓
Use HAVING
```

Example:

```text
Sales by region
       ↓
Only regions with revenue > 10000
       ↓
HAVING SUM(revenue) > 10000
```

---

# Code Examples

### Example 1 — Filtering Aggregated Revenue

```sql
SELECT region, SUM(revenue)
FROM sales
GROUP BY region
HAVING SUM(revenue) > 1000;
```

This returns regions with revenue greater than 1000.

---

### Example 2 — Filtering Average Price

```sql
SELECT category, AVG(price)
FROM products
GROUP BY category
HAVING AVG(price) > 100;
```

This shows product categories with an average price above 100.

---

### Example 3 — Filtering Counts

```sql
SELECT city, COUNT(*)
FROM customers
GROUP BY city
HAVING COUNT(*) > 50;
```

This returns cities with more than 50 customers.

---

### Example 4 — Combining WHERE and HAVING

```sql
SELECT region, SUM(sales)
FROM sales
WHERE year = 2024
GROUP BY region
HAVING SUM(sales) > 10000;
```

Process:

```text
WHERE filters rows first
GROUP BY creates groups
HAVING filters groups
```

---

# SQL / Excel Comparison

HAVING behaves similarly to filtering pivot tables in Excel.

| SQL | Excel | Python |
|---|---|---|
| GROUP BY | Pivot Table | df.groupby() |
| HAVING | Pivot filter | filtered aggregation |

Example Excel pivot workflow:

```text
Create Pivot Table
Group by Region
Filter regions with revenue > 10000
```

Equivalent SQL:

```sql
SELECT region, SUM(revenue)
FROM sales
GROUP BY region
HAVING SUM(revenue) > 10000;
```

Equivalent Python:

```python
df.groupby("region")["revenue"].sum().loc[lambda x: x > 10000]
```

---

# Practice Exercises

### Exercise 1

Tags: Filtering, WHERE, HAVING, Arithmetic

Return regions where total sales exceed **5000**.

Table:

```text
sales
```

---

### Exercise 2

Tags: Filtering, WHERE, HAVING, Arithmetic

Return departments where the average salary exceeds **60000**.

Table:

```text
employees
```

---

### Exercise 3

Tags: Filtering, HAVING, Arithmetic

Return cities with more than **20 customers**.

Table:

```text
customers
```

---

### Exercise 4

Tags: Filtering, WHERE, HAVING, Arithmetic

Filter product categories where total revenue exceeds **10000**.

---

# Common Mistakes

### Using WHERE with Aggregations

Incorrect:

```sql
SELECT region, SUM(sales)
FROM sales
WHERE SUM(sales) > 1000
GROUP BY region;
```

Correct:

```sql
SELECT region, SUM(sales)
FROM sales
GROUP BY region
HAVING SUM(sales) > 1000;
```

Aggregations must be filtered using HAVING.

---

### Forgetting GROUP BY

HAVING usually requires grouping.

Incorrect:

```sql
SELECT SUM(sales)
FROM sales
HAVING SUM(sales) > 1000;
```

Correct:

```sql
SELECT region, SUM(sales)
FROM sales
GROUP BY region
HAVING SUM(sales) > 1000;
```

---

### Using HAVING Instead of WHERE

Filtering rows should use WHERE.

Incorrect:

```sql
HAVING region = 'West'
```

Correct:

```sql
WHERE region = 'West'
```

---

# Real-World Use

HAVING is frequently used in reporting and analytics.

Examples:

```text
Regions with revenue above target
Products with high sales volume
Cities with many customers
Providers with high claim totals
```

Example business query:

```sql
SELECT provider_id, SUM(claim_amount)
FROM claims
GROUP BY provider_id
HAVING SUM(claim_amount) > 500000;
```

This identifies providers with **high total claims**.

HAVING helps analysts **identify important trends and outliers**.

---

# Lesson Recap

In this lesson you learned:

• how the HAVING clause filters aggregated results  
• the difference between WHERE and HAVING  
• how analysts filter grouped summaries  
• how HAVING works with aggregation functions

HAVING allows analysts to **filter summarized data after grouping**.

---

# Next Lesson

Next we will continue Module 12 with:

# Lesson 9 — Joining Tables (JOIN)

You will learn:

• how SQL combines data from multiple tables  
• how relational databases connect tables using keys  
• the most common types of joins  
• how analysts combine datasets for analysis.
