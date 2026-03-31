# Module 12 — SQL Foundations

# Lesson 7 — GROUP BY

---

# Lesson Objective

By the end of this lesson learners will understand:

• how SQL **groups rows into categories**  
• how aggregation functions work with grouped data  
• how analysts calculate **metrics by category**  
• how `GROUP BY` is similar to **Excel pivot tables**

Grouping is one of the most powerful features of SQL because it allows analysts to **summarize data by categories such as region, product, or department**.

---

# Overview

In the previous lesson you learned how aggregation functions summarize data.

Example:

```sql
SELECT SUM(revenue)
FROM sales;
```

This returns the **total revenue for the entire table**.

But analysts often want to answer more specific questions such as:

```text
What is revenue by region?
What are sales by product?
How many customers exist in each city?
```

To answer these questions, SQL provides the **GROUP BY clause**.

Example table:

| product | revenue |
|---|---|
| Laptop | 1200 |
| Phone | 800 |
| Laptop | 1200 |
| Tablet | 600 |

Query:

```sql
SELECT product, SUM(revenue)
FROM sales
GROUP BY product;
```

Result:

| product | total_revenue |
|---|---|
| Laptop | 2400 |
| Phone | 800 |
| Tablet | 600 |

The `GROUP BY` clause groups rows before performing the aggregation.

---

# Key Idea Cards (3 Cards)

### GROUP BY Creates Categories

`GROUP BY` divides rows into groups based on a column.

Example:

```sql
GROUP BY region
```

Each region becomes its own group.

---

### Aggregation Happens Within Each Group

When using `GROUP BY`, aggregation functions operate **inside each group**.

Example:

```sql
SELECT region, SUM(revenue)
FROM sales
GROUP BY region;
```

Each region gets its own revenue total.

---

### GROUP BY Is Similar to Excel Pivot Tables

`GROUP BY` behaves similarly to pivot tables.

Example pivot table:

```text
Rows → Region
Values → Sum of Sales
```

Equivalent SQL:

```sql
SELECT region, SUM(sales)
FROM sales
GROUP BY region;
```

---

# Key Concepts

## Grouping Data

The `GROUP BY` clause groups rows that share the same value.

Example table:

| region | revenue |
|---|---|
| West | 1200 |
| East | 800 |
| West | 900 |

Query:

```sql
SELECT region, SUM(revenue)
FROM sales
GROUP BY region;
```

Result:

| region | total_revenue |
|---|---|
| West | 2100 |
| East | 800 |

---

## Aggregations with GROUP BY

Aggregation functions commonly used with grouping include:

```text
COUNT
SUM
AVG
MAX
MIN
```

Example:

```sql
SELECT region, COUNT(*)
FROM customers
GROUP BY region;
```

This counts customers in each region.

---

## Multiple Grouping Columns

SQL allows grouping by more than one column.

Example:

```sql
SELECT region, product, SUM(sales)
FROM sales
GROUP BY region, product;
```

This groups data by **region and product**.

---

# Decision Flow

When summarizing data by categories:

```text
Need totals by category?
        ↓
Choose grouping column
        ↓
Use GROUP BY
        ↓
Apply aggregation
```

Example workflow:

```text
Need sales by product
        ↓
GROUP BY product
```

---

# Code Examples

### Example 1 — Sales by Region

```sql
SELECT region, SUM(sales)
FROM sales
GROUP BY region;
```

This returns total sales for each region.

---

### Example 2 — Counting Customers by City

```sql
SELECT city, COUNT(*)
FROM customers
GROUP BY city;
```

This returns the number of customers in each city.

---

### Example 3 — Average Salary by Department

```sql
SELECT department, AVG(salary)
FROM employees
GROUP BY department;
```

This calculates the average salary for each department.

---

### Example 4 — Multiple Grouping Columns

```sql
SELECT region, product, SUM(sales)
FROM sales
GROUP BY region, product;
```

This calculates revenue for each product within each region.

---

# SQL / Excel Comparison

Grouping data in SQL is similar to pivot tables in Excel.

| SQL | Excel | Python |
|---|---|---|
| GROUP BY | Pivot Table | df.groupby() |
| SUM | Sum Values | .sum() |
| COUNT | Count Values | .count() |

Example Excel pivot:

```text
Rows → Region
Values → Sum of Sales
```

Equivalent SQL:

```sql
SELECT region, SUM(sales)
FROM sales
GROUP BY region;
```

Equivalent Python:

```python
df.groupby("region")["sales"].sum()
```

---

# Practice Exercises

### Exercise 1

Tags: GROUP BY, Arithmetic

Calculate total sales by region.

Table:

```text
sales
```

---

### Exercise 2

Tags: GROUP BY, SQL

Count employees in each department.

Table:

```text
employees
```

---

### Exercise 3

Tags: GROUP BY, Arithmetic

Calculate average price by product category.

Table:

```text
products
```

---

### Exercise 4

Tags: GROUP BY, Arithmetic

Calculate total revenue by **region and product**.

---

# Common Mistakes

### Forgetting GROUP BY Column

Incorrect:

```sql
SELECT region, SUM(sales)
FROM sales;
```

Correct:

```sql
SELECT region, SUM(sales)
FROM sales
GROUP BY region;
```

SQL must know how to group rows.

---

### Grouping Too Many Columns

Adding unnecessary columns to GROUP BY can create too many groups.

Example:

```sql
GROUP BY region, date, product
```

This may produce overly granular results.

---

### Mixing Aggregated and Non-Aggregated Columns

Columns in SELECT must either:

```text
Be aggregated
OR
Appear in GROUP BY
```

Incorrect:

```sql
SELECT region, product, SUM(sales)
FROM sales
GROUP BY region;
```

Correct:

```sql
SELECT region, product, SUM(sales)
FROM sales
GROUP BY region, product;
```

---

# Real-World Use

GROUP BY is heavily used in analytics and reporting.

Example use cases:

```text
Revenue by region
Customers by city
Claims by provider
Sales by product category
```

Example business query:

```sql
SELECT provider_id, SUM(claim_amount)
FROM claims
GROUP BY provider_id;
```

This calculates the total claim value submitted by each provider.

GROUP BY allows analysts to **convert raw transactional data into meaningful business metrics**.

---

# Lesson Recap

In this lesson you learned:

• how SQL groups rows using GROUP BY  
• how aggregation works within groups  
• how analysts calculate metrics by category  
• how GROUP BY is similar to Excel pivot tables

GROUP BY is one of the **most important tools in data analysis**.

---

# Next Lesson

Next we will continue Module 12 with:

# Lesson 8 — Filtering Groups with HAVING

You will learn:

• how to filter aggregated results  
• how HAVING differs from WHERE  
• how analysts isolate specific groups  
• how to filter grouped summaries.
