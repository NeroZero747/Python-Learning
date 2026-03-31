# Module 13 — Advanced SQL for Data Analysis

# Lesson 5 — Running Totals

---

# Lesson Objective

By the end of this lesson learners will understand:

• what **running totals (cumulative totals)** are  
• how SQL calculates cumulative values using **window functions**  
• how running totals help analyze **trends over time**  
• how analysts use running totals in **business and financial analysis**

Running totals are commonly used to track **growth, trends, and accumulation of values over time**.

---

# Overview

A **running total** is the cumulative sum of values as new rows are processed.

Example dataset:

| order_date | revenue |
|---|---|
| Jan 1 | 100 |
| Jan 2 | 200 |
| Jan 3 | 150 |
| Jan 4 | 300 |

A running total would look like:

| order_date | revenue | running_total |
|---|---|---|
| Jan 1 | 100 | 100 |
| Jan 2 | 200 | 300 |
| Jan 3 | 150 | 450 |
| Jan 4 | 300 | 750 |

Each row adds to the **previous total**.

SQL calculates running totals using **window functions with ORDER BY**.

Example:

```sql
SELECT
    order_date,
    revenue,
    SUM(revenue) OVER(ORDER BY order_date) AS running_total
FROM sales;
```

---

# Key Idea Cards (3 Cards)

### Running Totals Track Accumulation

Running totals calculate the cumulative value as rows progress.

Example:

```text
100 → 300 → 450 → 750
```

Each row includes the total of all previous rows.

---

### Window Functions Enable Running Totals

Running totals use window functions such as:

```sql
SUM(column) OVER(ORDER BY column)
```

This calculates totals across rows in order.

---

### Running Totals Are Used for Trend Analysis

Running totals help analyze:

```text
Revenue growth
Customer acquisition
Inventory changes
Financial performance
```

They provide insight into **how values accumulate over time**.

---

# Key Concepts

## Running Total Using SUM()

Running totals are typically calculated using the `SUM()` function with a window.

Example:

```sql
SELECT
    order_date,
    revenue,
    SUM(revenue) OVER(ORDER BY order_date) AS running_total
FROM sales;
```

SQL processes rows sequentially and accumulates the total.

---

## Running Totals by Group

Running totals can also be calculated within groups.

Example dataset:

| region | order_date | revenue |
|---|---|---|
| West | Jan 1 | 100 |
| West | Jan 2 | 200 |
| East | Jan 1 | 150 |
| East | Jan 2 | 250 |

Query:

```sql
SELECT
    region,
    order_date,
    revenue,
    SUM(revenue) OVER(PARTITION BY region ORDER BY order_date) AS regional_running_total
FROM sales;
```

Each region has its own cumulative total.

---

## ORDER BY in Window Functions

Running totals depend on the **ORDER BY clause**.

Example:

```sql
SUM(revenue) OVER(ORDER BY order_date)
```

This ensures rows are processed in chronological order.

Without `ORDER BY`, the cumulative calculation would not make sense.

---

# Decision Flow

When calculating cumulative values:

```text
Need cumulative totals over time?
        ↓
Use SUM() with ORDER BY
```

If totals should reset within groups:

```text
Use PARTITION BY
```

Example workflow:

```text
Revenue growth by month
        ↓
Running total by month
```

---

# Code Examples

### Example 1 — Basic Running Total

```sql
SELECT
    order_date,
    revenue,
    SUM(revenue) OVER(ORDER BY order_date) AS running_total
FROM sales;
```

Tracks revenue growth over time.

---

### Example 2 — Running Total by Region

```sql
SELECT
    region,
    order_date,
    revenue,
    SUM(revenue) OVER(PARTITION BY region ORDER BY order_date) AS running_total
FROM sales;
```

Each region has its own cumulative revenue.

---

### Example 3 — Customer Purchase Totals

```sql
SELECT
    customer_id,
    order_date,
    amount,
    SUM(amount) OVER(PARTITION BY customer_id ORDER BY order_date) AS cumulative_spend
FROM orders;
```

Tracks how much each customer spends over time.

---

### Example 4 — Healthcare Claim Totals

Healthcare example:

```sql
SELECT
    provider_id,
    claim_date,
    claim_amount,
    SUM(claim_amount) OVER(PARTITION BY provider_id ORDER BY claim_date) AS provider_running_total
FROM claims;
```

This tracks cumulative claim amounts per provider.

---

# SQL / Excel / Python Comparison

Running totals exist across many tools.

| SQL | Python | Excel |
|---|---|---|
| SUM OVER ORDER BY | cumsum() | running total formula |

Python example:

```python
df["running_total"] = df["revenue"].cumsum()
```

Equivalent SQL:

```sql
SUM(revenue) OVER(ORDER BY order_date)
```

Excel example:

```text
=SUM($B$2:B2)
```

Each tool performs cumulative calculations in similar ways.

---

# Practice Exercises

### Exercise 1

Tags: Window Functions, Arithmetic

Calculate a running total of revenue by date.

Table:

```text
sales
```

---

### Exercise 2

Tags: Window Functions, Arithmetic

Calculate a cumulative purchase total for each customer.

Table:

```text
orders
```

---

### Exercise 3

Tags: Window Functions, Arithmetic

Calculate running sales totals by region.

Table:

```text
sales
```

---

### Exercise 4

Tags: Window Functions, Arithmetic

Calculate cumulative claim totals per provider.

Table:

```text
claims
```

---

# Common Mistakes

### Forgetting ORDER BY

Incorrect:

```sql
SUM(revenue) OVER()
```

This returns the same total for every row.

Correct:

```sql
SUM(revenue) OVER(ORDER BY order_date)
```

---

### Incorrect Sorting

Running totals require the correct sequence.

Example:

```sql
ORDER BY order_date
```

Sorting incorrectly can produce misleading totals.

---

### Not Using PARTITION BY When Needed

If totals should reset for groups, include:

```sql
PARTITION BY region
```

Otherwise, the total will accumulate across the entire dataset.

---

# Real-World Use

Running totals are used heavily in business analytics.

Examples include:

```text
Revenue growth tracking
Customer lifetime value
Inventory accumulation
Financial forecasting
```

Example business query:

```sql
SELECT
    order_date,
    SUM(revenue) OVER(ORDER BY order_date) AS cumulative_revenue
FROM sales;
```

This shows **total revenue growth over time**.

Running totals help analysts identify **trends and momentum in data**.

---

# Lesson Recap

In this lesson you learned:

• what running totals are  
• how SQL calculates cumulative values  
• how PARTITION BY creates grouped running totals  
• how analysts analyze trends using cumulative metrics

Running totals allow analysts to **track how values accumulate across time or groups**.

---

# Next Lesson

Next we will continue Module 13 with:

# Lesson 6 — Advanced Joins

You will learn:

• how **self joins** work  
• how to join **multiple tables**  
• how to join **aggregated datasets**  
• how analysts combine complex datasets in SQL.
