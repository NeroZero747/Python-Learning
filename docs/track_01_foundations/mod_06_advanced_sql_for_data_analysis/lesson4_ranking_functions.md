# Module 13 — Advanced SQL for Data Analysis

# Lesson 4 — Ranking Functions

---

# Lesson Objective

By the end of this lesson learners will understand:

• how SQL **ranking functions** work  
• the differences between **ROW_NUMBER(), RANK(), and DENSE_RANK()**  
• how ranking functions are used with **window functions**  
• how analysts identify **top-performing records**

Ranking functions are widely used in analytics to determine:

```text
Top customers
Highest revenue products
Top performing sales representatives
Largest claims or transactions
```

---

# Overview

Ranking functions assign a **rank value to each row** based on a sorting rule.

Example dataset:

| employee | salary |
|---|---|
| Alice | 90000 |
| Bob | 80000 |
| Maria | 80000 |
| James | 70000 |

If we rank employees by salary:

| employee | salary | rank |
|---|---|---|
| Alice | 90000 | 1 |
| Bob | 80000 | 2 |
| Maria | 80000 | 2 |
| James | 70000 | 4 |

SQL ranking functions use the **window function syntax**.

Example:

```sql
RANK() OVER(ORDER BY salary DESC)
```

This ranks rows from highest salary to lowest.

---

# Key Idea Cards (3 Cards)

### Ranking Functions Assign Order to Rows

Ranking functions assign a number to each row based on sorting rules.

Example:

```sql
RANK() OVER(ORDER BY revenue DESC)
```

Rows with higher revenue receive higher ranks.

---

### Ranking Uses Window Functions

Ranking functions require the **OVER() clause**.

Example:

```sql
ROW_NUMBER() OVER(ORDER BY salary DESC)
```

This assigns a unique number to each row.

---

### Ranking Is Common in Analytics

Ranking functions are used for:

```text
Top N analysis
Performance comparisons
Leaderboards
Customer segmentation
```

---

# Key Concepts

## ROW_NUMBER()

`ROW_NUMBER()` assigns a **unique number to each row**.

Example:

```sql
SELECT
    employee,
    salary,
    ROW_NUMBER() OVER(ORDER BY salary DESC) AS row_num
FROM employees;
```

Result:

| employee | salary | row_num |
|---|---|---|
| Alice | 90000 | 1 |
| Bob | 80000 | 2 |
| Maria | 80000 | 3 |
| James | 70000 | 4 |

Notice:

```text
Each row gets a unique number
```

Even if values are tied.

---

## RANK()

`RANK()` assigns the same rank for tied values.

Example:

```sql
SELECT
    employee,
    salary,
    RANK() OVER(ORDER BY salary DESC) AS rank
FROM employees;
```

Result:

| employee | salary | rank |
|---|---|---|
| Alice | 90000 | 1 |
| Bob | 80000 | 2 |
| Maria | 80000 | 2 |
| James | 70000 | 4 |

Notice:

```text
Ranks skip numbers after ties
```

---

## DENSE_RANK()

`DENSE_RANK()` also assigns equal ranks for ties but **does not skip numbers**.

Example:

```sql
SELECT
    employee,
    salary,
    DENSE_RANK() OVER(ORDER BY salary DESC) AS dense_rank
FROM employees;
```

Result:

| employee | salary | dense_rank |
|---|---|---|
| Alice | 90000 | 1 |
| Bob | 80000 | 2 |
| Maria | 80000 | 2 |
| James | 70000 | 3 |

---

# Ranking Function Comparison

| Function | Behavior |
|---|---|
| ROW_NUMBER | unique numbers |
| RANK | ties share rank, numbers skipped |
| DENSE_RANK | ties share rank, no gaps |

---

# Decision Flow

When ranking data:

```text
Need unique row numbers?
        ↓
Use ROW_NUMBER()

Need equal ranks for ties?
        ↓
Use RANK()

Need equal ranks but no gaps?
        ↓
Use DENSE_RANK()
```

---

# Code Examples

### Example 1 — Ranking Sales Representatives

```sql
SELECT
    sales_rep,
    revenue,
    RANK() OVER(ORDER BY revenue DESC) AS sales_rank
FROM sales;
```

This ranks sales representatives by revenue.

---

### Example 2 — Ranking Customers by Spending

```sql
SELECT
    customer_id,
    total_spent,
    DENSE_RANK() OVER(ORDER BY total_spent DESC) AS customer_rank
FROM customers;
```

This ranks customers based on total purchases.

---

### Example 3 — Ranking Products by Revenue

```sql
SELECT
    product_name,
    revenue,
    ROW_NUMBER() OVER(ORDER BY revenue DESC) AS product_rank
FROM products;
```

---

### Example 4 — Ranking Within Groups

Ranking can be applied **within groups** using `PARTITION BY`.

Example:

```sql
SELECT
    employee,
    department,
    salary,
    RANK() OVER(PARTITION BY department ORDER BY salary DESC) AS dept_rank
FROM employees;
```

Result:

Employees are ranked **within each department**.

---

# SQL / Excel / Python Comparison

Ranking exists in multiple tools.

| SQL | Python | Excel |
|---|---|---|
| RANK() | rank() | RANK() |
| ROW_NUMBER | index | helper column |
| PARTITION BY | groupby | pivot grouping |

Python example:

```python
df["rank"] = df["revenue"].rank(ascending=False)
```

Equivalent SQL:

```sql
RANK() OVER(ORDER BY revenue DESC)
```

---

# Practice Exercises

### Exercise 1

Tags: Window Functions, Streamlit

Rank employees by salary from highest to lowest.

Table:

```text
employees
```

---

### Exercise 2

Tags: Window Functions, SQL

Rank customers by total spending.

Table:

```text
customers
```

---

### Exercise 3

Tags: Window Functions, SQL

Rank products by sales revenue.

Table:

```text
products
```

---

### Exercise 4

Tags: Window Functions, Partitioning

Rank employees **within each department**.

Use:

```text
PARTITION BY department
```

---

# Common Mistakes

### Forgetting the OVER Clause

Incorrect:

```sql
RANK()
```

Correct:

```sql
RANK() OVER(ORDER BY salary DESC)
```

---

### Sorting in the Wrong Direction

If you want highest values ranked first:

```sql
ORDER BY revenue DESC
```

Without `DESC`, the lowest values appear first.

---

### Using ROW_NUMBER for Ties

ROW_NUMBER always assigns unique numbers.

If ties must share ranks, use:

```text
RANK
or
DENSE_RANK
```

---

# Real-World Use

Ranking functions are widely used in analytics.

Examples include:

```text
Top 10 customers by revenue
Highest performing providers
Most profitable products
Largest healthcare claims
```

Example healthcare query:

```sql
SELECT
    provider_id,
    SUM(claim_amount) AS total_claims,
    RANK() OVER(ORDER BY SUM(claim_amount) DESC) AS provider_rank
FROM claims
GROUP BY provider_id;
```

This ranks providers by total claim value.

Ranking functions help analysts **identify top performers and outliers**.

---

# Lesson Recap

In this lesson you learned:

• how SQL ranking functions work  
• the differences between ROW_NUMBER, RANK, and DENSE_RANK  
• how ranking works with window functions  
• how ranking is used in analytics workflows

Ranking functions are essential for **top-N analysis and performance comparisons**.

---

# Next Lesson

Next we will continue Module 13 with:

# Lesson 5 — Running Totals

You will learn:

• how SQL calculates cumulative totals  
• how running totals track growth over time  
• how window functions calculate rolling metrics  
• how analysts analyze trends using cumulative data.
