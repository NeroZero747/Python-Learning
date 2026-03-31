# Module 13 — Advanced SQL for Data Analysis

# Lesson 7 — CASE Statements

---

# Lesson Objective

By the end of this lesson learners will understand:

• what **CASE statements** are in SQL  
• how SQL performs **conditional logic**  
• how CASE compares to **IF statements in programming languages**  
• how analysts use CASE to **categorize and transform data**

CASE statements allow analysts to create **logic-based classifications directly inside SQL queries**.

---

# Overview

In many analytics situations, we need to categorize or transform values based on conditions.

For example:

```text
High revenue vs low revenue
Large claims vs small claims
Premium customers vs standard customers
```

SQL uses the **CASE statement** to implement conditional logic.

Example:

```sql
SELECT
    claim_amount,
    CASE
        WHEN claim_amount > 10000 THEN 'High Cost'
        ELSE 'Standard'
    END AS claim_category
FROM claims;
```

This query classifies each claim into categories.

Result:

| claim_amount | claim_category |
|---|---|
| 5000 | Standard |
| 15000 | High Cost |

---

# Key Idea Cards (3 Cards)

### CASE Provides Conditional Logic

CASE allows SQL queries to make decisions based on conditions.

Example:

```sql
CASE
    WHEN condition THEN result
    ELSE result
END
```

This allows SQL to categorize or transform values.

---

### CASE Works Like IF Statements

CASE in SQL behaves similarly to **if statements in programming languages**.

Example logic:

```text
If claim_amount > 10000
        ↓
Label = "High Cost"
Else
        ↓
Label = "Standard"
```

---

### CASE Is Often Used for Data Categorization

Analysts frequently use CASE to group values into categories.

Examples:

```text
Revenue tiers
Customer segments
Risk levels
Product categories
```

---

# Key Concepts

## Basic CASE Structure

The basic CASE syntax looks like this:

```sql
CASE
    WHEN condition THEN result
    WHEN condition THEN result
    ELSE result
END
```

Example:

```sql
SELECT
    salary,
    CASE
        WHEN salary > 100000 THEN 'High'
        WHEN salary > 60000 THEN 'Medium'
        ELSE 'Low'
    END AS salary_category
FROM employees;
```

---

## Multiple Conditions

CASE can evaluate multiple conditions sequentially.

Example:

```sql
SELECT
    revenue,
    CASE
        WHEN revenue >= 100000 THEN 'Enterprise'
        WHEN revenue >= 50000 THEN 'Mid Market'
        ELSE 'Small Business'
    END AS customer_segment
FROM customers;
```

SQL evaluates conditions **from top to bottom**.

---

## Using CASE in SELECT

CASE is most commonly used inside SELECT statements.

Example:

```sql
SELECT
    product_name,
    price,
    CASE
        WHEN price > 100 THEN 'Premium'
        ELSE 'Standard'
    END AS price_category
FROM products;
```

This creates a new derived column.

---

## Using CASE in Aggregations

CASE can also be used inside aggregate functions.

Example:

```sql
SELECT
    SUM(
        CASE
            WHEN claim_amount > 10000 THEN claim_amount
            ELSE 0
        END
    ) AS high_cost_claims
FROM claims;
```

This sums only high-cost claims.

---

# Decision Flow

When transforming data:

```text
Need conditional logic?
        ↓
Use CASE
```

Example workflow:

```text
Identify claim risk levels
        ↓
Classify claim amounts
        ↓
Use CASE statement
```

---

# Code Examples

### Example 1 — Customer Spending Tier

```sql
SELECT
    customer_id,
    total_spent,
    CASE
        WHEN total_spent > 10000 THEN 'Premium'
        ELSE 'Standard'
    END AS customer_tier
FROM customers;
```

---

### Example 2 — Product Price Category

```sql
SELECT
    product_name,
    price,
    CASE
        WHEN price > 100 THEN 'Expensive'
        ELSE 'Affordable'
    END AS price_category
FROM products;
```

---

### Example 3 — Revenue Segmentation

```sql
SELECT
    company,
    revenue,
    CASE
        WHEN revenue >= 1000000 THEN 'Enterprise'
        WHEN revenue >= 100000 THEN 'Mid Market'
        ELSE 'Small Business'
    END AS segment
FROM companies;
```

---

### Example 4 — Healthcare Claim Classification

Healthcare example:

```sql
SELECT
    claim_id,
    claim_amount,
    CASE
        WHEN claim_amount > 20000 THEN 'High Risk'
        WHEN claim_amount > 10000 THEN 'Moderate Risk'
        ELSE 'Low Risk'
    END AS claim_risk_level
FROM claims;
```

This categorizes claims by financial risk.

---

# SQL / Excel / Python Comparison

Conditional logic appears across many tools.

| SQL | Python | Excel |
|---|---|---|
| CASE | if / elif | IF() |
| multiple conditions | if/elif/else | nested IF |

Python example:

```python
if salary > 100000:
    category = "High"
elif salary > 60000:
    category = "Medium"
else:
    category = "Low"
```

Equivalent SQL:

```sql
CASE
    WHEN salary > 100000 THEN 'High'
    WHEN salary > 60000 THEN 'Medium'
    ELSE 'Low'
END
```

Excel example:

```text
=IF(A1>100000,"High","Low")
```

---

# Practice Exercises

### Exercise 1

Tags: CASE Statements, SQL

Classify products into price categories:

```text
price > 100 → Premium
else → Standard
```

Table:

```text
products
```

---

### Exercise 2

Tags: CASE Statements, SQL

Classify customers by spending.

```text
> 5000 → High Value
else → Standard
```

Table:

```text
customers
```

---

### Exercise 3

Tags: CASE Statements, SQL

Categorize employee salaries into three levels:

```text
High
Medium
Low
```

Table:

```text
employees
```

---

### Exercise 4

Tags: CASE Statements, SQL

Classify healthcare claims by risk level.

Table:

```text
claims
```

---

# Common Mistakes

### Forgetting the END Keyword

Incorrect:

```sql
CASE
    WHEN revenue > 1000 THEN 'High'
```

Correct:

```sql
CASE
    WHEN revenue > 1000 THEN 'High'
END
```

---

### Incorrect Condition Order

SQL evaluates conditions **top to bottom**.

Example:

Incorrect:

```sql
WHEN revenue > 1000
WHEN revenue > 10000
```

The second condition will never be reached.

Always start with the **largest condition first**.

---

### Missing ELSE Clause

If no ELSE clause exists, SQL returns **NULL** when conditions are not met.

Example:

```sql
ELSE 'Standard'
```

---

# Real-World Use

CASE statements are heavily used in analytics.

Examples include:

```text
Customer segmentation
Revenue tiers
Risk classification
Performance grading
```

Healthcare example:

```sql
SELECT
    provider_id,
    SUM(claim_amount) AS total_claims,
    CASE
        WHEN SUM(claim_amount) > 500000 THEN 'High Cost Provider'
        ELSE 'Standard Provider'
    END AS provider_category
FROM claims
GROUP BY provider_id;
```

This classifies providers based on claim totals.

CASE statements allow analysts to **transform raw data into meaningful categories**.

---

# Lesson Recap

In this lesson you learned:

• how SQL CASE statements work  
• how SQL performs conditional logic  
• how analysts categorize and transform data  
• how CASE compares to Python and Excel logic

CASE statements allow analysts to **create dynamic classifications within SQL queries**.

---

# Next Lesson

Next we will continue Module 13 with:

# Lesson 8 — NULL Handling

You will learn:

• what **NULL values** represent in SQL  
• how SQL handles missing data  
• how functions like **COALESCE and NULLIF** work  
• how analysts handle missing data in real datasets.
