# Module 13 — Advanced SQL for Data Analysis

# Lesson 8 — NULL Handling

---

# Lesson Objective

By the end of this lesson learners will understand:

• what **NULL values** represent in SQL  
• how SQL treats **missing or unknown data**  
• how to use **IS NULL** and **IS NOT NULL**  
• how functions like **COALESCE() and NULLIF()** work  
• how analysts manage missing data in real datasets

Handling NULL values correctly is essential because many real-world datasets contain **incomplete or missing information**.

---

# Overview

In SQL, **NULL represents missing or unknown data**.

Example dataset:

| customer_id | phone |
|---|---|
| 101 | 555-1111 |
| 102 | NULL |
| 103 | 555-3333 |

Customer 102 does not have a phone number stored.

NULL does **not mean zero or empty text**.

```text
NULL ≠ 0
NULL ≠ ""
```

NULL simply means:

```text
Data is missing or unknown
```

Because of this, SQL treats NULL values differently than normal values.

---

# Key Idea Cards (3 Cards)

### NULL Represents Missing Data

NULL means that a value is **unknown or not recorded**.

Examples:

```text
Missing phone numbers
Unknown salaries
Incomplete customer records
```

---

### NULL Cannot Be Compared with =

A common mistake is trying to compare NULL using the equals operator.

Incorrect:

```sql
phone = NULL
```

Correct:

```sql
phone IS NULL
```

---

### NULL Handling Is Critical in Data Analysis

Missing values can affect calculations.

Examples:

```text
Averages
Counts
Aggregations
Financial totals
```

Proper NULL handling ensures accurate results.

---

# Key Concepts

## Identifying NULL Values

To identify missing values, SQL uses the **IS NULL** condition.

Example:

```sql
SELECT *
FROM customers
WHERE phone IS NULL;
```

This returns customers with missing phone numbers.

---

## Finding Non-NULL Values

To return rows where values exist:

```sql
SELECT *
FROM customers
WHERE phone IS NOT NULL;
```

This filters rows with valid data.

---

## Using COALESCE()

`COALESCE()` replaces NULL values with a default value.

Example:

```sql
SELECT
    customer_id,
    COALESCE(phone, 'Unknown') AS phone_number
FROM customers;
```

Result:

| customer_id | phone_number |
|---|---|
| 101 | 555-1111 |
| 102 | Unknown |
| 103 | 555-3333 |

This improves readability in reports.

---

## Using NULLIF()

`NULLIF()` converts specific values to NULL.

Example:

```sql
SELECT
    NULLIF(discount, 0)
FROM orders;
```

If discount equals 0, SQL returns NULL.

This is useful when:

```text
Zero values represent missing information
```

---

## NULL in Aggregations

SQL aggregate functions treat NULL values differently.

Example dataset:

| salary |
|---|
| 60000 |
| 70000 |
| NULL |

Query:

```sql
SELECT AVG(salary)
FROM employees;
```

Result:

```text
65000
```

NULL values are **ignored in aggregate functions**.

---

# Decision Flow

When working with missing values:

```text
Do you need to identify missing data?
        ↓
Use IS NULL
```

If missing values should be replaced:

```text
Use COALESCE()
```

If certain values should become NULL:

```text
Use NULLIF()
```

---

# Code Examples

### Example 1 — Find Missing Phone Numbers

```sql
SELECT *
FROM customers
WHERE phone IS NULL;
```

This identifies records with missing contact information.

---

### Example 2 — Replace NULL Values

```sql
SELECT
    customer_id,
    COALESCE(phone, 'Not Available') AS phone_number
FROM customers;
```

This replaces NULL values with readable text.

---

### Example 3 — Replace Missing Discounts

```sql
SELECT
    order_id,
    COALESCE(discount, 0) AS discount
FROM orders;
```

This replaces NULL discounts with zero.

---

### Example 4 — Healthcare Missing Provider Data

Healthcare example:

```sql
SELECT
    claim_id,
    COALESCE(provider_id, 'Unknown') AS provider
FROM claims;
```

This ensures missing provider IDs are labeled clearly.

---

# SQL / Excel / Python Comparison

Handling missing values exists across many tools.

| SQL | Python | Excel |
|---|---|---|
| NULL | NaN | Blank |
| COALESCE | fillna() | IF() |
| IS NULL | isna() | ISBLANK() |

Python example:

```python
df["phone"].fillna("Unknown")
```

Equivalent SQL:

```sql
COALESCE(phone, 'Unknown')
```

Excel example:

```text
=IF(A1="", "Unknown", A1)
```

---

# Practice Exercises

### Exercise 1

Tags: Missing Data, NULL Handling

Find all customers with missing phone numbers.

Table:

```text
customers
```

---

### Exercise 2

Tags: NULL Handling, Arithmetic

Replace NULL salaries with **0**.

Table:

```text
employees
```

---

### Exercise 3

Tags: Missing Data, NULL Handling

Identify orders with missing discounts.

Table:

```text
orders
```

---

### Exercise 4

Tags: Missing Data, NULL Handling

Replace missing provider IDs with **"Unknown"**.

Table:

```text
claims
```

---

# Common Mistakes

### Using = NULL

Incorrect:

```sql
WHERE phone = NULL
```

Correct:

```sql
WHERE phone IS NULL
```

---

### Forgetting NULL Handling in Reports

If NULL values appear in dashboards, users may see blank fields.

Example fix:

```sql
COALESCE(column, 'Unknown')
```

---

### Confusing NULL with Zero

Example:

```text
NULL → missing value
0 → actual numeric value
```

They represent very different meanings.

---

# Real-World Use

Handling NULL values is extremely common in analytics.

Examples include:

```text
Missing patient contact information
Incomplete customer profiles
Missing product prices
Unknown transaction details
```

Healthcare example:

```sql
SELECT
    provider_id,
    COUNT(*)
FROM claims
WHERE provider_id IS NULL;
```

This identifies claims with missing provider data.

Managing missing data correctly ensures **accurate analysis and reporting**.

---

# Lesson Recap

In this lesson you learned:

• what NULL values represent in SQL  
• how SQL handles missing data  
• how to identify NULL values  
• how functions like COALESCE and NULLIF work

Understanding NULL values is essential when working with **real-world datasets that contain incomplete data**.

---

# Next Lesson

Next we will continue Module 13 with:

# Lesson 9 — Query Optimization

You will learn:

• how SQL queries impact database performance  
• how indexes improve query speed  
• how analysts write efficient queries  
• how to avoid common performance issues.
