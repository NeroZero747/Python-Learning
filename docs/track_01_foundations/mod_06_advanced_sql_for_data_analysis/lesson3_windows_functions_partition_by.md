# Module 13 — Advanced SQL for Data Analysis

# Lesson 3 — Window Functions (PARTITION BY)

---

# Lesson Objective

By the end of this lesson learners will understand:

• what **window functions** are in SQL  
• how the **OVER() clause** works  
• how **PARTITION BY** divides data into groups  
• how window functions differ from **GROUP BY**

Window functions are one of the most powerful SQL tools because they allow calculations **across rows while still keeping the original rows visible**.

---

# Overview

In previous lessons you learned how to use **GROUP BY**.

Example:

```sql
SELECT department, AVG(salary)
FROM employees
GROUP BY department;
```

Result:

| department | avg_salary |
|---|---|
| Finance | 85000 |
| HR | 72000 |

The problem is that **GROUP BY collapses rows into summary results**.

Sometimes analysts want to:

```text
See each employee
AND
See the department average
```

This is where **window functions** are used.

Example:

```sql
SELECT
    employee,
    department,
    salary,
    AVG(salary) OVER(PARTITION BY department) AS dept_avg
FROM employees;
```

Result:

| employee | department | salary | dept_avg |
|---|---|---|---|
| Alice | Finance | 90000 | 85000 |
| Bob | Finance | 80000 | 85000 |
| Maria | HR | 70000 | 72000 |
| James | HR | 74000 | 72000 |

Notice that **every row remains visible**, while the department average is calculated.

---

# Key Idea Cards (3 Cards)

### Window Functions Do Not Collapse Rows

Unlike `GROUP BY`, window functions keep the original rows.

Example:

```sql
AVG(salary) OVER(PARTITION BY department)
```

Each row remains visible.

---

### OVER() Defines the Window

The `OVER()` clause defines how the calculation should be performed.

Example:

```sql
AVG(salary) OVER()
```

This calculates the average across the entire dataset.

---

### PARTITION BY Creates Groups

`PARTITION BY` divides rows into groups before performing calculations.

Example:

```sql
AVG(salary) OVER(PARTITION BY department)
```

This calculates averages **within each department**.

---

# Key Concepts

## Basic Window Function Structure

Window functions follow this structure:

```sql
FUNCTION(column) OVER(
    PARTITION BY column
)
```

Example:

```sql
AVG(salary) OVER(PARTITION BY department)
```

---

## PARTITION BY

`PARTITION BY` divides rows into groups.

Example dataset:

| employee | department | salary |
|---|---|---|
| Alice | Finance | 90000 |
| Bob | Finance | 80000 |
| Maria | HR | 70000 |
| James | HR | 74000 |

Query:

```sql
SELECT
    employee,
    department,
    salary,
    AVG(salary) OVER(PARTITION BY department)
FROM employees;
```

Each department is calculated separately.

---

## Window Functions Without PARTITION

You can calculate metrics across the entire dataset.

Example:

```sql
SELECT
    employee,
    salary,
    AVG(salary) OVER() AS company_avg
FROM employees;
```

Result:

| employee | salary | company_avg |
|---|---|---|
| Alice | 90000 | 78500 |
| Bob | 80000 | 78500 |
| Maria | 70000 | 78500 |
| James | 74000 | 78500 |

---

## Window Functions vs GROUP BY

| Feature | GROUP BY | Window Functions |
|---|---|---|
| collapses rows | yes | no |
| row-level data visible | no | yes |
| used for summaries | yes | yes |

Example:

GROUP BY:

```sql
SELECT department, AVG(salary)
FROM employees
GROUP BY department;
```

Window function:

```sql
SELECT employee, AVG(salary) OVER(PARTITION BY department)
FROM employees;
```

---

# Decision Flow

When analyzing grouped data:

```text
Do you need only summary results?
        ↓
Use GROUP BY

Do you need row-level data plus summaries?
        ↓
Use window functions
```

Example:

```text
Employee salary vs department average
```

Window functions are ideal.

---

# Code Examples

### Example 1 — Department Average Salary

```sql
SELECT
    employee,
    department,
    salary,
    AVG(salary) OVER(PARTITION BY department) AS dept_avg
FROM employees;
```

---

### Example 2 — Company Average Salary

```sql
SELECT
    employee,
    salary,
    AVG(salary) OVER() AS company_avg
FROM employees;
```

---

### Example 3 — Sales by Region

```sql
SELECT
    region,
    sales,
    SUM(sales) OVER(PARTITION BY region) AS regional_sales
FROM transactions;
```

---

### Example 4 — Claim Totals by Provider

Healthcare example:

```sql
SELECT
    provider_id,
    claim_amount,
    SUM(claim_amount) OVER(PARTITION BY provider_id) AS provider_total
FROM claims;
```

This calculates total claims per provider while keeping each claim row.

---

# SQL / Excel / Python Comparison

Window functions resemble operations in other tools.

| SQL | Python | Excel |
|---|---|---|
| PARTITION BY | groupby transform | pivot with row context |
| window function | transform() | advanced formulas |

Python equivalent:

```python
df["dept_avg"] = df.groupby("department")["salary"].transform("mean")
```

Equivalent SQL:

```sql
AVG(salary) OVER(PARTITION BY department)
```

---

# Practice Exercises

### Exercise 1

Tags: Window Functions, Arithmetic, Partitioning

Calculate **average salary by department** using a window function.

Table:

```text
employees
```

---

### Exercise 2

Tags: Window Functions, Arithmetic, Partitioning

Calculate **total sales per region** using a window function.

Table:

```text
sales
```

---

### Exercise 3

Tags: Arithmetic, Partitioning

Calculate the **average claim amount per provider**.

Table:

```text
claims
```

---

### Exercise 4

Tags: Arithmetic, Partitioning

Calculate the **company-wide average salary** for each employee.

---

# Common Mistakes

### Forgetting the OVER Clause

Incorrect:

```sql
AVG(salary)
```

Correct:

```sql
AVG(salary) OVER()
```

Window functions require `OVER()`.

---

### Using GROUP BY Instead of Window Functions

If row-level data is needed, GROUP BY will remove rows.

Example problem:

```text
Need individual employee rows plus department average
```

Solution:

```sql
AVG(salary) OVER(PARTITION BY department)
```

---

### Confusing PARTITION BY With GROUP BY

`PARTITION BY` groups rows **without collapsing them**.

`GROUP BY` collapses rows.

---

# Real-World Use

Window functions are heavily used in analytics.

Examples:

```text
Sales comparisons by region
Employee salary comparisons
Provider claim totals
Customer purchase history
```

Healthcare example:

```sql
SELECT
    provider_id,
    claim_amount,
    AVG(claim_amount) OVER(PARTITION BY provider_id)
FROM claims;
```

This allows analysts to compare **individual claims to provider averages**.

Window functions are one of the most **powerful SQL tools for analytics**.

---

# Lesson Recap

In this lesson you learned:

• what window functions are  
• how the OVER clause works  
• how PARTITION BY divides rows into groups  
• how window functions differ from GROUP BY

Window functions allow analysts to **perform advanced calculations while keeping row-level detail**.

---

# Next Lesson

Next we will continue Module 13 with:

# Lesson 4 — Ranking Functions

You will learn:

• how SQL ranks rows  
• how `ROW_NUMBER`, `RANK`, and `DENSE_RANK` work  
• how analysts identify top-performing results  
• how ranking is used in business analytics.
